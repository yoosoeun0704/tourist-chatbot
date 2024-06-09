import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random

# 모델과 토크나이저 로드
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 관광 명소 정보
tourist_spots = {
    "팜랜드": {
        "description": "안성 팜랜드는 다양한 동물과 자연을 즐길 수 있는 테마파크입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEwMTlfMTE4%2FMDAxNjk3NjQxMjg1NTM3.Fcjp-dKWWdrHRazvq9dfXJPcsN-JRnHN8coGpcsuJxog.FWfzF-789oEEQXTB9IPpvZ682J4IqfP2wjDuAbAfzeog.JPEG.otter86%2F1697641262847.jpg"
    },
    "남사당놀이마을": {
        "description": "안성 남사당놀이마을은 한국 전통 공연과 문화를 체험할 수 있는 곳입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140930_238%2Funique_space_1412004099043pC1li_PNG%2F%25BD%25BA%25C5%25A9%25B8%25B0%25BC%25A6_2014-09-30_%25BF%25C0%25C0%25FC_12.21.24.png&type=sc960_832"
    },
    "안성맞춤랜드": {
        "description": "안성맞춤랜드는 가족과 함께 즐길 수 있는 놀이 시설과 자연 경관을 제공합니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzA1MjJfMjEx%2FMDAxNDk1NDI1NDE3NDQx.0GN2nJlWyUjjQyiVNc2Ie7kUMHqMu7P1Sw69D5iSdzgg.Jpw9sLfl77Z-Mu8UkNzL8OvbxfVYPyS-64QnlNb7gwog.JPEG.wendellgee%2FDSC_5996.jpg"
    },
    "서운산": {
        "description": "서운산은 아름다운 경관과 등산로로 유명한 산입니다.",
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjEwMzFfNjMg%2FMDAxNjY3MTk4NzQ3MDc5.JtEA_IPJY7cHXQbwVyGlU4lO41RJLlFWUafeTjpqm5Mg.V668ub27T0rSkM3N2PwdeEroWTMfZhR9T_lICCxcKhkg.JPEG.gjtndkql70%2FDSC06824.JPG&type=sc960_832"
    },
}

def generate_response(prompt, model, tokenizer, max_length=50):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def chatbot_response(user_input):
    if "안성의 관광명소를 추천해줘" in user_input:
        recommendations = list(tourist_spots.keys())[:3]
        random_recommendation = random.choice(list(tourist_spots.keys()))
        return recommendations, random_recommendation
    for spot in tourist_spots.keys():
        if spot in user_input:
            return [spot], None
    return generate_response(user_input, model, tokenizer), None

# Streamlit UI
st.title("안성 관광명소 챗봇")
user_input = st.text_input("안성의 관광명소에 대해 물어보세요!")
if st.button("대답하기"):
    response, random_recommendation = chatbot_response(user_input)
    if isinstance(response, list):
        for spot in response:
            info = tourist_spots.get(spot)
            if info:
                st.image(info['image_url'], caption=spot)
                st.write(f"**{spot}**: {info['description']}")
        if random_recommendation:
            st.write("이 곳을 추천해드립니다:")
            info = tourist_spots.get(random_recommendation)
            if info:
                st.image(info['image_url'], caption=random_recommendation)
                st.write(f"**{random_recommendation}**: {info['description']}")
    else:
        st.write(response)
