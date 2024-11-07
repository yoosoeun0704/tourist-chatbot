# app.py

import streamlit as st
import random

# 관광지 데이터
destinations = [
    {
        "name": "경복궁",
        "description": "한국의 전통과 역사를 경험할 수 있는 서울의 대표 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA5MDRfODcg%2FMDAxNzI1NDU5OTg1ODcx.20ZW5yxoZO6aCc1Ds-nDzGMyAx-qObh5n9Ke5Jo3HVYg.JA7cHnv7gZ2JWYfRzBJ5s-xZVCq40sBvwqOmLGsZ5kog.JPEG%2F3C4A9776_1.jpg&type=sc960_832",
        "tags": ["문화/역사 탐방", "도심", "유적지", "문화/역사 체험", "사진 명소", "좋은 접근성"]
    },
    {
        "name": "서울숲",
        "description": "푸르른 한강과 함께 자연을 즐길 수 있는 서울의 인기있는 힐링 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200728_296%2F1595899415265D5A3d_JPEG%2F%25B0%25A1%25C1%25B7%25B8%25B6%25B4%25E71.jpg",
        "tags": ["자연 탐험", "자연", "사진 명소", "힐링", "좋은 접근성", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "더현대 서울",
        "description": "즐거운 먹거리를 즐기고, 쇼핑을 할 수 있는 현대백화점 더현대 서울입니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210527_297%2F16220986701968f1N7_JPEG%2F1.jpg",
        "tags": ["쇼핑", "도심", "사진 명소", "새로운 음식 시도", "좋은 접근성"]
    },
    {
        "name": "예술의 전당",
        "description": "음악, 미술, 무용, 뮤지컬 등 여러 공연을 즐길 수 있는 명소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEyMDVfMTI2%2FMDAxNzAxNzQ4ODQzMjQz.LwfjHhRI_NeOqn-vOd1rH_MrXE4tlwHFl5y1Ov0iPlcg.jtiRkigo0KpI3fYgl2slZVJyUYPaBzmGFRQrQQJzNacg.JPEG.wooyu96%2Foutput_3532954624.jpg&type=sc960_832",
        "tags": ["문학적 활동", "음악 활동", "무용 활동", "미술 활동", "도심", "사진 명소", "문화/역사 체험", "예술 관련 교양 쌓기", "좋은 접근성"]
    },
    {
        "name": "인사동길",
        "description": "전통과 현대가 어우러진 거리로, 한국의 전통 공예품과 예술작품을 구매할 수 있는 곳입니다.",
        "image_url": "https://www.museum.go.kr/uploadfile/ecms/media/2024/09/520C4D4F-5E17-F88B-024D-1B0AB916AC5C.jpg",
        "tags": ["쇼핑", "도심", "사진 명소", "문화/역사사 체험", "예술 관련 교양 쌓기", "좋은 접근성", "독특한 장소"]
    },
    {
        "name": "남산서울타워",
        "description": "서울의 상징적인 전망대로, 도시 전경을 한눈에 볼 수 있는 인기 있는 관광지입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/n%EC%84%9C%EC%9A%B8%ED%83%80%EC%9B%8C",
        "tags": ["자연 탐험", "액티비티", "자연", "사진 명소", "힐링", "저렴한 가격"]
    },
    {
        "name": "서울 국립중앙박물관",
        "description": "한국의 역사와 문화를 담고 있는 대규모 박물관으로, 다양한 전시와 교육 프로그램을 제공합니다.",
        "image_url": "https://www.museum.go.kr/uploadfile/ecms/media/2024/09/520C4D4F-5E17-F88B-024D-1B0AB916AC5C.jpg",
        "tags": ["문화/역사 탐방", "도심", "유적지", "문화/역사 체험", "예술 관련 교양 쌓기", "좋은 접근성", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "북촌한옥마을",
        "description": "전통 한옥이 잘 보존된 지역으로, 한국의 전통 건축과 문화를 체험할 수 있는 곳입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%B6%81%EC%B4%8C-%ED%95%9C%EC%98%A5-%EB%A7%88%EC%9D%84",
        "tags": ["문화/역사 탐방", "도심", "유적지", "사진 명소", "문화/역사 체험", "독특한 장소", "좋은 접근성", "저렴한 가격"]
    },
    {
        "name": "명동거리",
        "description": "쇼핑과 먹거리가 풍부한 서울의 대표적인 상업지구로, 젊은이들 사이에서 인기 있는 장소입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%AA%85%EB%8F%99",
        "tags": ["쇼핑", "도심", "새로운 음식 시도", "문화/역사 체험", "좋은 접근성"]
    },
    {
        "name": "남대문시장",
        "description": "다양한 상품과 먹거리를 저렴하게 구매할 수 있는 전통 시장으로, 현지인과 관광객 모두에게 사랑받는 곳입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%82%A8%EB%8C%80%EB%AC%B8%EC%9E%A5",
        "tags": ["쇼핑", "도심", "문화/역사 체험", "새로운 음식 시도", "좋은 접근성", "안전하고 편안한 환경", "저렴한 가격"]
    },
    {
        "name": "광장시장",
        "description": "한국의 전통 음식과 다양한 먹거리를 즐길 수 있는 시장으로, 특히 빈대떡과 마약김밥이 유명합니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EA%B4%91%EC%9E%A5%EC%9E%A5%EC%9C%A0",
        "tags": ["쇼핑", "도심", "문화/역사 체험", "새로운 음식 시도", "좋은 접근성", "안전하고 편안한 환경", "저렴한 가격"]
    },
    {
        "name": "동대문디자인플라자",
        "description": "현대적인 디자인과 건축의 상징으로, 전시, 패션, 문화 행사 등이 열리는 복합 문화 공간입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%8F%99%EB%8C%80%EB%AC%B8%EB%94%94%EC%9E%90%ED%94%84%EB%9D%BC%EC%9A%B0",
        "tags": ["쇼핑", "도심", "문화/역사사 체험", "예술 관련 교양 쌓기", "좋은 접근성", "독특한 장소"]
    },
    {
        "name": "북한산 국립공원",
        "description": "아름다운 자연 경관과 다양한 등산로를 제공하는 서울 근교의 인기 있는 국립공원입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%B6%81%ED%95%9C%EC%82%B0",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "사진 명소", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "서울스카이",
        "description": "롯데월드타워에 위치한 전망대로, 서울의 전경을 360도 파노라마로 감상할 수 있는 곳입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%84%9C%EC%9A%B8%EC%8A%A4%EC%B9%B4%EC%9D%B4",
        "tags": ["액티비티", "도심", "사진 명소", "힐링", "독특한 장소"]
    },
    {
        "name": "롯데월드",
        "description": "실내외 테마파크와 쇼핑몰이 결합된 복합 엔터테인먼트 공간으로, 가족 단위 방문객에게 인기가 많습니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%A1%AF%EB%8D%B0%EC%9B%94%EB%93%9C",
        "tags": ["액티비티", "도심", "사진 명소", "도전적인 활동", "좋은 접근성", "독특한 장소"]
    },
    {
        "name": "홍대거리",
        "description": "젊은 예술가와 음악가들이 모여드는 활기찬 거리로, 다양한 카페와 클럽, 갤러리가 즐비합니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%ED%99%8D%EB%8C%80%EA%B1%B0%EB%A6%AC",
        "tags": ["쇼핑", "액티비티", "음악 활동", "도심", "도전적인 활동", "새로운 음식 시도", "좋은 접근성"]
    },
    {
        "name": "익선동 한옥마을",
        "description": "전통 한옥을 개조한 카페와 상점들이 있는 지역으로, 독특한 분위기를 자랑합니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%9D%B8%EC%82%AC%EB%8F%99-%ED%95%9C%EC%98%A5%EB%A7%88%EC%9D%84",
        "tags": ["문화/역사 탐방", "쇼핑", "도심", "힐링", "문화/역사사 체험", "사진 명소", "독특한 장소"]
    },
    {
        "name": "서울로 7017",
        "description": "도심 속의 고가 보행도로 공원으로, 산책과 휴식을 즐길 수 있는 공간입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%84%9C%EC%9A%B8%EB%A1%9C-7017",
        "tags": ["자연 탐험", "도심", "자연", "사진 명소", "힐링", "좋은 접근성", "안전하고 편안한 환경"]
    },
    {
        "name": "코엑스",
        "description": "대규모 전시와 컨벤션 센터로, 쇼핑몰과 아쿠아리움, 도서관 등이 함께 있는 복합 문화 공간입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%BD%94%EC%97%91%EC%8A%A4",
        "tags": ["쇼핑", "액티비티", "문학적 활동", "미술 활동", "도심", "문화/역사 체험", "예술 관련 교양 쌓기", "좋은 접근성", "독특한 장소"]
    },
    {
        "name": "서울시립미술관",
        "description": "현대 미술 작품을 중심으로 다양한 전시를 개최하는 미술관으로, 예술 애호가들에게 인기 있는 장소입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%84%9C%EC%9A%B8%EC%8B%9C%EB%A6%BD%EB%AF%B8%EC%88%A0%EA%B4%80",
        "tags": ["미술 활동", "도심", "문화/역사 체험", "예술 관련 교양 쌓기", "독특한 장소", "안전하고 편안한 환경"]
    },
    {
        "name": "서대문형무소",
        "description": "일제강점기 한국의 독립운동 역사와 관련된 박물관으로, 역사 교육의 중요한 장소입니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%84%9C%EB%8C%80%EB%AC%B8%ED%98%95%EB%AC%B4%EC%86%8C",
        "tags": ["문화/역사 탐방", "도심", "유적지", "문화/역사 체험", "독특한 장소", "저렴한 가격"]
    },
    {
        "name": "청와대",
        "description": "대한민국 대통령의 전 공식 관저로, 아름다운 정원과 역사적인 건축물로 구성되어 있습니다.",
        "image_url": "https://www.istockphoto.com/kr/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%B2%AD%EC%99%80%EB%8C%80",
        "tags": ["문화/역사 탐방", "도심", "문화/역사 체험", "독특한 장소", "안전하고 편안한 환경"]
    },
    {
        "name": "수원화성",
        "description": "수원화성은 조선시대의 대표적인 성곽으로, 유네스코 세계문화유산으로 지정되어 있습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA1MjNfMTYw%2FMDAxNzE2MzkwNDkzNTkw.hGbTTrdhPUfzRFbRWP43dpPpRTLXfWC2QbadfEv-ewcg.-J48L9rp25B-ek0ZpX-fiVUQIpyctcjCV34yJC3RRDkg.JPEG%2F20240426-_C6A8780.jpg&type=sc960_832",
        "tags": ["문화/역사 탐방", "유적지", "문화/역사 체험", "사진 명소", "좋은 접근성", "저렴한 가격"]
    },
    {
        "name": "구리 동구릉",
        "description": "구리 동구릉은 조선 왕릉 중 하나로, 아름다운 자연경관과 함께 역사적 의미를 지닌 장소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140911_179%2Fesilvia_1410396962773dvXGA_JPEG%2F%25B5%25BF%25B1%25B8%25B8%25AA-%25B0%25C7%25BF%25F8%25B8%25AA-%25C1%25B6%25BC%25B1_%25BF%25D5%25B8%25AA-%25BC%25BC%25B0%25E8%25C0%25AF%25BB%25EA-%25C0%25AF%25B3%25D7%25BD%25BA%25C4%25DA_%25BC%25BC%25B0%25E8%25C0%25AF%25BB%25EA-018-20140911-1.JPG&type=sc960_832",
        "tags": ["문화/역사 탐방", "유적지", "문화/역사 체험", "사진 명소", "안전하고 편안한 환경"]
    },
    {
        "name": "파주 임진각",
        "description": "임진각은 남북 분단의 상징적인 장소로, 평화와 통일을 기원하는 공간입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA5MTJfMjMw%2FMDAxNjk0NTAxMjkyNDIy.Y7sNP9lTBzSNY2tnS282vF1XPiSsbsmkaOTZEfrwsoYg.vrB_I9gZcoGAjhzpCrlJ7sHs0Kj1DLN4TcI1ueAffAAg.JPEG.bgrace823%2F1694501291656.jpg&type=sc960_832",
        "tags": ["문화/역사 탐방", "자연", "문화/역사 체험", "사진 명소", "독특한 장소", "안전하고 편안한 환경"]
    },
    {
        "name": "안성 남사당놀이",
        "description": "남사당놀이는 전통적인 한국의 민속 공연으로, 다양한 예술적 요소가 결합된 공연입니다.",
        "image_url": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fimg3.yna.co.kr%2Fphoto%2Fyna%2FYH%2F2014%2F11%2F26%2FPYH2014112602920006100_P4.jpg&type=sc960_832",
        "tags": ["음악 활동", "무용 활동", "도심", "유적지", "문화/역사 체험", "예술 관련 교양 쌓기", "저렴한 가격", "독특한 장소"]
    },
    {
        "name": "광주 남한산성",
        "description": "남한산성은 조선시대의 방어 시설로, 역사적 가치가 높은 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA0MDFfMTMx%2FMDAxNzExOTM4NTAxMTk0.Xfva0FMJTvPuKHk4cyDfHMdZ58sb-lj6s0GE9QaSdZUg.sDUyoDQn_DMBicrbgLSN3QaMvUYRPkeM_7YWTRUJKLsg.PNG%2FAR07C9150HZS%25B3%25B2%25C7%25D1%25BB%25EA%25BC%25BA.png&type=sc960_832",
        "tags": ["문화/역사 탐방", "유적지", "문화/역사 체험", "사진 명소", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "포천 국립수목원",
        "description": "국립수목원은 다양한 식물과 자연을 체험할 수 있는 공간으로, 힐링을 제공합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzA2MTRfMzAw%2FMDAxNDk3NDQxMTk4MjA2.S2RxbQ9-mIpffoZ_p4-2w9GMf7zGJBdjocDqZad08Usg.FL0UoAYDAIwPZPn0CcqouqYnAGMm688LqFXFnZ3uscUg.JPEG.inblue99%2FDSC02579.JPG&type=sc960_832",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "저렴한 가격", "독특한 장소", "좋은 접근성", "안전하고 편안한 환경"]
    },
    {
        "name": "포천 산정호수",
        "description": "산정호수는 아름다운 경관과 함께 다양한 레저 활동을 즐길 수 있는 장소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA5MTJfNzUg%2FMDAxNzI2MTI5NTE4MTA4.H3knrJSeKiHWRdPlejhO3MFvldiwF_yj3KWtg3D8ZBgg.7H1TLWHPrZRfdyqdLzkmna3KFuFX4XM8ug8ghOd3tgwg.JPEG%2F20240829_151032.jpg&type=sc960_832",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "사진 명소", "도전적인 활동", "독특한 장소", "좋은 접근성"]
    },
    {
        "name": "여주 영릉",
        "description": "영릉은 조선 왕릉 중 하나로, 역사적 가치가 높은 유적지입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA5MTdfMjU2%2FMDAxNjAwMzE2NDMxMjAx.bDmsrSiQiVAO5slVEGsnIdtaZVerUGiIIr-pnJm7ww0g.WvpdpNVukbY_lW514Y0WStVwQHO6sPWb5QGKWdfGiUIg.JPEG.gassembly%2Fthumb_5e51fe1bb8534ebf8d52baecc62bf60b_1438672254893.jpg&type=sc960_832",
        "tags": ["문화/역사 탐방", "유적지", "문화/역사 체험", "사진 명소", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "양평 두물머리",
        "description": "두물머리는 아름다운 자연경관과 함께 힐링을 제공하는 장소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEwMThfNjEg%2FMDAxNzI5MjI2ODkzNzQ4.Nf6pEchDl80YZJ-s9LMevaAF8K18p3D5-9mbiGRb9mMg.Uqbm_vtwnoEunei6by5bDLfQtcdJawGeetUSWAUenPAg.JPEG%2F%25B5%25CE%25B9%25B0%25B8%25D3%25B8%25AE01.jpg&type=sc960_832",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "좋은 접근성", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "가평 아침고요수목원",
        "description": "아침고요수목원은 다양한 식물과 아름다운 경관을 제공하는 힐링 공간입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA2MTVfMjk3%2FMDAxNzE4NDQ0OTkxNjUx.LcyvDUZnMuR4bpxi4T0hglYk05XxGcb4Hs93zUWlRVYg.chIjkDGfPgi87XUJ9ne57TjLvstFdhma8j_a2Cam3Uwg.JPEG%2FIMG_5499.jpg&type=sc960_832",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "좋은 접근성", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "가평 쁘띠프랑스",
        "description": "쁘띠프랑스는 프랑스의 작은 마을을 재현한 테마파크로, 다양한 문화 체험이 가능합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA2MTVfMjEx%2FMDAxNzE4NDUxNDU2MTcw.hH6WQ4bY-N6gedv1qd9U0fR4KE9KEUDhYUAeSwg9uwMg.FiAUaKn65XuKXcNKR8_qpO_OlREkACzCxCJxOu7JDR0g.JPEG%2FKakaoTalk_20240615_175216993_08.jpg&type=sc960_832",
        "tags": ["문화/역사 탐방", "쇼핑", "도심", "문화/역사 체험", "사진 명소", "새로운 음식 시도", "독특한 장소", "안전하고 편안한 환경"]
    },
    {
        "name": "파주 헤이리예술마을",
        "description": "헤이리예술마을은 다양한 예술가들이 모여 만든 문화 공간으로, 예술과 문화를 체험할 수 있습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2Fdata35%2F2008%2F9%2F4%2F91%2Fimg_4648-anndam.jpg&type=sc960_832",
        "tags": ["문화/역사 탐방", "미술 활동", "도심" "문화/역사 체험", "예술 관련 교양 쌓기", "사진 명소", "독특한 장소", "안전하고 편안한 환경"]
    },
    {
        "name": "용인 에버랜드",
        "description": "에버랜드는 다양한 놀이기구와 테마가 있는 대형 테마파크로, 가족 단위 방문객에게 인기가 많습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAzMzFfNDAg%2FMDAxNzExODE0Mjc4OTc1.j7jI-qsvEUOLtjA8vYu6-yTOAru7L5GLKcn3P1-TXuMg.nPwsczRYIoUN7AEYVryS9vblR4QN6GP42RGnWCuu8SQg.JPEG%2FIMG_2660.jpg&type=sc960_832",
        "tags": ["액티비티", "도심", "자연", "사진 명소", "도전적인 활동", "독특한 장소"]
    },
    {
        "name": "용인 한국민속촌",
        "description": "한국민속촌은 전통 한국 문화를 체험할 수 있는 공간으로, 다양한 전통 공연과 체험 프로그램이 있습니다.",
        "image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200525_120%2F1590394419044DhFmg_JPEG%2FSp-rpylEcqrQII9AKbA7Bamy.jpg",
        "tags": ["문화/역사 탐방", "음악 활동", "무용 활동", "액티비티", "유적지", "문화/역사 체험", "도전적인 활동", "새로운 음식 시도", "사진 명소", "좋은 접근성", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "연천 한탄강",
        "description": "한탄강은 아름다운 자연경관과 함께 다양한 레저 활동을 즐길 수 있는 장소입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA3MTFfNjgg%2FMDAxNjg5MDgzMDgyMTU1.H-lfBOA3r3l4FexsBanABC71P1PvJumM6OsdXzm2suAg.liQzEveNHZkpRFNEtlBu0c4mS32dmXNbXWC29XR2d6Ig.JPEG.windyuzin%2F%25C5%25A9%25B1%25E2%25BA%25AF%25C8%25AFIMG_1997.jpg&type=sc960_832",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "사진 명소", "도전적인 활동", "독특한 장소", "안전하고 편안한 환경"]
    },
    {
        "name": "과천 서울랜드",
        "description": "서울랜드는 다양한 놀이기구와 테마가 있는 대형 테마파크로, 가족 단위 방문객에게 인기가 많습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA2MTNfMjQz%2FMDAxNjg2NjU2NTY2MDk5.9hPWbxxWFI460J2-swcOb1hWEIxk97dVlV-TwqDyksAg.po3SZKf_h-1PIqEy_QizrB6CPZQj-4gp9apizsse-CYg.JPEG.k30935%2F20230611%25A3%25DF183853.jpg&type=sc960_832",
        "tags": ["액티비티", "도심", "도전적인 활동", "사진 명소", "독특한 장소"]
    },
    {
        "name": "서울대공원",
        "description": "서울대공원은 동물원과 식물원이 함께 있는 대형 공원으로, 가족 단위 방문객에게 인기가 많습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEwMzBfMzEg%2FMDAxNzMwMjIyNzE4NDc0.gavDBRGkM2Firv-2l1WpaY3ueaypY--Qfk3n3e4bK40g.Px9e_GzC-hwWPPD1h6WGXxfDo8jrvUOcLbW-E7Sr4psg.JPEG%2FJHW03360.JPG",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "사진 명소", "좋은 접근성", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "광명동굴",
        "description": "광명동굴은 다양한 동굴 탐험과 체험을 제공하는 관광지로, 신비로운 자연을 경험할 수 있습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAzMTdfMjMg%2FMDAxNzEwNjYwMzk3Nzcx.01hdE4mfhDZI3qeODG6Y3-tkO3_xrH2Yr4clZcdwyYwg.Hy-BAQpvkF584P79uEk7O7zXTdtShWKkmbEbz8_zC6og.JPEG%2FDSC04113.JPG&type=sc960_832",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "도전적인 활동", "사진 명소", "독특한 장소"]
    },
    {
        "name": "화성 제부도",
        "description": "제부도는 아름다운 해변과 자연경관을 제공하는 관광지로, 힐링을 제공합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAyMzExMDZfMTgz%2FMDAxNjk5MjM0NDUwODYy.6sYu-1BRmOjfWwpTNAE2mxNQWrMSrl4osVtLoztYGhUg.NZXIaBxuvPoPrhOpFSToEl65iiZAfkwLRteUnc7wcT0g.PNG%2FIksbJj1bBxB2QAUu8BPCpUFEn5Mw.jpg&type=sc960_832",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "광주 화담숲",
        "description": "화담숲은 다양한 식물과 아름다운 경관을 제공하는 힐링 공간입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjEwMjBfMTQ0%2FMDAxNjY2MjM4NzEzNDI1.qCO0t7FNTsrmJe6top5AlUcBlC5JvoZGXSoZoUQHieQg.mFy1vdqnjivvmyWgqpgttzzt1V0geiSLjNkk4LjyXcIg.JPEG.dal831%2F20221016%25A3%25DF111958.jpg&type=sc960_832",
        "tags": ["자연 탐험", "자연", "힐링", "사진 명소", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "포천아트밸리",
        "description": "포천아트밸리는 예술과 자연이 어우러진 공간으로, 다양한 액티비티와 문화 체험이 가능합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEyMzBfMTk5%2FMDAxNzAzOTI4NzIwMDQ5.W3fzYG94ieXm_S-P6UyJS-YC1TeSWDqpZIP37QrRrzUg.lew0rGFAKpayjvshZ4MMtLidtMuHPFt6NuEC6vz5Voog.JPEG.tototorlck%2F20230520%25A3%25DF120832.jpg&type=sc960_832",
        "tags": ["액티비티", "자연 탐험", "자연", "도전적인 활동", "힐링", "사진 명소", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "안성팜랜드",
        "description": "안성팜랜드는 농업과 자연을 체험할 수 있는 공간으로, 가족 단위 방문객에게 인기가 많습니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEwMTFfMjgx%2FMDAxNzI4NjA2OTkxMjQ4.vJfbYsc0tdBzXZKaVUblkasPjcs4Z_2TB6MAuj9tTFog.mSrIiZEqm40TpdV00fC4kAMkYUQEzOaLrKiaHpnQIKIg.JPEG%2F%25BE%25C8%25BC%25BA%25C6%25CA%25B7%25A3%25B5%25E5%25C7%25CE%25C5%25A9%25B9%25C4%25B8%25AE_19.jpg&type=sc960_832",
        "tags": ["액티비티", "문화/역사 탐방", "자연", "문화/역사 체험", "사진 명소", "힐링", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "포천 허브아일랜드",
        "description": "허브아일랜드는 다양한 허브와 식물을 체험할 수 있는 공간으로, 힐링을 제공합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEwMjBfMjQ0%2FMDAxNjk3NzU0MTU1NDA3.L9G4pFLgwD9Kbb9nToi12JdU5R2UYENX3c0CszIFGHwg.Dzd9uHcj4lTHc_pqLbb5jghUjNi7HIAY-ETpzNtWsd8g.JPEG.maum0577%2F4.jpg&type=sc960_832",
        "tags": ["자연 탐험", "자연", "힐링", "새로운 음식 시도", "사진 명소", "독특한 장소", "저렴한 가격", "안전하고 편안한 환경"]
    },
    {
        "name": "연천 재인폭포 공원",
        "description": "재인폭포 공원은 아름다운 폭포와 자연경관을 제공하는 관광지로, 힐링을 제공합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDEwMTFfMjU0%2FMDAxNzI4NjI0NTY2NzEw.1a98yvC8jSDVfFv-aGqcYvMusv5EJt1cb_3lLH0NGiUg.JLNNxqjG_89doOyCleoXU0Ti-todHD5YB4BNXjNLctog.JPEG%2F20240528_132303_HDR.jpg&type=sc960_832",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "사진 명소", "독특한 장소", "저렴한 가격"]
    },
    {
        "name": "가평 자라섬",
        "description": "자라섬은 아름다운 자연경관과 다양한 레저 활동을 즐길 수 있는 장소입니다.",
        "image_url": "https://search.pstatic.net/sunny/?src=http%3A%2F%2Fwww.dicalove.com%2Ffiles%2Fattach%2Fimages%2F154%2F317%2F466%2F025%2Fcb9d9632331b0e0ddf528c3922d23083.jpg&type=sc960_832",
        "tags": ["자연 탐험", "액티비티", "자연", "힐링", "도전적인 활동", "사진 명소", "독특한 장소", "저렴한 가격"]
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

# Streamlit 앱 레이아웃 설정
st.title("여행 스타일 기반 관광지 추천 챗봇")

user_answers = []  # 사용자의 답변을 저장

# 각 질문에 대해 선택할 수 있도록 UI를 구성
for i, q in enumerate(questions_options):
    answer = st.selectbox(q["question"], options=q["options"], key=f"question_{i}")
    user_answers.append(answer)

# 추천 버튼
if st.button("추천받기"):
    # 사용자의 여행 스타일에 해당하는 우선순위 태그들
    priority_tags = ["문화/역사 탐방", "자연 탐험", "쇼핑", "액티비티", 
                     "문학적 활동", "음악 활동", "무용 활동", "미술 활동", 
                     "도심", "자연", "유적지"]
    
    # 각 관광지의 일치하는 태그 개수를 저장
    matching_scores = []
    
    for destination in destinations:
        # 일치하는 태그 수 계산
        score = sum(tag in destination["tags"] for tag in user_answers)
        matching_scores.append((destination, score))
    
    # 일치 태그 개수가 높은 순으로 정렬하고 상위 네 개 선택
    matching_scores.sort(key=lambda x: x[1], reverse=True)
    top_destinations = [destination for destination, score in matching_scores[:4]]

    # 사용자가 선택한 태그 중 우선순위 태그와 일치하는 관광지 필터링
    priority_destinations = [
        destination for destination in top_destinations
        if any(tag in priority_tags and tag in destination["tags"] for tag in user_answers)
    ]
    
    # 우선순위 태그와 일치하는 관광지가 두 개 이상이면 무작위 두 개 선택
    if len(priority_destinations) >= 2:
        recommended_destinations = random.sample(priority_destinations, 2)
    elif len(priority_destinations) == 1:
        # 하나만 있으면 그 하나를 추천
        recommended_destinations = priority_destinations
    else:
        # 우선순위 태그와 일치하는 관광지가 없을 경우 상위 네 개 중 무작위 두 개 선택
        recommended_destinations = random.sample(top_destinations, 2)

    # 추천 결과 표시
    for place in recommended_destinations:
        st.subheader(place["name"])
        st.write(place["description"])
        st.image(place["image_url"], use_column_width=True)
