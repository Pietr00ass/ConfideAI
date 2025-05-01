from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from ..services.ocr import anonymize_image
import io

router = APIRouter()

@router.post('/anonymize')
def api_ocr(file: UploadFile = File(...)):
    try:
        img_bytes = anonymize_image(file)
        return StreamingResponse(io.BytesIO(img_bytes), media_type='image/png')
    except Exception as e:
        raise HTTPException(400, str(e))
