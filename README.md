
# UCCIS Signal Layer – Production Integration Sprint

## Overview

This project provides a FastAPI-based Signal Layer designed to act as an upstream operational data provider for UCCIS integration workflows.

The service generates structured operational signals, exposes them through REST APIs, and supports downstream consumption through a standardized schema.

---

## Features

* Standardized signal schema
* Traceable signal generation
* Operational dataset support
* FastAPI REST endpoints
* Health monitoring endpoint
* Error handling
* Integration-ready payloads

---

## Signal Schema

Each signal follows the structure below:

```json
{
  "signal_id": "SIG001",
  "trace_id": "TRACE_1001",
  "signal_type": "Flood Alert",
  "source_system": "WaterMonitoring",
  "location_id": "LOC001",
  "timestamp": "2025-06-10T10:00:00Z",
  "status": "ACTIVE",
  "confidence": 0.94,
  "payload": {}
}
```

---

## Operational Scenarios

The dataset contains the following operational scenarios:

* Flood Alert
* Traffic Congestion
* Medical Emergency
* Power Failure
* Cyber Incident
* Water Level Alert
* TTG Scenario

---

## API Endpoints

### Get All Signals

```http
GET /signals
```

Returns all available operational signals.

<img width="1366" height="680" alt="image" src="https://github.com/user-attachments/assets/d2d7cb71-b26d-4d91-915d-2b2fe4736cfa" />


---

### Get Signal By ID

```http
GET /signal/{signal_id}
```

Returns a specific signal.

Example:

```http
GET /signal/SIG001
```

<img width="1364" height="677" alt="image" src="https://github.com/user-attachments/assets/0d73843b-ee07-4594-951d-7c9347b28b60" />


---

## Health Check

```http
GET /health
```

Returns the current operational status of the Signal Provider service.

Example Response:

```{
  "status": "healthy",
  "service": "signal-provider",
  "timestamp": "2026-06-11T08:28:11"
}
```

{
  "status": "healthy",
  "service": "signal-provider",
  "timestamp": "2026-06-11T08:28:11"
}

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Project Structure

```text
.
├── app.py
├── trace.py
├── traffic.json
├── requirements.txt
├── README.md
└── REVIEW_PACKET.md
```

---

## Technologies Used

* Python
* FastAPI
* Uvicorn
* JSON

---

## Runtime Flow

Signal Generated

↓

API Exposed

↓

Signal Retrieved

↓

Ready for UCCIS Consumption

---


