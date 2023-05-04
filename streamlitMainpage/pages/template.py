import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
from PIL import Image
st.title('项目名称 xxx项目')
st.title('项目描述')
st.text('该项目是xxxxx')
st.title('项目展示')
st.subheader('点击链接跳转至yolov3预测结果展示')

link = '[Visit Streamlit](https://streamlit.io/)'
st.markdown(link, unsafe_allow_html=True)


st.title('代码块展示')
st.code('''
def hello():
    print("Hello, Streamlit!")''', language='python')

st.title('表格引入')
df = pd.DataFrame(
    np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))
 
st.table(df)
st.dataframe(df)

st.title('json引入')
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
st.title('图片引入')
path='/home/ts/work/ShunTong-2023/streamlitMainpage/pages/moon.jpg'
image = Image.open(path)
st.image(image, caption='moon')

st.title('视频引入')
path = '/home/ts/work/ShunTong-2023/streamlitMainpage/pages/star.mp4'
video_file = open(path, 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.title('音频引入')
path = '/home/ts/work/ShunTong-2023/streamlitMainpage/pages/testmusic.mp3'
audio_file = open(path, 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/3gpp')


st.title('联系方式')
st.text('github: ')
st.text('email: ')
