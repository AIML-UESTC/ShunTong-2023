import streamlit as st
import webbrowser 
st.markdown("### 脑干胶质瘤的分割结果 ❄️")
#st.sidebar.markdown("# 脑干胶质瘤的分割结果 ❄️")


st.subheader('点击链接跳转至脑干胶质瘤的分割结果-streamlit cloud')

link = '[Visit 脑干胶质瘤的分割结果](https://tong-cao-visontransformer-streamlit-show-2wq9qt.streamlit.app/)'
st.markdown(link, unsafe_allow_html=True)

st.subheader('点击链接跳转至脑干胶质瘤的分割结果-本地服务器docker')
link = '[Visit 脑干胶质瘤的分割结果](http://121.48.165.52:8504)'
st.markdown(link, unsafe_allow_html=True)
