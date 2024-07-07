import pygame as p
from funk import *
from statorg import * 

def grid_gen(scr_w,scr_h):
    grid = []
    for w in range(0,23):
        line = []
        for h in range(0,12):
            line.append((scr_w/23*w+scr_w/46,scr_h/12*h+scr_h/24))
        grid.append(line)
    return grid
color_k = {0:"blue",1:"white",2:"white",3:"white",4:"white",5:"yellow",7:"red",8:"green"}

tablica = [
    [0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0] 
]
def main():
    
    p.init()
    
    screen = p.display.set_mode((1104, 576))
    clock = p.time.Clock()
    running = True
    dt = 0
    m_last = False
    scr_w = screen.get_width()
    scr_h = screen.get_height()
    grid = grid_gen(scr_w,scr_h)

    TG = [row[:] for row in tablica]
    TK = [row[:] for row in tablica]
    re = [True]
    losowanie = True
    print("czy chesz wczytac zapis?(t/n)")
    if(getin()=='t'):
        try:
            odczyt(TG,TK)
            losowanie = False
        except:
            print("nie ma pliku program zostanie zamknięty")
            re[0] = False
            return

    while(re[0] == True):

        if(losowanie):
            zeruj(TG)
            zeruj(TK)
            lost(TG)
            lost(TK)
            losowanie = False
        
        screen.fill("purple")
        for i in range(1,11):
            for j in range(1,11):
                if TK[i][j] == 0:
                    p.draw.circle(screen,color_k[TK[i][j]],grid[i][j],scr_w/46)
        for i in range(12,22):
            for j in range(1,11):
                if TG[i-11][j] == 0:
                    p.draw.circle(screen,color_k[TG[i-11][j]],grid[i][j],scr_w/46)
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
        keys = p.key.get_pressed()
        if keys[p.K_q] == True:
            re[0] = False
        
    p.quit()

if __name__ == "__main__":
    main()
