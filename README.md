# Agentic IT Interview Platform

This is an interactive IT interview simulator powered by OpenAI’s GPT-4o, deployed on Raspberry Pi or AWS EC2.
It features two agents: one that asks realistic IT interview questions and another that answers them based on a resume and job description.

## Features
- Two-agent simulation: interviewer & interviewee
- Accepts resume & job description input
- Runs on Raspberry Pi or cloud
- SSH keypair & user account setup for secure deployment
- Web interface built with Flask

## Setup

### Prerequisites
- Python 3.7+
- OpenAI API key

### Install dependencies
```bash
pip install -r requirements.txt
```

### Configure
Rename `.env.example` to `.env` and set your API key:
```bash
OPENAI_API_KEY=your-api-key
```

### Run
```bash
python app.py
```

Visit: [http://localhost:5050](http://localhost:5050)

## Run in Docker (optional)
```bash
docker build -t agentic-interview .
docker run -d -p 5050:5050 --env-file .env agentic-interview
```
