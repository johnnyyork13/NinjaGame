SCREEN_RESOLUTION = 500,500
FPS = 60

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

TILE_SIZE = 50

PLAYER_START = ((SCREEN_RESOLUTION[1]/2 - TILE_SIZE - 10),(SCREEN_RESOLUTION[0]/2))


mydic = {(0, 1): 5, (0,2): 6}

for _ in mydic.items():
    print(_[1])
