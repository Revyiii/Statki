import pygame as p

p.init()
screen = p.display.set_mode((1280, 720))
clock = p.time.Clock()
running = True
dt = 0

player_pos = p.Vector2(screen.get_width() / 2, screen.get_height() / 2)
scr_w = screen.get_width()
scr_h = screen.get_height()
grid = []
for w in range(0,22):
    line = []
    for h in range(0,11):
        line.append((scr_w/22*w,scr_h/11*h))
    grid.append(line)
__import__('pprint').pprint(grid)
while running:

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    screen.fill("purple")
    
    for line in grid:
        for pos in line:
            p.draw.circle(screen,(pos[0]/scr_w*255,pos[1]/scr_h*255,255),pos,5)

    p.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

p.quit()

