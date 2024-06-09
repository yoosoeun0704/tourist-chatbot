import streamlit as st
import random

# GPT 모델 정의
def generate_response(prompt):
    responses = {
        "안성의 관광명소를 추천해줘": ["팜랜드", "남사당놀이마을", "안성맞춤랜드"],
        "팜랜드": {
            "description": "안성 팜랜드는 다양한 동물과 자연을 즐길 수 있는 테마파크입니다.",
            "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEwMTlfMTE4%2FMDAxNjk3NjQxMjg1NTM3.Fcjp-dKWWdrHRazvq9dfXJPcsN-JRnHN8coGpcsuJxog.FWfzF-789oEEQXTB9IPpvZ682J4IqfP2wjDuAbAfzeog.JPEG.otter86%2F1697641262847.jpg"
        },
        "남사당놀이마을": {
            "description": "안성 남사당놀이마을은 한국 전통 공연과 문화를 체험할 수 있는 곳입니다.",
            "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140707_222%2Fhjne121_1404712263020yeWwV_PNG%2F11.png"
        },
        "안성맞춤랜드": {
            "description": "안성맞춤랜드는 가족과 함께 즐길 수 있는 놀이 시설과 자연 경관을 제공합니다.",
            "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzA1MjJfMjEx%2FMDAxNDk1NDI1NDE3NDQx.0GN2nJlWyUjjQyiVNc2Ie7kUMHqMu7P1Sw69D5iSdzgg.Jpw9sLfl77Z-Mu8UkNzL8OvbxfVYPyS-64QnlNb7gwog.JPEG.wendellgee%2FDSC_5996.jpg"
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
        # 이미지 URL 가져오기
        image_url = response["image_url"]
        # 이미지 표시
        st.image(image_url, caption=user_input)
        st.write(f"**{user_input}**: {response['description']}")
    else:
        st.write(response)
