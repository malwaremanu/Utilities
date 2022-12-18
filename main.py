import base64
import io

from fastapi import FastAPI
from pydantic import BaseModel
from qrcode import make
from qrcode.constants import ERROR_CORRECT_L

app = FastAPI()

class QrCodeRequest(BaseModel):
    url: str

def generate_qr_code(url: str) -> str:
    img = make(url, error_correction=ERROR_CORRECT_L)
    with io.BytesIO() as buffer:
        img.save(buffer, "PNG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")

@app.post("/qr-code")
def generate_qrr_code(request: QrCodeRequest):
    qr_code = generate_qr_code(request.url)
    #qr_code = generate_qr_code("https://www.google.com")
    return {"qr_code": qr_code}
