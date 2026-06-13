from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Smart City IoT Ingestion API")


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
    print(
        f"--> Incoming Data Verified | Truck: {data.vehicle_id} | Speed: {data.speed} km/h"
    )
    return {"status": "success", "received_vehicle_id": data.vehicle_id}
