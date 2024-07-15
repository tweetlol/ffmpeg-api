from typing import Union

import fastapi
import requests
import subprocess

app = fastapi.FastAPI()

#example method at static endpoint
@app.get("/")
def get_root():
    return {"Response": "Hello world, this is root."}

#example method at variable endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str,None] = None):
    return {"item_id": item_id, "q": q}

#conversion endpoint GET method
@app.get("/convert/image-to-video/")
def convert_image_to_video(image_link: Union[str,None] = None, arg2: str = ""):
    
    img_data = requests.get(image_link).content
    with open('image-to-convert.jpg', 'wb') as file:
        file.write(img_data)

    

    video_url = "dummy-link-to-video"

    return {
        "videoUrl": video_url,
        "incoming_data":{
            "image_link": image_link,
            "arg2": arg2
        }
    }

