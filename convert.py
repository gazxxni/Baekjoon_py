# import os
# import datetime
# import re
# import time
# import subprocess
# from openai import OpenAI

# SOURCE_DIR = "auto_upload"
# OUTPUT_DIR = "blog_posts"
# PROCESSED_FILE = ".processed_files.txt"
# ##수정
# def get_git_commit_date(file_path):
#     """Git에서 파일의 최초 커밋 날짜 가져오기"""
#     try:
#         # 파일의 첫 커밋 날짜 가져오기
#         result = subprocess.run(
#             ['git', 'log', '--diff-filter=A', '--follow', '--format=%aI', '--', file_path],
#             capture_output=True,
#             text=True,
#             cwd=os.path.dirname(os.path.abspath(file_path)) or '.'
#         )
        
#         if result.stdout.strip():
#             # ISO 8601 형식을 YYYY-MM-DD로 변환
#             date_str = result.stdout.strip().split('\n')[-1]  # 가장 오래된 커밋
#             date_obj = datetime.datetime.fromisoformat(date_str.replace('Z', '+00:00'))
#             return date_obj.strftime("%Y-%m-%d")
#     except Exception as e:
#         print(f"[WARN] Could not get git date for {file_path}: {e}")
    
#     # Git 정보를 가져올 수 없으면 오늘 날짜 반환
#     return datetime.datetime.now().strftime("%Y-%m-%d")

# def load_processed_files():
#     """이미 처리된 파일 목록 로드"""
#     if os.path.exists(PROCESSED_FILE):
#         with open(PROCESSED_FILE, 'r', encoding='utf-8') as f:
#             return set(line.strip() for line in f if line.strip())
#     return set()

# def save_processed_file(file_path):
#     """처리된 파일 기록"""
#     with open(PROCESSED_FILE, 'a', encoding='utf-8') as f:
#         f.write(f"{file_path}\n")

# def get_problem_info_from_path(file_path):
#     """폴더명에서 문제 번호 추출"""
#     match = re.search(r'[/\\](\d+)\.', file_path)
#     if match:
#         return match.group(1)
#     return None

# def parse_readme(readme_path):
#     """README.md에서 문제 정보 파싱"""
#     try:
#         with open(readme_path, 'r', encoding='utf-8') as f:
#             content = f.read()
        
#         data = {
#             "title": "",
#             "problem_id": "",
#             "description": "",
#             "input": "",
#             "output": "",
#             "category": "",
#             "memory": "",
#             "time": ""
#         }
        
#         title_match = re.search(r'#\s*\[.*?\]\s*(.+?)\s*-\s*(\d+)', content)
#         if title_match:
#             data["title"] = title_match.group(1).strip()
#             data["problem_id"] = title_match.group(2).strip()
        
#         perf_match = re.search(r'메모리:\s*(\d+\s*KB).*?시간:\s*(\d+\s*ms)', content)
#         if perf_match:
#             data["memory"] = perf_match.group(1)
#             data["time"] = perf_match.group(2)
        
#         category_match = re.search(r'### 분류\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
#         if category_match:
#             data["category"] = category_match.group(1).strip()
        
#         desc_match = re.search(r'### 문제 설명\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
#         if desc_match:
#             desc = desc_match.group(1).strip()
#             desc = re.sub(r'<[^>]+>', '', desc)
#             data["description"] = desc.strip()
        
#         input_match = re.search(r'### 입력\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
#         if input_match:
#             inp = input_match.group(1).strip()
#             inp = re.sub(r'<[^>]+>', '', inp)
#             data["input"] = inp.strip()
        
#         output_match = re.search(r'### 출력\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
#         if output_match:
#             out = output_match.group(1).strip()
#             out = re.sub(r'<[^>]+>', '', out)
#             data["output"] = out.strip()
        
#         return data
        
#     except Exception as e:
#         print(f"[ERROR] README parsing failed: {e}")
#         return None

# def generate_solution_with_ai(problem_data, code_content):
#     """OpenAI GPT로 풀이 생성 (RPM 제한 회피)"""
#     api_key = os.environ.get("OPENAI_API_KEY")
    
#     if not api_key:
#         print("[ERROR] OPENAI_API_KEY is empty or not set")
#         return None
    
#     print(f"[DEBUG] API key found (length: {len(api_key)})")

#     try:
#         client = OpenAI(api_key=api_key)
        
#         prompt = f"""백준 문제 풀이를 작성해주세요.

# 문제 번호: {problem_data.get('problem_id', '')}
# 제목: {problem_data.get('title', '')}
# 분류: {problem_data.get('category', '')}
# 설명: {problem_data.get('description', '')}
# 입력: {problem_data.get('input', '')}
# 출력: {problem_data.get('output', '')}

# 정답 코드:
# ```python
# {code_content}
# ```

