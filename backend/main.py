from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "✅ FastAPI chạy ngon lành"}

