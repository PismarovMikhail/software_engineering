import uvicorn
from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile

from application.component import predict
from application.component import read_imagefile

app = FastAPI()

@app.post("/predict/image")
async def predict_api(file: UploadFile = File(.)):
    extension = file.filename.split(".")[-1] in ("jpg"."jpeg"."png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)
    
    return prediction

@app.post("/api/covid-symptom-chek")  
def check_risk(symptom: Sympton):
    return symptom_chek.get_risk_level(symptom)

if __main__ = "__main__":
    uvicorn.run(app, debug = True)              
