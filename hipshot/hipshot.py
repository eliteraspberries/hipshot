#!/usr/bin/env python2

'''Hipshot converts a video file into a single image
simulating a long-exposure photograph.
'''

import cv

from avena import ocv


__author__ = 'Mansour Moufid'
__copyright__ = 'Copyright 2013, 2014, Mansour Moufid'
__license__ = 'ISC'
__version__ = '0.4.2'
__email__ = 'mansourmoufid@gmail.com'
__status__ = 'Development'


_EXT = '.png'


def merge(file, alpha, display=None):
    '''Average the frames of a file with a weight of alpha,
    optionally display the process in an OpenCV NamedWindow.
    '''
    acc = None
    frames = ocv.get_frames(file, as_array=False)
    for frame in frames:
        if not acc:
            acc = ocv._template_image(frame, cv.IPL_DEPTH_32F)
        cv.RunningAvg(frame, acc, alpha)
        if display:
            cv.ShowImage(display, acc)
            k = cv.WaitKey(1)
            k = k & 255
            if k == ord('q'):
                break
            elif k == ord('z'):
                cv.SetZero(acc)
            elif k == ord('s'):
                print ocv._save_image(acc, file, random=True, ext=_EXT)
    return ocv._save_image(acc, file, random=True, ext=_EXT)


if __name__ == '__main__':
    pass
