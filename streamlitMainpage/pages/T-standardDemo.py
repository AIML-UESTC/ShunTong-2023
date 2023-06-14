import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
import os
from PIL import Image
pathpwd = os.getcwd()
st.markdown('## 实验室标准项目架构组织')
st.markdown("#### 此页为实验室项目代码的组织形式，分为")
st.markdown("##### 1.深度学习训练/开发代码目录 - develop")
st.markdown("##### 2.模型保存目录 -models")
st.markdown("##### 3.streamlit页面代码目录 -webpage")
st.markdown("##### 4.打包成docker镜像dockerfile目录 -dockerimage")

st.text("")
st.markdown("#### 实际项目组织demo如下")

link = '[standardDemo-ShunTong](https://github.com/AIML-UESTC/ShunTong-2023/tree/main/standardDemo)'
st.markdown(link, unsafe_allow_html=True)

link = '[standardDemo展示页面](http://121.48.165.52:8507/)'
st.markdown(link, unsafe_allow_html=True)
st.text("实际就是将streamlit-webrtc-example-main里面第一个例子抽取出来")

code='''项目的树形结构如下
standardDemo --项目名称和主目录
   ├── builddockerimage.sh --打包docker镜像脚本,进入dockerimage目录,删除原镜像并打包同名新镜像
   ├── develop --深度学习训练/开发目录
   ├── dockerimage --打包成docker镜像目录
   |   ├── Dockerfile   --编写的dockerfile文件
   │   └── requirements.txt --导出的项目依赖文件
   ├── models  --存放模型的目录
   │   ├── MobileNetSSD_deploy.caffemodel
   │   └── MobileNetSSD_deploy.prototxt.txt
   └── webpage --存放streamlit页面的目录
       ├── app.py
       ├── home.py
       ├── pages --streamlit标签页存放
       │   └── 1_object_detection.py
       └── sample_utils --streamlit项目用到的工具代码等.这里使用了webrtc
           ├── download.py
           ├── __init__.py
           ├── __pycache__
           │   ├── download.cpython-38.pyc
           │   ├── __init__.cpython-38.pyc
           │   └── turn.cpython-38.pyc
           └── turn.py
'''
st.code(code, language='shell')
st.markdown("### 🎈后续项目组织请参考本节教程提供的demo进行")
st.markdown("### 🎈该demo打包docker镜像只需要运行builddockerimage.sh脚本就行")


