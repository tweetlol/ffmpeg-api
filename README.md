# ffmpeg-api

run with

```sh
fastapi run ffmpeg-api.py
fastapi dev ffmpeg-api.py
```

after hosting, api documentation can be accessed at an endpoint

```sh
localhost:8000/docs
```

example usage

```sh
curl -X 'GET' \
  'http://localhost:8000/convert/image-to-video' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "post_id": 787878,
  "image_url": "https://uploads-ssl.webflow.com/663134cb541be68ddf54b115/668fb01f38d3656e032a9e90_AJQWtBNnOwq_Om7ltjJ6Pp9uvL0vtuGWW7qedsLuchMlMuKAQNtIySXg_DaNoCW0p-CV9MougjOVsRBCUWDyjFBzUgAQmMu4P1XPgAaJ2LLM8fPmcw.jpeg"
}'
```

the api returns a video file

requirements:

```sh
pip install fastapi requests
```

.sh scripts are called from the .py process during runtime
