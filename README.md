# Video Agent

Backend prototype for a real-time communication application.

## Description
This project is an early-stage prototype of a video communication system.
The current focus is on building a FastAPI backend with WebSocket support,
which will later be used for real-time subtitles, chat, and AI-assisted features.

## Features (current)
- FastAPI backend
- WebSocket endpoint (`/ws`)
- Real-time message exchange (echo test)
- Isolated Python virtual environment

## Tech stack
- Python 3
- FastAPI
- Uvicorn
- WebSockets

## How to run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload

