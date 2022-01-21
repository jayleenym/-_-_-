import streamlit as st

def page():
    global next
    st.title("✍🏻리뷰의 재발견")
    # st.subheader("안녕하세요, 🧠무뇌형 인간🧠입니다")
    st.markdown("""
    #### 팀원 소개
문예진 | 이상민 | 정수연 | 정승연 | 황의린


#### Review? Re-View!""")
    c1, c2 = st.columns([1, 5])
    with c1: pass
    with c2: st.image("../images/home1.png", caption = '출처: 올리브영', width = 500)
    st.markdown("""
###### 물건 살 때 여러분이 보는 그 리뷰의 **⭐️유용성⭐️**, 저희가 알려드립니다! 

📌 리뷰 유용성 판단부터   
📌 토픽으로 알아보는 리뷰 유용성 결정 요인 분석  
📌 군집화를 통한 대표 리뷰 추출까지

*우리 같이 Review를 Re-View해봐요♥️*
 """)
    _, c2 = st.columns([16, 1])
    with c2: next = st.button('Next')