# app.py

import streamlit as st
import random

# 관광지 데이터
destinations = [
    {
        "name": "경복궁",
        "description": "한국의 전통과 역사를 경험할 수 있는 서울의 대표 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA5MDRfODcg%2FMDAxNzI1NDU5OTg1ODcx.20ZW5yxoZO6aCc1Ds-nDzGMyAx-qObh5n9Ke5Jo3HVYg.JA7cHnv7gZ2JWYfRzBJ5s-xZVCq40sBvwqOmLGsZ5kog.JPEG%2F3C4A9776_1.jpg&type=sc960_832",
        "tags": ["문화, 역사 탐방", "도심", "유적지", "문화 체험", "사진 명소"]
    },
    {
        "name": "제주도 성산 일출봉",
        "description": "아름다운 일출과 함께 자연을 만끽할 수 있는 제주의 인기 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA4MDhfMjk2%2FMDAxNjkxNDYxNDQxNTY4.6Ev421h1hStxTq98GjJ3qKSKLJ6uXGvaJbj4r2odk0kg.rCANTQkA8QVDm9IpRBgiHKfdKZ-FGs-jd4cgKElBoqgg.PNG.raimongmall%2F%25BC%25BA%25BB%25EA%25C0%25CF%25C3%25E2%25BA%25C0.png&type=sc960_832",
        "tags": ["자연 탐험", "자연", "바다", "사진 명소", "힐링"]
    },
    {
        "name": "수원화성",
        "description": "한국의 전통과 역사를 경험할 수 있는 수원의 대표 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA1MjNfMTYw%2FMDAxNzE2MzkwNDkzNTkw.hGbTTrdhPUfzRFbRWP43dpPpRTLXfWC2QbadfEv-ewcg.-J48L9rp25B-ek0ZpX-fiVUQIpyctcjCV34yJC3RRDkg.JPEG%2F20240426-_C6A8780.jpg&type=sc960_832",
        "tags": ["문화, 역사 탐방", "도심", "사진 명소", "유적지", "문화 체험"]
    },
    {
        "name": "서울숲",
        "description": "푸르른 한강과 함께 자연을 즐길 수 있는 서울의 인기있는 힐링 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200728_296%2F1595899415265D5A3d_JPEG%2F%25B0%25A1%25C1%25B7%25B8%25B6%25B4%25E71.jpg",
        "tags": ["자연 탐험", "자연", "사진 명소", "힐링", "좋은 접근성"]
    },
    {
        "name": "남산서울타워",
        "description": "서울 도심 속에서 밝게 빛나는 야경 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190711_62%2F1562823704121InE2t_JPEG%2Fusfc9L8iEAQfjJK8oKoBwa4d.jpg",
        "tags": ["자연 탐험", "자연", "사진 명소", "힐링", "좋은 접근성"]
    },
    {
        "name": "더현대 서울",
        "description": "즐거운 먹거리를 즐기고, 쇼핑을 할 수 있는 현대백화점 더현대 서울입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210527_297%2F16220986701968f1N7_JPEG%2F1.jpg",
        "tags": ["쇼핑", "도심", "사진 명소", "새로운 음식 시도", "좋은 접근성"]
    },
    {
        "name": "코엑스",
        "description": "도서관, 팝업스토어, 영화관, 음식점 등 여러 활동을 즐길 수 있는 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAzMDFfMTM1%2FMDAxNzA5MjkzMjk5MTA4.gdVknLSuCHHQuBK9_SHBnqe_rN0P5WV5WNF4FORD8tcg.Fbe6GAgm6FSNxiXz0uJ01v1zPFhhCsCHICjwM3ChaR0g.JPEG%2F0cosunokci003.jpg&type=sc960_832",
        "tags": ["쇼핑", "문학 활동" "도심", "사진 명소", "새로운 음식 시도", "예술 관련 교양 쌓기", "좋은 접근성"]
    },
    {
        "name": "예술의 전당",
        "description": "음악, 미술, 무용, 뮤지컬 등 여러 공연을 즐길 수 있는 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEyMDVfMTI2%2FMDAxNzAxNzQ4ODQzMjQz.LwfjHhRI_NeOqn-vOd1rH_MrXE4tlwHFl5y1Ov0iPlcg.jtiRkigo0KpI3fYgl2slZVJyUYPaBzmGFRQrQQJzNacg.JPEG.wooyu96%2Foutput_3532954624.jpg&type=sc960_832",
        "tags": ["문학적 활동", "음악 활동", "무용 활동", "미술 활동", "도심", "사진 명소", "예술 관련 교양 쌓기", "좋은 접근성"]
    },
    {
        "name": "에버랜드",
        "description": "가족, 연인, 친구와 함께 여러 놀이기구와 먹거리를 즐길 수 있는 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAzMzFfNDAg%2FMDAxNzExODE0Mjc4OTc1.j7jI-qsvEUOLtjA8vYu6-yTOAru7L5GLKcn3P1-TXuMg.nPwsczRYIoUN7AEYVryS9vblR4QN6GP42RGnWCuu8SQg.JPEG%2
        "tags": ["액티비티", "자연", "사진 명소", "도전적인 활동", "독특한 장소"]
    },
    {
        "name": "981 파크 제주",
        "description": "카트 레이싱, 서바이벌 등 재밌는 여러 액티비티를 즐길 수 있는 제주의 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210527_297%2F16220986701968f1N7_JPEG%2F1.jpg",
        "tags": ["액티비티", "도심", "사진 명소", "도전적인 활동", "독특한 활동"]
    }
]

