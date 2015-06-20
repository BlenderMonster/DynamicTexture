import bge
from mutil import sensors
from mbge import context

# BGE callables
def prepareBlueScreen():
    if not sensors.allPositive:
        return

    filter = bge.texture.FilterBlueScreen()
    
    colorSetup = context.owner.get("filter.color", str(filter.color)[1:-1])
    filter.color = parseIntegers(colorSetup)
    
    limitsSetup = context.owner.get("filter.limits", str(filter.limits)[1:-1])
    filter.limits = parseIntegers(limitsSetup)
    
    storeFilter(filter)

# End of BGE callables

INTERNAL_PROPERTY_FILTER = "filter"

def parseIntegers(input):
    parts = input.split(",")
    return [int(part) for part in parts]

def storeFilter(filter):
    context.owner[INTERNAL_PROPERTY_FILTER] = filter

def retrieveFilter():
    return context.owner.get(INTERNAL_PROPERTY_FILTER)

    