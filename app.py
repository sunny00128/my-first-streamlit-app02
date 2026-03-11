import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="台積電股價分析", page_icon="📈")

st.title("📈 台積電 (2330.TW) 股價查詢系統")

# 設定股票代號
ticker = "2330.TW"

# 側邊欄設定時間範圍
with st.sidebar:
    st.header("查詢設定")
    period = st.selectbox("選擇時間範圍", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)

# 抓取數據
data = yf.Ticker(ticker)
df = data.history(period=period)

if not df.empty:
    # 顯示最新收盤價
    latest_price = df['Close'].iloc[-1]
    prev_price = df['Close'].iloc[-2]
    diff = latest_price - prev_price
    
    col1, col2 = st.columns(2)
    col1.metric("今日收盤價", f"{latest_price:.2f} TWD", f"{diff:.2f}")
    col2.metric("查詢區間", period)

    # 繪製折線圖
    st.subheader(f"歷史趨勢圖 ({period})")
    st.line_chart(df['Close'])

    # 顯示原始數據表格
    if st.checkbox("顯示數據明細"):
        st.write(df.tail(10))
else:
    st.error("無法取得數據，請稍後再試。")

st.caption("數據來源：Yahoo Finance")
