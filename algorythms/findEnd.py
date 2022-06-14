from map import Objects
import time

def findEnd(startX, startY, map, printMap = False):
    pointsUp = []
    pointsDown = []
    mapX, mapY = map.width, map.height
    currentXr, currentXl = (startX,)*2
    while True:
        if map.map[startY][currentXr] != Objects.wall:
            pointsUp.append([currentXr, startY])
            pointsDown.append([currentXr, startY])

        if map.map[startY][currentXl] != Objects.wall:
            pointsUp.append([currentXl, startY])
            pointsDown.append([currentXl, startY])

        for points_ in pointsUp:
            
            if map.map[points_[1]][points_[0]] == Objects.end:
                return tuple(points_)
            elif map.map[points_[1]][points_[0]] == Objects.wall:
                pointsUp.remove(points_)
            elif printMap and map.map[points_[1]][points_[0]] == Objects.NULL:
                map.spawn(Objects.path, points_)

            if points_[1] > 0:
                points_[1] -= 1

        for points_ in pointsDown:
            if map.map[points_[1]][points_[0]] == Objects.end:
                return tuple(points_)
            elif map.map[points_[1]][points_[0]] == Objects.wall:
                pointsDown.remove(points_)
            elif printMap and map.map[points_[1]][points_[0]] == Objects.NULL:
                map.spawn(Objects.path, points_)

            if points_[1] < mapY:
                points_[1] += 1

        if currentXr < mapX:
            currentXr += 1
        if currentXl > 0:
            currentXl -= 1
        
        if printMap:
            map.print()
            time.sleep(0.03)