# 아래 형식으로 작성해주세요:

# ### 풀이 핵심 로직
# (핵심 아이디어 2-3문장)

# ### 동작 과정
# (예시 입력으로 단계별 설명)

# ### 시간 복잡도
# (빅오 표기법)"""

#         print("[DEBUG] Sending request to OpenAI API...")
        
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": "당신은 알고리즘 문제 풀이를 명확하게 설명하는 전문가입니다."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.7,
#             max_tokens=1024
#         )
        
#         if response and response.choices:
#             solution = response.choices[0].message.content.strip()
#             print("[OK] AI solution generated successfully")
            
#             print("[INFO] Waiting 4 seconds to avoid rate limit...")
#             time.sleep(4)
            
#             return solution
#         else:
#             print(f"[ERROR] Empty response from OpenAI")
#             time.sleep(4)
#             return None
        
#     except Exception as e:
#         print(f"[ERROR] OpenAI API exception: {type(e).__name__}: {e}")
#         import traceback
#         traceback.print_exc()
        
#         print("[INFO] Waiting 4 seconds before retry...")
#         time.sleep(4)
#         return None

# def create_markdown(py_path, readme_path, problem_id, commit_date):
#     """마크다운 파일 생성 (커밋 날짜 사용)"""
    
#     with open(py_path, 'r', encoding='utf-8') as f:
#         code_content = f.read()

#     problem_data = parse_readme(readme_path)
    
#     if not problem_data:
#         print(f"[WARN] README parsing failed, using fallback")
#         problem_data = {
#             "title": f"{problem_id}번",
#             "problem_id": problem_id,
#             "description": "",
#             "input": "",
#             "output": "",
#             "category": "",
#             "memory": "",
#             "time": ""
#         }

#     ai_solution = generate_solution_with_ai(problem_data, code_content)
    
#     if not ai_solution:
#         ai_solution = """### 풀이 핵심 로직
# (AI 생성 실패)

# ### 동작 과정
# -

# ### 시간 복잡도
# -"""

#     title = problem_data.get('title', problem_id)
#     post_title = f"[백준] {problem_id}번 {title} (Python)"
#     filename = f"{commit_date}-baekjoon-{problem_id}.md"

#     lines = [
#         "---",
#         "layout: post",
#         f'title: "{post_title}"',
#         f"date: {commit_date}",
#         "categories: [Algorithm, Baekjoon]",
#         f'tags: [python, algorithm, baekjoon, "{problem_id}", {problem_data.get("category", "")}]',
#         "---",
#         "",
#         "## 문제 링크",
#         f"[https://www.acmicpc.net/problem/{problem_id}](https://www.acmicpc.net/problem/{problem_id})",
#         "",
#         "---",
#         "",
#         "## 문제",
#         problem_data.get("description", "-") or "-",
#         "",
#         "---",
#         "",
#         "## 입력",
#         problem_data.get("input", "-") or "-",
#         "",
#         "---",
#         "",
#         "## 출력",
#         problem_data.get("output", "-") or "-",
#         "",
#         "---",
#         "",
#         "## 성능 요약",
#         f"메모리: {problem_data.get('memory', '-')}, 시간: {problem_data.get('time', '-')}",
#         "",
#         "---",
#         "",
#         "## 풀이",
#         "",
#         ai_solution,
#         "",
#         "---",
#         "",
#         "## 코드",
#         "```python",
#         code_content,
#         "```",
#     ]
    
#     markdown_content = "\n".join(lines)

#     if not os.path.exists(OUTPUT_DIR):
#         os.makedirs(OUTPUT_DIR)

#     output_path = os.path.join(OUTPUT_DIR, filename)
    
#     with open(output_path, 'w', encoding='utf-8') as f:
#         f.write(markdown_content)
    
#     print(f"[OK] Created: {filename}")

# def main():
#     processed_files = load_processed_files()
#     new_files = []
    
#     print(f"[INFO] Scanning {SOURCE_DIR}...")
#     print(f"[DEBUG] OPENAI_API_KEY exists: {bool(os.environ.get('OPENAI_API_KEY'))}")
#     print(f"[INFO] Using model: gpt-4o-mini with 4s delay between requests")
#     print(f"[INFO] Already processed: {len(processed_files)} files")
    
#     # auto_upload 폴더 내의 백준 폴더만 스캔
#     baekjoon_dir = os.path.join(SOURCE_DIR, "백준")
    
#     if not os.path.exists(baekjoon_dir):
#         print(f"[ERROR] {baekjoon_dir} not found!")
#         return
    
#     for root, dirs, files in os.walk(baekjoon_dir):
#         if ".git" in root or OUTPUT_DIR in root:
#             continue
        
#         py_files = [f for f in files if f.endswith(".py")]
#         has_readme = "README.md" in files
        
