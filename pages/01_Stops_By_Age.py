import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data 
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = load_data("officer_Traffic_stops.csv")

age_bar = alt.Chart(stops).mark_bar().encode(
    alt.X("Driver_Age", bin=alt.Bin(maxbins=10)),
    y='count()',
    tooltip= alt.Tooltip(['Driver_Age','count()'])
)
st.altair_chart(age_bar)