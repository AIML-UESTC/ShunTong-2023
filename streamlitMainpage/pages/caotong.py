import streamlit as st
import webbrowser 
st.markdown("# ViT demo ❄️")
st.sidebar.markdown("# ViT demo ❄️")


st.title('点击链接跳转至ViT demo')

link = '[Visit ViT demo](https://tong-cao-visontransformer-streamlit-show-2wq9qt.streamlit.app/)'
st.markdown(link, unsafe_allow_html=True)
