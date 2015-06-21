import bge
from mutil import sensors, properties
from mbge import context
import texture

# BGE callables
def prepareBlueScreen():
    if not sensors.allPositive:
        return

    filter = bge.texture.FilterBlueScreen()
    
    colorSetup = context.owner.get("filter.color", str(filter.color)[1:-1])
    filter.color = properties.parseAsList(colorSetup)
    
    limitsSetup = context.owner.get("filter.limits", str(filter.limits)[1:-1])
    filter.limits = properties.parseAsList(limitsSetup)
    
    texture.storeFilter(filter)

# End of BGE callables





    