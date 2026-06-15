import time
import random
import requests

vehicles = [
    {
        "vehicle_id": "DXB-TRUCK-001",
        "route": [
            [25.0765, 55.1504],
            [25.0932, 55.1645],
            [25.1154, 55.1901],
            [25.1412, 55.2188],
            [25.1685, 55.2455],
            [25.1972, 55.2744],
        ],
        "current_index": 0,
        "fuel": 100.0,
    },
    {
        "vehicle_id": "DXB-TRUCK-002",
        "route": [
            [25.1320, 55.2612],
            [25.1544, 55.2750],
            [25.1788, 55.2905],
            [25.1911, 55.3022],
            [25.2048, 55.2708],
        ],
        "current_index": 0,
        "fuel": 100.0,
    },
    {
        "vehicle_id": "DXB-TRUCK-003",
        "route": [
            [25.1102, 55.2140],
            [25.1155, 55.2210],
            [25.1201, 55.2265],
            [25.1224, 55.2301],
        ],
        "current_index": 0,
        "fuel": 100.0,
    },
]

print("Starting IoT Vehicle Simulator... Press CTRL+C to stop.\n")

url = "http://127.0.0.1:8000/telemetry"

while True:
    for vehicle in vehicles:
        vehicle_json = {}
        current_time = int(time.time())

        if vehicle["current_index"] >= (len(vehicle["route"]) - 1):
            vehicle["current_index"] = 0

        current_coords = vehicle["route"][vehicle["current_index"]]

        lat = current_coords[0]
        lng = current_coords[1]

        vehicle["fuel"] -= random.uniform(0.1, 0.3)
        vehicle["fuel"] = max(0, round(vehicle["fuel"], 2))

        vehicle_json.update(
            {
                "vehicle_id": vehicle["vehicle_id"],
                "lat": lat,
                "lng": lng,
                "fuel": vehicle["fuel"],
                "speed": random.randint(60, 80),
                "timestamp": current_time,
            }
        )

        vehicle["current_index"] += 1

        response = requests.post(url, json=vehicle_json)

        print(
            f"Broadcasted {vehicle['vehicle_id']} -> Server Response: {response.status_code}"
        )

    print("-" * 50)
    time.sleep(3)
