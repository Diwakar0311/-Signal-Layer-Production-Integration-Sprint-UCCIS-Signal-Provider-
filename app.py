from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import json

from trace import generate_trace_id

app = FastAPI(
    title="UCCIS Signal Provider",
    version="1.0"
)

with open("traffic.json", "r") as file:
    raw_data = json.load(file)


def build_signals():

    signals = []

    for item in raw_data:

        signal = {
            "signal_id": item["signal_id"],
            "trace_id": generate_trace_id(),
            "signal_type": item["signal_type"],
            "source_system": item["source_system"],
            "location_id": item["location_id"],
            "timestamp": datetime.utcnow().isoformat(),
            "status": item["status"],
            "confidence": item["confidence"],
            "payload": item["payload"]
        }

        print("Signal Generated ->", signal["signal_id"])

        signals.append(signal)

    return signals


@app.get("/signals")
def get_signals():
    return build_signals()


@app.get("/signal/{signal_id}")
def get_signal(signal_id: str):

    signals = build_signals()

    for signal in signals:
        if signal["signal_id"] == signal_id:
            return signal

    return JSONResponse(
        status_code=404,
        content={
            "error": "SIGNAL_NOT_FOUND",
            "trace_id": generate_trace_id()
        }
    )


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "signal-provider",
        "timestamp": datetime.utcnow().isoformat()
    }