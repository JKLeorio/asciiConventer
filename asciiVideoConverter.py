import os
import sys
from pathlib import Path
import cv2
import argparse

from PIL import Image
from asciiImageConverter import convertImageToAscii


def convertVideoToAscii(filename, dirname):
	video = cv2.VideoCapture(filename)
	if not Path(f"{dirname}/").exists():
		os.mkdir(dirname)

	frame_id = 1
	while video.isOpened():

		ret , frame = video.read()
		print(frame_id)
		if not ret:
			break
		img = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
		pimg = Image.fromarray(img)
		aimg = "\n".join(convertImageToAscii(pimg, w = 6, scale = 2.22, moreLevels = False))
		with open(f"{dirname}\\{frame_id}.txt", "w") as file:
			file.write(aimg+"\n")
		frame_id+=1

	video.release()


def main():
	convertVideoToAscii("files/NicoNico Douga - Bad Apple.mp4", "badappleascii")


if __name__ == '__main__':
    main()