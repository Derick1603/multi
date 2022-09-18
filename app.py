import streamlit as st

st.set_page_config(
	page_title="Main Menu",
	page_icon="✌",

)
st.title("Main Page")
st.sidebar.success("Select a page above.")
url = "https://derick1603-stockss-app-8b7qas.streamlitapp.com/"
st.write("[For Prediction](%s)" % url)
st.write('---')
st.info('Investing in the stock market is one of the most complicated and sophisticated ways to conduct business. The stock market is very uncertain since stock values fluctuate due to a variety of factors, making stock prediction a difficult and exceedingly hard task. Investors nowadays require rapid and reliable information to make efficient judgments, with rapidly expanding technology breakthroughs in stock price prediction. This has attracted their interest in the research area. Understanding the pattern of stock price of a particular company and predicting their future development and financial growth will be highly beneficial. This paper focuses on the usage of a type of RNN(recurrent neural network) based Machine learning which is known as Long Short-Term Memory (LSTM) to predict stock values')
