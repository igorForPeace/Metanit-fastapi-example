from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import status


app = FastAPI()


@app.get("/")
def index():
    content = HTMLResponse("<h1>Hello Metanit</h1>", status_code=status.HTTP_200_OK)
    return content