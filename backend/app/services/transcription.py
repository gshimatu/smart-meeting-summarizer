import whisper
from pathlib import Path
from app.core.logger import logger

class TranscriptionService:
    def __init__(self, model_size: str = "base"):
        logger.info("Loading Whisper model...")
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path: Path) -> str:
        logger.info(f"Starting transcription for {audio_path}")
        result = self.model.transcribe(str(audio_path))
        return result["text"]
