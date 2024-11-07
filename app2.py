import streamlit as st
import random

# 관광지 데이터
destinations = [
    {
        "name": "경복궁",
        "description": "한국의 전통과 역사를 경험할 수 있는 서울의 대표 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA5MDRfODcg%2FMDAxNzI1NDU5OTg1ODcx.20ZW5yxoZO6aCc1Ds-nDzGMyAx-qObh5n9Ke5Jo3HVYg.JA7cHnv7gZ2JWYfRzBJ5s-xZVCq40sBvwqOmLGsZ5kog.JPEG%2F3C4A9776_1.jpg&type=sc960_832",
        "tags": ["문화, 역사 탐방", "도심", "유적지", "문화 체험", "사진 명소"],
        "summary": "경복궁은 서울의 대표적인 궁궐로, 조선 시대의 역사와 문화유산을 경험할 수 있습니다.",
        "surrounding_area": "경복궁 근처에는 북촌한옥마을과 인사동길이 있어 전통 문화를 더욱 체험할 수 있습니다."
    },
    {
        "name": "인사동길",
        "description": "한국의 전통 공예품과 예술작품을 구매할 수 있는 거리입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAxMTRfMTg3%2FMDAxNjcwNzEwMzE3NTgx.a1w6ffUSGpSM0f5v1ZYjXUlsOXScfsFbBuwBOms7J0wg.6W1OpdRfpGZAfTg9nmJSZn9TnMlIHmlHL4ohbyhP0o8g.JPEG%2FIMG_2724.jpg&type=sc960_832",
        "tags": ["문화, 역사 탐방", "도심", "전통", "예술", "사진 명소"],
        "summary": "인사동길은 한국 전통과 현대적 예술이 어우러진 곳으로 다양한 공예품을 구매할 수 있습니다.",
        "surrounding_area": "인사동길 주변에는 경복궁, 북촌한옥마을, 그리고 다양한 전통 찻집이 있습니다."
    },
    {
        "name": "남산서울타워",
        "description": "서울 도심 속에서 밝게 빛나는 야경 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190711_62%2F1562823704121InE2t_JPEG%2Fusfc9L8iEAQfjJK8oKoBwa4d.jpg",
        "tags": ["자연 탐험", "자연", "사진 명소", "힐링", "좋은 접근성"],
        "summary": "남산서울타워는 서울의 전경을 한눈에 볼 수 있는 명소로, 야경이 특히 아름답습니다.",
        "surrounding_area": "남산서울타워 주변에는 남산공원이 있어 산책이나 하이킹을 즐기기 좋습니다."
    },
    {
        "name": "서울 국립중앙박물관",
        "description": "한국의 역사와 문화를 배우고 체험할 수 있는 박물관입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190930_201%2F15698070053875P5RY_JPEG%2F2020_서울국립중앙박물관.jpg&type=sc960_832",
        "tags": ["문화, 역사 탐방", "도심", "유적지", "문화 체험", "사진 명소"],
        "summary": "서울 국립중앙박물관은 한국의 역사적인 유물을 전시하며, 문화 탐방에 이상적인 장소입니다.",
        "surrounding_area": "박물관 근처에는 이태원과 한남동이 있어 다양한 음식과 쇼핑을 즐길 수 있습니다."
    },
    {
        "name": "북촌한옥마을",
        "description": "조선시대의 전통 가옥인 한옥을 경험할 수 있는 곳입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20191009_21%2F1570608403202uFsHs_JPEG%2F1570608403202.jpg&type=sc960_832",
        "tags": ["문화, 역사 탐방", "도심", "유적지", "문화 체험", "사진 명소"],
        "summary": "북촌한옥마을은 전통적인 한옥이 모여있는 지역으로, 고즈넉한 분위기 속에서 전통 문화를 체험할 수 있습니다.",
        "surrounding_area": "북촌한옥마을 근처에는 경복궁과 인사동이 있어 한국의 전통 문화를 함께 즐길 수 있습니다."
    },
    {
        "name": "명동거리",
        "description": "서울의 대표적인 쇼핑 거리로, 다양한 브랜드와 맛집이 즐비한 곳입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190711_62%2F1562823704121InE2t_JPEG%2Fusfc9L8iEAQfjJK8oKoBwa4d.jpg",
        "tags": ["쇼핑", "도심", "사진 명소", "새로운 음식 시도", "좋은 접근성"],
        "summary": "명동거리는 다양한 쇼핑 매장과 음식점들이 있어 서울의 중심에서 쇼핑과 음식을 즐기기 좋습니다.",
        "surrounding_area": "명동거리 주변에는 남산서울타워와 남대문시장이 있어 관광과 쇼핑을 동시에 즐길 수 있습니다."
    },
    # 추가적으로 다른 관광지 데이터를 이어서 작성할 수 있습니다.
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

        # 관광지 요약과 주변 상권 표시 버튼
        if st.button(f"{place['name']}에 대해 더 알아보기"):
            st.write("### 요약")
            st.write(place["summary"])
            st.write("### 주변 상권")
            st.write(place["surrounding_area"])


