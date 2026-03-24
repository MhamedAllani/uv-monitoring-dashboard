import streamlit as st
import pandas as pd
from datetime import datetime

MAX_HOURS = 14000

# Sample data (no Excel needed)
data = [
    {"id": 1, "name": "UV Broodstock 1", "location": "Broodstock 1", "start_date": "01-01-2025"},
    {"id": 2, "name": "UV Broodstock 2", "location": "Broodstock 2", "start_date": "01-02-2025"},
    {"id": 3, "name": "UV Broodstock 3", "location": "Broodstock 3", "start_date": "01-03-2025"},
]

df = pd.DataFrame(data)

def calculate(start_date):
    now = datetime.now()
    start = datetime.strptime(start_date, "%d-%m-%Y")

    elapsed = (now - start).total_seconds() / 3600
    remaining = MAX_HOURS - elapsed

    if remaining > 1440:
        color = "green"
        status = "GOOD"
    elif remaining > 720:
        color = "orange"
        status = "WARNING"
    else:
        color = "red"
        status = "CRITICAL"

    return int(elapsed), int(remaining), color, status


st.title("💡 UV Monitoring Dashboard")

cols = st.columns(3)

for i, row in df.iterrows():
    used, remaining, color, status = calculate(row["start_date"])

    with cols[i]:
        st.subheader(row["name"])
        st.write(f"📍 {row['location']}")
        st.write(f"⏱ Used: {used} h")
        st.write(f"⏳ Remaining: {remaining} h")

        st.progress(min(used / MAX_HOURS, 1.0))

        if color == "green":
            st.success(status)
        elif color == "orange":
            st.warning(status)
        else:
            st.error(status)