from fastapi import FastAPI
from api.instagram_api import app as insta_app  # Ensure correct path

app = FastAPI()

# Mount Instagram API
app.mount("/public", insta_app)

@app.get("/")
def home():
    return {"message": "Instagram Public API is running!"}
