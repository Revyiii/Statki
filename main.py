import pygame as p

p.init()
screen = p.display.set_mode((1104, 576))
clock = p.time.Clock()
running = True
dt = 0
m_last = False
scr_w = screen.get_width()
scr_h = screen.get_height()
grid = []
for w in range(0,23):
    line = []
    for h in range(0,12):
        line.append((scr_w/23*w+scr_w/46,scr_h/12*h+scr_h/24))
    grid.append(line)
__import__('pprint').pprint(grid)
while running:

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    screen.fill("purple")
    for i in range(1,11):
        for j in range(1,11):
            p.draw.circle(screen,"red",grid[i][j],scr_w/46)
    for i in range(12,22):
        for j in range(1,11):
            p.draw.circle(screen,"green",grid[i][j],scr_w/46)
    if p.mouse.get_pressed(num_buttons=3)[0] == False:
        m_last = False
    if p.mouse.get_pressed(num_buttons=3)[0] == True and m_last == False:
        m_last = True
        m_pos = p.mouse.get_pos() 
        m_grid_x = int(m_pos[0]/48)
        m_grid_y = int(m_pos[1]/48)
        print(f"{m_grid_x},{m_grid_y}")
    p.display.flip()

    dt = clock.tick(60) / 1000

p.quit()

