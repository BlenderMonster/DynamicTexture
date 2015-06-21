import bge
from mutil import sensors, properties
from mbge import context
import texture

PROPERTY_COMPONENT = "normal:component"
'''A string property of the color component to filter on (red, green, or blue)'''
PROPERTY_DEPTH = "normal:depth"
'''The depth of the relief (float)'''

# BGE callables
def setup():
    if not sensors.allPositive:
        return

    filter = bge.texture.FilterNormal()
    
    componentName = context.owner.get(PROPERTY_COMPONENT)
    if componentName:
        filter.colorIdx = componentMapping[componentName]

    filter.depth = float(context.owner.get(PROPERTY_DEPTH, filter.depth))

    texture.storeFilter(filter)

# End of BGE callables

componentMapping = {
    "red" : 0,
    "green" : 1,
    "blue" : 2
}




    