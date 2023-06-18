import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
import os
from PIL import Image
pathpwd = os.getcwd()
#path=os.path.join(pathpwd,"pages/resources/moon.jpg")

st.title('streamlit实验室主页开发运维(DevOps)')
st.markdown('前置背景: streamlit docker python shell 等')
st.markdown('在自己的深度学习项目完成之后将涉及到使用streamlit开发界面进行展示')
st.markdown('#### 实验室主页及相关项目地址')
link = '[streamlit TongShun主页](https://github.com/AIML-UESTC/ShunTong-2023.git)'
st.markdown('https://github.com/AIML-UESTC/ShunTong-2023.git')
st.markdown(link, unsafe_allow_html=True)
st.markdown('#### git安装')
code='''
#本机安装git:
在linux (ubuntu)服务器上:
可以先查看是否已经安装:
git --help
如果出现以下输出,则证明已经安装
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]...
如果没有出现则使用 
sudo apt-get install git
进行安装
window系统中,可以下载客户端
https://git-scm.com/download/win
安装步骤使用默认设置即可,一般下载安装windows64位
安装后空白处单击鼠标右键,会出现git bash here, git GUI here此类选项
'''
st.code(code, language='shell')

st.markdown('#### git克隆到本地及仓库内项目介绍')
code='''
#项目克隆到本地
git clone https://github.com/AIML-UESTC/ShunTong-2023.git
#仓库内项目介绍
--------------------------------------------------------------------
dockerimagescript:此为已经打包完成的镜像的启动脚本,
采用的是后台启动并重定向日志文件到logs文件夹下
--------------------------------------------------------------------

--------------------------------------------------------------------
dockerstreamlit:此为收集的各个同学的dockerfile文件
--------------------------------------------------------------------

--------------------------------------------------------------------
powerpoint:此为之前讲过的云服务器购买部署streamlit项目教程
--------------------------------------------------------------------

--------------------------------------------------------------------
streamlitMainpage:此为实验室主页代码项目,分为教程和各个同学
标签页,每个同学的页面都放在pages里面,网页上面的标签页名称就
是每个python文件的名称
streamlitMainpage --项目目录
├── Dockerfile    --本项目docker打包的dockerfile
├── generateDocker.sh --生成docker镜像的脚本
├── main_page.py  --运行的实际主界面
├── pages         --各个标签页存放的地址
│   ├── A-caotong.py    --每个标签页,标签页名称与文件名相同
│   ├── A-dongzheming.py
│   ├── A-huangyanxin.py
│   ├── A-tianzijia.py
│   ├── A-wangfuchen.py
│   ├── A-wangjing.py
│   ├── A-xuzhixin.py
│   ├── resources  --在标签页中用到的资源存放目录,注意使用相对路径
│   │   ├── ice验证页面.png
│   │   ├── moon.jpg
│   │   ├── star.mp4
│   │   ├── testmusic.mp3
│   │   ├── 浏览器设置.png
│   │   └── 阿里云界面.png
│   ├── T-DevOps.py
│   ├── T-dockerdeployment.py
│   ├── T-template.py
│   └── T-webrtcICEtutorial.py
└── requirements.txt --部署本项目需要用到的依赖项
--------------------------------------------------------------------

'''
st.code(code,language='shell')

st.markdown('#### streamlit服务器本地开发')
st.markdown('#### 实验室主页开发运维必看🎈')
code='''
在本地拉取下来仓库代码以后以后,进入streamlitMainpage项目
也可以将代码放置到服务器上,本地使用vscode pycharm等ide通过ssh口令登录服务器,
代码调试完成后将代码提交到github

提交步骤:
#查看目前文件状态,可以看到哪些是未被追踪或者已有文件但被更新
git status
#添加改动,无特别需要,将git status里面未被追踪或者已有的修改文件直接全部添加
git add .
#添加本次的提交的内容说明,"" 双引号内就是其内容
git commit -m "update main page, add new xxx tab"
#最后提交到github
git push origin main
#注意如果提交之后显示权限问题或者使用邮箱用户名和密码登陆后显示不能提交,
是因为github已经不支持使用用户名和密码验证了,正确方式是使用ssh公钥和私钥,
本地创建好公钥和私钥,将公钥复制到github的设置页,参考
https://blog.csdn.net/weixin_42310154/article/details/118340458

#注意事项
因为streamlit有热更新机制,使用streamlit进行开发时
建议在121.48.165.52服务器上使用conda 创建虚拟环境
说明-n后是指定的虚拟环境名称, python=3.8是指定python版本
如果已有环境,则直接激活即可,如果要创建新的虚拟环境,
则需要将-n后面的名称换成自己想要的名称,并且python换成自己想要的版本
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
#在你修改项目后,浏览器页面重新点击即可看到修改而无需停止并重新运行项目
'''
st.code(code, language='shell')


st.subheader('streamlit运行和维护')
st.markdown('使用虚拟环境和streamlit run 命令成功运行后,参考T-dockerdeployment进行docker部署和使用')
code = '''
#docker images启动容器shell脚本
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
王晶    kmeans聚类      wj8506                  8506
童顺    标准项目架构     standarddemo8507        8507
马博俊  雷达识别         mbj8508                 8508

已经开放端口:8501 8502 8503 8504 8505 8506 8507 8508 8509 8510
后续需要新增端口则需要连接老师办公室wifi 192.168.1.100 输入账号密码后进入转发规则界面进行新增。
'''
st.code(code,language='text')