#         if py_files and has_readme:
#             readme_path = os.path.join(root, "README.md")
            
#             for py_file in py_files:
#                 py_path = os.path.join(root, py_file)
                
#                 # 이미 처리한 파일인지 확인
#                 if py_path in processed_files:
#                     continue
                
#                 problem_id = get_problem_info_from_path(py_path)
                
#                 if problem_id:
#                     new_files.append((py_path, readme_path, problem_id))
    
#     if not new_files:
#         print("[INFO] No new files to process")
#         return
    
#     print(f"[INFO] Found {len(new_files)} new problem(s) to process")
    
#     for py_path, readme_path, problem_id in new_files:
#         print(f"\n[INFO] Processing problem {problem_id}...")
#         print(f"[INFO] File: {py_path}")
        
#         # Git 커밋 날짜 가져오기
#         commit_date = get_git_commit_date(py_path)
#         print(f"[INFO] Commit date: {commit_date}")
        
#         create_markdown(py_path, readme_path, problem_id, commit_date)
#         save_processed_file(py_path)
    
#     print(f"\n{'='*50}")
#     print(f"[DONE] Successfully processed {len(new_files)} new problems")
#     print(f"{'='*50}")

# if __name__ == "__main__":
#     main()

==============================================================================
==============================================================================
==============================================================================

# import os
# import datetime
# import re
# import time
# import subprocess
# import ast
# from openai import OpenAI

# # ==========================================
# # 설정 (Settings)
# # ==========================================
# SOURCE_DIR = "auto_upload"
# OUTPUT_DIR = "blog_posts"
# PROCESSED_FILE = ".processed_files.txt"
# MAX_RETRIES = 3  # AI 생성 실패 시 재시도 횟수

# # ==========================================
# # 헬퍼 함수 (Helper Functions)
# # ==========================================
# def get_git_commit_date(file_path):
#     """Git에서 파일의 최초 커밋 날짜 가져오기"""
#     try:
#         # 파일이 있는 디렉토리 기준
#         cwd = os.path.dirname(os.path.abspath(file_path)) or '.'
#         result = subprocess.run(
#             ['git', 'log', '--diff-filter=A', '--follow', '--format=%aI', '--', file_path],
#             capture_output=True,
#             text=True,
#             cwd=cwd
#         )
        
#         if result.stdout.strip():
#             # ISO 8601 형식을 YYYY-MM-DD로 변환
#             date_str = result.stdout.strip().split('\n')[-1]
#             date_obj = datetime.datetime.fromisoformat(date_str.replace('Z', '+00:00'))
#             return date_obj.strftime("%Y-%m-%d")
#     except Exception as e:
#         print(f"[WARN] Could not get git date for {file_path}: {e}")
    
#     # Git 정보를 가져올 수 없으면 오늘 날짜 반환
#     return datetime.datetime.now().strftime("%Y-%m-%d")

# def load_processed_files():
#     """이미 처리된 파일 목록 로드"""
#     if os.path.exists(PROCESSED_FILE):
#         with open(PROCESSED_FILE, 'r', encoding='utf-8') as f:
#             return set(line.strip() for line in f if line.strip())
#     return set()

# def save_processed_file(file_path):
#     """처리된 파일 기록"""
#     with open(PROCESSED_FILE, 'a', encoding='utf-8') as f:
#         f.write(f"{file_path}\n")

# def get_problem_info_from_path(file_path):
#     """폴더명에서 문제 번호 추출"""
#     match = re.search(r'[/\\](\d+)\.', file_path)
#     if match:
#         return match.group(1)
#     return None

# def parse_readme(readme_path):
#     """README.md에서 문제 정보 파싱"""
#     try:
#         with open(readme_path, 'r', encoding='utf-8') as f:
#             content = f.read()
        
#         data = {
#             "title": "", "problem_id": "", "description": "",
#             "input": "", "output": "", "category": "",
#             "memory": "", "time": ""
#         }
        
#         # 제목 및 문제 번호 추출
#         title_match = re.search(r'#\s*\[.*?\]\s*(.+?)\s*-\s*(\d+)', content)
#         if title_match:
#             data["title"] = title_match.group(1).strip()
#             data["problem_id"] = title_match.group(2).strip()
        
#         # 시간 및 메모리 제한 추출
#         perf_match = re.search(r'메모리:\s*(\d+\s*KB).*?시간:\s*(\d+\s*ms)', content)
#         if perf_match:
#             data["memory"] = perf_match.group(1)
#             data["time"] = perf_match.group(2)
        
