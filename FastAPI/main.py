from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routers.router import router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.include_router(router)
app.mount('/static', StaticFiles(directory='static'), 'static')


@app.get("/")
def read_root():
    html_content = ""
    return HTMLResponse(content=html_content)
