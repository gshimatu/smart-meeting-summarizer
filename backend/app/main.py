from fastapi import FastAPI
from app.api.routes import router
from app.core.logger import logger

app = FastAPI(
    title="SmartMeeting Summarizer API",
    description="API for meeting transcription and summarization",
    version="0.1.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    logger.info("Health check called")
    return {"status": "ok"}
