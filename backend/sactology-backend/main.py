
from fastapi import FastAPI, HTTPException
from grading import grade_diarrhoea

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "SACTology API is running"}


@app.post("/symptoms/diarrhoea")
def log_diarrhoea(extra_stools: int):
    # Illustrative thresholds only; real values need clinical sign-off
    try:
       grade = grade_diarrhoea(extra_stools)
    except ValueError as error:
       raise HTTPException(status_code=422, detail=str(error))
    return {"grade": grade}