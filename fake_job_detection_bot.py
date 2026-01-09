import streamlit as st
import os
from openai import OpenAI

# Page config
st.set_page_config(page_title="Fake Job Detection Bot", layout="centered")

st.title("🕵️ Fake Job Detection Bot")
st.write(
    "Analyze job messages, emails, or internship offers to check if they are "
    "Fake, Genuine, or Suspicious."
)

# Get API key from Streamlit Secrets
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

job_message = st.text_area(
    "📩 Paste Job Message Here",
    height=220,
    placeholder="Paste WhatsApp / Email / Job Description here..."
)

if st.button("🔍 Analyze Job"):
    if job_message.strip() == "":
        st.warning("Please enter a job message.")
    else:
        with st.spinner("Analyzing job offer..."):
            prompt = f"""
You are an intelligent AI assistant called “Fake Job Detection Bot”.

Your task is to analyze job-related messages and classify them as:
1) Fake Job
2) Genuine Job
3) Suspicious (Needs Verification)

Instructions:
- Look for money requests, personal data requests, urgency,
  unrealistic salary, WhatsApp/Telegram-only communication,
  or no interview.
- Be student-friendly and calm.

Response Format:
1. Final Verdict: Fake / Genuine / Suspicious
2. Reasons (bullet points)
3. Safety Advice

Job Message:
\"\"\"{job_message}\"\"\"
"""

            # ✅ NEW OpenAI API (IMPORTANT)
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )

            st.success("✅ Analysis Complete")
            st.markdown(response.output_text)

