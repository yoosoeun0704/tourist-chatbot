import streamlit as st
import random

# 관광지 데이터
destinations = [
    {
        "name": "경복궁",
        "description": "한국의 전통과 역사를 경험할 수 있는 서울의 대표 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA5MDRfODcg%2FMDAxNzI1NDU5OTg1ODcx.20ZW5yxoZO6aCc1Ds-nDzGMyAx-qObh5n9Ke5Jo3HVYg.JA7cHnv7gZ2JWYfRzBJ5s-xZVCq40sBvwqOmLGsZ5kog.JPEG%2F3C4A9776_1.jpg&type=sc960_832",
        "tags": ["문화, 역사 탐방", "도심", "유적지", "문화 체험", "사진 명소"],
        "summary": "경복궁은 조선 왕조의 정궁으로, 아름다운 건축물과 정원이 있습니다.",
        "surrounding_area": "인사동, 북촌한옥마을, 청와대 등 다양한 문화 명소가 인근에 위치해 있습니다."
    },
    {
        "name": "서울숲",
        "description": "푸르른 한강과 함께 자연을 즐길 수 있는 서울의 인기있는 힐링 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200728_296%2F1595899415265D5A3d_JPEG%2F%25B0%25A1%25C1%25B7%25B8%25B6%25B4%25E71.jpg",
        "tags": ["자연 탐험", "자연", "사진 명소", "힐링", "좋은 접근성"],
        "summary": "서울숲은 도심 속에서 자연을 만끽할 수 있는 공간으로, 다양한 식물과 동물이 있습니다.",
        "surrounding_area": "한강공원, 성수동 카페거리 등 다양한 명소가 인근에 있습니다."
    },
    {
        "name": "더현대 서울",
        "description": "즐거운 먹거리를 즐기고, 쇼핑을 할 수 있는 현대백화점 더현대 서울입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210527_297%2F16220986701968f1N7_JPEG%2F1.jpg",
        "tags": ["쇼핑", "도심", "사진 명소", "새로운 음식 시도", "좋은 접근성"],
        "summary": "더현대 서울은 최신 유행의 쇼핑과 다양한 먹거리를 즐길 수 있는 복합 문화 공간입니다.",
        "surrounding_area": "여의도, IFC몰 등 다양한 상업시설이 인근에 있습니다."
    },
    {
        "name": "예술의 전당",
        "description": "음악, 미술, 무용, 뮤지컬 등 여러 공연을 즐길 수 있는 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEyMDVfMTI2%2FMDAxNzAxNzQ4ODQzMjQz.LwfjHhRI_NeOqn-vOd1rH_MrXE4tlwHFl5y1Ov0iPlcg.jtiRkigo0KpI3fYgl2slZVJyUYPaBzmGFRQrQQJzNacg.JPEG.wooyu96%2Foutput_3532954624.jpg&type=sc960_832",
        "tags": ["문학적 활동", "음악 활동", "무용 활동", "미술 활동", "도심", "사진 명소", "예술 관련 교양 쌓기", "좋은 접근성"],
        "summary": "예술의 전당은 다양한 공연과 전시가 열리는 문화 공간으로, 음악과 미술을 동시에 즐길 수 있습니다.",
        "surrounding_area": "서초동, 반포한강공원 등 다양한 명소가 인근에 있습니다."
    },
    {
        "name": "인사동길",
        "description": "전통과 현대가 어우러진 거리로, 한국의 전통 공예품과 예술작품을 구매할 수 있는 곳입니다.",
        "image_url": "https://www.museum.go.kr/uploadfile/ecms/media/2024/09/520C4D4F-5E17-F88B-024D-1B0AB916AC5C.jpg",
        "tags": ["문화 체험", "쇼핑", "도심", "예술 관련 교양 쌓기", "역사 탐방"],
        "summary": "인사동길은 전통과 현대가 어우러진 거리로, 다양한 공예품과 예술작품을 구매할 수 있습니다.",
        "surrounding_area": "경복궁, 북촌한옥마을 등 다양한 문화 명소가 인근에 있습니다."
    },
    {
        "name": "남산서울타워",
        "description": "서울의 상징적인 전망대로, 도시 전경을 한눈에 볼 수 있는 인기 있는 관광지입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/n%EC%84%9C%EC%9A%B8%ED%83%80%EC%9B%8C",
        "tags": ["사진 명소", "도심", "힐링", "자연", "액티비티"],
        "summary": "남산서울타워는 서울의 상징적인 전망대로, 360도 파노라마 뷰를 제공합니다.",
        "surrounding_area": "남산공원, 명동거리 등 다양한 관광지가 인근에 있습니다."
    },
    {
        "name": "서울 국립중앙박물관",
        "description": "한국의 역사와 문화를 담고 있는 대규모 박물관으로, 다양한 전시와 교육 프로그램을 제공합니다.",
        "image_url": "https://www.museum.go.kr/uploadfile/ecms/media/2024/09/520C4D4F-5E17-F88B-024D-1B0AB916AC5C.jpg",
        "tags": ["문화 체험", "역사 탐방", "도심", "예술 관련 교양 쌓기", "안전하고 편안한 환경"],
        "summary": "서울 국립중앙박물관은 한국의 역사와 문화를 담고 있는 대규모 박물관입니다.",
        "surrounding_area": "용산, 이태원 등 다양한 문화 명소가 인근에 있습니다."
    },
    {
        "name": "북촌한옥마을",
        "description": "전통 한옥이 잘 보존된 지역으로, 한국의 전통 건축과 문화를 체험할 수 있는 곳입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%B6%81%EC%B4%8C-%ED%95%9C%EC%98%A5-%EB%A7%88%EC%9D%84",
        "tags": ["문화 체험", "역사 탐방", "도심", "독특한 장소", "힐링"],
        "summary": "북촌한옥마을은 전통 한옥이 잘 보존된 지역으로, 한국의 전통 문화를 체험할 수 있습니다.",
        "surrounding_area": "경복궁, 인사동 등 다양한 문화 명소가 인근에 있습니다."
    },
    {
        "name": "명동거리",
        "description": "쇼핑과 먹거리가 풍부한 서울의 대표적인 상업지구로, 젊은이들 사이에서 인기 있는 장소입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%AA%85%EB%8F%99",
        "tags": ["쇼핑", "도심", "새로운 음식 시도", "문화 체험", "액티비티"],
        "summary": "명동거리는 쇼핑과 먹거리가 풍부한 서울의 대표적인 상업지구입니다.",
        "surrounding_area": "남대문시장, 명동성당 등 다양한 명소가 인근에 있습니다."
    },
    {
        "name": "남대문시장",
        "description": "다양한 상품과 먹거리를 저렴하게 구매할 수 있는 전통 시장으로, 현지인과 관광객 모두에게 사랑받는 곳입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%82%A8%EB%8C%80%EB%AC%B8%EC%9E%A5",
        "tags": ["쇼핑", "저렴한 가격", "문화 체험", "도전적인 활동", "안전하고 편안한 환경"],
        "summary": "남대문시장은 다양한 상품과 먹거리를 저렴하게 구매할 수 있는 전통 시장입니다.",
        "surrounding_area": "명동, 남산 등 다양한 관광지가 인근에 있습니다."
    },
    {
        "name": "광장시장",
        "description": "한국의 전통 음식과 다양한 먹거리를 즐길 수 있는 시장으로, 특히 빈대떡과 마약김밥이 유명합니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EA%B4%91%EC%9E%A5%EC%9E%A5%EC%9C%A0",
        "tags": ["문화 체험", "새로운 음식 시도", "저렴한 가격", "액티비티", "안전하고 편안한 환경"],
        "summary": "광장시장은 한국의 전통 음식과 다양한 먹거리를 즐길 수 있는 시장입니다.",
        "surrounding_area": "동대문, 종로 등 다양한 명소가 인근에 있습니다."
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

# 세션 상태 초기화
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = []
if 'recommended_destinations' not in st.session_state:
    st.session_state.recommended_destinations = []

# 각 질문에 대해 선택할 수 있도록 UI를 구성
for i, q in enumerate(questions_options):
    answer = st.selectbox(q["question"], options=q["options"], key=f"question_{i}")
    if len(st.session_state.user_answers) < len(questions_options):
        st.session_state.user_answers.append(answer)

# 추천 버튼
if st.button("추천받기"):
    # 각 관광지의 일치하는 태그 개수를 저장
    matching_scores = []
    
    for destination in destinations:
        # 일치하는 태그 수 계산
        score = sum(tag in destination["tags"] for tag in st.session_state.user_answers)
        matching_scores.append((destination, score))
    
    # 일치 태그 개수가 높은 순으로 정렬하고 상위 네 개 선택
    matching_scores.sort(key=lambda x: x[1], reverse=True)
    top_destinations = [destination for destination, score in matching_scores[:4]]
    
    # 상위 네 개 중 두 개를 무작위로 선택
    st.session_state.recommended_destinations = random.sample(top_destinations, 2)

# 추천 결과 표시
for place in st.session_state.recommended_destinations:
    st.subheader(place["name"])
    st.write(place["description"])
    st.image(place["image_url"], use_column_width=True)
    
    # 주변 상권과 요약 표시 버튼
    if st.button(f"{place['name']}에 대해 더 알아보기"):
        st.write("### 요약")
        st.write(place["summary"])
        st.write("### 주변 상권")
        st.write(place["surrounding_area"])




