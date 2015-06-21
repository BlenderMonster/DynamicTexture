import bge
from mutil import sensors, properties
from mbge import context
import texture

DEFAULT_PREFIX = "normal"
'''The prefix to search for controller specific proeprties. Format: <prefix>:<property>'''

PROPERTY_COMPONENT = "component"
'''The suffix of a property containing the color component to filter on (red, green, or blue)'''
PROPERTY_DEPTH = "depth"
'''The suffix of a property containing the depth of the relief (float)'''

# BGE callables
def setup():
    if not sensors.allPositive:
        return

    filter = bge.texture.FilterNormal()
    
    componentName = properties.getWithControllerPrefix(DEFAULT_PREFIX, PROPERTY_COMPONENT)
    if componentName:
        filter.colorIdx = componentMapping[componentName]

    filter.depth = float(properties.getWithControllerPrefix(DEFAULT_PREFIX, PROPERTY_DEPTH, filter.depth))

    texture.storeFilter(filter)

# End of BGE callables

componentMapping = {
    "red" : 0,
    "green" : 1,
    "blue" : 2
}




    