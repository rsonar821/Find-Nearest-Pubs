import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center'>Basic information of the pub dataset</h1>", unsafe_allow_html=True)
df = pd.read_csv('G:\\Raj\Innomatics Research Lab\\Streamlit\\Nearest Pub Task\\data\\pubs.csv')
st.markdown("<h3 style='text-align: center'>First 5 rows of the dataset</h3>", unsafe_allow_html=True)
st.dataframe(df.head())
st.markdown("<h3 style='text-align: center'>Statistical Description of the Dataset</h3>", unsafe_allow_html=True)
st.dataframe(df.describe())
df_map = df[['lat', 'lon']]
st.map(df_map)