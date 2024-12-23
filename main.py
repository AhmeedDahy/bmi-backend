from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()

class BMICalculator(BaseModel):
    weight: float
    height: float

@app.post("/submit/")
async def submit_form(data: BMICalculator):
    if data.weight <= 0 or data.height <= 0:
        raise HTTPException(status_code=400, detail="Weight and height must be positive numbers.")
    bmi = round(data.weight / (data.height ** 2), 2)
    return {"bmi": bmi, "message": "BMI calculated successfully"}

# Mangum handler for AWS Lambda
handler = Mangum(app)
