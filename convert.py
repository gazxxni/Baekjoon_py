import os
import datetime
import re
import time
from openai import OpenAI

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
        
        title_match = re.search(r'#\s*\[.*?\]\s*(.+?)\s*-\s*(\d+)', content)
        if title_match:
            data["title"] = title_match.group(1).strip()
            data["problem_id"] = title_match.group(2).strip()
        
        perf_match = re.search(r'메모리:\s*(\d+\s*KB).*?시간:\s*(\d+\s*ms)', content)
        if perf_match:
            data["memory"] = perf_match.group(1)
            data["time"] = perf_match.group(2)
        
        category_match = re.search(r'### 분류\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
        if category_match:
            data["category"] = category_match.group(1).strip()
        
        desc_match = re.search(r'### 문제 설명\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
        if desc_match:
            desc = desc_match.group(1).strip()
            desc = re.sub(r'<[^>]+>', '', desc)
            data["description"] = desc.strip()
        
        input_match = re.search(r'### 입력\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
        if input_match:
            inp = input_match.group(1).strip()
            inp = re.sub(r'<[^>]+>', '', inp)
            data["input"] = inp.strip()
        
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
    """OpenAI GPT로 풀이 생성 (RPM 제한 회피)"""
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("[ERROR] OPENAI_API_KEY is empty or not set")
        return None
    
    print(f"[DEBUG] API key found (length: {len(api_key)})")

    try:
        client = OpenAI(api_key=api_key)
        
        prompt = f"""백준 문제 풀이를 작성해주세요.

문제 번호: {problem_data.get('problem_id', '')}
제목: {problem_data.get('title', '')}
분류: {problem_data.get('category', '')}
설명: {problem_data.get('description', '')}
입력: {problem_data.get('input', '')}
출력: {problem_data.get('output', '')}

정답 코드:
```python
{code_content}
```

아래 형식으로 작성해주세요:

### 풀이 핵심 로직
(핵심 아이디어 2-3문장)

### 동작 과정
(예시 입력으로 단계별 설명)

### 시간 복잡도
(빅오 표기법)"""

        print("[DEBUG] Sending request to OpenAI API...")
        
        # GPT-4o-mini 사용 (저렴하고 빠름)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "당신은 알고리즘 문제 풀이를 명확하게 설명하는 전문가입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        
        # 응답 확인
        if response and response.choices:
            solution = response.choices[0].message.content.strip()
            print("[OK] AI solution generated successfully")
            
            # RPM 제한 회피: 4초 대기
            print("[INFO] Waiting 4 seconds to avoid rate limit...")
            time.sleep(4)
            
            return solution
        else:
            print(f"[ERROR] Empty response from OpenAI")
            print(f"[DEBUG] Response object: {response}")
            
            # 실패해도 대기 (다음 요청을 위해)
            time.sleep(4)
            return None
        
    except Exception as e:
        print(f"[ERROR] OpenAI API exception: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        
        # 에러 발생해도 대기 (다음 요청을 위해)
        print("[INFO] Waiting 4 seconds before retry...")
        time.sleep(4)
        return None

def create_markdown(py_path, readme_path, problem_id):
    """마크다운 파일 생성"""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open(py_path, 'r', encoding='utf-8') as f:
        code_content = f.read()

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

    ai_solution = generate_solution_with_ai(problem_data, code_content)
    
    if not ai_solution:
        ai_solution = """### 풀이 핵심 로직
(AI 생성 실패)

### 동작 과정
-

### 시간 복잡도
-"""

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
    print(f"[DEBUG] OPENAI_API_KEY exists: {bool(os.environ.get('OPENAI_API_KEY'))}")
    print(f"[INFO] Using model: gpt-4o-mini with 4s delay between requests")
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        if ".git" in root or OUTPUT_DIR in root:
            continue
        
        py_files = [f for f in files if f.endswith(".py")]
        has_readme = "README.md" in files
        
        if py_files and has_readme:
            readme_path = os.path.join(root, "README.md")
            
            for py_file in py_files:
                py_path = os.path.join(root, py_file)
                problem_id = get_problem_info_from_path(py_path)
                
                if problem_id and problem_id not in processed:
                    found_any = True
                    print(f"\n[INFO] Processing problem {problem_id}...")
                    print(f"[INFO] Found: {py_path}")
                    create_markdown(py_path, readme_path, problem_id)
                    processed.add(problem_id)
    
    if not found_any:
        print("[WARN] No valid problem folders found")
    else:
        print(f"\n{'='*50}")
        print(f"[DONE] Successfully processed {len(processed)} problems")
        print(f"{'='*50}")

if __name__ == "__main__":
    main()
