from map import Map, Objects, prettifier
import algorythms

import random

VIEW_ANIMATIONS = True

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
startX = getValue(0, mapX-1)
startY = getValue(0, mapY-1)
map.spawn(Objects.start, (startX, startY))

for y in range(100):
    map.spawn(Objects.wall, (getValue(0, mapX-1, [startX]), getValue(0, mapY-1, [startY])))

map.spawn(Objects.end, (getValue(0, mapX-1, [startX]), getValue(0, mapY-1, [startY])))



# Find the nearest end
nearestEnd = algorythms.findEnd(startX, startY, map, False)
print(f'nearestEnd = {prettifier.position(nearestEnd)}')

map.clearAnimations()

result = algorythms.findPath((startX, startY), nearestEnd, map, VIEW_ANIMATIONS)
map.print()
print(f'Path Result >> {len(result)} steps')
print(', '.join(f'X{x}-Y{y}' for x, y in result))