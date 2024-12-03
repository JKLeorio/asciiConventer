import os
import sys
from moviepy import VideoFileClip
from pathlib import Path
import argparse


def Separate_audio_from_video(Videofilename, dirname , outfile_type = "wav"):
	path = Path(Videofilename)
	filename, pref = os.path.splitext(path.name)

	video = VideoFileClip(Videofilename)
	video.audio.write_audiofile(f"{dirname}\\{filename}.{outfile_type}")

if __name__=="__main__":
	desc = "This program Separate audio from video"
	parser = argparse.ArgumentParser(description = desc)
	parser.add_argument("--vf", dest = "videoFile", required = True)
	parser.add_argument("--dir", dest = "dirnameForOut", required = True)
	parser.add_argument("--type", dest = "filetype", required = False)
	arguments = parser.parse_args()
	videoFile = arguments.videoFile
	dirname = arguments.dirnameForOut
	filetype = "wav"
	if arguments.filetype is not None:
		filetype = arguments.filetype

	Separate_audio_from_video(videoFile, dirname, filetype)