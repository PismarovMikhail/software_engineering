import uvicorn
import numpy as np

from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
from fastapi.exceptions import HTTPException

from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.applications.resnet50 import decode_predictions
from keras.preprocessing import image

from PIL import Image
from io import BytesIO

app = FastAPI(title="ResNet50 Classification App")
model = ResNet50(weights="imagenet")


@app.get("/")
def root():
    """
    The function welcomes the user of the application.
    It is also used to test the availability of the
    application when accessing the server root.
    """
    return {"message": "Hello, dear friend!"}


@app.get("/attetion")
async def pay_attention():
    """
    The function displays a warning to look at the list of classes
    that the ResNet50 network can predict. An attempt to predict another
    class of object will lead to incorrect results.
    """
    return {"message": "See ResNet50 Class List on"
                       "deeplearning.cms.waikato.ac.nz"}


@app.post("/file_properties/")
async def create_image_properties(file: UploadFile):
    """
    The function checks the format and size of the aploaded file (image).
    If the file has weight greater than 10 Mb, a message about the need
    to upload a smaller file is displayed. If the file format is different
    from jpg/jpeg, the message about the necessity to upload a file of
    jpg/jpeg format is displayed.The function also outputs information
    about the file name and its format and size.
    """
    file.file.seek(0, 2)
    file_size = file.file.tell()
    await file.seek(0)
    if file_size > 10000000:
        raise HTTPException(status_code=400,
                            detail="File too large!"
                            "Download file < 10 Mb!")
    content_type = file.content_type
    if content_type not in ['image/jpeg', 'image/jpg']:
        raise HTTPException(status_code=400,
                            detail="Invalid file type!"
                            "Download jpeg/jpg format file!")
    return ({"filename": file.filename},
            {"file_size": file_size},
            {"content_type": content_type})


@app.post("/uploadfile/")
async def predict_image(file: bytes = File(...)):
    """
    The main function that predicts the class of an image.
    """
    image = read_image(file)
    prediction = process_image(image)
    return prediction


def read_image(file) -> Image.Image:
    """
    The funtion reads the received information as a bute stream and
    converts it into a pixel image . 
    """
    pixel_image = Image.open(BytesIO(file))
    return pixel_image


def process_image(file: Image.Image):
    """
    The function performs image pocessing and predicts.
    The prediction results are the names of the three
    best-fit classes with an indicdtion of the prediction
    probability .
    """

    img = np.asarray(file.resize((224, 224)))[..., :3]
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    prediction = model.predict(img)

    print('Predicted:', decode_predictions(prediction, top=3)[0])
    result = decode_predictions(model.predict(img), 3)[0]
    response = []
    for i, res in enumerate(result):
        resp = {}
        resp["class"] = res[1]
        resp["confidence"] = f"{res[2]*100:0.2f} %"

        response.append(resp)

    return response


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')
