from datetime import date
from typing import List
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="Tatkal Assistant Pro API",
    description=(
        "Demo API for journey preparation. Train data is illustrative; no ticket transactions are performed. "
        "Connect an authorized railway data/booking provider before production use."
    ),
    version="0.1.0",
)

# Local development defaults. Restrict this list to your actual frontend origins in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

class Train(BaseModel):
    no: str
    name: str
    from_station: str = Field(alias="from")
    to_station: str = Field(alias="to")
    dep: str
    arr: str
    duration: str
    classes: List[str]
    status: str

class TrainSearchResponse(BaseModel):
    demo: bool = True
    message: str
    trains: List[Train]

DEMO_TRAINS = [
    {"no":"12301","name":"Howrah Rajdhani Express","from":"HWH","to":"NDLS","dep":"16:55","arr":"09:55","duration":"17h 00m","classes":["3A","2A","1A"],"status":"Demo only — verify with authorized provider"},
    {"no":"12313","name":"Sealdah Rajdhani Express","from":"SDAH","to":"NDLS","dep":"16:50","arr":"10:05","duration":"17h 15m","classes":["3A","2A","1A"],"status":"Demo only — verify with authorized provider"},
    {"no":"12321","name":"Mumbai Mail","from":"HWH","to":"CSMT","dep":"22:00","arr":"05:20","duration":"31h 20m","classes":["SL","3A","2A"],"status":"Illustrative route — verify details"},
]

@app.get("/")
def root():
    return {"name": "Tatkal Assistant Pro API", "status": "ok", "docs": "/docs", "demo_data": True}

@app.get("/health")
def health():
    return {"status": "healthy", "demo_data": True}

@app.get("/api/trains", response_model=TrainSearchResponse)
def search_trains(
    from_station: str = Query(alias="from", min_length=2, max_length=10),
    to_station: str = Query(alias="to", min_length=2, max_length=10),
    journey_date: date = Query(alias="date"),
    quota: str = Query(default="Tatkal", max_length=30),
    class_code: str = Query(default="3A", max_length=5),
):
    """Return illustrative train cards for UI development, never live availability."""
    trains = [t for t in DEMO_TRAINS if t["from"].casefold() == from_station.casefold() and t["to"].casefold() == to_station.casefold()]
    if not trains:
        # Return a clearly labeled placeholder instead of pretending a live result exists.
        trains = [{
            "no": "DEMO", "name": f"Example service: {from_station.upper()} to {to_station.upper()}",
            "from": from_station.upper(), "to": to_station.upper(), "dep": "--:--", "arr": "--:--",
            "duration": "Check official timetable", "classes": [class_code.upper()],
            "status": "Placeholder only — no live train lookup configured"
        }]
    return TrainSearchResponse(
        demo=True,
        message=f"Illustrative data for {journey_date.isoformat()} / {quota}; not live schedule or availability.",
        trains=[Train(**t) for t in trains],
    )
