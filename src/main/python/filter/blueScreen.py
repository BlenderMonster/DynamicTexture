import bge
from mutil import sensors, properties
from mbge import context
import texture

PROPERTY_COLOR = "blueScreen:color"
'''A string property with the comma separated components (r,g,b) of a color as integer from 0..255.'''
PROPERTY_LIMITS = "blueScreen:limits"
'''A string property with the comma separated components (lower, upper) of the limits as integer.'''

# BGE callables
def setup():
    if not sensors.allPositive:
        return

    filter = bge.texture.FilterBlueScreen()
    
    colorSetup = context.owner.get(PROPERTY_COLOR, str(filter.color)[1:-1])
    filter.color = properties.parseAsList(colorSetup)

    limitsSetup = context.owner.get(PROPERTY_LIMITS, str(filter.limits)[1:-1])
    filter.limits = properties.parseAsList(limitsSetup)

    texture.storeFilter(filter)

# End of BGE callables





    