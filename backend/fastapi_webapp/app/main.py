from fastapi import FastAPI, File, UploadFile
from routers.server import router

app = FastAPI()
app.include(router)


