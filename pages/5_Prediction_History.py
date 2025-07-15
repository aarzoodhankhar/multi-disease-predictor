import streamlit as st
import plotly.express as px
from firebase_config import db
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Prediction History", page_icon="📚")

st.markdown("""
<h1 style="color:#7b1fa2;">📚 Your Prediction History</h1>
<p style="font-size:17px; color:#555;">Track your past health checks in one place.</p>
<hr style="border:1px solid #e0e0e0;">
""", unsafe_allow_html=True)

user = st.session_state.get("user", None)

if user:
    user_id = user.get('localId')
    id_token = user.get('idToken')

    try:
        records = db.child("predictions").child(user_id).get(id_token)
        data = []

        if records.each():
            for record in records.each():
                entry = record.val()
                data.append({
                    "Date": datetime.strptime(entry['date'], "%Y-%m-%d %H:%M:%S.%f"),
                    "Disease": entry['disease'],
                    "Result": "Positive" if entry['result'] == 1 else "Negative"
                })

            df = pd.DataFrame(data).sort_values("Date", ascending=False)

            # Table view
            st.dataframe(df, use_container_width=True)

            # Chart: Disease Prediction Frequency
            chart_data = df["Disease"].value_counts().reset_index()
            chart_data.columns = ["Disease", "Count"]
            fig = px.pie(chart_data, names="Disease", values="Count",
                         title="Prediction Distribution", color_discrete_sequence=px.colors.sequential.RdPu)
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.info("You haven’t made any predictions yet.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
else:
    st.warning("Please log in to see your prediction history.")
