from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Smart City IoT Ingestion API")

DB_FILE = "smart_city.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id TEXT NOT NULL,
            lat REAL NOT NULL,
            lng REAL NOT NULL,
            fuel REAL NOT NULL,
            speed INTEGER NOT NULL,
            timestamp INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_db()


class VehicleTelemetry(BaseModel):
    vehicle_id: str
    lat: float
    lng: float
    fuel: float
    speed: int
    timestamp: int


@app.get("/")
def read_root():
    return {"status": "online", "message": "Smart City IoT API is operational"}


@app.post("/telemetry")
def receive_telemetry(data: VehicleTelemetry):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO telemetry (vehicle_id, lat, lng, fuel, speed, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (data.vehicle_id, data.lat, data.lng, data.fuel, data.speed, data.timestamp),
    )

    conn.commit()
    conn.close()

    print(
        f"--> Saved to Database | Truck: {data.vehicle_id} | Speed: {data.speed} km/h"
    )
    return {"status": "success", "stored_vehicle_id": data.vehicle_id}
