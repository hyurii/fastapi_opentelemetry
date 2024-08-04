from fastapi import FastAPI
import requests

from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from utils import init_otel

init_otel()

RequestsInstrumentor().instrument()


app = FastAPI()
FastAPIInstrumentor.instrument_app(app)


@app.get("/google")
def root():
    print("Making request.")
    response = requests.get(url="https://www.example.com")
    response = requests.get(url="http://localhost:8000/google2")
    return {"status_code": response.status_code}


@app.get("/google2")
def root2():
    print("Making request.2")
    response = requests.get(url="https://www.example.com")
    return {"status_code": response.status_code}
