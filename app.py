# app.py

import streamlit as st
import random

# 관광지 데이터
destinations = [
    {
        "name": "경복궁",
        "description": "한국의 전통과 역사를 경험할 수 있는 서울의 대표 유적지입니다.",
        "image_url": "https://example.com/경복궁.jpg",
        "tags": ["문화", "역사 탐방", "도심", "유적지", "문화 체험"]
    },
    {
        "name": "제주도 성산 일출봉",
        "description": "아름다운 일출과 함께 자연을 만끽할 수 있는 제주의 인기 명소입니다.",
        "image_url": "https://example.com/성산일출봉.jpg",
        "tags": ["자연 탐험", "자연", "바다", "사진 명소", "힐링"]
    },
    {
        "name": "수원화성",
        "description": "한국의 전통과 역사를 경험할 수 있는 수원의 대표 유적지입니다.",
        "image_url": "https://sl.bing.net/VIE13OkuYe",
        "tags": ["문화", "역사 탐방", "도심", "유적지", "문화 체험"]
    }
]

# 질문
questions = [
    "어떤 종류의 활동을 즐기시나요? (문화, 역사 탐방 / 자연 탐험/쇼핑/액티비티/예술)",
    "어떤 환경에서 여행을 즐기고 싶으신가요? (도심/자연/바다/유적지)",
    "여행 중 어떤 경험을 가장 중시하시나요? (사진 명소/문화 체험/힐링/도전적인 활동/새로운 음식 시도)",
    "여행 중 어떤 것을 가장 중요하게 생각하시나요? (좋은 접근성 / 독특한 장소/ 저렴한 가격/ 안전하고 편안한 환경)"
]

# Streamlit 앱 레이아웃 설정
st.title("여행 스타일 기반 관광지 추천 챗봇")

user_answers = []  # 사용자의 답변을 저장

# 각 질문에 대해 선택할 수 있도록 UI를 구성
for i, question in enumerate(questions):
    answer = st.selectbox(question, options=destinations[i]["tags"], key=f"question_{i}")
    user_answers.append(answer)

# 추천 버튼
if st.button("추천받기"):
    # 답변을 바탕으로 관광지 추천
    matched_destinations = [
        destination for destination in destinations
        if all(answer in destination["tags"] for answer in user_answers)
    ]
    
    # 일치하는 관광지가 부족할 경우 무작위로 두 개 선택
    if len(matched_destinations) < 2:
        matched_destinations = random.sample(destinations, 2)
    
    # 추천 결과 표시
    for place in random.sample(matched_destinations, 2):
        st.subheader(place["name"])
        st.write(place["description"])
        st.image(place["image_url"], use_column_width=True)
