from pydantic import BaseModel
from datetime import datetime


class SensorDataIn(BaseModel):
    sensor_id: int
    distance: float


class SensorData(BaseModel):
    sensor_id: int
    distance: float
    created_date: datetime
