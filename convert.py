import os
import datetime
import re
import google.generativeai as genai

SOURCE_DIR = "auto_upload"
OUTPUT_DIR = "blog_posts"

def get_problem_info_from_path(file_path):
    """폴더명에서 문제 번호 추출"""
    match = re.search(r'[/\\](\d+)\.', file_path)
    if match:
        return match.group(1)
    return None

def parse_readme(readme_path):
    """README.md에서 문제 정보 파싱"""
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {
            "title": "",
            "problem_id": "",
            "description": "",
            "input": "",
            "output": "",
            "category": "",
            "memory": "",
            "time": ""
        }
        
        # 제목과 문제번호: # [Bronze V] Hello Judge - 9316
        title_match = re.search(r'#\s*\[.*?\]\s*(.+?)\s*-\s*(\d+)', content)
        if title_match:
            data["title"] = title_match.group(1).strip()
            data["problem_id"] = title_match.group(2).strip()
        
        # 성능 요약: 메모리: 108384 KB, 시간: 84 ms
        perf_match = re.search(r'메모리:\s*(\d+\s*KB).*?시간:\s*(\d+\s*ms)', content)
        if perf_match:
            data["memory"] = perf_match.group(1)
            data["time"] = perf_match.group(2)
        
        # 분류
        category_match = re.search(r'### 분류\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
        if category_match:
            data["category"] = category_match.group(1).strip()
        
        # 문제 설명 (HTML 태그 제거)
        desc_match = re.search(r'### 문제 설명\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
        if desc_match:
            desc = desc_match.group(1).strip()
            desc = re.sub(r'<[^>]+>', '', desc)  # HTML 태그 제거
            data["description"] = desc.strip()
        
        # 입력
        input_match = re.search(r'### 입력\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
        if input_match:
            inp = input_match.group(1).strip()
            inp = re.sub(r'<[^>]+>', '', inp)
            data["input"] = inp.strip()
        
        # 출력
        output_match = re.search(r'### 출력\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
        if output_match:
            out = output_match.group(1).strip()
            out = re.sub(r'<[^>]+>', '', out)
            data["output"] = out.strip()
        
        return data
        
    except Exception as e:
        print(f"[ERROR] README parsing failed: {e}")
        return None

def generate_solution_with_ai(problem_data, code_content):
    """Gemini API로 풀이 생성"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY not found in environment")
        return None

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""당신은 알고리즘 블로그 작성자입니다. 아래 백준 문제와 정답 코드를 분석하여 풀이를 작성해주세요.

## 문제 정보
- 번호: {problem_data.get('problem_id', '')}
- 제목: {problem_data.get('title', '')}
- 분류: {problem_data.get('category', '')}
- 설명: {problem_data.get('description', '')}
- 입력: {problem_data.get('input', '')}
- 출력: {problem_data.get('output', '')}

## 정답 코드
```python
{code_content}
```

## 작성 요청
아래 형식 그대로 마크다운을 작성해주세요:

### 풀이 핵심 로직
(이 문제를 푸는 핵심 아이디어를 2-3문장으로 설명)

### 동작 과정
(간단한 예시 입력으로 코드가 어떻게 동작하는지 단계별로 설명)

### 시간 복잡도
(빅오 표기법과 간단한 이유)

---
서론, 인사말, 마무리 없이 위 세 섹션만 작성."""

        response = model.generate_content(prompt)
        result = response.text.strip()
        print(f"[OK] AI solution generated")
        return result
        
    except Exception as e:
        print(f"[ERROR] Gemini API failed: {e}")
        return None

def create_markdown(py_path, readme_path, problem_id):
    """마크다운 파일 생성"""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 코드 읽기
    with open(py_path, 'r', encoding='utf-8') as f:
        code_content = f.read()

    # README 파싱
    problem_data = parse_readme(readme_path)
    
    if not problem_data:
        print(f"[WARN] README parsing failed, using fallback")
        problem_data = {
            "title": f"{problem_id}번",
            "problem_id": problem_id,
            "description": "",
            "input": "",
            "output": "",
            "category": "",
            "memory": "",
            "time": ""
        }

    # AI 풀이 생성
    ai_solution = generate_solution_with_ai(problem_data, code_content)
    
    if not ai_solution:
        ai_solution = """### 풀이 핵심 로직
(AI 생성 실패)

### 동작 과정
-

### 시간 복잡도
-"""

    # 마크다운 생성
    title = problem_data.get('title', problem_id)
    post_title = f"[백준] {problem_id}번 {title} (Python)"
    filename = f"{today}-baekjoon-{problem_id}.md"

    lines = [
        "---",
        "layout: post",
        f'title: "{post_title}"',
        f"date: {today}",
        "categories: [Algorithm, Baekjoon]",
        f"tags: [python, algorithm, baekjoon, {problem_id}, {problem_data.get('category', '')}]",
        "---",
        "",
        "## 문제 링크",
        f"[https://www.acmicpc.net/problem/{problem_id}](https://www.acmicpc.net/problem/{problem_id})",
        "",
        "---",
        "",
        "## 문제",
        problem_data.get("description", "-") or "-",
        "",
        "---",
        "",
        "## 입력",
        problem_data.get("input", "-") or "-",
        "",
        "---",
        "",
        "## 출력",
        problem_data.get("output", "-") or "-",
        "",
        "---",
        "",
        "## 성능 요약",
        f"메모리: {problem_data.get('memory', '-')}, 시간: {problem_data.get('time', '-')}",
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
    
    print(f"[INFO] Scanning {SOURCE_DIR}...")
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        if ".git" in root or OUTPUT_DIR in root:
            continue
        
        # 폴더 내 .py 파일과 README.md 찾기
        py_files = [f for f in files if f.endswith(".py")]
        has_readme = "README.md" in files
        
        if py_files and has_readme:
            readme_path = os.path.join(root, "README.md")
            
            for py_file in py_files:
                py_path = os.path.join(root, py_file)
                problem_id = get_problem_info_from_path(py_path)
                
                if problem_id and problem_id not in processed:
                    found_any = True
                    print(f"[INFO] Found: {py_path}")
                    print(f"[INFO] README: {readme_path}")
                    create_markdown(py_path, readme_path, problem_id)
                    processed.add(problem_id)
    
    if not found_any:
        print("[WARN] No valid problem folders found")
    else:
        print(f"[DONE] Processed {len(processed)} problems")

if __name__ == "__main__":
    main()
