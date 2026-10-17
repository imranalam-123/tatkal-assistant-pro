# Tatkal Assistant Pro

A React + Vite frontend and FastAPI backend starter for organizing railway journey searches and preparing for Tatkal booking.

> **Important:** This project does not book tickets, access IRCTC accounts, solve CAPTCHAs, bypass queues or guarantee availability. The displayed trains and countdown are demo content, not live railway data.

## Included in this repository

- Responsive React UI with train search fields, class/quota selection and sample train cards.
- Demo Tatkal countdown and pre-booking checklist.
- Saved journey shortlist held in the current browser session only.
- FastAPI `/health` and `/api/trains` endpoints using illustrative sample data.
- Separate CSS, JavaScript/JSX, HTML, Python backend and Dockerfile.

## Run locally

### 1. Backend

Use Python 3.10+:

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API documentation: http://127.0.0.1:8000/docs

### 2. Frontend

Use Node.js 20+ in a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Vite prints a local URL, usually http://localhost:5173. By default, the frontend calls `http://127.0.0.1:8000`. Set `VITE_API_BASE_URL` to your deployed API URL when deploying the frontend.

## Deployment outline

- **Frontend:** deploy `frontend/` as a Vite static site on Vercel, Netlify or another static host. Build command: `npm run build`; output directory: `dist`.
- **Backend:** deploy `backend/` to a Python-capable service such as Render. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
- Set `CORS_ORIGINS` on the backend to the exact frontend origin.

## One-click deployment on Render

This repository includes a Blueprint at `render.yaml` that creates two services together: a static Vite frontend and the FastAPI backend. Connect your Render account to GitHub and review both services before deploying.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/imranalam-123/tatkal-assistant-pro)

After Render provisions both services, open the frontend service URL. The Blueprint wires the backend's public URL into the frontend build and configures the API's CORS setting. The free API service may sleep after inactivity and take time to wake up.

## Before production

1. Integrate an authorized train data provider and clearly cite its source.
2. Add secure authentication, server-side database storage, rate limiting, error monitoring and privacy controls.
3. Store any provider credentials in the hosting platform's secret manager; never commit them.
4. Use only authorized booking handoff flows and follow railway rules. Do not automate CAPTCHA or queue bypasses.
5. Do not present demo train results or the example countdown as live information.
