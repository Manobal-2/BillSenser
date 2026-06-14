
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from backend.parser import extract_text
from agents import explain_bill, generate_savings, dispute_generator
from forecast import forecast_bill

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_bill(file: UploadFile = File(...)):
    contents = await file.read()

    text = extract_text(contents)

    explanation = explain_bill(text)

    savings = generate_savings(text)

    forecast = forecast_bill()

    dispute = dispute_generator(text)

    return {
        "bill_text": text,
        "explanation": explanation,
        "forecast": forecast,
        "savings": savings,
        "dispute_template": dispute
    }
