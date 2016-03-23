import bge
from mutil import sensors, properties
from mbge import context
import texture

DEFAULT_PREFIX = "blueScreen"
'''The prefix to search for controller specific proeprties. Format: <prefix>:<property>'''

PROPERTY_COLOR = "color"
'''The suffix of a property containing the comma separated components (r,g,b) of a color as integer from 0..255.'''
PROPERTY_LIMITS = "limits"
'''The suffix of a property containing  the comma separated components (lower, upper) of the limits as integer.'''

# BGE callables
def setup():
    if not sensors.allPositive:
        return

    filter = bge.texture.FilterBlueScreen()
    
    colorSetup = properties.getWithControllerPrefix(DEFAULT_PREFIX, PROPERTY_COLOR, str(filter.color)[1:-1])
    filter.color = properties.parseAsList(colorSetup)

    limitsSetup = properties.getWithControllerPrefix(DEFAULT_PREFIX, PROPERTY_LIMITS, str(filter.limits)[1:-1])
    filter.limits = properties.parseAsList(limitsSetup)

    texture.storeFilter(filter)

# End of BGE callables





    