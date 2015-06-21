'''
texture
=======

Projects render sourcen onto materials as textures and creates
image and camera sources.
Currently these source types can be set up:
    - image
    - camera
    - video (see video module)

The source will be projected at the first material only.
The sources will be configured via properties.
    
Assumptions:
------------
    - One game object hhas one dynamic texture only.
    - The operations belong to the object that performs them.

Remarks:
--------
    - Updating a source (video, camera) requires a refresh on the texture
    - Refreshing the texture does not update the source
    - Shared materials are updated on all objects
    
    
History:
    2.0 - 18Jun2015 - exchanged bgeUtil by mbge and mutil
    1.2 - 03Jun2015 - added support for prepared filters
    1.1 - 16Jul2014 - enabled cameras from other scenes
    1.0 - 02Jun2014 - initial version
'''
__version__ = "2.0"
__date__ = "18 Jun 2015"
__author__ = "Monster"

import bge
from mbge import context, path
from mutil import sensors
import filter

PROPERTY_CAMERA_NAME = "camera"
'Provides the name of the camera to be used to create a camera resource.'
PROPERTY_IMAGE_FILE_NAME = "image"
'Provides the name of the image file to be used to create an image source.'

# BGE callables

def setImage():
    'Replaces the first material texture with an image source'
    if not sensors.allPositive:
        return
    
    source = createImageSource() 
    applyPreparedFilter(source)
    texture = createDynamicTexture(source)
    storeTexture(texture)

def setCamera():
    'Replaces the first material texture with a camera source'
    if not sensors.allPositive:
        return
 
    source = createCameraSource()
    applyPreparedFilter(source)
    texture = createDynamicTexture(source)
    storeTexture(texture)

    
def refresh():
    'Refreshes the currently applied texture'
    if not sensors.allPositive:
        return
    
    retrieveTexture().refresh(True)

# End of BGE callables

INTERNAL_PROPERTY_TEXTURE = "_texture"
FIRST_MATERIAL_ID = 0

def createImageSource():
    fileName = path.expandPath("//"+getImageFileName())
    return bge.texture.ImageFFmpeg(fileName)

def createCameraSource():
    camera = retrieveAssignedCamera()
    source = bge.texture.ImageRender(camera.scene, camera)
    source.background = [0,0,0,0]
    source.alpha = False
    return source

def retrieveAssignedCamera():
    return findCamera(context.owner.get(PROPERTY_CAMERA_NAME))

def findCamera(name, scene=None):
    if scene:
        return scene.cameras.get(name)
    camera = bge.logic.getCurrentScene().cameras.get(name)
    if camera:
        return camera
    for scene in bge.logic.getSceneList():
        camera = findCamera(name, scene)
        if camera:
            return camera
    raise KeyError("There is no camera with name '{}'".format(name))

def createDynamicTexture(source):
    texture = bge.texture.Texture(context.owner, FIRST_MATERIAL_ID)
    texture.source = source
    texture.refresh(False)
    return texture

def applyPreparedFilter(source):
    preparedFilter = filter.retrieveFilter()
    if preparedFilter:
        source.filter = preparedFilter 

def storeTexture(texture):
    context.owner[INTERNAL_PROPERTY_TEXTURE] = texture

def retrieveTexture():
    try:
        return context.owner[INTERNAL_PROPERTY_TEXTURE]
    except KeyError:
        raise KeyError("No texture assigned yet. Setup a dynamic texture first. E.g. via texture.setImage")

def getImageFileName():
    try:
        return context.owner[PROPERTY_IMAGE_FILE_NAME]
    except KeyError:
        raise KeyError("Please set up string property '{}' with the path to the image file"
                       .format(PROPERTY_IMAGE_FILE_NAME))

