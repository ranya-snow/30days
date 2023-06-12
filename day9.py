import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
  np.random.randn(50,15),
  columns = ['snowfall', 'temp', 'rainfall'])

st.line_chart(chart_data)
