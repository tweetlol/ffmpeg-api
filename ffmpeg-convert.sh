#!/bin/bash

#converts image to video
#arg1 = post_id
ffmpeg -loop 1 -i ./converted/$1/$1.jpg -c:v libx264 -t 5 -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" -pix_fmt yuv420p ./converted/$1/$1.mp4 -y
