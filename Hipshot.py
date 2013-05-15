#!/usr/bin/env python2
# Copyright 2013, Mansour Moufid <mansourmoufid@gmail.com>

import cv
try:
    from os import EX_DATAERR as _EX_DATAERR
    from os import EX_NOINPUT as _EX_NOINPUT
    from os import EX_USAGE as _EX_USAGE
except ImportError:
    _EX_DATAERR, _EX_NOINPUT, _EX_USAGE = 1, 2, 3
from os.path import basename, exists, splitext
from random import randint
from sys import argv as _argv, exit as _exit, stderr as _stderr
from sys import float_info as _float_info

def _template_image(image, depth):
    size = (image.width, image.height)
    channels = image.nChannels
    dup = cv.CreateImage(size, depth, channels)
    return dup

def _save_image(image, file):
    while True:
        newfile = splitext(file)[0] + '-'
        newfile = newfile + str(randint(0,1000)) + '.png'
        if not exists(newfile):
            break
    newimage = _template_image(image, cv.IPL_DEPTH_8U)
    cv.ConvertScaleAbs(image, newimage, scale = 255)
    cv.SaveImage(newfile, newimage)
    return

def _fail(code):
    print>>_stderr, 'usage: Hipshot.py <file> [alpha]'
    _exit(code)

def num_frames(video_file):
    cap = cv.CaptureFromFile(video_file)
    if not cap:
        _exit(_EX_DATAERR)
    n = cv.GetCaptureProperty(cap, cv.CV_CAP_PROP_FRAME_COUNT)
    return int(n)

def get_frames(video_file):
    cap = cv.CaptureFromFile(video_file)
    if not cap:
        _exit(_EX_DATAERR)
    i = 0
    while i < num_frames(video_file):
        img = cv.QueryFrame(cap)
        if not img:
            break
        yield img
        i += 1

if '__main__' in __name__:
    if len(_argv) == 2:
        file = _argv[1]
        if not exists(file):
            _exit(_EX_NOINPUT)
    elif len(_argv) == 3:
        file = _argv[1]
        if not exists(file):
            _exit(_EX_NOINPUT)
        try:
            alpha = float(_argv[2])
        except ValueError:
            _fail(_EX_USAGE)
        if alpha <= 10.0 * _float_info.epsilon or \
            alpha >= 1.0 - 10.0 * _float_info.epsilon:
            _fail(_EX_USAGE)
    else:
        _fail(_EX_USAGE)

    frames = get_frames(file)

    cv.NamedWindow('Hipshot', flags = cv.CV_WINDOW_AUTOSIZE)

    try:
        alpha
    except NameError:
        alpha = 5e-3 / num_frames(file)
    acc = None
    for frame in frames:
        if not acc:
            acc = _template_image(frame, cv.IPL_DEPTH_32F)
        cv.ShowImage('Hipshot', acc)
        k = cv.WaitKey(1)
        if k == ord('q'):
            break
        elif k == ord('z'):
            cv.SetZero(acc)
        elif k == ord('s'):
            _save_image(acc, file)
        cv.RunningAvg(frame, acc, alpha)

    _save_image(acc, file)
