import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
from PIL import Image
st.title('项目名称 xxx项目')
st.title('项目描述')
st.text('该项目是xxxxx')
st.title('项目展示')
st.subheader('点击链接跳转至细胞核分割结果展示')

link = '[Visit 细胞核分割](https://binbin-2593-medical-image-nuclear-segmentatio-srcdisplay-cnn9qf.streamlit.app)'
st.markdown(link, unsafe_allow_html=True)



st.title('联系方式')
st.text('github: ')
st.text('email: ')