#         # 상세 내용 추출 (분류, 설명, 입력, 출력)
#         patterns = [
#             ("category", r'### 분류\s*\n(.+?)(?=\n###|\n#|\Z)'),
#             ("description", r'### 문제 설명\s*\n(.+?)(?=\n###|\n#|\Z)'),
#             ("input", r'### 입력\s*\n(.+?)(?=\n###|\n#|\Z)'),
#             ("output", r'### 출력\s*\n(.+?)(?=\n###|\n#|\Z)'),
#         ]
        
#         # 카테고리는 백준(분류) / 프로그래머스(구분) 둘 다 지원
#         cat_match = re.search(r'### (?:분류|구분)\s*\n(.+?)(?=\n###|\n#|\Z)', content, re.DOTALL)
#         if cat_match:
#             data["category"] = re.sub(r'<[^>]+>', '', cat_match.group(1).strip()).strip()

#         for key, pattern in patterns[1:]:  # category는 위에서 처리했으므로 스킵
#             match = re.search(pattern, content, re.DOTALL)
#             if match:
#                 clean_text = re.sub(r'<[^>]+>', '', match.group(1).strip())
#                 data[key] = clean_text.strip()
        
#         return data
        
#     except Exception as e:
#         print(f"[ERROR] README parsing failed: {e}")
#         return None

# # ==========================================
# # 핵심 로직 (AI Generation & Fallback)
# # ==========================================
# def extract_fallback_content(code_content):
#     """[Fallback] AI 실패 시 코드 주석을 추출하여 내용 생성"""
#     fallback_text = ""
    
#     # 1. Python Docstring ("""...""") 추출 시도
#     try:
#         tree = ast.parse(code_content)
#         docstring = ast.get_docstring(tree)
#         if docstring:
#             fallback_text = docstring
#     except:
#         pass

#     # 2. 상단 주석(#) 추출 시도 (Docstring이 없을 경우)
#     if not fallback_text:
#         comments = []
#         lines = code_content.split('\n')
#         for line in lines:
#             stripped = line.strip()
#             if stripped.startswith('#'):
#                 comments.append(stripped.lstrip('#').strip())
#             elif not stripped:
#                 continue
#             else:
#                 # 코드가 시작되면 주석 읽기 중단
#                 break
#         if comments:
#             fallback_text = "\n".join(comments)

#     # 3. Fallback 문구 생성
#     if fallback_text:
#         return f"""### 풀이 핵심 로직 (Fallback)
# {fallback_text}

# ### 동작 과정
# (코드 내 주석을 참고해주세요)

# ### 시간 복잡도
# -"""
    
#     return """### 풀이 핵심 로직
# (AI 생성 실패 및 주석 없음)

# ### 동작 과정
# -

# ### 시간 복잡도
# -"""

# def generate_solution_with_ai(problem_data, code_content, source="백준"):
#     """OpenAI GPT로 풀이 생성 (Retry 로직 포함)"""
#     api_key = os.environ.get("OPENAI_API_KEY")
#     if not api_key:
#         print("[ERROR] OPENAI_API_KEY is empty")
#         return None

#     client = OpenAI(api_key=api_key)

#     # [중요] 포맷팅 깨짐 방지를 위해 백틱을 변수로 사용합니다.
#     bt3 = "`" * 3

#     prompt = f"""{source} 문제 풀이를 작성해주세요.
# 문제: {problem_data.get('title', '')} ({problem_data.get('problem_id', '')})
# 분류: {problem_data.get('category', '')}
# 설명: {problem_data.get('description', '')}
# 입력: {problem_data.get('input', '')}
# 출력: {problem_data.get('output', '')}

# 코드:
# {bt3}python
# {code_content}
# {bt3}

# 형식:
# ### 풀이 핵심 로직
# (핵심 아이디어 2-3문장)

# ### 동작 과정
# (예시 입력으로 단계별 설명)

# ### 시간 복잡도
# (빅오 표기법)"""

#     # 재시도 루프 (Retry Loop)
#     for attempt in range(MAX_RETRIES):
#         try:
#             print(f"[DEBUG] AI request attempt {attempt + 1}/{MAX_RETRIES}...")
#             response = client.chat.completions.create(
#                 model="gpt-4o-mini",
#                 messages=[
#                     {"role": "system", "content": "당신은 알고리즘 문제 풀이를 명확하게 설명하는 전문가입니다."},
#                     {"role": "user", "content": prompt}
#                 ],
#                 temperature=0.7,
#                 max_tokens=1024
#             )
            
#             if response and response.choices:
#                 print("[OK] AI solution generated")
#                 # Rate Limit 방지를 위한 대기
#                 time.sleep(2)
#                 return response.choices[0].message.content.strip()
                
#         except Exception as e:
#             print(f"[WARN] Attempt {attempt + 1} failed: {e}")
#             # 지수 백오프 (2초, 4초, 8초 대기)
#             time.sleep(2 ** (attempt + 1))
            
#     print("[ERROR] All AI retries failed")
#     return None

