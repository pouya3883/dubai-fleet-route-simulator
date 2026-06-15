# Dubai Fleet Route Simulator

A local data pipeline that simulates delivery trucks moving along preset highway routes in Dubai, transmits their coordinates over a local network, logs them in a SQL database, and displays them on a map interface.

This project was built to practice writing decoupled, multi-layered software applications where the frontend and backend are completely separate.

## System Workflow (How it Works)

The application consists of three independent components running simultaneously:

1. **The Python Simulator (`simulator.py`):** An infinite loop script that iterates through pre-defined arrays of GPS coordinates (representing highway routes). Every 3 seconds, it generates random speed and fuel drops, packs the data into a JSON structure, and transmits it via an HTTP POST request.
2. **The FastAPI Gateway (`main.py`):** A lightweight web server running locally on port 8000. It catches the network packets, enforces basic data type safety, and appends each incoming log as a new row inside a local SQLite database (`smart_city.db`).
3. **The Web Dashboard (`dashboard/`):** A modular single-page frontend. It makes background API requests to the server every 3 seconds to fetch the most recent data rows and updates Leaflet.js markers over map graphics. It also draws fixed dashed polylines to show the path tracks.

## Project Structure

```text
├── simulator.py       # Generates route data and handles network transmissions
├── main.py            # API server that receives requests and connects to SQL
├── .gitignore         # Keeps local database runtime logs out of version control
└── dashboard/         # The frontend assets
    ├── index.html     # Page layout structure
    ├── style.css      # Map and title canvas dimensions
    └── app.js         # Map initialization and background data polling logic
```

## Setup & How to Run Natively

### 1. Run the Backend Server

Make sure you have your virtual environment active and dependencies installed, then boot the API gateway:

```bash
uvicorn main:app --reload
```

### 2. Launch the Data Streamer

Open a separate terminal window and run the Python route sequencer:

```bash
python simulator.py
```

### 3. Open the Viewport

Natively double-click `dashboard/index.html` inside your file browser to open the map canvas and watch the background updates stream in real-time.
