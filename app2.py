import streamlit as st

# 관광지 데이터 (모든 장소 포함)
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
    # 추가 관광지 데이터...
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

    # 추천된 관광지 리스트
    for place in top_destinations:
        # 관광지 이미지와 이름을 보여줍니다.
        if st.button(f"{place['name']} 이미지 보기"):
            st.image(place["image_url"], caption=place["name"], use_column_width=True)

        # 해당 장소의 이미지 클릭 시, 더 알아보기 버튼 생성
        selected_place = st.radio("어떤 관광지에 대해 더 알아보시겠어요?", [place["name"]])
        
        if selected_place == place["name"]:
            st.write(f"**요약**: {place['summary']}")
            st.write(f"**주변 상권**: {place['surrounding_area']}")


