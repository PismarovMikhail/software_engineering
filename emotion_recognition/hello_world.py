from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/index')
def hello_world():
    return "Hello! World"

if __name__=="__main__":
    uvicorn.run(app, port = 8082, host='0.0.0.0')