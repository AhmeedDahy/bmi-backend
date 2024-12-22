from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bmi import bmi
# Pydantic Model for JSON Input
class BMICalculator(BaseModel):
    weight: float
    height: float

# FastAPI App Instance
app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; replace "*" with specific origins for security
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/submit/")
async def submit_form(data: BMICalculator):
    """
    Endpoint to calculate BMI given height and weight.
    Accepts JSON payload with 'weight' and 'height'.
    """
    # Inline BMI Calculation
    bmi = round(data.weight / ((data.height / 100) ** 2), 2)  # Height in cm

    return JSONResponse(content={
        "message": "Form received successfully",
        "data": {
            "bmi": bmi
        }
    })
