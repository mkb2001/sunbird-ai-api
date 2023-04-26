from fastapi import APIRouter, HTTPException, status, File, UploadFile, Form
from app.models.tasks import STTTranscript, TranslationRequest, TranslationResponse
from app.inference_services.stt_inference import transcribe
from app.inference_services.translate_inference import translate

router = APIRouter()


@router.post("/stt")
async def speech_to_text(
        audio: UploadFile(...) = File(...),
        language: str = Form("Luganda"),
        return_confidences: bool = Form(False)) -> STTTranscript:  # TODO: Make language an enum

    response = transcribe(audio)
    return STTTranscript(text=response)

@router.post("/translate", response_model=TranslationResponse)
async def translate_(translation_request: TranslationRequest):

    response = translate(translation_request.text, translation_request.source_language, translation_request.target_language)
    return TranslationResponse(text=response)
