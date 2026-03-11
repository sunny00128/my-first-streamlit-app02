import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="金融投資模擬器", page_icon="💰")

st.title("💰 金融投資組合回報模擬器")
st.write("輸入股票代號（多檔請用逗號隔開），查看過去一年的累積收益率！")

# 1. 使用者輸入區
col1, col2 = st.columns([3, 1])
with col1:
    # 預設提供幾檔熱門標的：台積電(2330.TW)、標普500(SPY)、輝達(NVDA)
    tickers_input = st.text_input("請輸入股票代號 (Yahoo Finance 格式):", value="2330.TW, SPY, NVDA")
with col2:
    period = st.selectbox("時間區間", ["6mo", "1y", "2y", "5y"], index=1)

# 處理輸入的字串
ticker_list = [t.strip().upper() for t in tickers_input.split(",")]

# 2. 抓取與計算數據
if st.button("開始分析"):
    try:
        with st.spinner('正在分析市場數據...'):
            # 抓取收盤價
            data = yf.download(ticker_list, period=period)['Close']
            
            # 計算累積收益率： (今日價格 / 起始價格) - 1
            # 這樣可以讓不同價格等級的股票在同一基準點比較
            returns_df = (data / data.iloc[0] - 1) * 100

            # 3. 視覺化展示
            st.subheader(f"📊 累積收益率比較 (%) - {period}")
            st.line_chart(returns_df)

            # 顯示各標的最終表現
            st.write("### 最終累積回報率明細：")
            latest_returns = returns_df.iloc[-1]
            
            # 用欄位方式顯示績效
            cols = st.columns(len(latest_returns))
            for i, (ticker, val) in enumerate(latest_returns.items()):
                cols[i].metric(ticker, f"{val:.2f}%")

    except Exception as e:
        st.error(f"發生錯誤，請檢查代號是否正確。錯誤訊息: {e}")

st.divider()
st.info("💡 小提醒：台股請加 .TW (如 2330.TW)，美股直接輸入代號 (如 AAPL)。")
