import streamlit as st
import pandas as pd

st.markdown("#### 就业去向")
# Import pandas library

# initialize list of lists
data = [['李颖', '华为'], ['何小芳', '腾讯'], ['李芳卉','阿里'],['王梓再', '阿里'],['王凌锋','中兴'],['王富臣','集度'],['马博俊','达佳互联'],
        ['董哲明','智明达'],['童顺','精灵云']]


# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['姓名', '去向'])

st.table(df)
