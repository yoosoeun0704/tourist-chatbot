import streamlit as st
import random

# 관광지 데이터
destinations = [
    {
        "name": "경복궁",
        "description": "한국의 전통과 역사를 경험할 수 있는 서울의 대표 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA5MDRfODcg%2FMDAxNzI1NDU5OTg1ODcx.20ZW5yxoZO6aCc1Ds-nDzGMyAx-qObh5n9Ke5Jo3HVYg.JA7cHnv7gZ2JWYfRzBJ5s-xZVCq40sBvwqOmLGsZ5kog.JPEG%2F3C4A9776_1.jpg&type=sc960_832",
        "tags": ["문화, 역사 탐방", "도심", "유적지", "문화 체험", "사진 명소"],
        "summary": "경복궁은 조선 왕조의 정궁으로, 궁궐 내부의 아름다운 건축물과 정원이 관광객에게 큰 인기를 끌고 있습니다. 광화문을 중심으로 서울의 역사적인 중심지에 위치해 있으며, 근처에는 다양한 문화재와 박물관도 있습니다. 궁중문화체험과 전통 공연도 즐길 수 있습니다.",
        "surrounding_area": "인사동, 삼청동, 북촌한옥마을, 광화문 일대는 전통적인 한지, 도자기, 고미술품을 파는 상점들과 카페가 많습니다. 관광객들이 많이 찾는 전통 찻집과 한식 맛집들이 위치해 있습니다."
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
        "summary": "전통과 현대가 어우러지는 인사동은 한국의 전통 문화와 예술을 체험할 수 있는 명소입니다. 골목마다 전통 찻집, 갤러리, 공예품 상점이 자리잡고 있어 한국 문화를 즐기기에 최적입니다. 다양한 거리 공연과 문화 행사가 열리기도 합니다.",
        "surrounding_area": "전통 공예품, 민속 기념품을 판매하는 상점들이 많고, 다양한 한국 전통 음식점이 즐비합니다. 한옥 카페와 현대적인 쇼핑몰이 혼재된 상권입니다."
    },
    {
        "name": "남산서울타워",
        "description": "서울의 상징적인 전망대로, 도시 전경을 한눈에 볼 수 있는 인기 있는 관광지입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/n%EC%84%9C%EC%9A%B8%ED%83%80%EC%9B%8C",
        "tags": ["사진 명소", "도심", "힐링", "자연", "액티비티"],
        "summary": "서울의 상징적인 전망대인 남산서울타워는 서울을 한눈에 볼 수 있는 최고의 장소입니다. 야경 명소로 유명하며, 탑을 중심으로 다양한 레스토랑과 카페들이 있습니다. 케이블카를 타고 올라가며 서울의 경치를 감상할 수 있습니다.",
        "surrounding_area": "남산 일대는 고급 레스토랑과 카페, 기념품 가게가 밀집해 있으며, 남산 도서관과 서울타워 주변의 공원도 많은 관광객들의 방문지입니다."
    },
    {
        "name": "서울 국립중앙박물관",
        "description": "한국의 역사와 문화를 담고 있는 대규모 박물관으로, 다양한 전시와 교육 프로그램을 제공합니다.",
        "image_url": "https://www.museum.go.kr/uploadfile/ecms/media/2024/09/520C4D4F-5E17-F88B-024D-1B0AB916AC5C.jpg",
        "tags": ["문화 체험", "역사 탐방", "도심", "예술 관련 교양 쌓기", "안전하고 편안한 환경"],
        "summary": "서울 국립중앙박물관은 한국의 역사와 문화를 깊이 이해할 수 있는 박물관으로, 다양한 유물과 전시가 있습니다. 고대부터 현대까지의 다양한 예술 작품을 관람할 수 있으며, 한국의 국보와 보물들이 전시되어 있습니다. 가족 단위 방문객들에게 적합한 장소입니다.",
        "surrounding_area": "박물관 근처에는 용산 전자상가, 한남동 카페 거리, 이태원 상권 등이 위치해 있어, 다양한 음식과 쇼핑을 즐길 수 있는 명소입니다."
    },
    {
        "name": "북촌한옥마을",
        "description": "전통 한옥이 잘 보존된 지역으로, 한국의 전통 건축과 문화를 체험할 수 있는 곳입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%B6%81%EC%B4%8C-%ED%95%9C%EC%98%A5-%EB%A7%88%EC%9D%84",
        "tags": ["문화 체험", "역사 탐방", "도심", "독특한 장소", "힐링"],
        "summary": "북촌한옥마을은 서울의 전통적인 한옥 건축을 그대로 보존한 마을로, 조선시대 상류층의 주거지였던 곳입니다. 좁은 골목길을 걸으며 전통 한옥과 예술작품들을 감상할 수 있습니다. 다양한 문화 체험과 전통 음식도 제공됩니다.",
        "surrounding_area": "북촌 한옥마을은 삼청동과 인사동, 창덕궁과 가까워 고전적인 분위기의 카페와 갤러리, 기념품 가게가 많습니다. 한복 체험과 전통 음식을 제공하는 가게들도 많습니다."
    },
    {
        "name": "명동거리",
        "description": "쇼핑과 먹거리가 풍부한 서울의 대표적인 상업지구로, 젊은이들 사이에서 인기 있는 장소입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%AA%85%EB%8F%99",
        "tags": ["쇼핑", "도심", "새로운 음식 시도", "문화 체험", "액티비티"],
        "summary": "명동은 서울의 대표적인 쇼핑 거리로, 다양한 패션 브랜드와 화장품 매장이 밀집해 있습니다. 외국인 관광객들 사이에서 매우 인기 있는 지역으로, 거리 음식과 카페도 풍성합니다. 밤에도 활기찬 분위기를 자랑합니다.",
        "surrounding_area": "명동 주변은 화장품 가게, 의류 매장, 카페들이 즐비하며, 명동성당, 남산과의 접근성도 좋습니다. 외식과 쇼핑을 동시에 즐길 수 있는 중심지입니다."
    },
    {
        "name": "남대문시장",
        "description": "다양한 상품과 먹거리를 저렴하게 구매할 수 있는 전통 시장으로, 현지인과 관광객 모두에게 사랑받는 곳입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%82%A8%EB%8C%80%EB%AC%B8%EC%9E%A5",
        "tags": ["쇼핑", "저렴한 가격", "문화 체험", "도전적인 활동", "안전하고 편안한 환경"],
        "summary": "남대문시장은 서울의 대표적인 재래시장으로, 다양한 상품을 저렴한 가격에 구매할 수 있는 곳입니다. 의류, 잡화, 식료품 등 여러 가지 물건을 취급하며, 한국 전통 시장의 분위기를 경험할 수 있습니다. 관광객뿐만 아니라 현지인들 사이에서도 인기 있는 장소입니다.",
        "surrounding_area": "남대문시장 주변에는 회현역과 서울역이 가까워 교통이 편리합니다. 다양한 저렴한 음식점과 상점들이 많아 쇼핑과 식사를 동시에 즐길 수 있습니다."
    },
    {
        "name": "광장시장",
        "description": "한국의 전통 음식과 다양한 먹거리를 즐길 수 있는 시장으로, 특히 빈대떡과 마약김밥이 유명합니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EA%B4%91%EC%9E%A5%EC%9E%A5%EC%9C%A0",
        "tags": ["문화 체험", "새로운 음식 시도", "저렴한 가격", "액티비티", "안전하고 편안한 환경"],
        "summary": "광장시장은 전통적인 한국 재래시장의 모습과 먹거리를 즐길 수 있는 명소입니다. 빈대떡, 마약김밥 등 전통 음식을 맛볼 수 있으며, 다양한 길거리 음식들이 제공됩니다. 관광객뿐만 아니라 현지인들 사이에서도 인기 있는 장소입니다.",
        "surrounding_area": "광장시장은 종로와 동대문 근처로, 의류 시장과 쇼핑몰들이 밀집해 있습니다. 전통적인 시장과 현대적인 상점들이 어우러져 있는 상권입니다."
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




