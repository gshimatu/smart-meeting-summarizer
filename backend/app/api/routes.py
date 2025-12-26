from fastapi import APIRouter, UploadFile, File
from app.core.logger import logger
from app.utils.file_handler import save_uploaded_file

router = APIRouter(prefix="/api")

@router.post("/upload")
async def upload_meeting(file: UploadFile = File(...)):
    file_path = save_uploaded_file(file)
    logger.info(f"File saved at {file_path}")
    return {
        "message": "File uploaded successfully",
        "file_path": str(file_path)
    }
