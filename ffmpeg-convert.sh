#!/bin/bash

#converts image to video
#arg1 = post_id
ffmpeg -loop 1 -i ./converted/$1/$1.jpg -c:v libx264 -t 5 -pix_fmt yuv420p ./converted/$1/$1.mp4 -y
