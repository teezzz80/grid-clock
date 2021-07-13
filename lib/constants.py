API_URL = "http://worldtimeapi.org/api/timezone/America/Edmonton"
WEB_QUERY_DELAY = 3600  # sync time delay in s, default is 3600
RETRY_DELAY = 5  # sync time retry delay in s
BRIGHTNESS = 0.1  # screen brightness between 0 and 1
REFRESH_DELAY = 5000  # display refresh delay in ms

TIME_FONT = [
    '111 101 101 101 111',  #0
    '010 010 010 010 010',  #1
    '111 001 111 100 111',  #2
    '111 001 111 001 111',  #3
    '101 101 111 001 001',  #4
    '111 100 111 001 111',  #5
    '111 100 111 101 111',  #6
    '111 001 001 001 001',  #7
    '111 101 111 101 111',  #8
    '111 101 111 001 111',  #9
]

ALPHA_FONT = [
    '010 101 111 101 101', #A
    '110 101 110 101 110', #B
    '011 100 100 100 011', #C
    '110 101 101 101 110', #D
    '111 100 110 100 111', #E
    '111 100 110 100 100', #F
    '010 100 111 101 011', #G
    '101 101 111 101 101', #H
    '111 010 010 010 111', #I
    '111 010 010 010 100', #J
    '101 101 110 101 101', #K
    '100 100 100 100 111', #L
    '101 111 111 101 101', #M
    '111 101 101 101 101', #N
    '010 101 101 101 010', #O
    '110 101 110 100 100', #P
    '010 101 101 111 011', #Q
    '110 101 110 101 101', #R
    '111 100 111 001 111', #S
    '111 010 010 010 010', #T
    '101 101 101 101 111', #U
    '101 101 101 101 010', #V
    '101 101 111 111 101', #W
    '101 101 010 101 101', #X
    '101 101 111 010 010', #Y
    '111 001 010 100 111', #Z
    '000 000 000 000 101', #..
    '010 010 010 000 010', #!
]

ALPHA_ENUM = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
    '.': 26,
    '!': 27,
}

COLORS = {
    'red': (255, 0, 0),
    'orange': (255, 64, 0),
    'yellow': (255, 255, 0),
    'green': (0, 255, 0),
    'cyan': (0, 128, 255),
    'blue': (0, 0, 255),
    'purple': (191, 0, 255),
    'pink': (255, 0, 255),
    'white': (255, 255, 255),
}

THEMES = [
    ['white', 'white', 'green', 'green'],
    ['white', 'white', 'orange', 'orange'],
    ['white', 'white', 'blue', 'blue'],
    ['blue', 'blue', 'orange', 'orange'],
    ['red', 'red', 'blue', 'blue'],
    ['cyan', 'cyan', 'pink', 'pink'],
    ['red', 'green', 'blue', 'yellow'],
]

DATETIME_ENUM = {
    'year': 0,
    'month': 1,
    'day': 2,
    'day_of_week': 3,
    'hour': 4,
    'minute': 5,
    'second': 6,
    'millisecond': 7,
}