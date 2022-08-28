import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center'>Select a local authority to check the pubs on the map</h1>", unsafe_allow_html=True)

df = pd.read_csv('G:\\Raj\\Innomatics Research Lab\\Streamlit\\Nearest Pub Task\\Find-Nearest-Pubs\\data\\pubs.csv')

option = st.selectbox(
     'Select Local Authority',
     tuple(df['local_authority'].unique()))

df_local = df[df['local_authority']==option]
df_local = df_local[['lat', 'lon']]
st.map(df_local)
