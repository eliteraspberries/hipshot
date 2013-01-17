#!/usr/bin/env python

import cv
try:
    from os import EX_DATAERR, EX_NOINPUT, EX_USAGE
except ImportError:
    EX_DATAERR, EX_NOINPUT, EX_USAGE = 1, 2, 3
from os.path import basename, exists, splitext
from random import randint
from sys import argv, exit, float_info, stderr

def TemplateImage(image, depth):
    size = (image.width, image.height)
    channels = image.nChannels
    dup = cv.CreateImage(size, depth, channels)
    return dup

def SaveImage(image, file):
    while True:
        newfile = splitext(file)[0] + '-'
        newfile = newfile + str(randint(0,1000)) + '.png'
        if not exists(newfile):
            break
    newimage = TemplateImage(image, cv.IPL_DEPTH_8U)
    cv.ConvertScaleAbs(image, newimage, scale = 255)
    cv.SaveImage(newfile, newimage)
    return

def fail(code):
    print>>stderr, 'usage: Hipshot.py <file> [alpha]'
    exit(code)

if '__main__' in __name__:
    if len(argv) == 2:
        file = argv[1]
        if not exists(file):
            exit(EX_NOINPUT)
    elif len(argv) == 3:
        file = argv[1]
        try:
            alpha = float(argv[2])
        except ValueError:
            fail(EX_USAGE)
        if alpha <= 10.0 * float_info.epsilon or \
            alpha >= 1.0 - 10.0 * float_info.epsilon:
            fail(EX_USAGE)
    else:
        fail(EX_USAGE)

    cap = cv.CaptureFromFile(file)
    if not cap:
        exit(EX_DATAERR)
    img = cv.QueryFrame(cap)
    if not img:
        exit(EX_DATAERR)
    acc = TemplateImage(img, cv.IPL_DEPTH_32F)

    cv.NamedWindow('Hipshot', flags = cv.CV_WINDOW_AUTOSIZE)

    n = cv.GetCaptureProperty(cap, cv.CV_CAP_PROP_FRAME_COUNT)
    n = int(n)
    try:
        alpha
    except NameError:
        alpha = 5e-3 / n
    for i in xrange(1, n):
        cv.ShowImage('Hipshot', acc)
        k = cv.WaitKey(1)
        if k == ord('q'):
            break
        elif k == ord('z'):
            cv.SetZero(acc)
        elif k == ord('s'):
            SaveImage(acc, file)
        img = cv.QueryFrame(cap)
        if not img:
            break
        cv.RunningAvg(img, acc, alpha)

    SaveImage(acc, file)