# # ==========================================
# # 파일 생성 및 실행 (Main Execution)
# # ==========================================
# def create_markdown(py_path, readme_path, problem_id, commit_date, source="백준", level=None):
#     """마크다운 파일 생성"""
#     with open(py_path, 'r', encoding='utf-8') as f:
#         code_content = f.read()

#     problem_data = parse_readme(readme_path)
#     if not problem_data:
#         problem_data = {"title": f"{problem_id}번", "problem_id": problem_id}

#     # 1. AI 풀이 생성 시도
#     ai_solution = generate_solution_with_ai(problem_data, code_content, source)

#     # 2. AI 실패 시 Fallback 로직 실행 (주석 가져오기)
#     if not ai_solution:
#         print(f"[INFO] Using Fallback logic for {problem_id}...")
#         ai_solution = extract_fallback_content(code_content)

#     # [중요] 포맷팅 깨짐 방지를 위해 백틱을 변수로 사용합니다.
#     bt3 = "`" * 3
#     title = problem_data.get('title', problem_id)

#     if source == "프로그래머스":
#         level_str = f"Level {level} " if level else ""
#         post_title = f"[프로그래머스] {level_str}{title} (Python)"
#         filename = f"{commit_date}-programmers-{problem_id}.md"
#         problem_url = f"https://school.programmers.co.kr/learn/courses/30/lessons/{problem_id}"
#         categories = "categories: [Algorithm, Programmers]"
#         tags = f'tags: [python, algorithm, programmers, "{problem_id}", {problem_data.get("category", "")}]'
#         # 프로그래머스는 입/출력 섹션 없음
#         body_lines = [
#             "## 문제 링크",
#             f"[{problem_url}]({problem_url})",
#             "",
#             "## 문제",
#             problem_data.get("description", "-") or "-",
#             "",
#             "## 풀이",
#             ai_solution,
#             "",
#             "## 코드",
#             f"{bt3}python",
#             code_content,
#             bt3,
#         ]
#     else:
#         post_title = f"[백준] {problem_id}번 {title} (Python)"
#         filename = f"{commit_date}-baekjoon-{problem_id}.md"
#         problem_url = f"https://www.acmicpc.net/problem/{problem_id}"
#         categories = "categories: [Algorithm, Baekjoon]"
#         tags = f'tags: [python, algorithm, baekjoon, "{problem_id}", {problem_data.get("category", "")}]'
#         body_lines = [
#             "## 문제 링크",
#             f"[{problem_url}]({problem_url})",
#             "",
#             "## 문제",
#             problem_data.get("description", "-") or "-",
#             "",
#             "## 입력",
#             problem_data.get("input", "-") or "-",
#             "",
#             "## 출력",
#             problem_data.get("output", "-") or "-",
#             "",
#             "## 풀이",
#             ai_solution,
#             "",
#             "## 코드",
#             f"{bt3}python",
#             code_content,
#             bt3,
#         ]

#     # Front Matter 및 전체 내용 조립
#     lines = [
#         "---",
#         "layout: post",
#         f'title: "{post_title}"',
#         f"date: {commit_date}",
#         categories,
#         tags,
#         "---",
#         "",
#         *body_lines,
#     ]
    
#     if not os.path.exists(OUTPUT_DIR):
#         os.makedirs(OUTPUT_DIR)

#     output_path = os.path.join(OUTPUT_DIR, filename)
#     with open(output_path, 'w', encoding='utf-8') as f:
#         f.write("\n".join(lines))
    
#     print(f"[OK] Created: {filename}")

# def process_directory(source_dir, source, processed_files):
#     """지정된 디렉토리의 파일들을 처리"""
#     if not os.path.exists(source_dir):
#         print(f"[WARN] Directory not found: {source_dir}")
#         return

#     for root, dirs, files in os.walk(source_dir):
#         if ".git" in root or OUTPUT_DIR in root:
#             continue

#         py_files = [f for f in files if f.endswith(".py")]

#         for py_file in py_files:
#             py_path = os.path.join(root, py_file)
#             readme_path = os.path.join(root, "README.md")

#             if not os.path.exists(readme_path):
#                 continue

#             if py_path in processed_files:
#                 continue

#             problem_id = get_problem_info_from_path(py_path)
#             if not problem_id:
#                 continue

#             # 프로그래머스는 경로에서 레벨 추출 (예: 프로그래머스/2/...)
#             level = None
#             if source == "프로그래머스":
#                 level_match = re.search(r'프로그래머스[/\\](\d+)[/\\]', py_path)
#                 if level_match:
#                     level = level_match.group(1)

#             print(f"\n[INFO] [{source}] Processing: {problem_id}")
#             commit_date = get_git_commit_date(py_path)
#             create_markdown(py_path, readme_path, problem_id, commit_date, source=source, level=level)
#             save_processed_file(py_path)


