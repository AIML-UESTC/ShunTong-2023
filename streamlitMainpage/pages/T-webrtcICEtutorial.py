import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
import os
from PIL import Image
pathpwd = os.getcwd()
#path=os.path.join(pathpwd,"pages/resources/moon.jpg")

st.title('webrtc部署以及ice创建')
st.text('该项目使用使用webrtc demo为例子,将其中使用的google ice替换成部署在阿里云服务器上的TURN,最终运行')
st.text('该webtrcdemo被我修改了相应依赖,之前原版demo依赖存在问题')
link = '[Visit webrtcdemo-修改版](https://github.com/AIML-UESTC/ShunTong-2023/tree/main/streamlit-webrtc-example-main)'
st.markdown(link, unsafe_allow_html=True)
link = '[Visit webrtcdemo-原版](https://github.com/whitphx/streamlit-webrtc-example)'
st.markdown(link, unsafe_allow_html=True)

st.subheader('阿里云服务器申请')
st.text('租用云服务器,这里选择的是阿里云的学生云服务器,完成学生身份验证可以领取一个月的ecs')
st.text('完成实验与验证(baidu google搜答案)可以免费续6个月')
st.text('学生验证页面链接')
#st.text('链接https://developer.aliyun.com/plan/student#J_5144437010')
link = '[Visit 阿里云学生云服务器租用](https://developer.aliyun.com/plan/student#J_5144437010)'
st.markdown(link, unsafe_allow_html=True)

path=os.path.join(pathpwd,"pages/resources/阿里云界面.png")
image = Image.open(path)
st.image(image, caption='阿里云学生服务器申请界面')


st.text('购买后修改root密码,参考本github项目中powerpoint文件夹下的pptstreamlit云服务器部署')
st.text('除此之外记住开放所有端口,因为ice需要暴露端口访问,同样也是在上面的ppt中')
st.text('修改好密码后准备把阿里云服务器部署成ICE,这里使用的是coturn')
st.text(' ')

st.subheader('coturn安装到阿里云服务器上')
code = '''#克隆coturn项目
git https://github.com/coturn/coturn.git
#切换到克隆的项目文件夹中
cd coturn
#运行configure,如果无法运行需要添加权限使用 chmod +x configure
#如果有依赖问题,google一下解决,我忘记了当时需要安装什么依赖了
./configure
#使用make编译安装,等待安装完成
make
'''
st.code(code, language='bash')
st.text(' ')

st.subheader('coturn配置修改和应用')
st.text('安装好之后需要进行coturn的各项配置了')
code='''
#切换到配置文件所在路径
cd /usr/local/etc
#拷贝一份默认配置文件,后续将在里面进行我们的各项配置
cp turnserver.conf.default turnserver.conf
'''
st.code(code, language='bash')
st.text(' ')

st.text('使用生成coturn的用户名和密码以及realm,后续我们将会写进配置文件')
code='''
#turnadmin -a -u USERNAME -p PASSWORD -r REALM
#在这里生成的用户名为qiteam,密码为qiteamuestc, realm为7team
turnadmin -a -u qiteam -p qiteamuestc -r 7team
'''
st.code(code, language='bash')
st.text(' ')

st.text('将turnserver.conf里面原有内容清空,并将以下内容粘贴进去,参数含义看我给出的注释')
code = '''
#客户端密码:这里随便设置,不设置会有报错。
cli-password=7team
#云服务器网ip,在阿里云服务器管理界面去查看,一般都是172开头
listening-ip=172.21.95.85
#配置监听端口,按照这个来即可
listening-port=3478
tls-listening-port=5349
#配置relay-ip,与上述云服务器内网ip一致即可
relay-ip=172.21.95.85
#外网ip,云服务器的公网访问ip,在云服务器管理界面查看
external-ip=47.120.40.60
#用户=用户名:密码 刚才使用turnadmin命令生成的,上面生成的是什么,这里就是什么
user=qiteam:qiteamuestc
realm=7team
#剩下的按照这个来就行
cert=/ssl/turn_server_cert.pem
pkey=/ssl/turn_server_public_key.pem
no-tls
no-dtls
no-tcp'''
st.code(code, language='bash')
st.text(' ')

st.subheader('coturn的turnserver带参数应用编写的配置文件启动')
st.text('配置完成后可以进行启动,启动参数就是turnserver 加参数 -v选择配置文件,配置文件就是刚才设置的内容')
code='''
#直接启动,终端结束则停止
turnserver -v /usr/local/etc/turnserver.conf
#后台启动,终端结束不会停止,长期运行必采用此方式,并加上日志重定向方便查看日志
nohup turnserver -v /usr/local/etc/turnserver.conf > turnserver.out 2>&1 &
'''
st.code(code, language='bash')
st.text(' ')

st.subheader('阿里云部署的turn ice验证')
st.text('在阿里云上部署了ice之后,有一个网站链接可以测试是否部署成功,如果返回了relay则代表成功了')
link = '[Visit ice验证页面](https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/)'
st.markdown(link, unsafe_allow_html=True)
path=os.path.join(pathpwd,"pages/resources/ice验证页面.png")
image = Image.open(path)
st.image(image, caption='ice验证页面,按照我的输入即可')

st.text('')
st.subheader('coturn的turnserver应用在python代码中')
st.text('随后的样例在streamlit-webrtc-example-main中')
st.text('将原先的sample_utils/turn.py下的get_ice_servers方法返回的ice换成我们的阿里云TURN')

code ='''def get_ice_servers():
    try:
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    except KeyError:
        logger.warning(
            "Twilio credentials are not set. "  # noqa: E501
        )
        #这段代码只需要看这里,其他不用看
        #注意此处,原先的demo是当没有配置本地twilio相关环境变量时,返回一个google的stun服务器
        #return [{"urls": ["stun:stun.l.google.com:19302"]}]
        #现在改成了返回我们的阿里云服务器turn,记住要带上turn:外网ip+端口 
        #username:用户名 credential:密码
        #严格按照我这里的return返回的格式。
        return [{"urls": ["turn:47.120.40.60:3478"],
                 "username": ["qiteam"],
                 "credential": ["qiteamuestc"]}]
    client = Client(account_sid, auth_token)
    token = client.tokens.create()
    return token.ice_servers'''
st.code(code, language='python')

st.subheader('项目使用摄像头获取图像时报错问题navigatexx问题处理')
st.text('如果报错:Error: navigator.mediaDevices is undefined. ')
st.text('It seems the current document is not loaded securely.')
st.text('因为没有配置域名证书等,所以目前只有http访问,需要对浏览器进行相应设置')
st.text('在浏览器地址栏输入  chrome://flags/#unsafely-treat-insecure-origin-as-secure')
path=os.path.join(pathpwd,"pages/resources/浏览器设置.png")
image = Image.open(path)
st.image(image, caption='浏览器设置页面')
st.text('浏览器设置页面,将Insecure origins treated as secure设置成Enabled')
st.text('然后将要访问的http地址+端口按照我给出的样式进行设置,随后重启浏览器')
