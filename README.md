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
- [ ] Adaptive engine
- [ ] Session tracking

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