from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
client = OpenAI()

QUERYBOT_SYSTEM_PROMPT = """
You are an IT hiring manager. Ask an interview question for the role below.
Mix technical, behavioral, and scenario-based questions. Ask only one question at a time.
"""

ANSWERBOT_SYSTEM_PROMPT = """
You are a job candidate. Answer the question in a professional tone.
Use STAR format for behavioral questions. Use the resume and job description if provided.
"""

def get_openai_response(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error contacting OpenAI API: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    question = ""
    answer = ""
    resume = ""
    job_desc = ""

    if request.method == 'POST':
        resume = request.form.get('resume', '')
        job_desc = request.form.get('job_desc', '')

        query_messages = [
            {"role": "system", "content": QUERYBOT_SYSTEM_PROMPT},
            {"role": "user", "content": f"Role: {job_desc}\nResume: {resume}"}
        ]

        question = get_openai_response(query_messages)

        answer_messages = [
            {"role": "system", "content": ANSWERBOT_SYSTEM_PROMPT},
            {"role": "user", "content": f"Question: {question}\nResume: {resume}\nJob Description: {job_desc}"}
        ]

        answer = get_openai_response(answer_messages)

    return render_template('index.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
