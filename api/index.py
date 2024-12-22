from main import app  # Import the FastAPI app from main.py

# Expose the app as ASGI
from mangum import Mangum
handler = Mangum(app)
