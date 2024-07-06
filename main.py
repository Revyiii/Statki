import pygame as p

p.init()
screen = p.display.set_mode((1104, 576))
clock = p.time.Clock()
running = True
dt = 0

player_pos = p.Vector2(screen.get_width() / 2, screen.get_height() / 2)
scr_w = screen.get_width()
scr_h = screen.get_height()
grid = []
for w in range(0,23):
    line = []
    for h in range(0,12):
        line.append((scr_w/23*w+scr_w/46,scr_h/12*h+scr_h/23))
    grid.append(line)
__import__('pprint').pprint(grid)
while running:

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    screen.fill("purple")
    
    for line in grid:
        for pos in line:
            p.draw.circle(screen,(pos[0]/scr_w*255,pos[1]/scr_h*255,255),pos,scr_w/46)

    p.display.flip()

    dt = clock.tick(60) / 1000

p.quit()