# def main():
#     print(f"[INFO] Starting converter...")
#     processed_files = load_processed_files()

#     process_directory(os.path.join(SOURCE_DIR, "백준"), "백준", processed_files)
#     process_directory(os.path.join(SOURCE_DIR, "프로그래머스"), "프로그래머스", processed_files)

#     print(f"\n[DONE] Processing complete.")

# if __name__ == "__main__":
#     main()

==============================================================================
==============================================================================
==============================================================================

import os
import datetime
import re
import time
import subprocess
import ast
from openai import OpenAI

# ==========================================
# 설정 (Settings)
# ==========================================
SOURCE_DIR = "auto_upload"
OUTPUT_DIR = "blog_posts"
PROCESSED_FILE = ".processed_files.txt"
MAX_RETRIES = 3  # AI 생성 실패 시 재시도 횟수


# ==========================================
# YAML / Markdown 안전 처리 유틸
# ==========================================
def yaml_escape(text):
    """YAML double-quoted string 안전 escape"""
    if text is None:
        return ""
    return str(text).replace("\\", "\\\\").replace('"', '\\"')


def split_category_tags(category_text):
    """
    category 문자열을 tags용 리스트로 분리
    예:
    '구현, 문자열' -> ['구현', '문자열']
    'dp / 그래프' -> ['dp', '그래프']
    """
    if not category_text:
        return []

    cleaned = re.sub(r'\s+', ' ', str(category_text)).strip()
    parts = re.split(r'[,/|]+', cleaned)
    return [p.strip() for p in parts if p.strip()]


def build_tags(problem_id, category_text, source, level=None):
    """tags 배열 안전 생성"""
    tags = ["python", "algorithm"]

    if source == "백준":
        tags.append("baekjoon")
    elif source == "프로그래머스":
        tags.append("programmers")
        if level:
            tags.append(f"level{level}")

    if problem_id:
        tags.append(str(problem_id))

    tags.extend(split_category_tags(category_text))

    # 중복 제거(순서 유지)
    deduped = []
    seen = set()
    for tag in tags:
        if tag not in seen:
            deduped.append(tag)
            seen.add(tag)

    return deduped


def render_yaml_list(items):
    """YAML inline list 문자열 생성"""
    safe_items = [f'"{yaml_escape(item)}"' for item in items if str(item).strip()]
    return "[" + ", ".join(safe_items) + "]"


def sanitize_markdown_content(text):
    """
    AI 출력 등에서 raw HTML로 들어온 위험한 anchor 태그 최소 정리
    - href 없는 <a> 제거
    - </a> 제거
    - href="" 빈 링크 제거
    """
    if not text:
        return text

    # href 없는 <a ...> 제거
    text = re.sub(r'<a(?![^>]*href=)[^>]*>', '', text, flags=re.IGNORECASE)

    # href="" 또는 href='' 인 a 태그 제거
    text = re.sub(r'<a[^>]*href\s*=\s*["\']\s*["\'][^>]*>', '', text, flags=re.IGNORECASE)

    # 닫는 태그 제거
    text = re.sub(r'</a>', '', text, flags=re.IGNORECASE)

    return text


# ==========================================
# 헬퍼 함수 (Helper Functions)
# ==========================================
def get_git_commit_date(file_path):
    """Git에서 파일의 최초 커밋 날짜 가져오기"""
    try:
        repo_root_result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True
        )
        repo_root = repo_root_result.stdout.strip()

        rel_path = os.path.relpath(os.path.abspath(file_path), repo_root)

        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%aI", "--", rel_path],
            capture_output=True,
            text=True,
            cwd=repo_root,
            check=False
        )

        if result.stdout.strip():
            date_str = result.stdout.strip().split("\n")[-1]
            date_obj = datetime.datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            return date_obj.strftime("%Y-%m-%d")

    except Exception as e:
        print(f"[WARN] Could not get git date for {file_path}: {e}")

    return datetime.datetime.now().strftime("%Y-%m-%d")


def load_processed_files():
    """이미 처리된 파일 목록 로드"""
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    return set()


def save_processed_file(file_path):
    """처리된 파일 기록"""
    with open(PROCESSED_FILE, "a", encoding="utf-8") as f:
        f.write(f"{file_path}\n")


def get_problem_info_from_path(file_path):
    """
    경로에서 문제 번호 추출
    예:
    auto_upload/백준/Silver/1234. 문제명/정답.py
    auto_upload/프로그래머스/2/12909. 올바른 괄호/solution.py
    """
    parts = re.split(r"[/\\]", file_path)

    for part in parts:
        m = re.match(r"^(\d+)", part.strip())
        if m:
            return m.group(1)

    return None


