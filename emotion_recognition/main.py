import uvicorn
import keras
import numpy as np
import tensorflow
from fastapi import FastAPI
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing import image



from fastapi import File
from fastapi import UploadFile




#from tensorflow.keras.applications.imagenet_utils import decode_predictions

from application.component import predict
from application.component import read_imagefile


app = FastAPI()

input_shape = (48, 48, 3)
classes = 7

# classes = ['angry', disgust, 'fear', 'happy', 'neutral', 'sad', 'surpruse']


def load_model():
    model = tensorflow.keras.applications.VGG16(input_shape = input_shape, 
                                                classes = classes, 
                                                include_top = False,
                                                weights="imagenet",
                                                )
    
    print("Model loaded")
    return model

model = load_model()

def create_image_to_array(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)

def predict_image_class():
#"""
#comments
#"""
    prediction = VGG16.predict(x)
    prediction = np.argmax(prediction[0])
    score = prediction[0]
    print("Class number:", prediction)
    print("Class name", classes[prediction])
    print("Probability", score)
    
    return  prediction, score
     



"""
def predict (image: Image.Image):
    
    image = np.asarray(image.resize((224.224[...])))]
    image = np.expand_dims(image, 0)
    image = image / 127.5
    
    result = decode_predictions(model.predict(image), 2) [0]
    
    response = []
    
    for i, res in enumerate(result):
        resp = {}
        resp["class"] = res[1]
        resp["confidence"] = f"{res[2] *100:0.2f}%"
        
        response.append(resp)
        
    return response    

"""


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
