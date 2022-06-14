# Path finding algorithm in python
from map import Map, Objects, prettifier

moveDown = lambda position: (position[0], position[1] + 1)
moveUp = lambda position: (position[0], position[1] - 1)
moveLeft = lambda position: (position[0] - 1, position[1])
moveRight = lambda position: (position[0] + 1, position[1])

def findPath(startPosition : tuple, endPosition : tuple, map : Map, viewAnimations = False):
    path = [startPosition]
    currentPosition = startPosition
    while currentPosition != endPosition:
        checks = [
            (currentPosition[0] > endPosition[0], moveLeft),
            (currentPosition[0] < endPosition[0], moveRight),
            (currentPosition[1] > endPosition[1], moveUp),
            (currentPosition[1] < endPosition[1], moveDown),
        ]

        for move in [check[1] for check in checks if check[0]]:
            currentPosition = move(currentPosition)
            path.append(currentPosition)
        
        if map.map[currentPosition[1]][currentPosition[0]] == Objects.NULL:
            map.spawn(Objects.path, currentPosition)
        if viewAnimations:
            map.print()
            print(f'currentPosition = {prettifier.position(currentPosition)}')
            print(f'endPosition = {prettifier.position(endPosition)}')

    return path

