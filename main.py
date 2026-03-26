from fastapi import FastAPI
from app.routes import auth

app = FastAPI(title="FastAPI Auth")

app.include_router(auth.router)

@app.get("/")
def health_check():
    return {"status": "running", "version": "1.0.0"}