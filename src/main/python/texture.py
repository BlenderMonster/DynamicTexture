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

def refresh():
    'Refreshes the currently applied texture'
    retrieveTexture().refresh(True)

INTERNAL_PROPERTY_TEXTURE = "_texture"
INTERNAL_PROPERTY_FILTERS = "_filters"
FIRST_MATERIAL_ID = 0

def createDynamicTexture(source):
    texture = bge.texture.Texture(context.owner, FIRST_MATERIAL_ID)
    texture.source = source
    texture.refresh(False)
    return texture

def applyPreparedFilter(source):
    filters = retrieveFilters()
    if not filters:
        return
    
    for filter in filters:
        if source.filter:
            filter.previous = source.filter
        source.filter = filter


def storeTexture(texture):
    context.owner[INTERNAL_PROPERTY_TEXTURE] = texture

def retrieveTexture():
    try:
        return context.owner[INTERNAL_PROPERTY_TEXTURE]
    except KeyError:
        raise KeyError("No texture assigned yet. Setup a dynamic texture at object '{}' first. E.g. via texture.setImage"
                       .format(context.owner))

def storeFilter(filter):
    try:
        filters = context.owner[INTERNAL_PROPERTY_FILTERS]
    except KeyError:
        filters = []
    filters.append(filter)
    context.owner[INTERNAL_PROPERTY_FILTERS] = filters

def retrieveFilters():
    return context.owner.get(INTERNAL_PROPERTY_FILTERS)