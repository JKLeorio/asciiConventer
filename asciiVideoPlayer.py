import sys
import os
import time
import timeit
import subprocess

import cv2

from pathlib import Path


def asciiVideoPlayer(dirname, fps = 30):
    dpath = Path(dirname)
    if dpath.exists():
        tdir = sorted([file for file in dpath.iterdir()], key = lambda f : int(f.stem))
        frame = tdir[0]
        with frame.open() as f:
            fdata = f.readlines()
            rows = len(fdata)
            cols = len(fdata[0])

        os.system(f"mode con: cols={cols} lines={rows}")



        vfile = cv2.VideoCapture("files\\NicoNico Douga - Bad Apple.mp4")


        os.system("cls")
        for i in range(1,4):
            print(f"{i}...")
            time.sleep(0.5)

        subprocess.Popen(('python PlayAudio.py --file files/"NicoNico Douga - Bad Apple.wav"'), shell = True, stdout = subprocess.PIPE)
        
        # timing = (1/fps) * 0.903
        timing = (1/fps) * 0.6

        window_name = "bad apple"

        cv2.namedWindow(window_name)
        cv2.moveWindow(window_name, 960, 50)

        t1 = 0
        t2 = 0
        fpsi = None

        ProgramTime = time.time()

        for file in tdir:
            timer = time.time()

            t1 = time.time()

            with file.open() as tfile:

                data = tfile.read()
                ret, frame = vfile.read()
                imW, imH, b = frame.shape
                imdim = (int(imH/3), int(imW/3))
                res_frame = cv2.resize(frame, imdim)

                fpsi = str(int(1/(t1-t2)))

                t2 = t1

                cv2.putText(res_frame, fpsi , (7, 70) , cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)

                cv2.imshow(window_name, res_frame)
                sys.stdout.write(data)
                if cv2.waitKey(1) == ord("q"):
                    break

            # t = time.time() - timer
            # if t < timing:
            #     time.sleep(timing - t)
            # timer = time.time()


                # os.system("cls")
                # time.sleep(0.024)

            while time.time() - timer < timing:
                pass

        print(f"Time - {time.time()-ProgramTime}")

    else:
        print("this dir is not exists")
    vfile.release()
    cv2.destroyAllWindows()


def main():
    asciiVideoPlayer("badappleascii")

if __name__ == '__main__':
    main()