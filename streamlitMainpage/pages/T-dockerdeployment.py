import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
import os
from PIL import Image
pathpwd = os.getcwd()
#path=os.path.join(pathpwd,"pages/resources/moon.jpg")

st.title('docker打包项目及部署教程')
st.text('本标签页教程是使用docker进行项目打包和启动运行')
st.text('参考链接如下:')
link = '[Docker-从入门到实践gitbook](https://yeasy.gitbook.io/docker_practice/install/ubuntu)'
st.markdown(link, unsafe_allow_html=True)
link = '[Docker docs](https://docs.docker.com/)'
st.markdown(link, unsafe_allow_html=True)

code = '''#docker安装步骤 -ubuntu环境
#链接教程 https://yeasy.gitbook.io/docker_practice/install/ubuntu
#可以使用脚本安装或者直接apt安装
# $ curl -fsSL test.docker.com -o get-docker.sh
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh --mirror Aliyun
# $ sudo sh get-docker.sh --mirror AzureChinaCloud
'''
st.code(code, language="shell")

st.subheader('启动docker')
code = '''sudo systemctl enable docker
sudo systemctl start docker'''
st.code(code, language="shell")

st.subheader('建立docker用户组')
st.text('这一步的目的是将docker用户加入docker用户组方便使用docker命令而不用使用root用户访问')
code='''#建立docker用户组
sudo groupadd docker
#将当前用户加入docker组
sudo usermod -aG docker $USER
#加入完成后退出当前终端并重新登陆,进行测试,
#这里即使用xshell重新打开终端或使用mobaxterm ctrl+shift+u快捷键
'''
st.code(code, language="shell")


st.subheader('测试docker是否安装正确')
code='''运行下面这一行代码
docker run --rm hello-world

#观察是否有下面这些输出
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
b8dfde127a29: Pull complete
Digest: sha256:308866a43596e83578c7dfa15e27a73011bdd402185a84c5cd7f32a88b501a24
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/'''
st.code(code, language="shell")
st.text('若能正常输出以上信息，则说明安装成功。')

st.title('Dockerfile编写教程')
st.text('参考链接如下:')
link = '[streamlit Deploy Streamlit using Docker](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)'
st.markdown(link, unsafe_allow_html=True)
st.text('')

st.subheader('python项目requirements.txt导出')
st.text('在使用docker部署python项目之前需要将其python依赖导出')
code = '''项目依赖导出需要安装pipreqs库
pip install pipreqs
#进入项目目录,以streamlit-webrtc-example-main为例,进入streamlit-webrtc-example-main/目录下
#使用pipreqs生成requirements.txt
pipreqs .
#如果pipreqs无法生成,则可以使用pip freeze命令,我也推荐使用此命令
#如果提示安装freeze,使用pip安装即可
pip freeze > requirements.txt
#在项目目录下如果能看到该requirements.txt,打开查看内容如果如下内容
opencv-python-headless<4.3
pydub==0.25.1
streamlit==1.21.0
streamlit_webrtc==0.44.7
twilio~=8.1.0
plotly>=5.0.0
#说明生成成功
'''
st.code(code, language='shell')
st.markdown("#### 🤡注意事项:生成的requirements.txt在进行docker镜像打包过程中可能会失败,此时需要根据报错进行排查,对错误的版本进行替换")


