__author__ = 'Monster'

import bge
from mbge import context, path
from mutil import sensors
import texture


PROPERTY_CAMERA_NAME = "camera"
'Provides the name of the camera to be used to create a camera resource.'

# BGE callable
def setup():
    'Replaces the first material texture with a camera source'
    if not sensors.allPositive:
        return

    source = createCameraSource()
    texture.applyPreparedFilter(source)
    texture.storeTexture(texture.createDynamicTexture(source))

def refresh():
    if sensors.allPositive:
        texture.refresh()

# End of BGE callable

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