def parse_readme(readme_path):
    """README.md에서 문제 정보 파싱"""
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
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

        # 제목 및 문제 번호 추출
        title_match = re.search(r"#\s*\[.*?\]\s*(.+?)\s*-\s*(\d+)", content)
        if title_match:
            data["title"] = title_match.group(1).strip()
            data["problem_id"] = title_match.group(2).strip()

        # 시간 및 메모리 추출
        perf_match = re.search(r"메모리:\s*(\d+\s*KB).*?시간:\s*(\d+\s*ms)", content, re.DOTALL)
        if perf_match:
            data["memory"] = perf_match.group(1).strip()
            data["time"] = perf_match.group(2).strip()

        # 카테고리(백준/프로그래머스 둘 다 대응)
        cat_match = re.search(r"###\s*(?:분류|구분)\s*\n(.+?)(?=\n###|\n#|\Z)", content, re.DOTALL)
        if cat_match:
            data["category"] = re.sub(r"<[^>]+>", "", cat_match.group(1).strip()).strip()

        # 문제 설명 / 입력 / 출력
        section_patterns = {
            "description": r"###\s*문제 설명\s*\n(.+?)(?=\n###|\n#|\Z)",
            "input": r"###\s*입력\s*\n(.+?)(?=\n###|\n#|\Z)",
            "output": r"###\s*출력\s*\n(.+?)(?=\n###|\n#|\Z)",
        }

        for key, pattern in section_patterns.items():
            match = re.search(pattern, content, re.DOTALL)
            if match:
                clean_text = re.sub(r"<[^>]+>", "", match.group(1).strip()).strip()
                data[key] = clean_text

        return data

    except Exception as e:
        print(f"[ERROR] README parsing failed: {e}")
        return None


# ==========================================
# AI 실패 시 Fallback
# ==========================================
def extract_fallback_content(code_content):
    """AI 실패 시 코드 주석 / docstring 기반 fallback 생성"""
    fallback_text = ""

    # 1) docstring
    try:
        tree = ast.parse(code_content)
        docstring = ast.get_docstring(tree)
        if docstring:
            fallback_text = docstring.strip()
    except Exception:
        pass

    # 2) 상단 주석
    if not fallback_text:
        comments = []
        lines = code_content.split("\n")
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#"):
                comments.append(stripped.lstrip("#").strip())
            elif not stripped:
                continue
            else:
                break

        if comments:
            fallback_text = "\n".join(comments).strip()

    if fallback_text:
        return f"""### 풀이 핵심 로직 (Fallback)
{fallback_text}

### 동작 과정
(코드 내 주석을 참고해주세요)

### 시간 복잡도
-"""

    return """### 풀이 핵심 로직
(AI 생성 실패 및 주석 없음)

### 동작 과정
-

### 시간 복잡도
-"""


# ==========================================
# AI 생성
# ==========================================
def generate_solution_with_ai(problem_data, code_content, source="백준"):
    """OpenAI GPT로 풀이 생성 (Retry 포함)"""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("[ERROR] OPENAI_API_KEY is empty")
        return None

    client = OpenAI(api_key=api_key)
    bt3 = "`" * 3

    prompt = f"""{source} 문제 풀이를 작성해주세요.
문제: {problem_data.get('title', '')} ({problem_data.get('problem_id', '')})
분류: {problem_data.get('category', '')}
설명: {problem_data.get('description', '')}
입력: {problem_data.get('input', '')}
출력: {problem_data.get('output', '')}

코드:
{bt3}python
{code_content}
{bt3}

반드시 아래 형식으로만 작성해주세요.

### 풀이 핵심 로직
(핵심 아이디어 2-3문장)

### 동작 과정
(예시 입력으로 단계별 설명)

### 시간 복잡도
(빅오 표기법)
"""

    for attempt in range(MAX_RETRIES):
        try:
            print(f"[DEBUG] AI request attempt {attempt + 1}/{MAX_RETRIES}...")

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "당신은 알고리즘 문제 풀이를 명확하게 설명하는 전문가입니다. HTML 태그를 사용하지 말고 Markdown만 사용하세요."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.4,
                max_tokens=1024
            )

            if response and response.choices and response.choices[0].message.content:
                print("[OK] AI solution generated")
                time.sleep(2)
                return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"[WARN] Attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** (attempt + 1))

    print("[ERROR] All AI retries failed")
    return None


