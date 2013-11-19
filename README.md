Hipshot converts a video file into a single image
simulating a long-exposure photograph.


Installation
============

Hipshot requires:

  - Python 2;
  - docopt;
  - NumPy;
  - the FFMPEG libraries; and
  - OpenCV and its Python bindings.

Hipshot consists of a package and a script.

To install them,

    gunzip < Hipshot-0.3.tar.gz | tar -xf -
    cd Hipshot-0.3/
    python setup.py install

or with pip,

    pip install hipshot
