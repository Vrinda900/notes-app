\# Notes API



A notes app backend built with FastAPI, SQLAlchemy and PostgreSQL.



\## Setup

1\. Create and activate a virtual environment:

&#x20;  `python -m venv venv` then `venv\\Scripts\\activate`

2\. Install packages: `pip install -r requirements.txt`

3\. Create a PostgreSQL database named `notes\_db`

4\. Copy `.env.example` to `.env` and put in your password

5\. Run: `uvicorn main:app --reload`

6\. Open http://127.0.0.1:8000/docs



\## Endpoints

\- POST /notes: create a note

\- GET /notes: list all notes

\- GET /notes/{id}: get one note

\- PUT /notes/{id}: update a note

\- DELETE /notes/{id}: delete a note

\- POST /notes/{id}/summarize: generate and save an AI summary of a note



\## Progress

\- Day 1: CRUD API with PostgreSQL (done)

\- Day 2: AI summarization with Google Gemini (done)
