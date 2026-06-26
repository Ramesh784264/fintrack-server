from fastapi import FastAPI, File, UploadFile
# from typing import List

app = FastAPI()

@app.get("/")
def view():
    return {"message": "Hello World"}

# ONLY FILE NAME READ

@app.post("/upload-read")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }