import streamlit as st 
import pandas as pd
import numpy as np

st.markdown("<h1 style='text-align: center'>Select a local authority to check the pubs on the map</h1>", unsafe_allow_html=True)

df = pd.read_csv('G:\\Raj\\Innomatics Research Lab\\Streamlit\\Nearest Pub Task\\Find-Nearest-Pubs\\data\\pubs.csv')

location=df[['lat', 'lon']]
lat = st.number_input("Enter Your Latitude:")
lon = st.number_input("Enter Your Longitude:")
button = st.button("Show Pubs")

new_location=np.array([lat,lon])
distances = np.sqrt(np.sum((new_location - location)**2, axis = 1))
n = 5
min_indices = np.argpartition(distances,n-1)[:n]
if button ==True:
    #st.text("The location corresponsing to below minimum distances : ")
    #st.dataframe(df.iloc[min_indices])
    #st.text("The minimum distances are:")
    #st.dataframe(distances.head(5))
    st.markdown("### Nearest Pubs Are")
    st.map(df.iloc[min_indices])