from .objects import Objects

color = '\033[38;2;148;227;68m'
reset = '\x1b[0m'

objects = {
    Objects.NULL: ' ',
    Objects.start: '█',
    Objects.end: 'X',
    Objects.wall: '#',
    Objects.path: '░',
    Objects.specialEnd: color + 'X' + reset,
}

class Lines:
    TOPLEFT = color + '╒'
    TOPRIGHT = color + '╕'
    BOTTOMLEFT = color + '╘'
    BOTTOMRIGHT = color + '╛'
    MIDDLE = color + '│'
    TOP = color + '═'


def position(pos):
    return f'X: {pos[0]}, Y: {pos[1]}'