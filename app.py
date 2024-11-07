# app.py

from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# 1. 질문과 답변을 받는 부분
# 질문은 미리 정의하고, 사용자의 답변을 받을 리스트를 생성합니다.
questions = [
    "어떤 종류의 활동을 즐기시나요? (문화, 역사 탐방 / 자연 탐험/쇼핑/액티비티/예술)",
    "어떤 환경에서 여행을 즐기고 싶으신가요?(도심/자연/바다/유적지)",
    "여행 중 어떤 경험을 가장 중시하시나요? (사진 명소/문화 체험/힐링/도전적인 활동/새로운 음식 시도)",
    "여행 중 어떤 것을 가장 중요하게 생각하시나요? (좋은 접근성 / 독특한 장소/ 저렴한 가격/ 안전하고 편안한 환경)"
]

user_answers = []  # 사용자의 답변을 저장할 리스트

# 2. 관광지 데이터 정의
# 관광지 리스트는 각 항목에 대한 설명과 이미지 URL을 포함합니다.
destinations = [
    {
        "name": "경복궁",
        "description": "한국의 전통과 역사를 경험할 수 있는 서울의 대표 유적지입니다.",
        "image_url": "https://example.com/경복궁.jpg",
        "tags": ["문화", "역사 탐방", "도심", "유적지", "문화 체험"]
    },
    {
        "name": "제주도 성산 일출봉",
        "description": "아름다운 일출과 함께 자연을 만끽할 수 있는 제주의 인기 명소입니다.",
        "image_url": "https://example.com/성산일출봉.jpg",
        "tags": ["자연 탐험", "자연", "바다", "사진 명소", "힐링"]
    },
    {
        "name": "수원화성",
        "description": "한국의 전통과 역사를 경험할 수 있는 수원의 대표 유적지입니다.",
        "image_url": "https://sl.bing.net/VIE13OkuYe",
        "tags": ["문화", "역사 탐방", "도심", "유적지", "문화 체험"]
    }
]

# 3. 질문에 답변을 받는 API 엔드포인트
@app.route('/ask', methods=['GET'])
def ask_question():
    question_number = len(user_answers)  # 현재 답변 받은 질문 수를 기준으로 다음 질문 선택
    if question_number < len(questions):
        return jsonify({"question": questions[question_number]})
    else:
        return recommend_destinations()  # 답변이 모두 모이면 추천 결과로 이동

# 4. 사용자의 답변을 받는 API 엔드포인트
@app.route('/answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    answer = data.get("answer")
    user_answers.append(answer)  # 답변을 저장
    return ask_question()  # 다음 질문을 요청

# 5. 답변에 기반한 관광지 추천 로직
def recommend_destinations():
    # 사용자의 답변과 일치하는 관광지를 찾습니다.
    matched_destinations = [
        destination for destination in destinations
        if all(answer in destination["tags"] for answer in user_answers)
    ]
    
    # 조건에 맞는 관광지가 부족하면 랜덤하게 두 곳을 선택
    if len(matched_destinations) < 2:
        matched_destinations = random.sample(destinations, 2)
    
    # 추천 관광지 두 곳을 선택해 응답으로 반환
    recommendations = random.sample(matched_destinations, 2)
    return jsonify({
        "recommendations": [
            {
                "name": place["name"],
                "description": place["description"],
                "image_url": place["image_url"]
            } for place in recommendations
        ]
    })

# 6. 챗봇 초기화
@app.route('/reset', methods=['POST'])
def reset_chat():
    global user_answers
    user_answers = []  # 답변 리스트 초기화
    return jsonify({"message": "챗봇이 초기화되었습니다."})

if __name__ == "__main__":
    app.run(debug=True)
