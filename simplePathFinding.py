from map import Map, Objects, prettifier
import algorythms

import random

VIEW_ANIMATIONS = False

def getValue(from_, to_, avoid = []):
    value = avoid[0] if len(avoid) > 0 else random.randint(from_, to_)
    while value in avoid:
        value = random.randint(from_, to_)
    return value


map = Map()
mapX = 100
mapY = 20
map.generateMap(mapX, mapY)

# Spawn the objects
startX = getValue(0, mapX)
startY = getValue(0, mapY)
map.spawn(Objects.start, (startX, startY))
map.spawn(Objects.end, (getValue(0, mapX, [startX]), getValue(0, mapY, [startY])))


# Find the nearest end
nearestEnd = algorythms.findEnd(startX, startY, map, VIEW_ANIMATIONS)
print(f'nearestEnd = {prettifier.position(nearestEnd)}')

map.clearAnimations()

result = algorythms.findPath((startX, startY), nearestEnd, map, VIEW_ANIMATIONS)
map.print()
print(f'Path Result >> {len(result)} steps')
print(', '.join(f'X{x}-Y{y}' for x, y in result))