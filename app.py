import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config (layout="wide")


df = pd.read_csv("data.csv", sep=";", decimal=",")
df["data"] = pd.to_datetime(df["data"], dayfirst=True)
df = df.sort_values(by='data', ascending=False)

y_axis_range = [60, 90]

fig = px.line(df, x='data', y='peso', 
              title='Peso ao longo do tempo',
              labels={'data': 'Data', 'peso': 'Peso'}, 
              range_y=y_axis_range)

fig

df
