'''
Configuration centrale de l'application
'''

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"

UPLOAD_DIR.mkdir(exist_ok=True)

MAX_FILE_SIZE_MB = 50
