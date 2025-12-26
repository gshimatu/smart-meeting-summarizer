from fastapi import UploadFile, HTTPException
from pathlib import Path
from app.core.config import UPLOAD_DIR, MAX_FILE_SIZE_MB

ALLOWED_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".m4a",
    ".mpeg",
    ".txt"
}



def save_uploaded_file(file: UploadFile) -> Path:
    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="File type not supported")

    file_path = UPLOAD_DIR / file.filename

    content = file.file.read()
    size_mb = len(content) / (1024 * 1024)

    if size_mb > MAX_FILE_SIZE_MB:
        raise HTTPException(status_code=400, detail="File too large")

    with open(file_path, "wb") as f:
        f.write(content)

    return file_path
