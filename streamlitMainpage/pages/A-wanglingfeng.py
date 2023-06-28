import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
from PIL import Image
st.subheader('项目名称 xxx项目')
st.subheader('项目描述')
st.text('该项目是xxxxx')
st.subheader('项目展示')

st.subheader('点击链接跳转至王凌锋项目展示-本地部署')
link = '[Visit 王凌锋项目展示](http://121.48.165.52:8511)'
st.markdown(link, unsafe_allow_html=True)

st.subheader('联系方式')
st.text('github: ')
st.text('email: ')
