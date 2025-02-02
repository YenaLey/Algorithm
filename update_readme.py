import requests
import datetime
import os
from bs4 import BeautifulSoup

USERNAME = "lyn010913"  # 백준 ID
README_PATH = "README.md"
TIER_LOG_PATH = "tier_log.txt"  # 티어 변경 로그 저장 파일
GRASS_IMAGE_PATH = "baekjoon_grass.svg"  # 백준 잔디 그래프 저장 파일
SOLVED_AC_BADGE = f"https://mazassumnida.wtf/api/v2/generate_badge?boj={USERNAME}"  # Solved.ac 티어 뱃지
BAEKJOON_PROFILE_URL = f"https://www.acmicpc.net/user/{USERNAME}"  # 백준 프로필 URL

# 백준 solved.ac API 요청 (현재 티어 가져오기)
def get_baekjoon_tier(username):
    url = f"https://solved.ac/api/v3/user/show?handle={username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["tier"]
    return None

# 티어 변환 (solved.ac 티어 값 → 문자열)
def convert_tier(tier_num):
    tiers = [
        "Unrated", "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I",
        "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I",
        "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I",
        "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I",
        "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I",
        "Ruby V", "Ruby IV", "Ruby III", "Ruby II", "Ruby I"
    ]
    return tiers[tier_num] if 0 <= tier_num < len(tiers) else "Unknown"

# 백준 잔디 그래프 크롤링 & 저장
def fetch_baekjoon_grass():
    response = requests.get(BAEKJOON_PROFILE_URL)
    
    if response.status_code != 200:
        print("백준 프로필 페이지를 가져오는 데 실패했습니다.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    svg_element = soup.find("svg", class_="js-calendar-graph-svg")  # 백준 잔디 그래프를 포함하는 SVG 태그 찾기
    
    if not svg_element:
        print("백준 잔디 그래프를 찾을 수 없습니다.")
        return

    with open(GRASS_IMAGE_PATH, "w", encoding="utf-8") as file:
        file.write(str(svg_element))

# README 업데이트
def update_readme():
    tier_num = get_baekjoon_tier(USERNAME)
    tier_str = convert_tier(tier_num)
    today_date = datetime.date.today().strftime("%Y-%m-%d")

    # 기존 티어 정보 로드
    previous_tier = None
    if os.path.exists(TIER_LOG_PATH):
        with open(TIER_LOG_PATH, "r", encoding="utf-8") as file:
            previous_tier = file.readline().strip()

    # 티어 변경 감지 & 로그 기록
    tier_log = []
    if tier_str != previous_tier:
        tier_log.append(f"| {today_date} | {tier_str} |\n")
        with open(TIER_LOG_PATH, "w", encoding="utf-8") as file:
            file.write(tier_str)  # 최신 티어 저장

    # README 불러오기
    with open(README_PATH, "r+", encoding="utf-8") as file:
        content = file.readlines()

    # 티어 변경 로그 위치 찾기
    tier_log_start = None
    for i, line in enumerate(content):
        if "| Date | Tier |" in line:
            tier_log_start = i + 2

    # 티어 변경 로그 추가
    tier_log_data = content[tier_log_start:] if tier_log_start else []
    tier_log_data = tier_log + tier_log_data

    # README 업데이트
    new_readme = (
        "## 🏆 Baekjoon Tier Badge\n\n"
        f"![Baekjoon Tier]({SOLVED_AC_BADGE})\n\n"
        "## 🌱 Baekjoon Contribution Graph\n\n"
        f"<img src=\"./{GRASS_IMAGE_PATH}\" alt=\"Baekjoon Grass\" />\n\n"
        "## 📜 Tier Change Log\n\n"
        "| Date | Tier |\n"
        "|------|------|\n"
        + "".join(tier_log_data) + "\n"
    )

    # 파일 업데이트
    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(new_readme)

if __name__ == "__main__":
    fetch_baekjoon_grass()  # 백준 잔디 크롤링
    update_readme()  # README 업데이트
