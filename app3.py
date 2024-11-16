import streamlit as st
import random

# 관광지 데이터
destinations = [
    {
        "name": "경복궁",
        "description": "한국의 전통과 역사를 경험할 수 있는 서울의 대표 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA5MDRfODcg%2FMDAxNzI1NDU5OTg1ODcx.20ZW5yxoZO6aCc1Ds-nDzGMyAx-qObh5n9Ke5Jo3HVYg.JA7cHnv7gZ2JWYfRzBJ5s-xZVCq40sBvwqOmLGsZ5kog.JPEG%2F3C4A9776_1.jpg&type=sc960_832",
        "tags": ["문화/역사 탐방", "도심", "유적지", "문화/역사 체험", "사진 명소", "좋은 접근성"],
        "summary": "경복궁은 조선 왕조의 정궁으로, 궁궐 내부의 아름다운 건축물과 정원이 관광객에게 큰 인기를 끌고 있습니다. 광화문을 중심으로 서울의 역사적인 중심지에 위치해 있으며, 근처에는 다양한 문화재와 박물관도 있습니다. 궁중문화체험과 전통 공연도 즐길 수 있습니다.",
        "surrounding_area": "인사동, 삼청동, 북촌한옥마을, 광화문 일대는 전통적인 한지, 도자기, 고미술품을 파는 상점들과 카페가 많습니다. 관광객들이 많이 찾는 전통 찻집과 한식 맛집들이 위치해 있습니다."
    },
    {
        "name": "서울숲",
        "description": "푸르른 한강과 함께 자연을 즐길 수 있는 서울의 인기있는 힐링 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200728_296%2F1595899415265D5A3d_JPEG%2F%25B0%25A1%25C1%25B7%25B8%25B6%25B4%25E71.jpg",
        "tags": ["자연 탐험", "자연", "사진 명소", "힐링", "좋은 접근성", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "서울숲은 서울의 강남과 강북을 연결하는 대표적인 도시 공원으로, 넓은 녹지와 다양한 테마 공간들이 특징입니다. 숲 속에는 다양한 동식물이 서식하고 있으며, 방문객들은 자연을 즐기며 산책할 수 있습니다. 서울숲은 예술과 문화 행사가 자주 열리는 곳으로, 서울의 여유로운 자연을 느낄 수 있는 명소입니다.",
        "surrounding_area": "서울숲 주변에는 다양한 카페, 레스토랑, 쇼핑몰이 자리잡고 있어, 서울숲을 방문한 후 즐길 수 있는 상권이 풍부합니다. 특히 인근에는 이태원과 성수동의 트렌디한 상업지구도 있어 쇼핑과 미식을 동시에 즐길 수 있습니다."
    },
    {
        "name": "더현대 서울",
        "description": "즐거운 먹거리를 즐기고, 쇼핑을 할 수 있는 현대백화점 더현대 서울입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210527_297%2F16220986701968f1N7_JPEG%2F1.jpg",
        "tags": ["쇼핑", "도심", "사진 명소", "새로운 음식 시도", "좋은 접근성"],
        "summary": "더현대 서울은 서울의 강남구에 위치한 현대백화점의 최신 플래그십 스토어로, 최신 패션, 뷰티, 라이프스타일 브랜드들이 입점해 있습니다. 이곳은 단순한 쇼핑을 넘어 예술과 문화를 함께 즐길 수 있는 공간으로, 다양한 전시와 문화 프로그램이 열리고 있습니다. 고객들이 쇼핑 외에도 다양한 문화적 경험을 할 수 있는 복합문화공간으로 자리잡고 있습니다.",
        "surrounding_area": "더현대 서울은 강남구의 중심에 위치하여, 다양한 쇼핑과 외식, 문화체험을 동시에 할 수 있는 상권을 제공합니다. 주변에는 코엑스, 삼성동 등이 있어 한 곳에서 쇼핑, 영화, 미식 등을 종합적으로 즐길 수 있는 곳입니다."
    },
    {
        "name": "예술의 전당",
        "description": "음악, 미술, 무용, 뮤지컬 등 여러 공연을 즐길 수 있는 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEyMDVfMTI2%2FMDAxNzAxNzQ4ODQzMjQz.LwfjHhRI_NeOqn-vOd1rH_MrXE4tlwHFl5y1Ov0iPlcg.jtiRkigo0KpI3fYgl2slZVJyUYPaBzmGFRQrQQJzNacg.JPEG.wooyu96%2Foutput_3532954624.jpg&type=sc960_832",
        "tags": ["문학적 활동", "음악 활동", "무용 활동", "미술 활동", "도심", "사진 명소", "문화/역사 체험", "예술 관련 교양 쌓기", "좋은 접근성"],
        "summary": "예술의 전당은 서울에서 가장 유명한 공연 예술 공간 중 하나로, 클래식 음악 공연, 연극, 무용 등 다양한 문화 행사가 열리는 곳입니다. 이곳은 공연장과 전시 공간이 잘 조화되어 있어, 예술과 문화를 사랑하는 사람들에게 사랑받는 명소입니다. 다양한 예술적 경험을 제공하며, 특히 클래식 음악을 좋아하는 이들에게 인기가 많습니다.",
        "surrounding_area": "예술의 전당 주변에는 대중적인 음식점과 카페들이 많이 있으며, 서울의 문화 중심지인 서초동에 위치해 있어, 전시나 공연을 보고 나서 여유로운 시간을 즐길 수 있는 곳입니다. 또한, 인근에 양재동과 교대역 등 상업적인 지역도 있어 쇼핑과 문화 생활을 함께 즐길 수 있습니다."
    },
    {
        "name": "인사동길",
        "description": "전통과 현대가 어우러진 거리로, 한국의 전통 공예품과 예술작품을 구매할 수 있는 곳입니다.",
        "image_url": "https://korean.visitseoul.net/comm/getImage?srvcId=POST&parentSn=80&fileTy=POSTTHUMB&fileNo=2",
        "tags": ["쇼핑", "도심", "사진 명소", "문화/역사 체험", "예술 관련 교양 쌓기", "좋은 접근성", "독특한 장소"],
        "summary": "전통과 현대가 어우러지는 인사동은 한국의 전통 문화와 예술을 체험할 수 있는 명소입니다. 골목마다 전통 찻집, 갤러리, 공예품 상점이 자리잡고 있어 한국 문화를 즐기기에 최적입니다. 다양한 거리 공연과 문화 행사가 열리기도 합니다.",
        "surrounding_area": "전통 공예품, 민속 기념품을 판매하는 상점들이 많고, 다양한 한국 전통 음식점이 즐비합니다. 한옥 카페와 현대적인 쇼핑몰이 혼재된 상권입니다."
    },
    {
        "name": "남산서울타워",
        "description": "서울의 상징적인 전망대로, 도시 전경을 한눈에 볼 수 있는 인기 있는 관광지입니다.",
        "image_url": "https://50plus.or.kr/upload/im/2020/07/69e4299c-7f5a-4643-ab02-37aa0643f80d.jpg",
        "tags": ["자연 탐험", "액티비티", "자연", "사진 명소", "힐링", "저렴한 가격"],
        "summary": "서울의 상징적인 전망대인 남산서울타워는 서울을 한눈에 볼 수 있는 최고의 장소입니다. 야경 명소로 유명하며, 탑을 중심으로 다양한 레스토랑과 카페들이 있습니다. 케이블카를 타고 올라가며 서울의 경치를 감상할 수 있습니다.",
        "surrounding_area": "남산 일대는 고급 레스토랑과 카페, 기념품 가게가 밀집해 있으며, 남산 도서관과 서울타워 주변의 공원도 많은 관광객들의 방문지입니다."
    },
    {
        "name": "서울 국립중앙박물관",
        "description": "한국의 역사와 문화를 담고 있는 대규모 박물관으로, 다양한 전시와 교육 프로그램을 제공합니다.",
        "image_url": "https://mohenichotel.com/data/file/attractions/2746012956_ckZlfV01_e96849551c4a2c8027d510886abf084196cc78b7.jpg",
        "tags": ["문화/역사 탐방", "도심", "유적지", "문화/역사 체험", "예술 관련 교양 쌓기", "좋은 접근성", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "서울 국립중앙박물관은 한국의 역사와 문화를 깊이 이해할 수 있는 박물관으로, 다양한 유물과 전시가 있습니다. 고대부터 현대까지의 다양한 예술 작품을 관람할 수 있으며, 한국의 국보와 보물들이 전시되어 있습니다. 가족 단위 방문객들에게 적합한 장소입니다.",
        "surrounding_area": "박물관 근처에는 용산 전자상가, 한남동 카페 거리, 이태원 상권 등이 위치해 있어, 다양한 음식과 쇼핑을 즐길 수 있는 명소입니다."
    },
    {
        "name": "북촌한옥마을",
        "description": "전통 한옥이 잘 보존된 지역으로, 한국의 전통 건축과 문화를 체험할 수 있는 곳입니다.",
        "image_url": "https://lh6.googleusercontent.com/proxy/PAHUXVl5DNJYQ8OT47BIdyZFaTmHxpaN-ffRNNzz0blNHjbPPR492GFDEQmLptUjznUdR2lrxi5a9-TXMYEGPTm6Mc9ZOceZRthGOHzssCKLtzpnNYm74cbxgJcIMpxYZdyEJ6mqpZ3YhNTGyAUjpak",
        "tags": ["문화/역사 탐방", "도심", "유적지", "사진 명소", "문화/역사 체험", "독특한 장소", "좋은 접근성", "저렴한 가격"],
        "summary": "북촌한옥마을은 서울의 전통적인 한옥 건축을 그대로 보존한 마을로, 조선시대 상류층의 주거지였던 곳입니다. 좁은 골목길을 걸으며 전통 한옥과 예술작품들을 감상할 수 있습니다. 다양한 문화 체험과 전통 음식도 제공됩니다.",
        "surrounding_area": "북촌 한옥마을은 삼청동과 인사동, 창덕궁과 가까워 고전적인 분위기의 카페와 갤러리, 기념품 가게가 많습니다. 한복 체험과 전통 음식을 제공하는 가게들도 많습니다."
    },
    {
        "name": "명동거리",
        "description": "쇼핑과 먹거리가 풍부한 서울의 대표적인 상업지구로, 젊은이들 사이에서 인기 있는 장소입니다.",
        "image_url": "https://lh3.googleusercontent.com/proxy/kk1Dx0y51tcKFj61Lwgn_PEB7muF_YoHzq49FaleZvb2SfLIi4mODkzIBigs7BPug2YVtNUcRu8",
        "tags": ["쇼핑", "도심", "새로운 음식 시도", "문화/역사 체험", "좋은 접근성"],
        "summary": "명동은 서울의 대표적인 쇼핑 거리로, 다양한 패션 브랜드와 화장품 매장이 밀집해 있습니다. 외국인 관광객들 사이에서 매우 인기 있는 지역으로, 거리 음식과 카페도 풍성합니다. 밤에도 활기찬 분위기를 자랑합니다.",
        "surrounding_area": "명동 주변은 화장품 가게, 의류 매장, 카페들이 즐비하며, 명동성당, 남산과의 접근성도 좋습니다. 외식과 쇼핑을 동시에 즐길 수 있는 중심지입니다."
    },
    {
        "name": "남대문시장",
        "description": "다양한 상품과 먹거리를 저렴하게 구매할 수 있는 전통 시장으로, 현지인과 관광객 모두에게 사랑받는 곳입니다.",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGNbZM1IWmH5OclBZLhjO2gbUyajDdAxvvrw&s",
        "tags": ["쇼핑", "도심", "문화/역사 체험", "새로운 음식 시도", "좋은 접근성", "안전하고 편안한 환경", "저렴한 가격"],
        "summary": "남대문시장은 서울의 대표적인 재래시장으로, 다양한 상품을 저렴한 가격에 구매할 수 있는 곳입니다. 의류, 잡화, 식료품 등 여러 가지 물건을 취급하며, 한국 전통 시장의 분위기를 경험할 수 있습니다. 관광객뿐만 아니라 현지인들 사이에서도 인기 있는 장소입니다.",
        "surrounding_area": "남대문시장 주변에는 회현역과 서울역이 가까워 교통이 편리합니다. 다양한 저렴한 음식점과 상점들이 많아 쇼핑과 식사를 동시에 즐길 수 있습니다."
    },
    {
        "name": "광장시장",
        "description": "한국의 전통 음식과 다양한 먹거리를 즐길 수 있는 시장으로, 특히 빈대떡과 마약김밥이 유명합니다.",
        "image_url": "https://i.namu.wiki/i/8NbM8k14zLteAUOILx2NjTKff56sd1JFug7peRz1XqM0J6N0g5XHUR0l7ZKhnwllvj4CbLuccmbxiGce-tpncA.webp",
        "tags": ["쇼핑", "도심", "문화/역사 체험", "새로운 음식 시도", "좋은 접근성", "안전하고 편안한 환경", "저렴한 가격"],
        "summary": "광장시장은 전통적인 한국 재래시장의 모습과 먹거리를 즐길 수 있는 명소입니다. 빈대떡, 마약김밥 등 전통 음식을 맛볼 수 있으며, 다양한 길거리 음식들이 제공됩니다. 관광객뿐만 아니라 현지인들 사이에서도 인기 있는 장소입니다.",
        "surrounding_area": "광장시장은 종로와 동대문 근처로, 의류 시장과 쇼핑몰들이 밀집해 있습니다. 전통적인 시장과 현대적인 상점들이 어우러져 있는 상권입니다."
    },
     {
        "name": "동대문디자인플라자",
        "description": "현대적인 디자인과 건축의 상징으로, 전시, 패션, 문화 행사 등이 열리는 복합 문화 공간입니다.",
        "image_url": "https://cdn.visitkorea.or.kr/img/call?cmd=VIEW&id=093a621e-affa-4137-a97b-822af2412e51",
        "tags": ["쇼핑", "도심", "문화/역사 체험", "예술 관련 교양 쌓기", "좋은 접근성", "독특한 장소"],
        "summary": "동대문디자인플라자는 현대적인 디자인과 문화가 융합된 복합문화공간입니다. 다양한 디자인 전시, 패션쇼, 문화 행사들이 열리며, 건축학적으로도 독특한 구조를 자랑합니다. 방문객들이 디자인과 혁신적인 아이디어를 접할 수 있는 곳입니다.",
        "surrounding_area": "동대문 일대는 의류 도매 시장과 쇼핑몰, 먹거리 골목이 밀집해 있으며, 젊은 층을 중심으로 활기찬 분위기를 자랑합니다."
    },
    {
        "name": "북한산 국립공원",
        "description": "아름다운 자연 경관과 다양한 등산로를 제공하는 서울 근교의 인기 있는 국립공원입니다.",
        "image_url": "https://korean.visitseoul.net/comm/getImage?srvcId=MEDIA&parentSn=56531&fileTy=MEDIA&fileNo=1",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "사진 명소", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "북한산 국립공원은 도심 근처에서 자연을 느낄 수 있는 최고의 산악 관광지입니다. 다양한 등산로와 함께 풍성한 자연 경관을 즐길 수 있으며, 사찰과 유적지 등 역사적인 장소도 많습니다.",
        "surrounding_area": "북한산 일대에는 등산로와 함께 여러 산책로가 있어 자연을 즐길 수 있는 카페와 음식점들이 위치해 있습니다. 특히 여름과 가을에는 트래킹을 즐기려는 사람들이 많이 찾는 곳입니다."

    },
    {
        "name": "서울스카이",
        "description": "롯데월드타워에 위치한 전망대로, 서울의 전경을 360도 파노라마로 감상할 수 있는 곳입니다.",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvJWCyZbgymUhsPpz93u06H3pvgwzXhhGDtg&s",
        "tags": ["액티비티", "도심", "사진 명소", "힐링", "독특한 장소"],
        "summary": "서울스카이는 롯데월드타워에 위치한 전망대입니다. 서울의 전경을 360도로 감상할 수 있는 공간으로, 고층에서 내려다보는 도시의 아름다움이 특징입니다. 특히 야경이 매우 아름답습니다.",
        "surrounding_area": "서울스카이가 위치한 롯데월드타워에는 고급 레스토랑, 쇼핑몰, 롯데월드가 있어 관광객들에게 다양한 체험을 제공합니다."
    },
    {
        "name": "롯데월드",
        "description": "실내외 테마파크와 쇼핑몰이 결합된 복합 엔터테인먼트 공간으로, 가족 단위 방문객에게 인기가 많습니다.",
        "image_url": "https://static.hanatour.com/product/2023/06/01/0853q6upl9/default.png",
        "tags": ["액티비티", "도심", "사진 명소", "도전적인 활동", "좋은 접근성", "독특한 장소"],
        "summary": "롯데월드는 국내 최대 규모의 실내 테마파크로, 다양한 놀이기구와 쇼핑몰, 레스토랑, 호텔 등이 한 곳에 모여 있는 복합문화공간입니다. 특히 겨울에는 스케이팅장과 연말 분위기가 돋보이며, 어린이부터 성인까지 즐길 수 있는 다양한 활동이 마련되어 있습니다.",
        "surrounding_area": "롯데월드는 잠실역과 가까워 쇼핑몰과 레스토랑, 영화관, 롯데백화점 등 다양한 상업시설을 즐길 수 있는 상권이 있습니다. 잠실 일대는 인기있는 먹거리와 카페가 많아 놀이공원 방문 후 여유로운 시간을 보내기 좋습니다."
    },
    {
        "name": "홍대거리",
        "description": "젊은 예술가와 음악가들이 모여드는 활기찬 거리로, 다양한 카페와 클럽, 갤러리가 즐비합니다.",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/6f/7b/71/photo6jpg.jpg?w=1200&h=1200&s=1",
        "tags": ["쇼핑", "액티비티", "음악 활동", "도심", "도전적인 활동", "새로운 음식 시도", "좋은 접근성"],
        "summary": "홍대거리는 서울의 대학로와 함께 젊은이들의 문화와 예술을 대표하는 거리로, 독특한 카페, 개성 있는 상점, 거리 공연 등이 끊임없이 열리는 곳입니다. 다양한 문화 행사와 공연이 자주 열리며, 홍대 근처의 클럽과 술집은 서울의 밤문화를 즐기기에 최적의 장소입니다.",
        "surrounding_area": "홍대거리는 상수동, 합정동, 연남동과 가까워 다양한 트렌디한 상권을 누릴 수 있습니다. 특히 홍대 근처의 골목길과 개성 있는 카페들이 많아 하루 종일 돌아다녀도 지루하지 않습니다."
    },
    {
        "name": "익선동 한옥마을",
        "description": "전통 한옥을 개조한 카페와 상점들이 있는 지역으로, 독특한 분위기를 자랑합니다.",
        "image_url": "https://tong.visitkorea.or.kr/cms/resource/22/2947522_image2_1.jpg",
        "tags": ["문화/역사 탐방", "쇼핑", "도심", "힐링", "문화/역사 체험", "사진 명소", "독특한 장소"],
        "summary": "익선동 한옥마을은 전통적인 한옥 건축을 기반으로 현대적인 디자인과 감각을 더한 상점들이 모여있는 특색 있는 거리입니다. 전통과 현대가 결합된 인테리어의 카페와 음식점, 다양한 공예품을 파는 가게들이 있어 서울의 옛 모습과 현대적인 트렌드를 동시에 즐길 수 있습니다. 특히 사진 촬영을 좋아하는 이들에게 인기 있는 명소입니다.",
        "surrounding_area": "익선동 한옥마을은 종로구와 가까워 경복궁, 북촌한옥마을, 인사동 등 전통적인 명소들이 밀집해 있습니다. 또한 근처에는 다양한 카페, 레스토랑, 갤러리들이 있어 한옥의 매력을 체험하며 여유로운 시간을 보낼 수 있습니다."
    },
    {
        "name": "서울로 7017",
        "description": "도심 속의 고가 보행도로 공원으로, 산책과 휴식을 즐길 수 있는 공간입니다.",
        "image_url": "https://i.namu.wiki/i/eOVv43UHs3HFPClUXvnv8Iw5DpAN8GX3FTIQLni-ieCsTqlQYc0t0NleDTgdROwuLriKFm4DDOxw85YM5AU4zg.webp",
        "tags": ["자연 탐험", "도심", "자연", "사진 명소", "힐링", "좋은 접근성", "안전하고 편안한 환경"],
        "summary": "서울로 7017은 과거의 고가도로를 새롭게 재개발하여 만든 도심 속 공원으로, 걷기 좋은 산책로와 녹지가 어우러져 있습니다. 다양한 예술작품과 벤치, 꽃들이 곳곳에 배치되어 있어 시민들이 휴식과 산책을 즐기기에 적합한 공간입니다.",
        "surrounding_area": "서울로 7017 주변은 서울역, 명동 등 상업지구와 가까워 쇼핑과 먹거리를 함께 즐길 수 있는 장소입니다. 또한 이곳은 문화와 예술의 중심지로, 근처에 다양한 미술관과 공연장이 있어 문화생활을 누리기에 좋은 장소입니다."
    },
    {
        "name": "코엑스",
        "description": "대규모 전시와 컨벤션 센터로, 쇼핑몰과 아쿠아리움, 도서관 등이 함께 있는 복합 문화 공간입니다.",
        "image_url": "https://cdn.ceorankingnews.com/news/photo/202208/76873_56832_3045.jpg",
        "tags": ["쇼핑", "액티비티", "문학적 활동", "미술 활동", "도심", "문화/역사 체험", "예술 관련 교양 쌓기", "좋은 접근성", "독특한 장소"],
        "summary": "코엑스는 전시와 컨벤션이 이루어지는 장소뿐만 아니라, 쇼핑몰, 대형 서점, 영화관, 다양한 레스토랑들이 입점해 있어 서울에서 가장 바쁜 상업 및 문화 중심지 중 하나입니다. 현대적인 시설과 여러 문화적 경험을 동시에 제공합니다.",
        "surrounding_area": "코엑스 주변은 강남구의 중심에 위치하여, 삼성동, 봉은사로 이어지는 트렌디한 상업지구가 밀집해 있습니다. 쇼핑, 음식, 문화 생활이 동시에 이루어지는 복합적인 상권을 즐길 수 있습니다."
    },
    {
        "name": "서울시립미술관",
        "description": "현대 미술 작품을 중심으로 다양한 전시를 개최하는 미술관으로, 예술 애호가들에게 인기 있는 장소입니다.",
        "image_url": "https://i.namu.wiki/i/2_v2_jSvc94bSqV_SCh5_Gv27bK9r-SZ8_1HHxlct-c2ui7f8R03aKdFckh_7HOPp02zldtypQX2VAKMiFHDDw.webp",
        "tags": ["미술 활동", "도심", "문화/역사 체험", "예술 관련 교양 쌓기", "독특한 장소", "안전하고 편안한 환경"],
        "summary": "서울시립미술관은 서울의 현대 미술을 대표하는 미술관으로, 다양한 예술 전시와 특별 전시가 주기적으로 개최됩니다. 미술관은 예술과 문화의 중심지로서, 많은 예술가들과 방문객들이 찾는 장소입니다.",
        "surrounding_area": "서울시립미술관 주변은 서울의 문화지구인 인사동과 가까워 전통 문화와 현대 미술을 동시에 즐길 수 있는 독특한 상권을 제공합니다."
    },
    {
        "name": "서대문형무소",
        "description": "일제강점기 한국의 독립운동 역사와 관련된 박물관으로, 역사 교육의 중요한 장소입니다.",
        "image_url": "https://www.imedialife.co.kr/news/photo/202407/51580_57737_524.jpg",
        "tags": ["문화/역사 탐방", "도심", "유적지", "문화/역사 체험", "독특한 장소", "저렴한 가격"],
        "summary": "서대문형무소는 일제강점기 독립운동가들이 수감되었던 역사적인 장소로, 현재는 박물관과 기념관으로 운영되고 있습니다. 이곳은 한국 역사에서 중요한 위치를 차지하는 장소로, 관람을 통해 일제강점기 독립운동의 이야기를 배울 수 있습니다.",
        "surrounding_area": "서대문형무소 주변은 신촌과 가까워 다양한 상업시설과 카페, 레스토랑 등이 밀집해 있습니다. 역사적인 장소와 근처 상권을 동시에 즐길 수 있는 유니크한 장소입니다."
    },
    {
        "name": "청와대",
        "description": "대한민국 대통령의 공식 관저로, 아름다운 정원과 역사적인 건축물로 구성되어 있습니다.",
        "image_url": "https://img.sbs.co.kr/newimg/news/20220509/201662572_500.jpg",
        "tags": ["문화/역사 탐방", "도심", "문화/역사 체험", "독특한 장소", "안전하고 편안한 환경"],
        "summary": "청와대는 대한민국 대통령이 거주하는 공식 관저로, 한국 정치의 상징적인 장소입니다. 역사적인 의미가 깊은 곳으로, 청와대 일대는 아름다운 자연경관을 자랑하며, 이곳을 방문하면 한국의 정치적, 역사적 배경을 이해할 수 있습니다.",
        "surrounding_area": "청와대 주변은 경복궁, 북촌한옥마을, 인사동 등 전통적인 문화 지역과 가까워, 역사와 문화가 얽힌 독특한 상권을 형성하고 있습니다."
    },
    {
        "name": "수원화성",
        "description": "수원화성은 조선시대의 대표적인 성곽으로, 유네스코 세계문화유산으로 지정되어 있습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEwMTNfNTgg%2FMDAxNzI4ODEwNDcyNTk3.s0GDsL_VcV7njnyQBlxlkHhecJraJINFdB_p0pNsKAkg.FRB4D4Vj2dbCOhRU9q-QGmnzt4R4w3LbI4fHCJ_ZGX8g.JPEG%2FKakaoTalk_20241011_235714368_17.jpg&type=sc960_832",
        "tags": ["문화/역사 탐방", "유적지", "문화/역사 체험", "사진 명소", "좋은 접근성", "저렴한 가격"],
        "summary": "수원화성은 18세기 정조대왕에 의해 건설된 성곽으로, 전략적 가치와 미학적 가치를 모두 지닌 역사적 명소입니다. 성곽과 함께 성안의 궁궐, 군사시설을 돌아볼 수 있습니다. 특히 야경이 아름다워 많은 관광객들이 찾습니다.",
        "surrounding_area": "수원화성 주변에는 전통적인 한국 음식을 즐길 수 있는 맛집들이 많이 위치해 있으며, 수원역과의 접근성도 좋아 쇼핑과 음식 문화도 함께 즐길 수 있는 상권입니다."

    },
    {
        "name": "구리 동구릉",
        "description": "구리 동구릉은 조선 왕릉 중 하나로, 아름다운 자연경관과 함께 역사적 의미를 지닌 장소입니다.",
        "image_url": "https://www.heritage.go.kr/unisearch/images/history_site/thumb/2021070816110901.jpg",
        "tags": ["문화/역사 탐방", "유적지", "문화/역사 체험", "사진 명소", "안전하고 편안한 환경"],
        "summary": "구리 동구릉은 조선왕조의 역사를 간직한 왕릉으로, 특히 정종, 태종의 묘소가 위치해 있습니다. 고요한 자연 속에서 왕의 위엄과 고풍스러운 분위기를 느낄 수 있는 곳입니다. 산책과 역사 체험에 좋은 장소입니다.",
        "surrounding_area": "동구릉 인근에는 자연경관이 뛰어난 산책로와 카페들이 위치해 있습니다. 구리시내와의 접근성도 좋아 관광객들에게 편리합니다."

    },
    {
        "name": "파주 임진각",
        "description": "임진각은 남북 분단의 상징적인 장소로, 평화와 통일을 기원하는 공간입니다.",
        "image_url": "https://tour.paju.go.kr/upload/tour/open/culture/gallery/99/191.JPG",
        "tags": ["문화/역사 탐방", "자연", "문화/역사 체험", "사진 명소", "독특한 장소", "안전하고 편안한 환경"],
        "summary": "임진각은 한국전쟁 당시의 상처를 치유하려는 의미를 담고 있는 평화의 기념관과 공원이 있습니다. 북녘을 향한 전망대와 평화의 불꽃이 있는 기념비 등 다양한 시설을 갖추고 있습니다. 가족 단위 방문객들에게 적합한 장소입니다.",
        "surrounding_area": "임진각 근처에는 휴게소와 전통적인 한국 음식점들이 있으며, 가까운 파주 출판도시와 헤이리 예술마을도 많은 관광객들이 찾는 명소입니다."
    },
    {
        "name": "안성 남사당놀이",
        "description": "남사당놀이는 전통적인 한국의 민속 공연으로, 다양한 예술적 요소가 결합된 공연입니다.",
        "image_url": "https://cdn.panews.co.kr/news/photo/201304/2231_2042_5454.jpg",
        "tags": ["음악 활동", "무용 활동", "도심", "유적지", "문화/역사 체험", "예술 관련 교양 쌓기", "저렴한 가격", "독특한 장소"],
        "summary": "남사당놀이에서는 전통적인 한국의 마당극, 탈춤, 줄타기 등을 감상할 수 있습니다. 이 공연은 유네스코 인류무형문화유산으로 지정된 전통 공연예술입니다. 다양한 전통 문화 체험 프로그램도 함께 제공됩니다.",
      "surrounding_area": "안성의 전통적인 시장과 음식점들이 많은데, 특히 농산물을 이용한 지역 특산물과 함께 전통 음식을 즐길 수 있습니다."
    },
    {
        "name": "광주 남한산성",
        "description": "남한산성은 조선시대의 방어 시설로, 역사적 가치가 높은 유적지입니다.",
        "image_url": "https://www.gjcity.go.kr/tour/img/sub01/img_namhan1.png",
        "tags": ["문화/역사 탐방", "유적지", "문화/역사 체험", "사진 명소", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "남한산성은 서울 근교에 위치한 고대 산성으로, 조선시대 왕들이 피난처로 사용한 곳입니다. 탁 트인 전망과 함께 산책로와 다양한 문화유적을 경험할 수 있습니다. 역사적인 의미를 지닌 장소입니다.",
        "surrounding_area": "남한산성 일대에는 자연을 즐길 수 있는 카페와 맛집들이 있으며, 캠핑과 등산을 즐길 수 있는 공간도 제공됩니다."
    },
    {
        "name": "포천 국립수목원",
        "description": "국립수목원은 다양한 식물과 자연을 체험할 수 있는 공간으로, 힐링을 제공합니다.",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_334dkQB-q3xkFsFT-ZpXGGLcFs9jU-TFTg&s",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "저렴한 가격", "독특한 장소", "좋은 접근성", "안전하고 편안한 환경"],
        "summary": "국립수목원은 다양한 식물들을 보존하고 연구하는 시설로, 울창한 숲속에서 자연을 만끽할 수 있습니다. 특히 식물과 함께 걷는 산책로와 다양한 자연 체험 프로그램이 인기입니다.",
        "surrounding_area": "포천의 자연 환경에 맞춘 카페와 음식점들이 있으며, 가벼운 하이킹과 자연을 즐기기 좋은 상권이 형성되어 있습니다."
    },
    {
        "name": "포천 산정호수",
        "description": "산정호수는 아름다운 경관과 함께 다양한 레저 활동을 즐길 수 있는 장소입니다.",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScJ7pG73wtZYjX0Ag-_nePdhC-aHmF8EWf6A&s",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "저렴한 가격", "독특한 장소", "좋은 접근성", "안전하고 편안한 환경"],
        "summary": "산정호수는 깨끗한 호수와 주변 자연경관이 뛰어난 관광지로, 여름철에는 보트 타기와 같은 수상 스포츠를 즐길 수 있습니다. 겨울철에는 호수 주변을 산책하며 자연의 고요함을 즐길 수 있습니다.",
        "surrounding_area": "호수 주변에는 레스토랑과 카페, 숙소들이 밀집해 있으며, 자연 친화적인 분위기에서 휴식과 식사를 즐길 수 있습니다."
    },
    {
        "name": "여주 영릉",
        "description": "영릉은 조선 왕릉 중 하나로, 역사적 가치가 높은 유적지입니다.",
        "image_url": "https://www.sunnews.co.kr/news/photo/202004/67963_45185_5621.jpg",
        "tags": ["문화/역사 탐방", "유적지", "문화/역사 체험", "사진 명소", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "영릉은 조선의 22대 왕인 정조의 묘소로, 매우 고풍스럽고 정교한 구조를 자랑합니다. 묘역 주변에는 자연경관이 아름다워 산책하기 좋은 곳입니다.",
        "surrounding_area": "여주 일대에는 전통적인 한국 음식점들이 많으며, 지역 특산물인 여주 쌀과 관련된 먹거리를 즐길 수 있습니다."
    },
    {
        "name": "양평 두물머리",
        "description": "두물머리는 아름다운 자연경관과 함께 힐링을 제공하는 장소입니다.",
        "image_url": "https://i.namu.wiki/i/9et9vbBvaXe7z5iIWvWn_znGyE7ugeJzWE9j3h_SnkJXGx1SvPusGsBvdUZVQLsj1_0DH2-skzoTDAbDISp-rg.webp",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "좋은 접근성", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "두물머리는 한강과 북한강이 만나는 아름다운 풍경으로 유명한 관광지입니다. 특히 일출과 일몰의 경치가 매우 아름다워 사진 촬영 명소로도 많이 알려져 있습니다.",
        "surrounding_area": "양평의 자연을 즐기기 좋은 카페와 레스토랑들이 많으며, 주변에는 다양한 농산물과 특산물을 판매하는 상점들이 있습니다."
    },
    {
        "name": "가평 아침고요수목원",
        "description": "아침고요수목원은 다양한 식물과 아름다운 경관을 제공하는 힐링 공간입니다.",
        "image_url": "https://www.gjcity.go.kr/tour/contents.do?mId=0101010100",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "좋은 접근성", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "아침고요수목원은 가평의 아름다운 자연 속에서 다양한 식물들을 감상할 수 있는 수목원입니다. 계절마다 다양한 꽃들이 피어나며, 야경도 아름다워 관광객들에게 인기가 많습니다.",
        "surrounding_area": "수목원 주변에는 산책로와 카페들이 있어 자연을 즐기며 여유로운 시간을 보낼 수 있습니다."
    },
    {
        "name": "가평 쁘띠프랑스",
        "description": "쁘띠프랑스는 프랑스의 작은 마을을 재현한 테마파크로, 다양한 문화 체험이 가능합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA2MTVfMjEx%2FMDAxNzE4NDUxNDU2MTcw.hH6WQ4bY-N6gedv1qd9U0fR4KE9KEUDhYUAeSwg9uwMg.FiAUaKn65XuKXcNKR8_qpO_OlREkACzCxCJxOu7JDR0g.JPEG%2FKakaoTalk_20240615_175216993_08.jpg&type=sc960_832",
        "tags": ["문화/역사 탐방", "쇼핑", "도심", "문화/역사 체험", "사진 명소", "새로운 음식 시도", "독특한 장소", "안전하고 편안한 환경"],
        "summary": "쁘띠프랑스는 프랑스를 테마로 한 작은 마을로, 프랑스의 건축 양식과 문화를 경험할 수 있는 장소입니다. 다양한 문화 행사와 공연도 열리며, 유럽의 매력을 느낄 수 있는 곳입니다.",
        "surrounding_area": "쁘띠프랑스 주변에는 다양한 테마파크와 자연 관광지가 위치해 있어 관광과 휴식을 동시에 즐길 수 있는 지역입니다."
    },
    {
        "name": "파주 헤이리예술마을",
        "description": "헤이리예술마을은 다양한 예술가들이 모여 만든 문화 공간으로, 예술과 문화를 체험할 수 있습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2Fdata35%2F2008%2F9%2F4%2F91%2Fimg_4648-anndam.jpg&type=sc960_832",
        "tags": ["문화/역사 탐방", "미술 활동", "도심" "문화/역사 체험", "예술 관련 교양 쌓기", "사진 명소", "독특한 장소", "안전하고 편안한 환경"],
        "summary": "헤이리예술마을은 예술과 문화를 주제로 다양한 갤러리와 작업실이 모여 있는 마을입니다. 예술 작품을 감상하고, 창작 과정을 직접 체험할 수 있는 프로그램들이 제공됩니다.",
        "surrounding_area": "헤이리 예술마을 주변에는 아트샵, 카페, 레스토랑들이 있어 예술적인 분위기 속에서 식사와 쇼핑을 즐길 수 있습니다."
    },
    {
        "name": "용인 에버랜드",
        "description": "에버랜드는 다양한 놀이기구와 테마가 있는 대형 테마파크로, 가족 단위 방문객에게 인기가 많습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAzMzFfNDAg%2FMDAxNzExODE0Mjc4OTc1.j7jI-qsvEUOLtjA8vYu6-yTOAru7L5GLKcn3P1-TXuMg.nPwsczRYIoUN7AEYVryS9vblR4QN6GP42RGnWCuu8SQg.JPEG%2FIMG_2660.jpg&type=sc960_832",
        "tags": ["액티비티", "도심", "자연", "사진 명소", "도전적인 활동", "독특한 장소"],
        "summary": "에버랜드는 놀이기구, 동물원, 수상쇼 등 다양한 즐길 거리를 제공하는 대형 테마파크입니다. 연령대에 상관없이 모든 사람이 즐길 수 있는 다양한 테마와 놀이기구가 준비되어 있습니다. 특히, 시즌별로 다채로운 축제와 공연이 열려 방문객들의 큰 인기를 끌고 있습니다.",
        "surrounding_area": "에버랜드 주변에는 자연을 즐길 수 있는 리조트와 음식점들이 위치해 있으며, 근처의 용인 한국민속촌도 함께 방문할 수 있는 인기 관광지입니다."
    },
    {
        "name": "용인 한국민속촌",
        "description": "한국민속촌은 전통 한국 문화를 체험할 수 있는 공간으로, 다양한 전통 공연과 체험 프로그램이 있습니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200525_120%2F1590394419044DhFmg_JPEG%2FSp-rpylEcqrQII9AKbA7Bamy.jpg",
        "tags": ["문화/역사 탐방", "음악 활동", "무용 활동", "액티비티", "유적지", "문화/역사 체험", "도전적인 활동", "새로운 음식 시도", "사진 명소", "좋은 접근성", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "한국민속촌은 전통적인 한국의 건축 양식과 생활 문화를 재현한 테마파크입니다. 한복을 입은 사람들과 전통 놀이, 음식 체험 등을 통해 한국의 역사와 문화를 배울 수 있는 장소입니다. 어린이들과 가족 단위 관광객에게 매우 인기 있습니다.",
        "surrounding_area": "한국민속촌 주변에는 전통적인 맛집들이 많고, 지역 특산물인 한과나 전통 음식을 맛볼 수 있는 곳도 많이 있습니다."
    },
    {
        "name": "연천 한탄강",
        "description": "한탄강은 아름다운 자연경관과 함께 다양한 레저 활동을 즐길 수 있는 장소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA3MTFfNjgg%2FMDAxNjg5MDgzMDgyMTU1.H-lfBOA3r3l4FexsBanABC71P1PvJumM6OsdXzm2suAg.liQzEveNHZkpRFNEtlBu0c4mS32dmXNbXWC29XR2d6Ig.JPEG.windyuzin%2F%25C5%25A9%25B1%25E2%25BA%25AF%25C8%25AFIMG_1997.jpg&type=sc960_832",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "사진 명소", "도전적인 활동", "독특한 장소", "안전하고 편안한 환경"],
        "summary": "연천 한탄강은 맑고 깨끗한 강물과 주변의 수려한 자연경관으로 유명한 곳입니다. 특히 래프팅과 카약, 수상레저를 즐길 수 있는 장소로도 인기가 많습니다. 가족이나 친구들과 함께 자연 속에서 활동적인 시간을 보낼 수 있습니다.",
        "surrounding_area": "한탄강 주변에는 캠핑장과 바베큐 시설이 있으며, 강을 따라 산책로도 잘 조성되어 있어 자연을 만끽할 수 있는 여유로운 장소입니다."
    },
    {
        "name": "과천 서울랜드",
        "description": "서울랜드는 다양한 놀이기구와 테마가 있는 대형 테마파크로, 가족 단위 방문객에게 인기가 많습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA2MTNfMjQz%2FMDAxNjg2NjU2NTY2MDk5.9hPWbxxWFI460J2-swcOb1hWEIxk97dVlV-TwqDyksAg.po3SZKf_h-1PIqEy_QizrB6CPZQj-4gp9apizsse-CYg.JPEG.k30935%2F20230611%25A3%25DF183853.jpg&type=sc960_832",
        "tags": ["액티비티", "도심", "도전적인 활동", "사진 명소", "독특한 장소"],
        "summary": "서울랜드는 서울 근교에 위치한 인기 놀이공원으로, 다양한 테마와 놀이기구가 있어 온 가족이 함께 즐길 수 있습니다. 계절마다 다채로운 축제와 행사가 열리며, 특히 어린이들에게 인기가 많습니다.",
        "surrounding_area": "서울랜드 주변에는 과천과 서울을 잇는 교통망이 발달되어 있으며, 서울대공원과 가까워 함께 방문할 수 있는 이점이 있습니다."
    },
    {
        "name": "서울대공원",
        "description": "서울대공원은 동물원과 식물원이 함께 있는 대형 공원으로, 가족 단위 방문객에게 인기가 많습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEwMzBfMzEg%2FMDAxNzMwMjIyNzE4NDc0.gavDBRGkM2Firv-2l1WpaY3ueaypY--Qfk3n3e4bK40g.Px9e_GzC-hwWPPD1h6WGXxfDo8jrvUOcLbW-E7Sr4psg.JPEG%2FJHW03360.JPG",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "사진 명소", "좋은 접근성", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "서울대공원은 서울 근교에 있는 대형 공원으로, 동물원, 식물원, 호수 등이 잘 조성되어 있어 산책과 여가를 즐기기 좋은 장소입니다. 동물원에서는 다양한 동물을 관람할 수 있으며, 자연 속에서 힐링할 수 있는 공간입니다.",
        "surrounding_area": "서울대공원 근처에는 맛집과 카페가 많고, 가까운 과천 서울랜드와 함께 관광할 수 있어 많은 방문객들이 찾습니다."
    },
    {
        "name": "광명동굴",
        "description": "광명동굴은 다양한 동굴 탐험과 체험을 제공하는 관광지로, 신비로운 자연을 경험할 수 있습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAzMTdfMjMg%2FMDAxNzEwNjYwMzk3Nzcx.01hdE4mfhDZI3qeODG6Y3-tkO3_xrH2Yr4clZcdwyYwg.Hy-BAQpvkF584P79uEk7O7zXTdtShWKkmbEbz8_zC6og.JPEG%2FDSC04113.JPG&type=sc960_832",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "도전적인 활동", "사진 명소", "독특한 장소"],
        "summary": "광명동굴은 폐광된 광산을 활용하여 만든 관광지로, 다양한 동굴 탐험과 테마 시설들이 있습니다. 특별한 체험을 원하는 방문객들에게 흥미로운 경험을 제공합니다. 또한 동굴 내부에서 열리는 문화 공연과 전시도 인기를 끌고 있습니다.",
        "surrounding_area": "광명동굴 주변에는 광명시의 다양한 상업시설과 쇼핑몰이 있어 쇼핑과 관광을 함께 즐길 수 있습니다."
    },
    {
        "name": "화성 제부도",
        "description": "제부도는 아름다운 해변과 자연경관을 제공하는 관광지로, 힐링을 제공합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAyMzExMDZfMTgz%2FMDAxNjk5MjM0NDUwODYy.6sYu-1BRmOjfWwpTNAE2mxNQWrMSrl4osVtLoztYGhUg.NZXIaBxuvPoPrhOpFSToEl65iiZAfkwLRteUnc7wcT0g.PNG%2FIksbJj1bBxB2QAUu8BPCpUFEn5Mw.jpg&type=sc960_832",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "제부도는 화성시의 작은 섬으로, 아름다운 바다 풍경과 조용한 분위기를 즐길 수 있는 곳입니다. 특히, 제부도의 모래사장에서 자전거를 타고 주변을 돌아보거나, 갯벌 체험을 할 수 있습니다.",
        "surrounding_area": "제부도 근처에는 해산물을 즐길 수 있는 식당들이 있으며, 섬 주변을 돌아볼 수 있는 카페와 상점들도 존재합니다."
    },
    {
        "name": "광주 화담숲",
        "description": "화담숲은 다양한 식물과 아름다운 경관을 제공하는 힐링 공간입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjEwMjBfMTQ0%2FMDAxNjY2MjM4NzEzNDI1.qCO0t7FNTsrmJe6top5AlUcBlC5JvoZGXSoZoUQHieQg.mFy1vdqnjivvmyWgqpgttzzt1V0geiSLjNkk4LjyXcIg.JPEG.dal831%2F20221016%25A3%25DF111958.jpg&type=sc960_832",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "화담숲은 광주에 위치한 큰 규모의 정원으로, 자연과 조화롭게 어우러진 다양한 식물들을 감상할 수 있는 공간입니다. 특히 봄과 가을에는 다양한 꽃과 단풍을 즐길 수 있는 명소로 알려져 있습니다.",
        "surrounding_area": "화담숲 주변에는 카페와 음식점들이 많아, 자연을 만끽하며 여유롭게 음식을 즐기기에 좋은 장소입니다."
    },
    {
        "name": "포천아트밸리",
        "description": "포천아트밸리는 예술과 자연이 어우러진 공간으로, 다양한 문화 체험이 가능합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEyMzBfMTk5%2FMDAxNzAzOTI4NzIwMDQ5.W3fzYG94ieXm_S-P6UyJS-YC1TeSWDqpZIP37QrRrzUg.lew0rGFAKpayjvshZ4MMtLidtMuHPFt6NuEC6vz5Voog.JPEG.tototorlck%2F20230520%25A3%25DF120832.jpg&type=sc960_832",
        "tags": ["액티비티", "자연 탐험", "자연", "도전적인 활동", "힐링", "사진 명소", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "포천아트밸리는 예술 작품과 자연이 어우러진 공간으로, 조각 공원, 전시관, 야외 공연장 등이 잘 조성되어 있습니다. 다양한 예술 작품을 감상할 수 있으며, 자연 속에서 여유로운 시간을 보낼 수 있습니다.",
        "surrounding_area": "아트밸리 주변에는 지역 농산물을 판매하는 마켓과 지역 특산물 가게들이 있으며, 포천의 자연을 즐길 수 있는 카페들이 많습니다."
    },
    {
        "name": "안성팜랜드",
        "description": "안성팜랜드는 농업과 자연을 체험할 수 있는 공간으로, 가족 단위 방문객에게 인기가 많습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEwMTFfMjgx%2FMDAxNzI4NjA2OTkxMjQ4.vJfbYsc0tdBzXZKaVUblkasPjcs4Z_2TB6MAuj9tTFog.mSrIiZEqm40TpdV00fC4kAMkYUQEzOaLrKiaHpnQIKIg.JPEG%2F%25BE%25C8%25BC%25BA%25C6%25CA%25B7%25A3%25B5%25E5%25C7%25CE%25C5%25A9%25B9%25C4%25B8%25AE_19.jpg&type=sc960_832",
        "tags": ["액티비티", "문화/역사 탐방", "자연", "문화/역사 체험", "사진 명소", "힐링", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "안성팜랜드는 농촌 체험과 함께 자연을 즐길 수 있는 곳입니다. 농작물을 수확하거나 동물들과 교감할 수 있는 프로그램들이 제공되어 어린이들과 가족 단위 방문객들에게 특히 인기가 많습니다.",
        "surrounding_area": "팜랜드 주변에는 농산물을 이용한 다양한 먹거리와 지역 특산물이 많이 있으며, 산책과 야외 활동을 즐기기에 좋은 장소입니다."
    },
    {
        "name": "포천 허브아일랜드",
        "description": "허브아일랜드는 다양한 허브와 식물을 체험할 수 있는 공간으로, 힐링을 제공합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEwMjBfMjQ0%2FMDAxNjk3NzU0MTU1NDA3.L9G4pFLgwD9Kbb9nToi12JdU5R2UYENX3c0CszIFGHwg.Dzd9uHcj4lTHc_pqLbb5jghUjNi7HIAY-ETpzNtWsd8g.JPEG.maum0577%2F4.jpg&type=sc960_832",
        "tags": ["자연 탐험", "자연", "힐링", "새로운 음식 시도", "사진 명소", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"],
        "summary": "포천 허브아일랜드는 허브를 테마로 한 정원과 테마파크로, 향긋한 허브 향을 즐기며 다양한 체험을 할 수 있는 공간입니다. 허브를 이용한 다양한 상품을 구매할 수 있으며, 허브 요리 체험도 가능합니다.",
        "surrounding_area": "허브아일랜드 주변에는 허브를 주제로 한 카페와 레스토랑이 많아, 자연 속에서 여유로운 시간을 보낼 수 있는 장소입니다."
    },
    {
        "name": "연천 재인폭포 공원",
        "description": "재인폭포 공원은 아름다운 폭포와 자연경관을 제공하는 관광지로, 힐링을 제공합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEwMTFfMjU0%2FMDAxNzI4NjI0NTY2NzEw.1a98yvC8jSDVfFv-aGqcYvMusv5EJt1cb_3lLH0NGiUg.JLNNxqjG_89doOyCleoXU0Ti-todHD5YB4BNXjNLctog.JPEG%2F20240528_132303_HDR.jpg&type=sc960_832",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "사진 명소", "독특한 장소", "저렴한 가격"],
        "summary": "연천 재인폭포는 맑고 깨끗한 물과 푸른 숲 속에 숨겨진 폭포로, 하이킹과 자연을 즐기기에 좋은 곳입니다. 주변은 깊은 숲과 계곡으로 둘러싸여 있어, 사계절 내내 다양한 자연경관을 감상할 수 있습니다. 특히 여름에는 물놀이를 즐기기 위해 많은 관광객들이 찾습니다.",
        "surrounding_area": "재인폭포 주변에는 트레킹 코스와 야영장이 있어 야외 활동을 즐기기에 적합합니다. 또한, 근처에는 지역 식당에서 신선한 재료로 만든 전통적인 음식을 맛볼 수 있습니다."
    },
    {
        "name": "가평 자라섬",
        "description": "자라섬은 아름다운 자연경관과 다양한 레저 활동을 즐길 수 있는 장소입니다.",
        "image_url": "https://search.pstatic.net/sunny/?src=http%3A%2F%2Fwww.dicalove.com%2Ffiles%2Fattach%2Fimages%2F154%2F317%2F466%2F025%2Fcb9d9632331b0e0ddf528c3922d23083.jpg&type=sc960_832",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "도전적인 활동", "사진 명소", "독특한 장소", "저렴한 가격"],
        "summary": "가평 자라섬은 북한강에 위치한 작은 섬으로, 아름다운 자연과 다양한 문화 활동을 즐길 수 있는 곳입니다. 매년 자라섬재즈페스티벌과 같은 대형 문화행사가 열려 많은 사람들이 찾습니다. 섬은 자전거 도로와 산책로가 잘 마련되어 있어 관광객들이 편안하게 자연을 즐길 수 있습니다.",
        "surrounding_area": "자라섬 주변에는 많은 카페와 레스토랑이 있어 방문객들이 지역 특산물인 가평 사과나 한정식 등을 즐길 수 있습니다. 또한, 북한강을 따라 자전거를 타거나 산책할 수 있는 좋은 환경이 마련되어 있습니다."
    }
]

# 질문 및 선택지 설정
questions_options = [
    {
        "question": "어떤 종류의 활동을 즐기시나요?",
        "options": ["문화/역사 탐방", "자연 탐험", "쇼핑", "액티비티", "문학적 활동", "음악 활동", "무용 활동", "미술 활동"]
    },
    {
        "question": "어떤 환경에서 여행을 즐기고 싶으신가요?",
        "options": ["도심", "자연", "유적지"]
    },
    {
        "question": "여행 중 어떤 경험을 가장 중시하시나요?",
        "options": ["사진 명소", "문화/역사 체험", "힐링", "도전적인 활동", "예술 관련 교양 쌓기", "새로운 음식 시도"]
    },
    {
        "question": "여행 중 어떤 것을 가장 중요하게 생각하시나요?",
        "options": ["좋은 접근성", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"]
    }
    
]

import random

# Streamlit 앱 레이아웃 설정
st.title("T.OUR: 관광지를 추천해드립니다")

# 세션 상태 초기화
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = []
if 'recommended_destinations' not in st.session_state:
    st.session_state.recommended_destinations = []
if 'selected_place' not in st.session_state:
    st.session_state.selected_place = None  # 더 알아보기 버튼 클릭 시 선택된 장소 저장

# 질문별 태그 분리
activity_tags = ["문화/역사 탐방", "자연 탐험", "쇼핑", "액티비티", 
                 "문학적 활동", "음악 활동", "무용 활동", "미술 활동"]
environment_tags = ["도심", "자연", "유적지"]

# 각 질문에 대해 선택할 수 있도록 UI를 구성
for i, q in enumerate(questions_options):
    answer = st.selectbox(q["question"], options=q["options"], key=f"question_{i}")
    if len(st.session_state.user_answers) < len(questions_options):
        st.session_state.user_answers.append(answer)

# 추천 버튼
if st.button("추천받기"):
    # 이전에 선택된 장소 초기화
    st.session_state.selected_place = None  # 더 알아보기 상태 초기화

    # 사용자 답변 필터링
    activity_answers = [answer for answer in st.session_state.user_answers if answer in activity_tags]
    environment_answers = [answer for answer in st.session_state.user_answers if answer in environment_tags]

    # "활동" 태그와 "환경" 태그 모두 포함하는 관광지 필터링
    filtered_destinations = [
        destination for destination in destinations
        if all(
            any(tag in activity_answers for tag in destination["tags"]),  # 활동 태그 포함 여부
            any(tag in environment_answers for tag in destination["tags"])  # 환경 태그 포함 여부
        )
    ]

    # 필터링된 결과에서 무작위로 2개 선택
    if len(filtered_destinations) >= 2:
        st.session_state.recommended_destinations = random.sample(filtered_destinations, 2)
    elif len(filtered_destinations) == 1:
        # 필터링된 관광지가 1개만 있을 경우 그 관광지를 추천
        st.session_state.recommended_destinations = filtered_destinations
    else:
        # 필터링 결과가 없으면 일치 개수로 상위 관광지를 추천
        matching_scores = []
        for destination in destinations:
            # 일치하는 태그 수 계산
            score = sum(tag in destination["tags"] for tag in st.session_state.user_answers)
            matching_scores.append((destination, score))

        # 일치 태그 개수 기준으로 정렬
        matching_scores.sort(key=lambda x: x[1], reverse=True)

        # 상위 두 개 선택
        st.session_state.recommended_destinations = [
            destination for destination, score in matching_scores[:2]
        ]

# 추천 결과 표시
for place in st.session_state.recommended_destinations:
    st.subheader(place["name"])
    st.write(place["description"])
    st.image(place["image_url"], use_column_width=True)
    
    # '더 알아보기' 버튼
    if st.button(f"{place['name']}에 대해 더 알아보기", key=f"more_{place['name']}"):
        st.session_state.selected_place = place  # 버튼 클릭 시 선택된 장소 저장
          # 한 번 클릭하면 하나만 표시되도록 'break' 추가

# 선택된 관광지의 세부 정보 표시
if st.session_state.selected_place:
    place = st.session_state.selected_place
    st.write("### 세 줄 요약")
    st.write(place.get("summary", "요약 정보가 없습니다."))
    st.write("### 주변 상권")
    st.write(place.get("surrounding_area", "주변 상권 정보가 없습니다."))
