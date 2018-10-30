#coding=utf8
import os
from moviepy.editor import *

L = []
for root, dirs, files in os.walk("iVgWbzbu"):
    files.sort()
    for file in files:
        if os.path.splitext(file)[1] == ".ts":
            file_path = os.path.join(root, file)
            L.append(file_path)

print(L)
index = 0
temp_movie_list = []
while index<=50:
    temp_movie_list = [VideoFileClip(file_path) for file_path in L[index: index+10]]
    print(temp_movie_list)
    temp_movie_slice = concatenate_videoclips(temp_movie_list)
    if os.path.exists("iVgWbzbu/last_slice.mp4"):
        temp_movie_slice.write_videofile("iVgWbzbu/this_slice.mp4")
        merge_slice = concatenate_videoclips(["iVgWbzbu/last_slice.mp4", "iVgWbzbu/this_slice.mp4"])
        os.remove("iVgWbzbu/this_slice.mp4")
        os.remove("iVgWbzbu/last_slice.mp4")
        merge_slice.write_videofile("iVgWbzbu/last_slice.mp4")
    else:
        temp_movie_slice.write_videofile("iVgWbzbu/last_slice.mp4")
    index += 10
# final_movie = concatenate_videoclips(L)
# final_movie.write_videofile("iVgWbzbu/iVgWbzbu_target_movie.mp4")
