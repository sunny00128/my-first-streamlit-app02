import streamlit as st

st.set_page_config(page_title="BMI 健康計算機", page_icon="⚖️")

st.title("⚖️ BMI 健康計算機")
st.write("輸入你的身高與體重，看看你的健康狀況！")

# 建立側邊欄輸入
with st.sidebar:
    st.header("個人參數")
    weight = st.number_input("體重 (公斤)", min_value=1.0, max_value=200.0, value=65.0)
    height = st.number_input("身高 (公分)", min_value=50.0, max_value=250.0, value=170.0)

# 計算 BMI
if st.button("開始計算"):
    bmi = weight / ((height / 100) ** 2)
    st.subheader(f"你的 BMI 指數為: {bmi:.2f}")

    # 判斷等級
    if bmi < 18.5:
        st.warning("體重過輕：建議多補充營養，並進行適度重訓。")
    elif 18.5 <= bmi < 24:
        st.success("正常範圍：太棒了！請繼續保持均衡飲食與運動。")
    elif 24 <= bmi < 27:
        st.info("過重：要注意飲食內容，減少加工食品攝取喔。")
    else:
        st.error("肥胖：建議諮詢專業營養師或醫師協助調整生活習慣。")

st.divider()
st.caption("本工具僅供參考，詳細健康資訊請洽詢專業人士。")
