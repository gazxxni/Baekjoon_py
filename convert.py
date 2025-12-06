import os
import datetime
import re

# 백준허브가 코드를 저장하는 디렉토리 구조에 맞춰 설정 (보통 '백준' 폴더 등)
# 깃허브 레포지토리의 구조를 봐야 정확하지만, 보통 최상위나 특정 폴더를 순회하도록 설정합니다.
SOURCE_DIR = "." 
POSTS_DIR = "_posts"  # 깃허브 블로그의 포스팅 저장 폴더 (Jekyll 기준)

def get_problem_info(filename):
    # 파일명에서 문제 번호 추출 (예: 1234.py -> 1234)
    match = re.search(r'(\d+)', filename)
    if match:
        return match.group(1)
    return None

def create_markdown(file_path, problem_id):
    # 오늘 날짜
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 소스 코드 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        code_content = f.read()

    # 파일 확장자에 따른 언어 설정
    ext = os.path.splitext(file_path)[1]
    language = "python" if ext == ".py" else "text"

    # 블로그 포스트 제목 생성
    post_title = f"[백준] {problem_id}번 풀이 (파이썬)"
    filename = f"{today}-baekjoon-{problem_id}.md"
    
    # 분석한 티스토리 스타일 템플릿 적용
    markdown_content = f"""---
layout: post
title:  "{post_title}"
date:   {today}
categories: [Algorithm, Baekjoon]
tags: [IT, 코드, 코딩, 파이썬, Algorithm, 풀이, 백준, 코테, baekjoon, {problem_id}]
---

#### **문제 링크**
[https://www.acmicpc.net/problem/{problem_id}](https://www.acmicpc.net/problem/{problem_id})

---

#### **문제**
(문제 설명 이미지는 저작권 및 기술적 이슈로 자동 첨부되지 않습니다. 위 링크를 참고하세요.)

---

#### **입력**
(입력 설명)

---

#### **출력**
(출력 설명)

---

#### **예제 입출력**
(예제 입출력)

---

#### **문제 풀이 및 코드**

- 문제의 핵심 로직을 여기에 작성하세요.
- (자동 생성된 포스팅입니다. 구체적인 풀이 설명은 수정이 필요합니다.)

**총 시간 복잡도: O(N)** (알고리즘에 맞춰 수정 필요)

```{language}
{code_content}

#IT #코드 #코딩 #파이썬 #Algorithm #풀이 #백준 #코테 #baekjoon #{problem_id} """

# _posts 폴더가 없으면 생성
if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

# 파일 쓰기
output_path = os.path.join(POSTS_DIR, filename)
# 이미 생성된 파일이 없을 경우에만 생성 (중복 방지)
if not os.path.exists(output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"Created post: {filename}")
else:
    print(f"Skipped (already exists): {filename}")

def main(): # 모든 파일 순회하며 .py 파일 찾기 for root, dirs, files in os.walk(SOURCE_DIR): # .git 폴더나 _posts 폴더 등은 제외 if ".git" in root or "_posts" in root: continue

    for file in files:
        if file.endswith(".py"): # 파이썬 파일만 대상
            problem_id = get_problem_info(file)
            if problem_id:
                create_markdown(os.path.join(root, file), problem_id)
if name == "main": main()
