import wave
import pyaudio
import sys
import argparse

CHUNK = 1024

def audioPlayer(filename):

	global CHUNK
	
	with wave.open(filename, "rb") as wf:
		Pl = pyaudio.PyAudio()

		stream = Pl.open(format = Pl.get_format_from_width(wf.getsampwidth()), 
						channels = wf.getnchannels(),
						rate = wf.getframerate(),
						output = True)

		while len(data := wf.readframes(CHUNK)):
			stream.write(data)

		stream.close()
		Pl.terminate()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = "Program for play audio files(.wav and others)")
	parser.add_argument("--file", dest = "filename", required = True)
	arguments = parser.parse_args()
	filename = arguments.filename
	audioPlayer(filename)