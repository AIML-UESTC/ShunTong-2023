import streamlit as st
import webbrowser 
st.markdown("# ViT demo ❄️")
st.sidebar.markdown("# ViT demo ❄️")


st.title('点击链接跳转至ViT demo')
link = '(https://tong-cao-visontransformer-streamlit-show-2wq9qt.streamlit.app/)'
if st.button(link):
    webbrowser.open_new_tab('https://tong-cao-visontransformer-streamlit-show-2wq9qt.streamlit.app/')
