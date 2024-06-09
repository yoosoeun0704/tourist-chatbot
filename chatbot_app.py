import streamlit as st
import random

# 관광 명소 정보
tourist_spots = {
    "팜랜드": {
        "description": "안성 팜랜드는 다양한 동물과 자연을 즐길 수 있는 테마파크입니다.",
        "image_url": "https://example.com/images/farm_land.jpg"  # 실제 이미지 URL로 교체
    },
    "남사당놀이마을": {
        "description": "안성 남사당놀이마을은 한국 전통 공연과 문화를 체험할 수 있는 곳입니다.",
        "image_url": "https://example.com/images/namsadang.jpg"  # 실제 이미지 URL로 교체
    },
    "안성맞춤랜드": {
        "description": "안성맞춤랜드는 가족과 함께 즐길 수 있는 놀이 시설과 자연 경관을 제공합니다.",
        "image_url": "https://example.com/images/ansung_land.jpg"  # 실제 이미지 URL로 교체
    },
    "서운산": {
        "description": "서운산은 아름다운 경관과 등산로로 유명한 산입니다.",
        "image_url": "https://example.com/images/seo_onsan.jpg"  # 실제 이미지 URL로 교체
    },
    "안성천생태공원": {
        "description": "안성천생태공원은 자연 생태계를 체험할 수 있는 공원입니다.",
        "image_url": "https://example.com/images/ansung_eco_park.jpg"  # 실제 이미지 URL로 교체
    }
}

# GPT 모델 정의
def generate_response(prompt):
    responses = {
        "안성의 관광명소를 추천해줘": ["팜랜드", "남사당놀이마을", "안성맞춤랜드", "서운산", "안성천생태공원"],
        "팜랜드": {
            "description": "안성 팜랜드는 다양한 동물과 자연을 즐길 수 있는 테마파크입니다.",
            "image_url": "https://example.com/images/farm_land.jpg"  # 실제 이미지 URL로 교체
        },
        "남사당놀이마을": {
            "description": "안성 남사당놀이마을은 한국 전통 공연과 문화를 체험할 수 있는 곳입니다.",
            "image_url": "https://example.com/images/namsadang.jpg"  # 실제 이미지 URL로 교체
        },
        "안성맞춤랜드": {
            "description": "안성맞춤랜드는 가족과 함께 즐길 수 있는 놀이 시설과 자연 경관을 제공합니다.",
            "image_url": "https://example.com/images/ansung_land.jpg"  # 실제 이미지 URL로 교체
        }
        
    }
    if prompt in responses:
        if isinstance(responses[prompt], list):
            return random.choice(responses[prompt])
        else:
            return responses[prompt]
    else:
        return "제가 알고 있는 안성의 관광명소가 아닌 것 같아요."

# Streamlit UI
st.title("안성 관광명소 챗봇")
user_input = st.text_input("안성의 관광명소에 대해 물어보세요!")
if st.button("대답하기"):
    response = generate_response(user_input)
    if isinstance(response, dict):
        for spot, info in tourist_spots.items():
            if spot == response["description"]:
                st.image(info['image_url'], caption=spot)
                st.write(f"**{spot}**: {response['description']}")
    else:
        st.write(response)

# 반복적으로 스트림릿을 실행해도 닫히지 않도록 하는 코드
# 방법 1: 스레드를 사용하는 방식
import threading
def streamlit_run():
    st.button("Stop Streamlit")
streamlit_thread = threading.Thread(target=streamlit_run)
streamlit_thread.start()

# 방법 2: Tornado를 사용하는 방식
# 방법 2: Tornado를 사용하는 방식
from tornado import web, httpserver, ioloop

class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Streamlit running!")

app = web.Application([(r"/", MainHandler)])
http_server = httpserver.HTTPServer(app)
http_server.listen(8502)  # 포트를 8502로 변경
ioloop.IOLoop.current().start()
