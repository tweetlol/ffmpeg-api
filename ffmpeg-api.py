from typing import Union

import fastapi
import requests
import subprocess
from pydantic import BaseModel

app = fastapi.FastAPI()

#example method at static endpoint
@app.get("/")
def get_root():
    return {"Response": "Hello world, this is root."}

#example method at variable endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str,None] = None):
    return {"item_id": item_id, "q": q}

#example model definition
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

#example conversion endpoint method with separate args, returns json
@app.get("/example")
def convert_image_to_video(post_id: int, image_url: str, arg2: Union[str,None] = "None"):
    
    #download the image from {image_url}
    img_data = requests.get(image_url).content
    with open('image-to-convert.jpg', 'wb') as file:
        file.write(img_data)
    
    video_url = "dummy-link-to-video"

    return {
        "videoUrl": video_url,
        "incoming_data":{
            "image_url": image_url,
            "arg2": arg2
        }
    }


#CONVERSION ENDPOINT BEGINS HERE
##Post model definition - defines expected json structure
class Post(BaseModel):
    post_id: int
    image_url: str
    arg3: str

##conversion endpoint
##expects Post model json structure as argument (data sent in request)
@app.get("/convert/image-to-video")
def post_convert(payload: Post):

    #runs prepare-dir.sh script with only argument being the directory name = payload.post_id
    subprocess.run(["./prepare-dir.sh", f"{payload.post_id}"])

    #download the image from {image_url}
    img_data = requests.get(payload.image_url).content
    with open(f"converted/{payload.post_id}/{payload.post_id}.jpg", 'wb') as file:
        file.write(img_data)

    #runs ffmpeg-convert.sh script to convert the DLed image to .mp4
    subprocess.run(["./ffmpeg-convert.sh", f"{payload.post_id}"])

    #pass the video file as a response
    return fastapi.responses.FileResponse(f"./converted/{payload.post_id}/{payload.post_id}.mp4")

