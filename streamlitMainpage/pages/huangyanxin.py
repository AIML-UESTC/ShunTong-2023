import streamlit as st
import webbrowser 
st.markdown("# 脑干胶质瘤的分割结果 ❄️")
st.sidebar.markdown("# 脑干胶质瘤的分割结果 ❄️")


st.title('点击链接跳转至脑干胶质瘤的分割结果')
link = '(https://huangyanxin-china-yanxinhuang-2025-new-by-me-0ykv6r.streamlit.app/)'
if st.button(link):
    webbrowser.open_new_tab('https://huangyanxin-china-yanxinhuang-2025-new-by-me-0ykv6r.streamlit.app/')
