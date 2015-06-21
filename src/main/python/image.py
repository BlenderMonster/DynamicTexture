__author__ = 'Monster'

import bge
from mbge import context, path
from mutil import sensors
import filter
import texture

PROPERTY_IMAGE_FILE_NAME = "image"
'Provides the name of the image file to be used to create an image source.'

# BGE callable
def setup():
    'Replaces the first material texture with an image source'
    if not sensors.allPositive:
        return

    source = createImageSource()
    texture.applyPreparedFilter(source)
    texture.storeTexture(texture.createDynamicTexture(source))

# End of BGE callable

def createImageSource():
    fileName = path.expandPath("//"+getImageFileName())
    return bge.texture.ImageFFmpeg(fileName)

def getImageFileName():
    try:
        return context.owner[PROPERTY_IMAGE_FILE_NAME]
    except KeyError:
        raise KeyError("Please set up string property '{}' with the path to the image file"
                       .format(PROPERTY_IMAGE_FILE_NAME))
