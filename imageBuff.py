__author__ = 'Monster'

import bge
from mbge import context, path
from mutil import sensors
import texture
import array

PROPERTY_IMAGE_FILE_NAME = "image"
'Provides the name of the image file to be used to create an image source.'

# BGE callable
def setup():
    'Replaces the first material texture with an image source'
    if not sensors.allPositive:
        return

    source = createImageSource()
    loadBuffer(source)
    texture.applyPreparedFilter(source)
    texture.storeTexture(texture.createDynamicTexture(source))

# End of BGE callable

def createImageSource():
    return bge.texture.ImageBuff()

def loadBuffer(source):
    width = 10
    height = 10
    buffer = generatePattern(width, height)
    source.load(buffer, width, height)

    fileName = path.expandPath("//image/MonsterScripts.png")
    imageSource = bge.texture.ImageFFmpeg(fileName)
    
    print(imageSource.size)
    #source.load(imageSource.image, *imageSource.size)
    
def generatePattern(width, height):
    buffer = array.array('B')
    for x in range(width):
        for y in range(height):
            addColor(buffer, toByte(x/width), toByte(y/height), 0)
    return buffer

def addColor(buffer, *color):
    for component in color:
        buffer.append(component)
def toByte(value):
    return int(value * 255)
