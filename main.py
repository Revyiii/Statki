import pygame as p
from funk import *
from statorg import *

p.init()
screen = p.display.set_mode((1104, 576))
clock = p.time.Clock()
running = True
dt = 0
m_last = False
scr_w = screen.get_width()
scr_h = screen.get_height()
grid = []
colour = {0:"blue",1:"grey",2:"grey",3:"grey",4:"grey",5:"blue",7:"red",8:"green"}

for w in range(0,23):
    line = []
    for h in range(0,12):
        line.append((scr_w/23*w+scr_w/46,scr_h/12*h+scr_h/24))
    grid.append(line)

TG = [row[:] for row in tablica]
TK = [row[:] for row in tablica]
print(cls+"\033[?25l")
re = [True]
losowanie = True
print("czy chesz wczytac zapis?(t/n)")
#if(getin()=='t'):
if(False):
    try:
        odczyt(TG,TK)
        losowanie = False
        plansza(TG, 3, 2)
        plansza(TK, 31,2)
    except:
        print("nie ma pliku program zostanie zamknięty")
        getch()

while running:

    if(losowanie):
        zeruj(TG)
        zeruj(TK)
        lost(TG)
        lost(TK)
        losowanie = False
    zapisz(TG,TK)
    
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    screen.fill("purple")
    for i in range(1,11):
        for j in range(1,11):
            p.draw.circle(screen,colour[TK[i][j]],grid[i][j],scr_w/46)
    for i in range(12,22):
        for j in range(1,11):
            p.draw.circle(screen,colour[TG[i-11][j]],grid[i][j],scr_w/46)
    if p.mouse.get_pressed(num_buttons=3)[0] == False:
        m_last = False
    if p.mouse.get_pressed(num_buttons=3)[0] == True and m_last == False:
        m_last = True
        m_pos = p.mouse.get_pos() 
        m_grid_x = int(m_pos[0]/48)
        m_grid_y = int(m_pos[1]/48)
        print(f"{m_grid_x},{m_grid_y}")
        if m_grid_x in range(1,11) and m_grid_y in range(1,11):
            if TK[m_grid_x][m_grid_y] == 0 or TK[m_grid_x][m_grid_y] == 5:
                TK[m_grid_x][m_grid_y] = 7
            elif TK[m_grid_x][m_grid_y] < 5 and TK[m_grid_x][m_grid_y]>0:
                TK[m_grid_x][m_grid_y] = 8
            SK(TG)
    p.display.flip()

    dt = clock.tick(60) / 1000

p.quit()

