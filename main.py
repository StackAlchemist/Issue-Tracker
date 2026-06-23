from fastapi import FastAPI
from app.routes.issues import router as issues_router


app = FastAPI()
app.include_router(issues_router)

items = [
    {"id": 1, "name":"Item One"},
    {"id": 2, "name":"Item Two"},
    {"id": 3, "name":"Item Three"},
]

@app.get("/health")
def health_check():
    return {"status":"ok"}