# ==========================================
# 마크다운 생성
# ==========================================
def create_markdown(py_path, readme_path, problem_id, commit_date, source="백준", level=None):
    """마크다운 파일 생성"""
    with open(py_path, "r", encoding="utf-8") as f:
        code_content = f.read()

    problem_data = parse_readme(readme_path)
    if not problem_data:
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
    ai_solution = generate_solution_with_ai(problem_data, code_content, source)

    # 실패 시 fallback
    if not ai_solution:
        print(f"[INFO] Using Fallback logic for {problem_id}...")
        ai_solution = extract_fallback_content(code_content)

    # HTML 위험 태그 정리
    ai_solution = sanitize_markdown_content(ai_solution)

    bt3 = "`" * 3
    title = problem_data.get("title", str(problem_id)).strip()
    category_text = problem_data.get("category", "").strip()

    if source == "프로그래머스":
        level_str = f"Level {level} " if level else ""
        post_title = f"[프로그래머스] {level_str}{title} (Python)"
        filename = f"{commit_date}-programmers-{problem_id}.md"
        problem_url = f"https://school.programmers.co.kr/learn/courses/30/lessons/{problem_id}"
        categories_list = ["Algorithm", "Programmers"]
        tags_list = build_tags(problem_id, category_text, source, level=level)

        body_lines = [
            "## 문제 링크",
            f"[{problem_url}]({problem_url})",
            "",
            "## 문제",
            problem_data.get("description", "-") or "-",
            "",
            "## 풀이",
            ai_solution,
            "",
            "## 코드",
            f"{bt3}python",
            code_content,
            bt3,
        ]
    else:
        post_title = f"[백준] {problem_id}번 {title} (Python)"
        filename = f"{commit_date}-baekjoon-{problem_id}.md"
        problem_url = f"https://www.acmicpc.net/problem/{problem_id}"
        categories_list = ["Algorithm", "Baekjoon"]
        tags_list = build_tags(problem_id, category_text, source)

        body_lines = [
            "## 문제 링크",
            f"[{problem_url}]({problem_url})",
            "",
            "## 문제",
            problem_data.get("description", "-") or "-",
            "",
            "## 입력",
            problem_data.get("input", "-") or "-",
            "",
            "## 출력",
            problem_data.get("output", "-") or "-",
            "",
            "## 성능 요약",
            f"메모리: {problem_data.get('memory', '-') or '-'}, 시간: {problem_data.get('time', '-') or '-'}",
            "",
            "## 풀이",
            ai_solution,
            "",
            "## 코드",
            f"{bt3}python",
            code_content,
            bt3,
        ]

    lines = [
        "---",
        "layout: post",
        f'title: "{yaml_escape(post_title)}"',
        f"date: {commit_date}",
        f"categories: {render_yaml_list(categories_list)}",
        f"tags: {render_yaml_list(tags_list)}",
        "---",
        "",
        *body_lines,
        ""
    ]

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    output_path = os.path.join(OUTPUT_DIR, filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[OK] Created: {filename}")


# ==========================================
# 디렉토리 처리
# ==========================================
def process_directory(source_dir, source, processed_files):
    """지정된 디렉토리의 파일들을 처리"""
    if not os.path.exists(source_dir):
        print(f"[WARN] Directory not found: {source_dir}")
        return

    for root, dirs, files in os.walk(source_dir):
        if ".git" in root or OUTPUT_DIR in root:
            continue

        py_files = [f for f in files if f.endswith(".py")]

        for py_file in py_files:
            py_path = os.path.join(root, py_file)
            readme_path = os.path.join(root, "README.md")

            if not os.path.exists(readme_path):
                continue

            if py_path in processed_files:
                continue

            problem_id = get_problem_info_from_path(py_path)
            if not problem_id:
                print(f"[WARN] Could not extract problem_id from path: {py_path}")
                continue

            level = None
            if source == "프로그래머스":
                level_match = re.search(r"프로그래머스[/\\](\d+)[/\\]", py_path)
                if level_match:
                    level = level_match.group(1)

            print(f"\n[INFO] [{source}] Processing: {problem_id}")
            print(f"[INFO] File: {py_path}")

            commit_date = get_git_commit_date(py_path)
            print(f"[INFO] Commit date: {commit_date}")

            create_markdown(
                py_path=py_path,
                readme_path=readme_path,
                problem_id=problem_id,
                commit_date=commit_date,
                source=source,
                level=level
            )
            save_processed_file(py_path)


# ==========================================
# 메인 실행
# ==========================================
def main():
    print("[INFO] Starting converter...")
    print(f"[INFO] SOURCE_DIR={SOURCE_DIR}")
    print(f"[INFO] OUTPUT_DIR={OUTPUT_DIR}")
    print(f"[INFO] OPENAI_API_KEY exists: {bool(os.environ.get('OPENAI_API_KEY'))}")

    processed_files = load_processed_files()
    print(f"[INFO] Already processed: {len(processed_files)} files")

    process_directory(os.path.join(SOURCE_DIR, "백준"), "백준", processed_files)
    process_directory(os.path.join(SOURCE_DIR, "프로그래머스"), "프로그래머스", processed_files)

    print("\n[DONE] Processing complete.")


if __name__ == "__main__":
    main()
