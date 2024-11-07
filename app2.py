import streamlit as st
import random

# 관광지 데이터
destinations = [
    {
        "name": "경복궁",
        "description": "한국의 전통과 역사를 경험할 수 있는 서울의 대표 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA5MDRfODcg%2FMDAxNzI1NDU5OTg1ODcx.20ZW5yxoZO6aCc1Ds-nDzGMyAx-qObh5n9Ke5Jo3HVYg.JA7cHnv7gZ2JWYfRzBJ5s-xZVCq40sBvwqOmLGsZ5kog.JPEG%2F3C4A9776_1.jpg&type=sc960_832",
        "tags": ["문화, 역사 탐방", "도심", "유적지", "문화 체험", "사진 명소"],
        "summary": "경복궁은 조선 왕조의 중심 궁궐로, 한국 전통 건축의 아름다움을 경험할 수 있습니다. 왕실의 역사와 문화, 궁궐 내부의 아름다운 정원과 건축물을 감상할 수 있습니다. 서울 중심에 위치해 있어 다른 주요 관광지와의 접근성이 뛰어납니다.",
        "surrounding": "인사동: 전통 공예품과 한식 찻집, 갤러리들이 모여있는 문화 거리. 광화문: 서울의 행정 중심지로, 다양한 상업 시설과 레스토랑이 밀집해 있습니다. 북촌 한옥마을: 전통 한옥을 체험할 수 있는 장소로, 고즈넉한 분위기에서 한국 문화를 느낄 수 있습니다."
    },
    {
        "name": "수원화성",
        "description": "한국의 전통과 역사를 경험할 수 있는 수원의 대표 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA1MjNfMTYw%2FMDAxNzE2MzkwNDkzNTkw.hGbTTrdhPUfzRFbRWP43dpPpRTLXfWC2QbadfEv-ewcg.-J48L9rp25B-ek0ZpX-fiVUQIpyctcjCV34yJC3RRDkg.JPEG%2F20240426-_C6A8780.jpg&type=sc960_832",
        "tags": ["문화, 역사 탐방", "도심", "사진 명소", "유적지", "문화 체험"],
        "summary": "수원화성은 조선시대의 대표적인 성곽으로, 군사적, 역사적 가치를 지닌 곳입니다. 성곽을 따라 걸으며 고유의 건축미와 함께 다양한 유적을 경험할 수 있습니다. 한국 역사와 문화에 대해 더 깊이 이해할 수 있는 기회입니다.",
        "surrounding": "수원시청: 수원 중심지에 위치하며, 다양한 먹거리와 쇼핑을 즐길 수 있습니다. 수원역: 교통이 편리하며 다양한 상업시설과 레스토랑이 밀집해 있습니다. 팔달문: 수원 화성의 중요한 문으로, 수원 문화의 중심을 느낄 수 있습니다."
    },
    {
        "name": "서울숲",
        "description": "푸르른 한강과 함께 자연을 즐길 수 있는 서울의 인기있는 힐링 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200728_296%2F1595899415265D5A3d_JPEG%2F%25B0%25A1%25C1%25B7%25B8%25B6%25B4%25E71.jpg",
        "tags": ["자연 탐험", "도심 속 자연", "사진 명소", "힐링", "좋은 접근성"],
        "summary": "서울숲은 도심 속에서 자연을 즐길 수 있는 공간으로, 다양한 식물과 동물들을 관찰할 수 있습니다. 한강과 인접해 있어 서울의 다양한 자연을 한 눈에 볼 수 있는 장점이 있습니다. 도심에 위치해 있어 접근성이 뛰어나며, 휴식과 힐링을 제공하는 장소입니다.",
        "surrounding": "압구정: 고급스러운 쇼핑과 레스토랑이 밀집한 지역. 강남역: 젊은층이 많이 찾는 쇼핑, 카페, 음식점들이 즐비해 있습니다. 한강: 자전거 도로와 산책로가 잘 마련되어 있어 여유로운 시간을 보낼 수 있습니다."
    },
    {
        "name": "남산서울타워",
        "description": "서울 도심 속에서 밝게 빛나는 야경 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190711_62%2F1562823704121InE2t_JPEG%2Fusfc9L8iEAQfjJK8oKoBwa4d.jpg",
        "tags": ["자연 탐험", "도심 속 자연", "사진 명소", "힐링", "좋은 접근성"],
        "summary": "남산서울타워는 서울의 랜드마크 중 하나로, 서울의 아름다운 전경을 감상할 수 있는 장소입니다. 야경이 특히 유명하며, 전망대에서 서울 시내를 한 눈에 내려다볼 수 있습니다. 케이블카나 도보로 쉽게 접근할 수 있어 많은 관광객들이 찾는 명소입니다.",
        "surrounding": "명동: 쇼핑과 음식을 즐길 수 있는 인기 지역. 서울역: 서울의 교통 중심지로, 다양한 쇼핑몰과 먹거리가 밀집해 있습니다. 남대문시장: 전통적인 재래시장으로, 다양한 물건을 구입할 수 있는 곳입니다."
    },
    {
        "name": "더현대 서울",
        "description": "즐거운 먹거리를 즐기고, 쇼핑을 할 수 있는 현대백화점 더현대 서울입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210527_297%2F16220986701968f1N7_JPEG%2F1.jpg",
        "tags": ["쇼핑", "도심", "사진 명소", "새로운 음식 시도", "좋은 접근성"],
        "summary": "더현대 서울은 다양한 브랜드와 음식점들이 입점해 있는 현대백화점으로, 서울의 가장 트렌디한 쇼핑 명소 중 하나입니다. 최신 유행을 반영한 상점들과 음식들이 많아 쇼핑과 먹거리를 동시에 즐길 수 있습니다. 다양한 문화 행사와 팝업 스토어도 자주 열립니다.",
        "surrounding": "여의도: 금융 중심지와 다양한 먹거리가 밀집한 지역. IFC몰: 세계적인 브랜드와 레스토랑들이 밀집한 쇼핑몰입니다. 한강공원: 한적하게 산책이나 자전거를 타며 여유로운 시간을 보낼 수 있습니다."
    },
    {
        "name": "코엑스",
        "description": "도서관, 팝업스토어, 영화관, 음식점 등 여러 활동을 즐길 수 있는 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAzMDFfMTM1%2FMDAxNzA5MjkzMjk5MTA4.gdVknLSuCHHQuBK9_SHBnqe_rN0P5WV5WNF4FORD8tcg.Fbe6GAgm6FSNxiXz0uJ01v1zPFhhCsCHICjwM3ChaR0g.JPEG%2F0cosunokci003.jpg&type=sc960_832",
        "tags": ["쇼핑", "문학 활동", "도심", "사진 명소", "새로운 음식 시도", "예술 관련 교양 쌓기", "좋은 접근성"],
        "summary": "코엑스는 서울의 중심부에 위치한 복합문화공간으로, 도서관, 영화관, 쇼핑몰 등이 한곳에 모여 있습니다. 다양한 문화 프로그램과 전시회가 열리며, 세계 각국의 음식을 즐길 수 있는 레스토랑들도 있습니다. 서울에서 가장 바쁜 도심 속의 오아시스 같은 공간입니다.",
        "surrounding": "삼성역: 서울의 중심지로, 쇼핑과 먹거리가 다양합니다. 봉은사: 서울의 유명한 사찰로, 고요하고 평화로운 분위기에서 문화 체험을 할 수 있습니다. 스타필드 코엑스몰: 다양한 쇼핑과 영화관이 있는 큰 복합 쇼핑몰입니다."
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
        "options": ["도심", "자연", "자연 속 도심", "도심 속 자연", "바다", "유적지"]
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
        st.write(f"**세 줄 요약**: {place['summary']}")
        st.write(f"**주변 상권**: {place['surrounding']}")
