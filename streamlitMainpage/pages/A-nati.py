import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
from PIL import Image
st.subheader('项目名称 xxx项目')
st.subheader('项目描述')
st.text('该项目是xxxxx')
st.subheader('项目展示')
#st.subheader('点击链接跳转至yolov5的目标检测展示-streamlit cloud')
#link = '[Visit yolov5的目标检测](https://133dzs-dongzheming-2023-main-hixde5.streamlit.app/)'
#st.markdown(link, unsafe_allow_html=True)

st.subheader('点击链接跳转至MoNUSeg -本地docker')
link = '[Visit Instance nuclei segmentation](http://121.48.165.52:8510)'
st.markdown(link, unsafe_allow_html=True)


st.subheader('联系方式')
st.text('github: ')
st.text('email: ')