# 질문 및 선택지 설정
questions_options = [
    {
        "question": "어떤 종류의 활동을 즐기시나요?",
        "options": ["문화, 역사 탐방", "자연 탐험", "쇼핑", "액티비티", "문학적 활동", "음악 활동", "무용 활동", "미술 활동"]
    },
    {
        "question": "어떤 환경에서 여행을 즐기고 싶으신가요?",
        "options": ["도심", "자연", "바다", "유적지"]
    },
    {
        "question": "여행 중 어떤 경험을 가장 중시하시나요?",
        "options": ["사진 명소", "문화 체험", "힐링", "도전적인 활동", "예술 관련 교양 쌓기", "새로운 음식 시도"]
    },
    {
        "question": "여행 중 어떤 것을 가장 중요하게 생각하시나요?",
        "options": ["좋은 접근성", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"]
    }
]

# Streamlit 앱 레이아웃 설정
st.title("여행 스타일 기반 관광지 추천 챗봇")

user_answers = []  # 사용자의 답변을 저장

# 각 질문에 대해 선택할 수 있도록 UI를 구성
for i, q in enumerate(questions_options):
    answer = st.selectbox(q["question"], options=q["options"], key=f"question_{i}")
    user_answers.append(answer)

# 추천 버튼
if st.button("추천받기"):
    # 각 관광지의 일치하는 태그 개수를 저장
    matching_scores = []
    
    for destination in destinations:
        # 일치하는 태그 수 계산
        score = sum(tag in destination["tags"] for tag in user_answers)
        matching_scores.append((destination, score))
    
    # 일치 태그 개수가 높은 순으로 정렬하고 상위 두 개 선택
    matching_scores.sort(key=lambda x: x[1], reverse=True)
    top_destinations = [destination for destination, score in matching_scores[:2]]

    # 추천 결과 표시
    for place in top_destinations:
        st.subheader(place["name"])
        st.write(place["description"])
        st.image(place["image_url"], use_column_width=True)
        # 관광지 요약과 주변 상권 표시
        if st.button(f"{place['name']}에 대해 더 알아보기"):
            st.write("### 요약")
            st.write(place["summary"])
            st.write("### 주변 상권")
            st.write(place["surrounding_area"])
