from fastapi import APIRouter, UploadFile, File
from app.core.logger import logger
from app.utils.file_handler import save_uploaded_file
from pathlib import Path
from app.services import transcription_service

router = APIRouter(prefix="/api")

@router.post("/upload")
async def upload_meeting(file: UploadFile = File(...)):
    file_path = save_uploaded_file(file)
    logger.info(f"File saved at {file_path}")
    return {
        "message": "File uploaded successfully",
        "file_path": str(file_path)
    }

@router.post("/transcribe")
async def transcribe_meeting(file: UploadFile = File(...)):
    file_path = save_uploaded_file(file)

    if file_path.suffix == ".txt":
        text = file_path.read_text(encoding="utf-8")
        return {"transcription": text}

    transcription = transcription_service.transcribe(file_path)

    return {
        "message": "Transcription completed",
        "transcription": transcription
    }