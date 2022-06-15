from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
from pytube import YouTube
import random
import os
import sys
import re


#commandLine: Video Length, Number Of Cuts, Urls...

# if len(sys.argv)<2: 
# 	exit(1)

# if not re.search('/^\d+$/',sys.argv[0]): 
# 	print("Please provide an integer video length")
# 	exit(1)

# finalVideoLength = int(sys.argv[0])
# print(finalVideoLength)
finalVideoLength = 100

# if not re.search("/^\\d+$/",sys.argv[1]): 
# 	print("Please provide an integer for number of cuts / clips")
# 	exit(1)

# numClips = int(sys.argv[2])
# print(numClips)
numClips = 50

# if not re.search("/https?:\\/\\/(www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{2,256}\\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\\+.~#()?&//=]*)/",sys.argv[1]): 
# 	print("Please provide at least one YouTube url")
# 	exit(1)

# subVideos = []

# for i in range(2,len(sys.argv)):
# 	subVideos.append(sys.argv[i])
# print(subVideos)

videoURL1 = "https://www.youtube.com/watch?v=IUN664s7N-c"
videoURL2 = "https://www.youtube.com/watch?v=Cl_kXbhTi8k"
videoURL3 = "https://www.youtube.com/watch?v=AA3bJ74uIPI"
videoURL4 = "https://www.youtube.com/watch?v=G5RpJwCJDqc"
videoURL5 = "https://www.youtube.com/watch?v=bVkZgH-iDlo"
subVideos = [videoURL1,videoURL2,videoURL3,videoURL4,videoURL5]


path = "/Users/sahilbambulkar/Desktop/videos/"

videoLengths = []
clips = []
for i,url in enumerate(subVideos):

	my_video = YouTube(url)

	print("Downloading ", end='')
	print(my_video.title, end='...\n')

	print("Video Length (seconds) ", end='')
	print(my_video.length,end='...\n') #in seconds

	videoLen = my_video.length
	videoLengths.append(videoLen)
	my_video = my_video.streams.get_highest_resolution()
	my_video.download(path,f"{i}.mp4")


# eachVidLen = finalVideoLength//len(subVideos)


currClip = 0
eachVidLen = finalVideoLength//10

clips = []
i = 0 

while currClip<numClips:
	currClip+=1
	videoLen = videoLengths[i]
	start = random.randint(0,videoLen-eachVidLen)
	end = start + eachVidLen
	fileName = f"{i}.mp4"
	fileName = path + fileName
	clip = VideoFileClip(fileName).subclip(start,end)
	clips.append(clip)
	i = (i+1) % len(subVideos)

combined = concatenate_videoclips(clips)
combined.write_videofile(path+"finalVideo.mp4")


##clean-up
for i,url in enumerate(subVideos):
	fileName = f"{i}.mp4"
	fileName = path + fileName
	os.remove(fileName)
