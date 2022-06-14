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
    BOTTOM_2_TOPRIGHT = color + '╒' + reset
    TOP_2_BOTTOMLEFT  = color + '╘' + reset
    BOTTOM_2_TOPLEFT  = color + '╕' + reset
    BOTTOMLEFT_2_TOP  = color + '╛' + reset
    MIDDLE = color + '│' + reset
    LINE = color + '═' + reset


def position(pos):
    return f'X: {pos[0]}, Y: {pos[1]}'