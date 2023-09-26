# It's only 18 lines of code:

import streamlit as st
import pandas as pd
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

benefits = {
    'Benefits': [
        "Scalability", 
        "Cost-Efficiency", 
        "Data Integrity", 
        "Real-time Insights", 
        "User Engagement", 
        "Compliance", 
        "Data Security", 
        "Business Agility", 
        "Competitive Advantage", 
        "Operational Efficiency"
    ]
}

# Create DataFrame
benefits = pd.DataFrame(benefits)

risks = {
    'Risks': [
        "Data Leakage", 
        "Compliance Violations", 
        "Vendor Lock-in", 
        "Complexity", 
        "Cost Overruns", 
        "Data Inconsistency", 
        "Performance Bottlenecks", 
        "Skill Gaps", 
        "Data Bias", 
        "Obsolescence"
    ]
}

# Create DataFrame for risks
risks = pd.DataFrame(risks)

data_in = {
    'Data_In': [
        "Raw Logs", 
        "User Events", 
        "Transactional Data", 
        "Social Media Feeds", 
        "IoT Device Data", 
        "Third-Party APIs", 
        "Batch Files", 
        "Real-time Streams", 
        "Web Scraping", 
        "Manual Entry"
    ]
}

# Create DataFrame for data_in
data_in = pd.DataFrame(data_in)

processing = {
    'Processing': [
        "Data Cleansing", 
        "Data Enrichment", 
        "Data Aggregation", 
        "Data Normalization", 
        "Data Transformation (ETL/ELT)", 
        "Data Indexing", 
        "Data Joining", 
        "Data Caching", 
        "Machine Learning Models", 
        "Real-time Analytics"
    ]
}

# Create DataFrame for processing
processing = pd.DataFrame(processing)

data_out = {
    'Data_Out': [
        "Aggregated Metrics", 
        "Data Warehouses", 
        "Data Lakes", 
        "Dashboards", 
        "Reports", 
        "Predictive Models", 
        "Anomaly Detection Alerts", 
        "Customer Segments", 
        "Business Insights", 
        "Data Visualizations"
    ]
}

# Create DataFrame for Data_Out
data_out = pd.DataFrame(data_out)


with st.form('Define data architecture details'):
  benefit = st.multiselect("Benefits of platform?", benefits)
  risk = st.multiselect("Risks of platform?", risks)
  source = st.multiselect("What data are you loading in?", data_in)
  process = st.multiselect("How are you processing this data?", processing)
  consumption = st.multiselect("How is your data being consumed?", data_out)
  submit = st.form_submit_button("Generate use case description")
  
  prompt = f"Generate a description of a data platform using the following informaiton elements: Benefits of the platform are {benefit}, risks of the platform are {risk}, the data sources being loaded in are {source}, the types of processing are {process} and the data is being used in the following ways: {consumption}"
  
  if submit:
    generate_response(prompt)
