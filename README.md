# Adaptive Document Preparation System

AI/ML Internship Assessment Project for Cloudly.

## Overview

This project is an adaptive document preparation system that:

- Parses a multi-section PDF
- Generates MCQs using an LLM
- Tracks user performance
- Adapts future questions based on weak areas

## Tech Stack

- FastAPI
- SQLite
- PyMuPDF
- Gemini Flash API
- SQLAlchemy

## Current Progress

## Current Progress

- [x] Project setup
- [x] PDF parsing
- [x] Gemini LLM integration
- [x] MCQ generation API
- [x] Adaptive engine
- [x] Session tracking

## Setup

```bash
pip install -r requirements.txt

## API Endpoints

### Generate Quiz

POST `/generate-quiz`

Example Request:

```json
{
  "sections": [1, 2],
  "num_questions": 5
}

## LLM Integration

The project uses Groq API with the Llama 3 70B versatile model.

Reason for choice:
- Free-tier availability
- Extremely fast inference
- Reliable structured output generation
- Easy API integration

## Adaptive Engine

The system tracks historical user performance and identifies weak topics based on repeated incorrect answers.

Adaptive behavior:
- Weak topics are prioritized in future MCQ generation
- Question-level history is persisted in SQLite
- Session tracking supports longitudinal preparation analysis

## Database Schema

### Sessions Table
Stores:
- session ID
- selected sections
- final score

### Question Results Table
Stores:
- question text
- user answer
- correct answer
- correctness
- topic
- explanation

## Additional Features

### Session History API
Retrieve all historical preparation sessions.

### Analytics API
Track topic-wise accuracy and identify weak areas.

### Session Detail API
Inspect question-level performance history.

### Export System
Session evaluation results are automatically exported as JSON reports.

## API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| /generate-quiz | POST | Generate adaptive MCQs |
| /submit-answers | POST | Submit answers and score |
| /sessions | GET | Retrieve session history |
| /session/{id} | GET | Retrieve session details |
| /analytics | GET | Retrieve performance analytics |