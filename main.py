from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status


app = FastAPI()


@app.get("/")
def index():
    content = HTMLResponse("<h1>Hello Metanit</h1>", status_code=status.HTTP_200_OK)
    return {"message": "Hello metanit"}


@app.get("/about")
def about():
    data = {"message": "Hello from about page", "data": "Some data from page about"}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data, status_code=status.HTTP_200_OK)