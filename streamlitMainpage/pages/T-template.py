import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
from PIL import Image
import os
pathpwd = os.getcwd()

st.title('个人标签页搭建参考模板')
st.subheader('项目名称 xxx项目')
st.subheader('项目描述')
st.text('该项目是xxxxx')
st.subheader('项目展示')
st.subheader('点击链接跳转至xxx结果展示')

link = '[Visit Streamlit](https://streamlit.io/)'
st.markdown(link, unsafe_allow_html=True)


st.subheader('代码块展示')
st.code('''import this
def hello():
    print("Hello, Streamlit!")''', language='python')

st.subheader('代码块展示')
code = '''#include<iostream>
int main(int argc, char** argv){
    std::cout << "helloworld" << std::endl;
    return 0;
}'''
st.code(code, language='cpp')

st.subheader('表格引入')
df = pd.DataFrame(
    np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))
 
st.table(df)
st.dataframe(df)

st.subheader('json引入')
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
         'stuff 1',
        'stuff 2',
        'stuff 3',
         'stuff 5',
    ],
 })
st.subheader('图片引入')
path=os.path.join(pathpwd,"pages/resources/moon.jpg")
image = Image.open(path)
st.image(image, caption='moon')

st.subheader('视频引入')
path=os.path.join(pathpwd,"pages/resources/star.mp4")
video_file = open(path, 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.subheader('音频引入')
path=os.path.join(pathpwd,"pages/resources/testmusic.mp3")
audio_file = open(path, 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/3gpp')


st.subheader('联系方式')
st.text('github: ')
st.text('email: ')
