#import libs
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotfly.express as px
from datetime import datetime

#define functions


#load data
df_agg = pd.read_csv('Aggregated_Metrics_By_Video.csv')
st.write(df_agg)
