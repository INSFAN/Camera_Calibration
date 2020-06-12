
import argparse
import logging
import os

import numpy as np
import time

import cv2

def parse_args():
    # Parse arguments
    parser = argparse.ArgumentParser(description='get camera cailbrate images')
    parser.add_argument('--save_path', default='./sreen_camera_cail_imgs/', help='path to save images')
    # parser.add_argument('--save_path', default='./sreen_camera_cail_imgs/', help='path to save images')
    args=parser.parse_args()
    logging.debug(args)
    return args

def main(args):

    cap = cv2.VideoCapture(0)
    cnt = 1
    t0 = time.clock()
    while True:
        ret, img = cap.read()
        if not ret:
            print('not input images')
            break
        cv2.imshow('img', img)
        dt = time.clock() - t0
        if dt >= 5:
            print ('3 s later save img')
        if (dt >= 8):
            # outfile = os.path.join(args.save_path, str(cnt) + '_chess.png')
            outfile = os.path.join(args.save_path, str(cnt) + '_sreen_camera.png')
            cv2.imwrite(outfile, img)
            print('saved no.%d img'%(cnt))
            cnt += 1
            t0 = time.clock()
        
        elif (cv2.waitKey(10) == ord('q') or cnt == 15):
            break


if __name__ == "__main__":
    args = parse_args()
    main(args)