from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bmi import bmi  # Ensure the bmi class is correctly implemented and imported

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
    # Validate inputs
    if data.weight <= 0 or data.height <= 0:
        raise HTTPException(status_code=400, detail="Weight and height must be positive values.")
    
    # BMI Calculation
    try:
        calc = bmi(data.weight, data.height)
        res = calc.calculate_bmi()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return JSONResponse(content={
        "message": "Form received successfully",
        "data": {
            "bmi": res
        }
    })
