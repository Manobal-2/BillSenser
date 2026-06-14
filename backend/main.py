from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from parser import parse_bill
from forecast import predict_bill
from recommendations import generate_recommendations

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

    bill_data = parse_bill(contents)

    forecast = predict_bill(bill_data)

    recommendations = generate_recommendations(bill_data)

    return {
        "bill_data": bill_data,
        "forecast": forecast,
        "recommendations": recommendations
    }