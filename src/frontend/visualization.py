import streamlit as st
from src.backend.Consumer import Consumer_
import matplotlib.pyplot as plt
import pandas as pd
import json

st.set_page_config(
    page_title="Real-Time Data Dashboard",
    layout='wide',
)

if "metrics" not in st.session_state:
    st.session_state["metrics"] = []
if "age" not in st.session_state:
    st.session_state["age"] = []

consumer = Consumer_(bootstrap_servers = 'localhost:9094', topic = 'resultsML', group_id = 'frontend')
consumer.subscribe_on_topic() 

st.title("Results")
chart_holder_metrics = st.empty()
chart_holder_predictions = st.empty()

while True:
    msg = consumer.get_messages(10)
    if msg != -1:
        results_data = json.loads(msg.value().decode('utf-8'))

        st.session_state['metrics'].append(results_data['metrics'])
        st.session_state['age'].append(results_data['age'])

        df = pd.DataFrame.from_dict(st.session_state['metrics'])
        chart_holder_metrics.line_chart(df)

        df_prediction = pd.DataFrame.from_dict(st.session_state['age'])
        df_prediction.columns = ['Age']
        chart_holder_predictions.line_chart(df_prediction, y='Age')
