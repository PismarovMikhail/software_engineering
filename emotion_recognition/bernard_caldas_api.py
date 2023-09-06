import uvicorn
import numpy as np
import tensorflow

from fastapi import FastAPI 
from fastapi import File
from fastapi import UploadFile 
from fastapi.exceptions import HTTPException

from tensorflow import keras
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.applications.resnet50 import decode_predictions
from keras.preprocessing import image

from PIL import Image
from io import BytesIO


app = FastAPI(title = "ResNet50 Classification App")


model = ResNet50(weights='imagenet')


@app.get("/comments")
async def pay_attension():
    return {"message": "See ResNet50 Class List on deeplearning.cms.waikato.ac.nz"}


@app.post("/file_properties/")
async def create_image_properties(file: UploadFile):
    
    file.file.seek(0, 2)
    file_size = file.file.tell()
    
    await file.seek(0)
    
    if file_size > 10000000:
        raise HTTPException(status_code = 400, detail = "File too large! Download file < 10 Mb!")
     
    content_type = file.content_type
    if content_type not in ['image/jpeg', 'image/jpg']:
        raise HTTPException(status_code = 400, detail = "Invalid file type! Download jpeg/jpg format file!")

    return {"filename": file.filename}, {"file_size": file_size} , {"content_type": content_type}
 

@app.post("/uploadfile/")
async def predict_image(file: bytes = File(...)):
    
    # read image
    image = read_image(file)
    # transform and prediction 
    prediction = process_image(image)   

    return prediction


def read_image(file) -> Image.Image:
    pixel_image = Image.open(BytesIO(file))
    #print('print dentro da funcao --- ok ')
    return pixel_image


def process_image(file: Image.Image):

    #img_path = 'image3.jpeg'
    #img = image.load_img(file, target_size=(224, 224))
    img = np.asarray(file.resize((224, 224)))[..., :3]
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    prediction = model.predict(img)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
    #result = {}
    print('Predicted:', decode_predictions(prediction, top = 3 )[0])
    #result = decode_predictions(preds, top=3)[0]
    result = decode_predictions(model.predict(img), 3)[0]
    
    response = []
    for i, res in enumerate(result):
        resp = {}
        resp["class"] = res[1]
        resp["confidence"] = f"{res[2]*100:0.2f} %"

        response.append(resp)

    return response

if __name__=="__main__":
    uvicorn.run(app, port = 8000, host='0.0.0.0')