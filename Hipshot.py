#!/usr/bin/env python2

'''Simulate long-exposure photography

Hipshot converts a video file into a single image file simulating
a long-exposure photograph.
'''


import cv
try:
    from os import EX_DATAERR as _EX_DATAERR
    from os import EX_NOINPUT as _EX_NOINPUT
    from os import EX_USAGE as _EX_USAGE
except ImportError:
    _EX_DATAERR, _EX_NOINPUT, _EX_USAGE = 1, 2, 3
from os.path import exists
from sys import argv as _argv, exit as _exit, stderr as _stderr
from sys import float_info as _float_info

import cvutils


__author__ = 'Mansour Moufid'
__copyright__ = 'Copyright 2013, Mansour Moufid'
__license__ = 'ISC'
__version__ = '0.2'
__email__ = 'mansourmoufid@gmail.com'
__status__ = 'Development'


def _fail(code):
    print>>_stderr, 'usage: Hipshot.py <file> [alpha]'
    _exit(code)


def merge(frames, alpha, display=None):
    '''Average a list of frames with a weight factor of alpha,
    and optionally display the process in an OpenCV NamedWindow.
    '''
    acc = None
    for frame in frames:
        if not acc:
            acc = cvutils._template_image(frame, cv.IPL_DEPTH_32F)
        cv.RunningAvg(frame, acc, alpha)
        if display:
            cv.ShowImage(display, acc)
            k = cv.WaitKey(1)
            if k == ord('q'):
                break
            elif k == ord('z'):
                cv.SetZero(acc)
            elif k == ord('s'):
                print cvutils._save_image(acc, file, random=True)
    return acc


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
        if (alpha <= 10.0 * _float_info.epsilon or
                alpha >= 1.0 - 10.0 * _float_info.epsilon):
            _fail(_EX_USAGE)
    else:
        _fail(_EX_USAGE)

    try:
        alpha
    except NameError:
        alpha = 5e-3 / cvutils.num_frames(file)

    try:
        frames = cvutils.get_frames(file, as_array=False)
        cv.NamedWindow('Hipshot', flags=cv.CV_WINDOW_AUTOSIZE)
        long_exp_img = merge(frames, alpha, display='Hipshot')
        print cvutils._save_image(long_exp_img, file, random=True)
    except IOError:
        _exit(_EX_DATAERR)
