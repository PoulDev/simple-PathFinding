# Path finding algorithm in python
from torch import t
from map import Map, Objects, prettifier

globalMap : Map = None
printProcess = True

def movementLogic(startPos, goingTo, baseFunction):
    global printProcess

    if globalMap.getPosition(goingTo) == Objects.wall:
        printProcess = False
        winner = -1
        rules = movementRules[baseFunction]
        tryToGo = rules[1]
        processes = [{
            'goingTo': baseFunction,
            'rule': rule,
            'position': startPos,
            'path': []
        } for rule in rules[0]]

        while winner == -1:
            for process in processes:
                position = process['position']
                process['path'] += process['rule'](position)

                canIGopls = tryToGo(position)
                process['position'] = process['path'][-1]

                if globalMap.getPosition(canIGopls[-1]) == Objects.NULL:
                    process['path'] += canIGopls
                    printProcess = True
                    for pos_ in process['path']:
                        globalMap.spawn(Objects.path, pos_)
                    return process['path']

                pass

    if printProcess:
        globalMap.spawn(Objects.path, goingTo)
    return [goingTo]


rawMoveUp = lambda position: [(position[0], position[1]-1)]
rawMoveDown = lambda position: [(position[0], position[1]+1)]
rawMoveLeft = lambda position: [(position[0]-1, position[1])]
rawMoveRight = lambda position: [(position[0]+1, position[1])]

def moveDown(position):
    return movementLogic(position, (position[0], position[1]+1), moveDown)

def moveUp(position):
    return movementLogic(position, (position[0], position[1]-1), moveUp)

def moveLeft(position):
    return movementLogic(position, (position[0]-1, position[1]), moveLeft)

def moveRight(position):
    return movementLogic(position, (position[0]+1, position[1]), moveRight)

def getChecks(currentPosition, endPosition):
    return [
        (currentPosition[-1][0] > endPosition[0], moveLeft),
        (currentPosition[-1][0] < endPosition[0], moveRight),
        (currentPosition[-1][1] > endPosition[1], moveUp),
        (currentPosition[-1][1] < endPosition[1], moveDown),
    ]

movementRules = {
    moveLeft: ([moveUp, moveDown], rawMoveLeft),
    moveRight: ([moveUp, moveDown], rawMoveRight),
    moveUp: ([moveLeft, moveRight], rawMoveUp),
    moveDown: ([moveLeft, moveRight], rawMoveDown)
}

def findPath(startPosition : tuple, endPosition : tuple, map : Map, viewAnimations = False):
    global globalMap
    globalMap = map
    path = [startPosition]
    currentPosition = [startPosition]
    while currentPosition[-1] != endPosition:
        checks = getChecks(currentPosition, endPosition)

        for move in [check[1] for check in checks if check[0]]:
            currentPosition = move(currentPosition[-1])
            path += currentPosition

        if viewAnimations:
            map.print()
            print(f'currentPosition = {prettifier.position(currentPosition[-1])}')
            print(f'endPosition = {prettifier.position(endPosition)}')

    return path

