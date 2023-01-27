import sys
import os
import time
import timeit
import subprocess
import argparse

import cv2

from pathlib import Path


def asciiVideoPlayer(dirname, filename, audiofile, fps = 30):
    dpath = Path(dirname)

    if dpath.exists():
        tdir = sorted([file for file in dpath.iterdir()], key = lambda f : int(f.stem))
        frame = tdir[0]
        with frame.open() as f:
            fdata = f.readlines()
            rows = len(fdata)
            cols = len(fdata[0])

        os.system(f"mode con: cols={cols} lines={rows}")



        vfile = cv2.VideoCapture(filename)

        audiofilename = str(audiofile.parent) + "/" + '"'+ audiofile.name + '"' if len(str(audiofile).split()) > 1 else str(audiofile.parent) + "/" + audiofile.name
        
        os.system("cls")
        for i in range(1,4):
            print(f"{i}...")
            time.sleep(0.5)


        subprocess.Popen((f'python PlayAudio.py --file {audiofilename}'), shell = True, stdout = subprocess.PIPE)
        
        time.sleep(0.22)

        timing = (1/fps)


        window_name = "bad apple"

        cv2.namedWindow(window_name)
        cv2.moveWindow(window_name, 900, 50)

        t1 = time.perf_counter()
        t2 = 0
        fpsi = str(fps)

        ProgramTime = time.perf_counter()

        timer = 1



        for file in tdir:


            with file.open() as tfile:

                data = tfile.read()
                
                ret, frame = vfile.read()

                # imH, imW, b = frame.shape

                # imdim = (int(imW/3), int(imH/3))

                # res_frame = cv2.resize(frame, imdim)

                cv2.putText(frame, fpsi , (7, 70) , cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 255, 0), 3, cv2.LINE_AA)

                while time.perf_counter() - timer < timing:
                    pass

                t1 = time.perf_counter()

                fpsi = str(round(1/(t1-t2)))
                t2 = t1


                timer = time.perf_counter()


                cv2.imshow(window_name, frame)

                sys.stdout.write(data)
                if cv2.waitKey(1) == ord("q"):
                    break


        print(f"Time - {time.perf_counter()-ProgramTime}")

    else:
        print("this dir is not exists")
    vfile.release()
    cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(description = "Program for Playing video")
    parser.add_argument("--dir", dest = "dirname", required = True)
    parser.add_argument("--vfile", dest = "videofilename", required = True)
    parser.add_argument("--afile", dest = "audiofilename", required = True, type = Path)
    arguments = parser.parse_args()
    dirname = arguments.dirname
    filename = arguments.videofilename
    audiofile = arguments.audiofilename
    asciiVideoPlayer(dirname, filename, audiofile)

if __name__ == '__main__':
    main()