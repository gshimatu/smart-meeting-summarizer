from app.services.transcription import TranscriptionService

transcription_service = TranscriptionService()

# Charger Whisper une seule fois et l'évite de recharger Whisper à chaque requête
