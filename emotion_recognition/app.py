from fastapi import FastAPI
from fastapi import UploadFile, File
from fastapi import File
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
import uvicorn

app = FastAPI()

input_shape = (224, 224, 3)

"""
@app.get('/index')
async def hello_world(name: str):
    return f"Hello {name}!"
"""
def load_model():
    model = tf.keras.applications.MobileNetV2(input_shape)
    return model

model = load_model()

@app.post('/api/predict')
async def predict_image(file: bytes = File(...)):
    image = read_image(await file)
    image = preprocess(image)
    predictions = predict(image)
    print(predictions)
    return predictions

def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image

def preprocess(image: Image.Image):
    image = image.resize(input_shape)
    image = np.asfarray(image)
    image = image / 127.5 - 1.0
    image = np.expand_dims(image, 0)
    return image

def predict(image:np.ndarray):
    model.predict(image)

if __name__=="__main__":
    uvicorn.run(app, port = 8081, host='0.0.0.0')