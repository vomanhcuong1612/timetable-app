from fastapi import FastAPI
from . import models, crud, database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cho phép frontend React gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # sau này bạn có thể fix thành http://localhost:3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "✅ FastAPI backend is running"}
