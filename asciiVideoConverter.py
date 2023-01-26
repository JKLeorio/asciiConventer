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
		aimg = "\n".join(convertImageToAscii(pimg, w = 4, scale = 2.22, moreLevels = False))
		with open(f"{dirname}\\{frame_id}.txt", "w") as file:
			file.write(aimg+"\n")
		frame_id+=1

	video.release()


def main():
	parser = argparse.ArgumentParser(description = "Program for Converting video")
	parser.add_argument("--file", dest = "filename", required = True)
	parser.add_argument("--dir", dest = "dirname", required = True)
	arguments = parser.parse_args()
	filename = arguments.filename
	dirname = arguments.dirname
	convertVideoToAscii(filename, dirname)


if __name__ == '__main__':
    main()