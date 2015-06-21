'''
video
=====

Creates and controls video sources.
Video sources can be projected onto materials and textures 
via the texture module.

The video source will be configured via properties.
The operations will be executed via Python controller (module mode).

Assumptions:
------------
    - One game object has one video source only.
    - The operations belong to the object that performs them

Remarks:
--------
    - Playing a video source does not update the texture it is projected on.

History:
    2.0 - 18Jum2015 - exchanged bgeUtil by mbge and mutil
    1.0 - 02Jun2014 - initial version
    1.1 - 18Jun2015 - added activateOnStop
'''
__version__ = "1.1"
__date__ = "18 Jun 2015"
__author__ = "Monster"

import bge
from mutil import sensors, actuators
from mbge import context, path
import texture

PROPERTY_VIDEO_FILE_NAME = "video"

# BGE callables
def setup():
    'Replaces the first material texture with an video source'
    if not sensors.allPositive:
        return

    source = createSource()
    texture.applyPreparedFilter(source)
    texture.storeTexture(texture.createDynamicTexture(source))


def play():
    if sensors.allPositive:
        retrieveVideo().play()

def pause():
    if sensors.allPositive:
        retrieveVideo().pause()

def stop():
    if sensors.allPositive:
        retrieveVideo().stop()

def activateOnStop():
    if retrieveVideo().status == SOURCE_STOPPED:
        actuators.activateAll()

# End of BGE callables

INTERNAL_PROPERTY_VIDEO = "_videoSource"

SOURCE_ERROR = -1
SOURCE_EMPTY = 0
SOURCE_READY = 1
SOURCE_PLAYING = 2
SOURCE_STOPPED = 3

def createSource():
    fileName = path.expandPath("//"+getFileName())
    source = bge.texture.VideoFFmpeg(fileName)
    source.play()
    storeVideo(source)
    return source

def getFileName():
    try:
        return context.owner[PROPERTY_VIDEO_FILE_NAME]
    except KeyError:
        raise KeyError("Please set up string property '{}' with the path to the video file"
                       .format(PROPERTY_VIDEO_FILE_NAME))
def storeVideo(video):
    context.owner[INTERNAL_PROPERTY_VIDEO] = video

def retrieveVideo():
    try:
        return context.owner[INTERNAL_PROPERTY_VIDEO]
    except KeyError:
        raise KeyError("No video source assigned yet. Setup a video source first. E.g. via texture.setVideo")
