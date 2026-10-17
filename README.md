# Tatkal Assistant Pro

A starter full-stack railway journey preparation dashboard. It helps users organize train searches, save journey preferences locally in the demo UI, view a Tatkal countdown, and prepare passenger details before using an authorized booking service.

> **Important:** This project does not book railway tickets, access IRCTC accounts, solve CAPTCHAs, bypass queues, or guarantee Tatkal availability. Live train data and actual transactions require an authorized railway provider/integration. The sample API uses demo data only.

## Stack
- Frontend: React + Vite
- Backend: FastAPI + Pydantic
- Demo endpoints: health, train search (mock), saved journey schema example
- No secrets or real passenger data are included.

## Run locally

### 1. Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
API docs: http://127.0.0.1:8000/docs

### 2. Frontend
Open a second terminal:
```bash
cd frontend
npm install
npm run dev
```
Open the local URL printed by Vite (usually http://localhost:5173).

The frontend calls the API at `http://127.0.0.1:8000`. Set `VITE_API_BASE_URL` if your API runs elsewhere.

## Deploying
- Frontend: Vercel, Netlify, or GitHub Pages (set `VITE_API_BASE_URL` to your deployed API URL; GitHub Pages only hosts the frontend).
- Backend: Render, Railway, or another Python host that supports FastAPI.
- Configure CORS, HTTPS, a production database, rate limits, logging, and secure authentication before accepting real user data.

## Roadmap
1. Authorized train data provider and source attribution.
2. Authentication, secure passenger profile storage, and PostgreSQL.
3. Official/authorized booking handoff (no CAPTCHA or queue bypass).
4. Notifications, PNR status where supported, and admin tools.
