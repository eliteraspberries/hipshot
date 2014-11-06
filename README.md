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

    gunzip < Hipshot-0.4.3.tar.gz | tar -xf -
    cd Hipshot-0.4.3/
    python setup.py install

or with pip,

    pip install hipshot


Usage
=====

The hipshot script takes a single argument: the video file.

    Hipshot - Simulate long-exposure photography

    Usage:
        hipshot <file>

    Options:
        -v, --version   Print version information.
        -h, --help      Print this help.


Example
=======

The following image was created from the video:
[ISS Near Aurora Borealis][iss-video].

![][iss-image]


[iss-image]: http://www.eliteraspberries.com/images/iss-borealis.png
[iss-video]: <http://www.youtube.com/watch?v=uYBYIhH4nsg>
