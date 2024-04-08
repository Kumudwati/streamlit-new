import streamlit as st
import pandas as pd

st.write('CMPD traffic Stops')

@st.cache_data 
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = load_data("data/officer_Traffic_stops.csv")

st.dataframe(stops)
