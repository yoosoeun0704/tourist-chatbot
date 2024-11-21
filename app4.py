import streamlit as st

# 앱 제목
st.title("범죄 예방 팁 제공")

# 범죄 발생 위험 시간대 버튼
time_input = st.text_input("이동하는 시간대가 어떻게 되나요? (예: 21:30)", key="time_input")

if st.button("범죄 발생 위험 시간대"):
    if time_input:
        try:
            # 입력된 시간을 시각으로 변환
            hour, minute = map(int, time_input.split(':'))
            time_in_minutes = hour * 60 + minute
            
            # 시간대에 따른 메시지 제공
            if 21 * 60 <= time_in_minutes <= 23 * 60 + 59:
                st.write("가장 위험한 시간대이니 조심하세요!")
            elif 18 * 60 <= time_in_minutes <= 20 * 60 + 59 or 0 <= time_in_minutes <= 2 * 60 + 59:
                st.write("위험한 시간대이니 조심하세요!")
            else:
                st.write("비교적으로 마음을 놓으셔도 됩니다! 하지만 방심은 금물이에요!!")
        except ValueError:
            st.write("올바른 시간 형식으로 입력해주세요 (예: HH:MM)")
    else:
        st.write("시간대를 입력해주세요.")

# 범죄 발생 위험 날씨 버튼
weather_input = st.text_input("이동할 날의 일기는 어떤가요? (어두움/흐림/맑음/비/눈)", key="weather_input")

if st.button("범죄 발생 위험 날씨"):
    if weather_input:
        weather_input = weather_input.strip()  # 공백 제거
        # 날씨에 따른 메시지 제공
        if weather_input == "어두움":
            st.write("조심하세요! 가장 위험한 일기입니다!")
        elif weather_input == "흐림":
            st.write("조심하세요! 위험한 일기입니다!")
        elif weather_input == "맑음":
            st.write("일상적으로 범죄가 자주 일어나는 일기입니다.")
        elif weather_input in ["비", "눈"]:
            st.write("상대적으로 범죄가 적게 일어난다고 마음을 놓아서는 안됩니다!")
        else:
            st.write("올바른 날씨 정보를 입력해주세요 (어두움/흐림/맑음/비/눈)")
    else:
        st.write("날씨 정보를 입력해주세요.")

# 범죄 예방 팁 받기 버튼
if st.button("범죄 예방 팁 받기"):
    st.write("### 2. 가정에서의 범죄 예방")
    st.write("문과 창문 잠금 확인: 집을 나설 때와 잘 때 문과 창문의 잠금을 항상 확인하세요. 보조 잠금장치를 설치하면 추가적인 보안을 제공할 수 있습니다.")
    st.write("CCTV나 비디오 도어벨 설치: 집 외부에 CCTV를 설치하거나, 누군가 초인종을 눌렀을 때 확인할 수 있는 스마트 비디오 도어벨을 사용하는 것도 좋습니다.")
    st.write("이웃과 소통: 이웃과 친분을 유지하면 긴급 상황에서 서로 도움을 주고받을 수 있습니다.")
    
    st.write("### 3. 길거리 및 공공장소에서의 안전")
    st.write("밝은 곳으로 다니기: 가로등이 잘 설치된 길을 이용하고, 어두운 골목길은 피하세요.")
    st.write("차량 진입 위치 주의: 택시나 대중교통을 이용할 때는 운전자와 차량 번호를 확인하세요. 택시 앱을 이용하면 더욱 안전합니다.")
    st.write("혼자 걸을 때 경계 유지: 뒤에서 따라오는 사람이 있거나, 낯선 사람이 다가오는 경우 거리를 유지하거나 도움을 요청하세요.")
    
    st.write("### 4. 온라인 및 디지털 보안")
    st.write("알 수 없는 링크 클릭 금지: 이메일, 문자 메시지 등에서 출처가 불분명한 링크를 클릭하지 마세요.")
    st.write("SNS에 위치 정보 게시 제한: 실시간으로 자신의 위치나 일정을 공유하지 않는 것이 안전합니다.")
    st.write("안전한 쇼핑 사이트 이용: 신뢰할 수 있는 사이트에서만 거래를 진행하고, 개인 정보를 공유하기 전 반드시 확인하세요.")
    
    st.write("### 5. 차량 및 교통 관련")
    st.write("차량 내부 점검: 차를 타기 전에 뒷좌석이나 트렁크 내부를 확인하세요.")
    st.write("귀중품 노출 금지: 차량 내 귀중품을 보이는 곳에 두지 않도록 합니다.")
    st.write("긴급 키트 준비: 차량에 비상용 키트(손전등, 배터리, 호신용 스프레이 등)를 준비하세요.")
    
    st.write("### 6. 호신 및 자기방어")
    st.write("호신용품 활용: 호신용 스프레이, 알람 장치 등을 소지하세요.")
    st.write("비상 연락처 저장: 휴대폰에 신속하게 연락할 수 있는 비상 연락처를 저장합니다.")
    st.write("위급 상황 시 소리 지르기: 주변의 도움을 얻기 위해 크고 명확한 목소리로 도움을 요청하세요.")

# 범죄 예방 안내 사이트 접속하기 버튼
if st.button("범죄 예방 안내 사이트 접속하기"):
    st.write("[법무부 범죄예방정책국](https://www.cppb.go.kr)")
    st.write("[경찰청 범죄예방 안전 서비스](https://www.police.go.kr)")
    st.write("[여성가족부 디지털 성범죄 예방](https://www.mogef.go.kr)")
