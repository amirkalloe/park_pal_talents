from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from datetime import datetime

from app.database.database import get_db
from app.models.park import SensorData
from app.schemas import park
import uvicorn

import logging

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Park Pal Talents",
    description="Park Pal Talents API docs",
    docs_url="/api-docs",
    redoc_url=None,
    swagger_ui_parameters={"displayRequestDuration": True},
    root_path="/api"
)

# Add CORS middleware
logger.info("Adding middlewares.")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# API Routes
@app.post("/sensor-data/", response_model=park.SensorDataIn)
async def create_sensor_data(park: park.SensorDataIn, db: Session = Depends(get_db)):
    db_park = SensorData(**park.model_dump())
    db.add(db_park)
    db.commit()
    db.refresh(db_park)
    return db_park


@app.get("/sensor-data/", response_model=List[park.SensorData])
async def get_all_sensor_data(db: Session = Depends(get_db)):
    return db.execute(select(SensorData)).scalars().all()

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)