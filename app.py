import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center'>Basic information of the pub dataset</h1>", unsafe_allow_html=True)

df = pd.read_csv('G:\\Raj\\Innomatics Research Lab\\Streamlit\\Nearest Pub Task\\Find-Nearest-Pubs\\data\\pubs.csv')

st.markdown("<h3 style='text-align: center'>First 5 rows of the dataset</h3>", unsafe_allow_html=True)
st.dataframe(df.head())

st.markdown("<h3 style='text-align: center'>Statistical Description of the Dataset</h3>", unsafe_allow_html=True)
st.dataframe(df.describe())

st.markdown("<h3 style='text-align: center'>Number of pubs in top 5 local authorities</h3>", unsafe_allow_html=True)
df_local_authority = pd.DataFrame(df['local_authority'].value_counts().reset_index().head())
st.bar_chart(df_local_authority)

st.markdown("<h3 style='text-align: center'>Pub locations in the country</h3>", unsafe_allow_html=True)
df_map = df[['lat', 'lon']]
st.map(df_map)

st.markdown(f"There are total {df['name'].nunique()} pubs in the country")

st.markdown(f"There are total {df['local_authority'].nunique()} local authorities in the country")