from datetime import datetime
from sqlalchemy import Integer, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.sql_app.database import Base


class SensorData(Base):
    __tablename__ = "sensor_data"
    __comment__ = "This is the table for sensor data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sensor_id: Mapped[int] = mapped_column(Integer)
    distance: Mapped[float] = mapped_column(Float(5))
    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
