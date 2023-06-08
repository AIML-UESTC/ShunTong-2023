import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
import os
from PIL import Image
pathpwd = os.getcwd()
#path=os.path.join(pathpwd,"pages/resources/moon.jpg")

st.title('streamlit项目开发运维(DevOps)')
st.markdown('前置背景: streamlit docker python shell 等')
st.markdown('在自己的深度学习项目完成之后将涉及到使用streamlit开发界面进行展示')
st.markdown('#### streamlit开发')
code='''streamlit有热更新机制,使用streamlit进行开发时
#建议在121.48.165.52服务器上使用conda 创建虚拟环境
#-n后是指定的虚拟环境名称, python=3.8是指定python版本
conda create -n hyx python=3.8
#随后查看conda虚拟环境
conda env list 
#类似输出如下
#
base                  *  /home/cq/miniconda3
centernet                /home/cq/miniconda3/envs/centernet
hyx                      /home/cq/miniconda3/envs/hyx
nnunet-pytorch           /home/cq/miniconda3/envs/nnunet-pytorch
webrtc                   /home/cq/miniconda3/envs/webrtc
#随后切入到刚刚创建的虚拟环境
conda activate hyx
#命令行将从(base)xxxx变成(hyx)xxxxx
#随后在该虚拟环境下安装依赖
#并启动你的streamlit项目
streamlit run xxx.py
#这时已经可以在浏览器上面看到streamlit页面
#在你修改项目后,浏览器页面重新点击即可看到修改
'''
st.code(code, language='shell')


st.subheader('stremalit运行和维护')
st.markdown('使用虚拟环境和streamlit run 命令成功运行后,参考T-dockerdeployment进行docker部署和使用')
code = '''#docker images启动容器shell脚本
#这里的脚本就是将之前的docker启动进行命令集中和整合
#!/bin/bash
nohup docker run -p 8501:8501 dzmyolov5-ascend8501 > logs/dzmyolov5-ascend8501.out 2>&1 &
nohup docker run -p 8502:8502 webrtc8502 > logs/webrtc8502.out 2>&1 &
nohup docker run -p 8503:8503 streamlitmainpage8503 > logs/streamlitmainpage8503.out 2>&1 &
nohup docker run -p 8505:8505 wfccellseg8505 > logs/wfccellseg8505.out 2>&1 & 
nohup docker run -p 8504:8504 hyx8504 > logs/hyx8504.out 2>&1 &
'''
st.code(code, language='shell')

code = '''#docker images停止容器shell脚本
#这里的脚本就是通过这docker ps命令查找到运行在850x端口的容器 并进行docker stop操作
#!/bin/bash
docker ps | grep 850 | awk '{print $1}' | xargs docker stop
'''
st.code(code, language='shell')
st.text('')
st.subheader('目前项目使用端口管理')
code = '''
姓名    docker内容      docker镜像名            端口
董哲明	yolo5         dzmyolov5-ascend8501    8501
童顺	webrtc        webrtc8502              8502
童顺	实验室主页      streamlitmainpage8503   8503
黄沿鑫	病灶           hyx8504                 8504
王富臣	细胞核分割      wfccellseg8505          8505
王晶    kmeans聚类     wj8506                 8506

已经开放端口:8501 8502 8503 8504 8505 8506 8507 8508 8509 8510
后续需要新增端口则需要连接老师办公室wifi,输入192.168.1.100
user:admin password:admin进入转发规则界面进行新增。
'''
st.code(code,language='text')

