import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
st.title('webrtc部署以及ice创建')
st.text('该项目使用使用webrtc demo为例子,将其中使用的google ice替换成部署在阿里云服务器上的TURN,最终运行')
st.title('阿里云服务器申请')
st.text('租用云服务器,这里选择的是阿里云的学生云服务器,完成学生身份验证可以领取一个月的ecs,完成实验与验证(搜答案)可以免费续6个月')
st.text('链接https://developer.aliyun.com/plan/student#J_5144437010')
st.text('购买后修改root密码,参考')
