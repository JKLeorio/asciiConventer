import cv2 
import os
import sys
import argparse
from moviepy.video.io.ffmpeg_tools import ffmpeg_resize


def resizeVideo(Videofilename, output):

	vfile = cv2.VideoCapture(Videofilename)
	if not vfile.isOpened():
		exit()

	ret , frame = vfile.read()

	imH, imW, b = frame.shape

	imdim = (int(imW/3), int(imH/3))

	ffmpeg_resize(Videofilename, output, imdim)

	vfile.release()

if __name__ == '__main__':

	descStr = "This program resize an video into new video"
	parser = argparse.ArgumentParser(description=descStr)
	parser.add_argument('--vf', dest='videofilename', required=True)
	parser.add_argument('--outfile', dest='outfilename', required=True)
	arguments = parser.parse_args()
	videofilename = arguments.videofilename
	outfilename  = arguments.outfilename
	resizeVideo(videofilename, outfilename)