import os
import datetime
import re
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

SOURCE_DIR = "auto_upload"
OUTPUT_DIR = "blog_posts"

def get_problem_info(file_path):
    """파일 경로(폴더명)에서 문제 번호 추출"""
    match = re.search(r'[/\\](\d+)\.', file_path)
    if match:
        return match.group(1)
    return None

def scrape_problem_data(problem_id):
    url = f"https://www.acmicpc.net/problem/{problem_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 문제 제목
        title_elem = soup.select_one("#problem_title")
        title = title_elem.get_text(strip=True) if title_elem else f"{problem_id}번"
        
        # 문제 설명
        desc_elem = soup.select_one("#problem_description")
        description = desc_elem.get_text("\n", strip=True) if desc_elem else ""
        
        # 입력 설명
        input_elem = soup.select_one("#problem_input")
        input_text = input_elem.get_text("\n", strip=True) if input_elem else ""
        
        # 출력 설명
        output_elem = soup.select_one("#problem_output")
        output_text = output_elem.get_text("\n", strip=True) if output_elem else ""
        
        # 예제 입출력
        samples = []
        index = 1
        while True:
            sample_input = soup.select_one(f"#sample-input-{index}")
            sample_output = soup.select_one(f"#sample-output-{index}")
            
            if not sample_input or not sample_output:
                break
            
            samples.append({
                "input": sample_input.get_text(strip=True),
                "output": sample_output.get_text(strip=True)
            })
            index += 1
        
        return {
            "title": title,
            "description": description,
            "input": input_text,
            "output": output_text,
            "samples": samples
        }
        
    except Exception as e:
        print(f"[ERROR] Scraping failed for {problem_id}: {e}")
        return None

def generate_solution_with_ai(problem_id, problem_data, code_content):
    """Gemini API로 풀이 생성"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY not found")
        return None

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 예제 데이터 준비
        example_str = ""
        if problem_data.get("samples"):
            ex = problem_data["samples"][0]
            example_str = f"예제 입력: {ex['input']}\n예제 출력: {ex['output']}"
        
        prompt = f"""당신은 알고리즘 블로그 작성자입니다. 아래 백준 문제와 정답 코드를 분석하여 블로그 포스팅용 풀이를 작성해주세요.

## 문제 정보
- 번호: {problem_id}
- 제목: {problem_data.get('title', '')}
- 설명: {problem_data.get('description', '')[:800]}
- {example_str}

## 정답 코드
```python
{code_content}
```

## 작성 요청사항
아래 형식으로 마크다운을 작성해주세요. 각 섹션 제목은 그대로 유지하고, 내용만 채워주세요.

### 풀이 핵심 로직
(이 문제를 푸는 핵심 아이디어와 알고리즘을 2-4문장으로 설명)

### 동작 과정
(예제 입력을 사용해서 코드가 어떻게 동작하는지 단계별로 시뮬레이션. 초기 상태 → 각 단계 → 최종 결과 형태로)

### 시간 복잡도
(빅오 표기법으로 시간 복잡도 명시하고 간단히 이유 설명)

---
서론, 인사말, 마무리 멘트 없이 위 세 섹션만 작성해주세요."""

        response = model.generate_content(prompt)
        return response.text.strip()
        
    except Exception as e:
        print(f"[ERROR] Gemini API failed: {e}")
        return None

def create_markdown(file_path, problem_id):
    """마크다운 파일 생성"""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        code_content = f.read()

    # 크롤링
    problem_data = scrape_problem_data(problem_id)
    
    if not problem_data:
        print(f"[WARN] Using fallback for {problem_id}")
        problem_data = {
            "title": f"{problem_id}번",
            "description": "문제 정보를 가져올 수 없습니다.",
            "input": "-",
            "output": "-",
            "samples": []
        }

    # AI 풀이 생성
    ai_solution = generate_solution_with_ai(problem_id, problem_data, code_content)
    
    if not ai_solution:
        ai_solution = """### 풀이 핵심 로직
(AI 생성 실패 - 코드 상단에 주석으로 풀이를 작성해주세요)

### 동작 과정
-

### 시간 복잡도
-"""

    # 예제 입출력 포맷팅
    samples_md = ""
    if problem_data["samples"]:
        for i, sample in enumerate(problem_data["samples"], 1):
            samples_md += f"""
**예제 입력 {i}**
```
{sample['input']}
```

**예제 출력 {i}**
```
{sample['output']}
```
"""
    else:
        samples_md = "예제 없음"

    # 마크다운 생성
    post_title = f"[백준] {problem_id}번 {problem_data['title']} (Python)"
    filename = f"{today}-baekjoon-{problem_id}.md"

    lines = [
        "---",
        "layout: post",
        f'title: "{post_title}"',
        f"date: {today}",
        "categories: [Algorithm, Baekjoon]",
        f"tags: [python, algorithm, baekjoon, {problem_id}]",
        "---",
        "",
        "## 문제 링크",
        f"[https://www.acmicpc.net/problem/{problem_id}](https://www.acmicpc.net/problem/{problem_id})",
        "",
        "---",
        "",
        "## 문제",
        problem_data["description"] if problem_data["description"] else "문제 설명 없음",
        "",
        "---",
        "",
        "## 입력",
        problem_data["input"] if problem_data["input"] else "-",
        "",
        "---",
        "",
        "## 출력",
        problem_data["output"] if problem_data["output"] else "-",
        "",
        "---",
        "",
        "## 예제",
        samples_md,
        "",
        "---",
        "",
        "## 풀이",
        "",
        ai_solution,
        "",
        "---",
        "",
        "## 코드",
        "```python",
        code_content,
        "```",
    ]
    
    markdown_content = "\n".join(lines)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    output_path = os.path.join(OUTPUT_DIR, filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"[OK] Created: {filename}")

def main():
    processed = set()
    found_any = False
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        if ".git" in root or OUTPUT_DIR in root:
            continue
            
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                problem_id = get_problem_info(file_path)
                
                if problem_id and problem_id not in processed:
                    found_any = True
                    print(f"[INFO] Processing: {file_path} -> Problem {problem_id}")
                    create_markdown(file_path, problem_id)
                    processed.add(problem_id)
    
    if not found_any:
        print("[WARN] No .py files found in auto_upload/")

if __name__ == "__main__":
    main()
