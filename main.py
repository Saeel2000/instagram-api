from fastapi import FastAPI
from api.instagram_api import app as public_app

app = FastAPI()

# Mount public API
app.mount("/public", public_app)

@app.get("/")
def home():
    return {"message": "Instagram Public API is running!"}
