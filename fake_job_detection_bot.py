import streamlit as st
from openai import OpenAI

# 🔑 Replace with your OpenAI API Key
client = OpenAI(api_key="your api key")

st.set_page_config(page_title="Fake Job Detection Bot", layout="centered")

st.title("🕵️ Fake Job Detection Bot")
st.write("Analyze job messages, emails, or internship offers to check if they are Fake, Genuine, or Suspicious.")

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
- Look for money requests, personal data requests, urgency, unrealistic salary,
  WhatsApp/Telegram-only communication, or no interview.
- Be student-friendly and calm.

Response Format:
1. Final Verdict: Fake / Genuine / Suspicious
2. Reasons (bullet points)
3. Safety Advice

Job Message:
\"\"\"{job_message}\"\"\"
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a Fake Job Detection Bot focused on student safety."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2
            )

            st.success("✅ Analysis Complete")
            st.markdown(response.choices[0].message.content)