st.subheader('Dockerfile创建和存放目录')
st.text('Dockerfile一般放在项目目录中,结构如下')
code = '''#例如在/home/cq/qiteam/FuchenWang2023/下
.
├── Dockerfile #会放在这个位置
├── imgs
├── models
│   └── trained_model_unet++.pth
├── packages.txt
├── README.md
├── requirements.txt 
├── src
│   ├── archs.py
│   ├── dataset.py
│   ├── Display.py
│   ├── __init__.py
│   ├── losses.py
│   ├── metrics.py
│   ├── seg_model.py
│   └── utils.py
'''
st.code(code, language='shell')
st.subheader('Dockfile编写')
code = '''# app/Dockerfile
#此处设置使用的python版本
FROM python:3.8
#此处设置在docker容器里面运行的项目文件夹
WORKDIR /app
#此处为ubuntu依赖安装,如果需要安装系统依赖,则添加到此处,并添加-y参数表明确认安装
RUN apt-get update && apt-get install -y && apt-get install libgl1 -y
#此Dockerfile是将本地目录里面所有文件复制到docker镜像里面对应位置,是本地项目的部署
COPY . .
#此处是安装要打包成docker镜像的python项目需要用到的所有依赖,导出requirements.txt在上面给了教程
RUN pip3 install -r requirements.txt
#暴露对外访问端口
EXPOSE 8503
#curl健康检查,可有可无
#HEALTHCHECK CMD curl --fail http://localhost:8503/_stcore/health
#设置入口和运行streamlit命令,当启动docker容器运行镜像时,会自动执行该命令
#该命令等效为 streamlit run main.py --server.port=8503, --server.address=0.0.0.0
#在编写Dockerfile时,streamlit的访问端口与上面EXPOSE的端口一致即可,以及部署的docker及每个同学分配的端口我会给出
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8503", "--server.address=0.0.0.0"]'''
st.code(code, language='docker')

st.subheader('docker image打包')
st.text('在编写好Dockerfile之后，将对其进行打包')
code='''#下面是docker打包命令
#docker build -t xxx .
#docker build 构建命令 
#-t 为指定镜像的名称这里是streamlitmainpage8503
#. 代表使用当前目录下的Dockerfile
docker build -t streamlitmainpage8503 .
'''
st.code(code, language='shell')
st.text('如果打包失败,则根据报错解决,大部分时候都是依赖包版本问题')

st.subheader('打包好后镜像查看')
code='''#命令输入：
docker images
#输出类似如下
REPOSITORY               TAG          IMAGE ID       CREATED         SIZE
wj8506                   latest       57ffe94eb628   47 hours ago    1.99GB
hyx8504                  latest       f8a6a9992da5   6 days ago      9.43GB
webrtc8502               latest       c3e8f948cd3b   2 weeks ago     2.17GB
->streamlitmainpage8503  latest       9bb50b79ca20   2 weeks ago     607MB   
wfccellseg8505           latest       54cbeb68f277   2 weeks ago     5.2GB
dzmyolov5-ascend8501     latest       e828cde8bb9a   2 weeks ago     8.85GB
'''
st.code(code, language='shell')
st.text('')
st.subheader('docker镜像启动')
st.text('在镜像成功打包之后,将启动镜像并进行效果查看')
code='''#直接启动,终端结束后将停止,仅用于效果验证
#docker run 启动 -p 容器端口:容器外端口 镜像名称
docker run -p 8503:8503 streamlitmainpage8503
#后台docker容器运行,服务长期部署时会采用该种方式,上述命令前加上nohup 并加上日志重定向,方便查看
nohup docker run -p 8503:8503 streamlitmainpage8503 > logs/streamlitmainpage8503.out 2>&1 &
'''
st.text('')

st.subheader("打开网页查看效果")
code = '''#在浏览器输入服务器地址+端口
121.48.165.52:8503
'''
st.markdown("### 😂实际的效果就是你现在看到的这个网页")
st.markdown("### 如果对代码有修改,则需要重新打包docker镜像并运行,可以停止之前的容器并删除旧的镜像,也可以打包新的镜像并运行")

st.subheader('docker 命令')
code='''#常用docker命令
#查看运行中的容器
docker ps 
#查看目前已经打包好的镜像
docker images
#删除镜像 
docker rmi xxx
#强制删除镜像
docker rm images -f xxx
#停止容器 先用docker ps查看运行的容器id
docker stop xxx容器id
'''
st.code(code, language='shell')
