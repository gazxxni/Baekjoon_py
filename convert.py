import os
import datetime
import re

# 설정: 소스 경로와 출력 경로
SOURCE_DIR = "."
OUTPUT_DIR = "blog_posts"

def get_problem_info(filename):
    match = re.search(r'(\d+)', filename)
    if match:
        return match.group(1)
    return None

def create_markdown(file_path, problem_id):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        code_content = f.read()

    ext = os.path.splitext(file_path)[1]
    language = "python" if ext == ".py" else "text"
    post_title = f"[백준] {problem_id}번 풀이 (파이썬)"
    filename = f"{today}-baekjoon-{problem_id}.md"

    # 블로그 본문 내용을 줄 단위로 리스트에 담아 합칩니다 (오류 방지용)
    lines = [
        "---",
        "layout: post",
        f"title:  \"{post_title}\"",
        f"date:   {today}",
        "categories: [Algorithm, Baekjoon]",
        f"tags: [IT, 코드, 코딩, 파이썬, Algorithm, 풀이, 백준, 코테, baekjoon, {problem_id}]",
        "---",
        "",
        "#### **문제 링크**",
        f"[https://www.acmicpc.net/problem/{problem_id}](https://www.acmicpc.net/problem/{problem_id})",
        "",
        "---",
        "",
        "#### **문제**",
        "(문제 설명 이미지는 저작권 및 기술적 이슈로 자동 첨부되지 않습니다. 위 링크를 참고하세요.)",
        "",
        "---",
        "",
        "#### **입력**",
        "(입력 설명)",
        "",
        "---",
        "",
        "#### **출력**",
        "(출력 설명)",
        "",
        "---",
        "",
        "#### **예제 입출력**",
        "(예제 입출력)",
        "",
        "---",
        "",
        "#### **문제 풀이 및 코드**",
        "",
        "- 문제의 핵심 로직을 여기에 작성하세요.",
        "- (자동 생성된 포스팅입니다. 구체적인 풀이 설명은 수정이 필요합니다.)",
        "",
        "**총 시간 복잡도: O(N)** (알고리즘에 맞춰 수정 필요)",
        "",
        f"```{language}",
        code_content,
        "```",
        "",
        f"#IT #코드 #코딩 #파이썬 #Algorithm #풀이 #백준 #코테 #baekjoon #{problem_id}"
    ]
    
    # 리스트를 하나의 문자열로 합침
    markdown_content = "\n".join(lines)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    output_path = os.path.join(OUTPUT_DIR, filename)
    
    if not os.path.exists(output_path):
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Created post: {filename}")
    else:
        print(f"Skipped (already exists): {filename}")

def main():
    for root, dirs, files in os.walk(SOURCE_DIR):
        # .git 폴더나 출력 폴더는 제외
        if ".git" in root or OUTPUT_DIR in root:
            continue
            
        for file in files:
            if file.endswith(".py"):
                problem_id = get_problem_info(file)
                if problem_id:
                    create_markdown(os.path.join(root, file), problem_id)

if __name__ == "__main__":
    main()
