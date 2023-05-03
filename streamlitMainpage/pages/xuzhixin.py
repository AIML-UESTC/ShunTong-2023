import streamlit as st
import webbrowser 
st.markdown("# 视差估计的streamlit示例 ❄️")
st.sidebar.markdown("# 视差估计的streamlit示例 ❄️")


st.title('点击链接跳转至视差估计的streamlit示例')
link = '(https://qq552082016-zhixinxu-2025-cvstreamlitshow-y8xvzn.streamlit.app/)'
if st.button(link):
    webbrowser.open_new_tab('https://qq552082016-zhixinxu-2025-cvstreamlitshow-y8xvzn.streamlit.app/')
