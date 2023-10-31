from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from apply_filter import process_image, normalizeVector
import io
import cv2


app = FastAPI()



@app.get("/")
async def defaultRoute():

    return {
        "message": "Default Route",
        "status": 200
    }

@app.post("/process_image/")
async def upload_image(file: UploadFile):
    processed_data = process_image(file.file)

    b,g,r=cv2.split(processed_data[0])
    b=normalizeVector(b)
    g=normalizeVector(g)
    r=normalizeVector(r)
    
    img_save=cv2.merge([r,g,b])

    res, im_png = cv2.imencode(".png", processed_data[0])

    print(res, im_png)

    return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
