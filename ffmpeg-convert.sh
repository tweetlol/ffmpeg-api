#!/bin/bash

ffmpeg -loop 1 -i /home/filip/Desktop/one-click-hello/ffmpeg-api/testcat.jpg -c:v libx264 -t 4 -pix_fmt yuv420p output.mp4
