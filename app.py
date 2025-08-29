import pandas as pd
import streamlit as st

# Load CSV
df = pd.read_csv("student_allocations.csv", dtype=str)

# Page config
st.set_page_config(page_title="Student Search", layout="centered")

# Header
st.markdown("""
<div style="
    background: linear-gradient(135deg, #4A90E2, #0052A2);
    color: white;
    text-align: center;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    position: relative;
    z-index: 1;
">
    <h1>🎓 Streamlit Student Search</h1>
    <p>Search results by entering your Student ID</p>
</div>
""", unsafe_allow_html=True)

# Input
student_id = st.text_input("Enter Student ID")

# Search button
if st.button("🔍 Search"):
    student_id = student_id.strip()
    if student_id in df['UniqueID'].values:
        result = df[df['UniqueID'] == student_id]
        st.markdown(
            f'<div style="margin-top:20px; padding:15px; background: black; color: white; \
                    border: 1px solid #444; border-radius: 10px; position: relative; z-index:1;">{result.to_html(index=False)}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div style="margin-top:20px; padding:15px; background: black; color: white; \
                    border: 1px solid #444; border-radius: 10px; position: relative; z-index:1;"><b>❌ Student ID not found.</b></div>',
            unsafe_allow_html=True
        )

