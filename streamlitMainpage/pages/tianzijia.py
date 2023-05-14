import streamlit as st
import webbrowser 
st.markdown("# yolov3预测结果展示 ❄️")
st.sidebar.markdown("# yolov3预测结果展示 ❄️")


st.title('点击链接跳转至yolov3预测结果展示')

link = '[Visit yolov3预测结果展示](https://tyrozj-zijiatian-2025-predict-test-fzm2z2.streamlit.app/)'
st.markdown(link, unsafe_allow_html=True)