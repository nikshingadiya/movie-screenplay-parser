from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi import APIRouter
from typing import List
import pdfplumber
from tempfile import NamedTemporaryFile
import httpx
router= APIRouter()


from extractor.pdf_reader import  extract_text_from_pdf


async def make_post_request(url: str, data: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data)
        return response.text

@router.post("/upload")
async def upload_pdf(files: List[UploadFile] = File(...)):
    if not files:
        return {"error": "No files provided"}
    for uploaded_file in files:
        with NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(await uploaded_file.read())
            tmp_file.close()
            extracted_text = extract_text_from_pdf(tmp_file.name)
    return {"extracted_text": extracted_text}



@router.post("/parse_data/")
async def parse_data(url: str, data: str):
    if not url:
        raise HTTPException(status_code=400, detail="No URL provided")

    response = await make_post_request(url, data)
    return {"response": response}