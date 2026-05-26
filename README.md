## Adaptive Document Preparation System

An AI-powered adaptive learning and quiz generation system that parses PDF documents, generates MCQs using LLMs, tracks user performance, and adapts future quizzes based on weak topics and historical sessions.

Built as part of the internship assessment project for Cloudly. Because apparently humans now make machines generate exams about documents so other humans can survive exams about documents. The circle of suffering closes elegantly.

## Features
# Core Features
PDF document parsing and section extraction
AI-generated MCQs using LLMs
Adaptive quiz generation based on weak topics
Historical session tracking
Topic-wise performance analytics
Knowledge base persistence
Automated evaluation scenario runner
CLI-based execution workflow
REST APIs using FastAPI
JSON export system for evaluation outputs
Logging system for debugging and monitoring

## Tech Stack

| Component   | Technology                     |
| ----------- | ------------------------------ |
| Backend     | FastAPI                        |
| LLM         | Groq + Llama 3.3 70B Versatile |
| PDF Parsing | PyMuPDF                        |
| Database    | SQLite                         |
| ORM         | SQLAlchemy                     |
| Validation  | Pydantic                       |
| Server      | Uvicorn                        |

## Why These Technologies Were Chosen
# FastAPI

Chosen for:

simple REST API development
automatic Swagger documentation
beginner-friendly structure
fast development speed

# Groq + Llama 3.3

Chosen because:

free API access
fast inference speed
strong text generation quality
suitable for MCQ generation workflows

# SQLite

Chosen because:

lightweight setup
easy local development
sufficient for project-scale relational storage

# PyMuPDF

Chosen because:

reliable PDF text extraction
simple API
fast parsing performance

# JSON-based Retrieval Instead of Vector DB

A vector database was intentionally not used because:

project scale was small
semantic embedding retrieval was unnecessary
structured JSON retrieval was sufficient for the assessment requirements

The architecture can later be extended using:

FAISS
ChromaDB
Pinecone

if semantic search becomes necessary.

## Project Architecture

PDF
 ↓
PDF Parser
 ↓
Section Extraction
 ↓
sections.json
 ↓
LLM MCQ Generator
 ↓
Quiz API
 ↓
User Answers
 ↓
Scoring Engine
 ↓
SQLite Knowledge Base
 ↓
Weak Topic Detection
 ↓
Adaptive Prompting
 ↓
Improved Future Quizzes

## Project Structure

adaptive-doc-prep/
│
├── app/
│   ├── main.py
│   ├── llm_service.py
│   ├── adaptive_engine.py
│   ├── analytics.py
│   ├── exporter.py
│   ├── scenario_exporter.py
│   ├── kb_snapshot.py
│   ├── logger.py
│   ├── pdf_parser.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── init_db.py
│   └── __init__.py
│
├── data/
│   └── sections.json
│
├── outputs/
│
├── logs/
│   └── system.log
│
├── run_scenario_b.py
├── prep.db
├── requirements.txt
├── README.md
├── .env
└── .gitignore

## Installation & Setup

# 1. Clone Repository

git clone <your-github-repo-link>
cd adaptive-doc-prep

# 2. Create Virtual Environment

# Windows

python -m venv venv

# Activate

venv\Scripts\activate

# 3. Install Dependencies

pip install -r requirements.txt

# 4. Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here

Get API key from: https://console.groq.com/home

# 5. Initialize Database

python -m app.init_db

# 6. Parse PDF Document

Place your PDF inside project root.

Run: python -m app.pdf_parser

This generates: data/sections.json

## Running the Backend

Start FastAPI server:  uvicorn app.main:app --reload

Server runs at:  http://127.0.0.1:8000

Swagger Documentation: http://127.0.0.1:8000/docs

## API Endpoints

# Generate Quiz

POST /generate-quiz

# Example Request

{
  "sections": [1, 2],
  "num_questions": 5
}

# Submit Answers

POST /submit-answers

# Example Request

{
  "sections": [1, 2],
  "answers": [
    {
      "question": "What is AI?",
      "correct_answer": "Artificial Intelligence",
      "user_answer": "Artificial Intelligence",
      "topic": "AI",
      "explanation": "AI refers to intelligent systems."
    }
  ]
}

# Get All Sessions

GET /sessions

# Get Session Details

GET /session/{session_id}

# Get Sessions by Section

GET /sessions/by-section/{section_id}

# Analytics

GET /analytics

Returns:

weak topics
topic frequencies
performance analytics

## Adaptive Intelligence Logic

The system adapts future quizzes using:

weak-topic detection
historical session analysis
previous question tracking
repetition avoidance prompts

# Adaptation Flow

Wrong Answers
 ↓
Weak Topic Detection
 ↓
Adaptive Prompt Injection
 ↓
Future Quiz Focus Adjustment

## Evaluation Scenario

# Scenario A

Generate quizzes for arbitrary sections using:

POST /generate-quiz

Example:

{
  "sections": [1, 2],
  "num_questions": 5
}

# Scenario B

Automated adaptive evaluation runner.

Run:

python run_scenario_b.py

This automatically executes:

| Iteration   | Sections  |
| ----------- | --------- |
| Iteration 1 | [5, 8]    |
| Iteration 2 | [6, 8, 9] |
| Iteration 3 | [8]       |


## Scenario B Output Structure

outputs/
│
├── scenario_b_iter1/
│   ├── questions_iter1.json
│   ├── submission_iter1.json
│   └── kb_snapshot_iter1.json
│
├── scenario_b_iter2/
│   ├── questions_iter2.json
│   ├── submission_iter2.json
│   └── kb_snapshot_iter2.json
│
├── scenario_b_iter3/
│   ├── questions_iter3.json
│   ├── submission_iter3.json
│   └── kb_snapshot_iter3.json

## Knowledge Base Design

The system stores:

# Session-Level Data
session ID
sections attempted
score
# Question-Level Data
question
user answer
correct answer
topic
explanation
correctness
# Retrieval Capabilities
retrieve sessions by section
retrieve historical sessions
detect repeated weak topics
export KB snapshots

## Logging

System logs are stored in:  logs/system.log

Includes:

quiz generation events
submission events
scoring activity

## Assumptions & Limitations

SQLite is used for lightweight local storage
No vector database was used
Adaptive logic is prompt-based
Semantic embeddings are not implemented
UI is currently Swagger-based
No Docker deployment included
No automated unit testing included

## Future Improvements

Potential future extensions:

vector database integration
semantic retrieval using embeddings
frontend dashboard UI
Docker containerization
authentication system
advanced analytics
real-time adaptive scoring
LangChain/LangGraph orchestration

## Submission Notes

This project focuses on:

adaptive intelligence
retrieval-aware quiz generation
historical performance tracking
evaluation automation
backend architecture

The implementation prioritizes:

functional correctness
clean architecture
reproducibility
evaluation compliance