import streamlit as st
import webbrowser 
st.markdown("# yolov3预测结果展示 ❄️")
st.sidebar.markdown("# yolov3预测结果展示 ❄️")


st.title('点击链接跳转至yolov3预测结果展示')
link = '(https://tyrozj-zijiatian-2025-predict-test-fzm2z2.streamlit.app/)'
if st.button(link):
    webbrowser.open_new_tab('https://tyrozj-zijiatian-2025-predict-test-fzm2z2.streamlit.app/')
