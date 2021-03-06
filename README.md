Hipshot converts a video file or series of photographs into
a single image simulating a long-exposure photograph.

[![](https://travis-ci.org/eliteraspberries/hipshot.svg)][build-status]
[![](https://img.shields.io/pypi/v/Hipshot.svg)][pypi]
![](https://img.shields.io/github/license/eliteraspberries/hipshot.svg)


Installation
============

Hipshot requires:

  - Python 2;
  - docopt;
  - the [Avena][] library;
  - the FFMPEG libraries; and
  - OpenCV and its Python bindings.

Install Hipshot with [pip][]:

    pip install hipshot


Usage
=====

The hipshot script takes a single argument: the video file.

    Hipshot - Simulate long-exposure photography

    Usage:
        hipshot [options] video <file>
        hipshot [options] photos <file>...
        hipshot -h | --help
        hipshot -v | --version

    Options:
        --display               Display the merging process.
        --no-display
        -h, --help              Print this help.
        -v, --version           Print version information.


Example
=======

The following image was created from the video:
[ISS Near Aurora Borealis][iss-video].

![][iss-image]

[Avena]: https://pypi.python.org/pypi/Avena
[pip]: https://pip.pypa.io/en/stable/
[iss-image]: http://www.eliteraspberries.com/images/iss-borealis.png
[iss-video]: <http://www.youtube.com/watch?v=uYBYIhH4nsg>
[build-status]: https://travis-ci.org/eliteraspberries/hipshot
[pypi]: https://pypi.python.org/pypi/Hipshot
