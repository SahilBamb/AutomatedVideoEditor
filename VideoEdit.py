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

mainVideoURL = "https://www.youtube.com/watch?v=0ZQAxWCuUoc"
mainVideoMinimum = 5


videoURL1 = "https://www.youtube.com/watch?v=0raJ1-1BJ7s"
videoURL2 = "https://www.youtube.com/watch?v=1MiZ685Tv6k"
videoURL3 = "https://www.youtube.com/watch?v=KMiwORlwUVw"
subVideos = [videoURL1,videoURL2,videoURL3]

path = "/Users/sahilbambulkar/Desktop/videos/"

videoLengths = []
clips = []

for i,url in enumerate(subVideos):

	fileName = f"{i}.mp4"
	my_video = YouTube(url)

	print("Downloading ", end='')
	print(my_video.title, end='...\n')

	print("Video Length (seconds) ", end='')
	print(my_video.length) #in seconds
	
	videoLen = my_video.length
	videoLengths.append(videoLen)

	if not os.path.exists(path+fileName):
		my_video = my_video.streams.get_highest_resolution()
		my_video.download(path,f"{i}.mp4")



	#else:

	# print(path+fileName,end=' ')
	# print('already downloaded')


# eachVidLen = finalVideoLength//len(subVideos)
if not os.path.exists(path+'main.mp4'):
	my_video = YouTube(mainVideoURL)
	mainvideoLen = my_video.length
	my_video = my_video.streams.get_highest_resolution()
	my_video.download(path,"main.mp4")

mainvideoLen = 186


currClip = 0
eachVidLen = finalVideoLength//numClips

clips = []
i = 0 

mainIdx = 0

fileName = path + "main.mp4"
clip = VideoFileClip(fileName).subclip(mainIdx,mainIdx+mainVideoMinimum)
clips.append(clip)

while currClip<numClips:
	currClip+=1
	videoLen = videoLengths[i]
	start = random.randint(0,videoLen-eachVidLen)
	end = start + eachVidLen
	fileName = f"{i}.mp4"
	fileName = path + fileName
	clip = VideoFileClip(fileName).subclip(start,end)
	clips.append(clip)
	

	if mainIdx<mainvideoLen:
		mainIdx += eachVidLen
		fileName = path + "main.mp4"
		endMain = mainIdx+mainVideoMinimum if mainIdx+mainVideoMinimum<mainvideoLen else mainvideoLen
		clip = VideoFileClip(fileName).subclip(mainIdx,endMain)
		mainIdx = endMain
		clips.append(clip)

	i = (i+1) % len(subVideos)

# if mainIdx<mainvideoLen:
# 	fileName = path + "main.mp4"
# 	clip = VideoFileClip(fileName).subclip(mainIdx,mainvideoLen)
# 	clips.append(clip)


combined = concatenate_videoclips(clips)
combined.write_videofile(path+"finalVideo.mp4")

#clean-up
for i,url in enumerate(subVideos):
	fileName = f"{i}.mp4"
	fileName = path + fileName
	os.remove(fileName)
