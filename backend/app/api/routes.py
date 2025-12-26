from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.logger import logger

router = APIRouter(prefix="/api")

@router.post("/upload")
async def upload_meeting(file: UploadFile = File(...)):
    logger.info(f"File received: {file.filename}")
    return {"message": "File uploaded successfully"}
