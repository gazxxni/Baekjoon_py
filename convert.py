import os
import datetime
import re
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

SOURCE_DIR = "auto_upload"  # 변경: 백준허브 폴더 지정
OUTPUT_DIR = "blog_posts"

def get_problem_info(file_path):
    """파일 경로(폴더명)에서 문제 번호 추출"""
    # 폴더 경로에서 문제번호 찾기 (예: "10101. 삼각형 외우기")
    match = re.search(r'/(\d+)\.', file_path)
    if match:
        return match.group(1)
    # 윈도우 경로 대응
    match = re.search(r'\\(\d+)\.', file_path)
    if match:
        return match.group(1)
    return None

def scrape_problem_data(problem_id):
    url = f"https://www.acmicpc.net/problem/{problem_id}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        desc_elem = soup.select_one("#problem_description")
        input_elem = soup.select_one("#problem_input")
        output_elem = soup.select_one("#problem_output")
        
        description = desc_elem.get_text("\n", strip=True) if desc_elem else "문제 설명을 가져올 수 없습니다."
        input_text = input_elem.get_text("\n", strip=True) if input_elem else "입력 설명을 가져올 수 없습니다."
        output_text = output_elem.get_text("\n", strip=True) if output_elem else "출력 설명을 가져올 수 없습니다."
        
        sample_io = []
        index = 1
        while True:
            sample_input = soup.select_one(f"#sample-input-{index}")
            sample_output = soup.select_one(f"#sample-output-{index}")
            
            if not sample_input or not sample_output:
                break
                
            input_val = sample_input.get_text("\n", strip=True)
            output_val = sample_output.get_text("\n", strip=True)
            
            sample_io.append(f"**예제 입력 {index}**\n```\n{input_val}\n```")
            sample_io.append(f"**예제 출력 {index}**\n```\n{output_val}\n```")
            index += 1
            
        sample_io_text = "\n\n".join(sample_io) if sample_io else "예제 입출력이 없습니다."
        
        return {
            "description": description,
            "input": input_text,
            "output": output_text,
            "sample": sample_io_text
        }
        
    except Exception as e:
        print(f"Error scraping problem {problem_id}: {e}")
        return None

def generate_logic_with_ai(problem_id, problem_data, code_content):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        당신은 알고리즘 블로그 작성자입니다. 다음 백준 문제와 파이썬 정답 코드를 보고 블로그 포스팅에 들어갈 '문제 풀이 핵심 로직'과 '시간 복잡도'를 작성해주세요.

        [문제 정보]
        번호: {problem_id}
        설명: {problem_data['description'][:500]}...

        [파이썬 코드]
        {code_content}

        [요청사항]
        1. 독자가 이해하기 쉽게 풀이 과정을 단계별로 설명해주세요.
        2. 시간 복잡도를 빅오 표기법으로 명시해주세요.
        3. 반환 형식은 마크다운 그대로 블로그 본문에 넣을 수 있게 작성해주세요. 서론이나 인사말은 생략하세요.
        """
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"AI Generation Failed: {e}")
        return None

def extract_logic_from_code(code_content):
    match = re.match(r'\s*"""(.*?)"""|\s*\'\'\'(.*?)\'\'\'', code_content, re.DOTALL)
    if match:
        logic = match.group(1) or match.group(2)
        return logic.strip()
    return "코드 상단에 주석을 작성하거나 AI API 키를 등록하면 자동으로 내용이 채워집니다."

def create_markdown(file_path, problem_id):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        code_content = f.read()

    problem_data = scrape_problem_data(problem_id)
    if not problem_data:
        problem_data = {
            "description": "정보 없음", "input": "-", "output": "-", "sample": "-"
        }

    logic_content = generate_logic_with_ai(problem_id, problem_data, code_content)
    if not logic_content:
        logic_content = extract_logic_from_code(code_content)

    ext = os.path.splitext(file_path)[1]
    language = "python" if ext == ".py" else "text"
    post_title = f"[백준] {problem_id}번 풀이 (파이썬)"
    filename = f"{today}-baekjoon-{problem_id}.md"

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
        problem_data["description"],
        "",
        "---",
        "",
        "#### **입력**",
        problem_data["input"],
        "",
        "---",
        "",
        "#### **출력**",
        problem_data["output"],
        "",
        "---",
        "",
        "#### **예제 입출력**",
        problem_data["sample"],
        "",
        "---",
        "",
        "#### **문제 풀이 및 코드**",
        "",
        logic_content,
        "",
        f"```{language}",
        code_content,
        "```",
        "",
        f"#IT #코드 #코딩 #파이썬 #Algorithm #풀이 #백준 #코테 #baekjoon #{problem_id}"
    ]
    
    markdown_content = "\n".join(lines)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    output_path = os.path.join(OUTPUT_DIR, filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"Created post: {filename}")

def main():
    processed = set()  # 중복 방지
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        if ".git" in root or OUTPUT_DIR in root:
            continue
            
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                problem_id = get_problem_info(file_path)  # 경로 전체 전달
                
                if problem_id and problem_id not in processed:
                    print(f"Processing: {file_path} -> Problem {problem_id}")
                    create_markdown(file_path, problem_id)
                    processed.add(problem_id)

if __name__ == "__main__":
    main()
