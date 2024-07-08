from os import error
from funk import *
top = ['0','A','B','C','D','E','F','G','H','I','J','0']

def plansza(tab,x,y):
    for i in range(12):
        gotoxy(x+i*2,y)
        print(green+bgwhite+top[i]+" ",end=normal)
        gotoxy(x+i*2, y+11)
        print(red+bgwhite+top[i]+" ",end=normal)
    for i in range(1,11):
        gotoxy(x,y+i)
        print(black+bgwhite+"  \033[2D"+str(i),end=normal)
        for j in range(1,11):
            gotoxy(x+(j*2),y+i)
            color(tab[i][j])
        gotoxy(x+22,y+i)
        print(black+bgwhite+"  \033[2D"+str(i),end=normal)

def zeruj(tab):
    for i in range(12):
        for j in tab[i]:
            j=0

def losx(tab,n):
    good = False
    k,x,y = 0,0,0
    while(good == False):
        k = los(2)-1
        x = los(7+(n-1)*k)
        y = los(10-(n-1)*k)
        good = True
        for i in range(n):
            if tab[y+i*k][x-(k-1)*i] != 0:
                good = False
                break
    for i in range(-1,n+1):
        tab[y+i*k][x-(k-1)*i]=n
        tab[y+i*k+(k-1)][x-(k-1)*i+k]=5
        tab[y+i*k-(k-1)][x-(k-1)*i-k]=5
    tab[y+k*n][x+(k-1)]=5
    tab[y-k][x-(k-1)*n]=5

def podaj(d,re):
    input = 0
    if d == 1:
        gotoxy(3,14)
        print("               ")
        gotoxy(3,15)
        print("Podaj Kolumne (A...I):")
    else:
        gotoxy(3,14)
        print("10 to ':'")
        gotoxy(3,15)
        print("Podaj Wiersz (1...10):")
    while(input<1 or input > 10):
        input = get(re)
        if input == 113:
            re = [False]
            break
        input -= (3-d)*48
    znak = chr(input + (3-d)*48)
    gotoxy(2+d, 16)
    print(znak)
    return input
    
def lost(tab):
    statki = [4,3,3,2,2,2,1,1,1,1]
    for i in statki:
        losx(tab,i)

def SG(tab, re):
    kol = podaj(1,re)
    if kol == 113:
        return
    wier = podaj(2,re)
    if wier == 113:
        return
    gotoxy(3,16)
    print("   ")
    if tab[wier][kol] == 0 or tab[wier][kol] == 5:
        tab[wier][kol] = 7
    elif tab[wier][kol] < 5 and tab[wier][kol]>0:
        tab[wier][kol] = 8

def SK(tab):
    kol,wier =0,0
    while tab[wier][kol]==8 or tab[wier][kol]==7:
        kol =los(10)
        wier = los(10)
    if tab[wier][kol] == 0 or tab[wier][kol] == 5:
        tab[wier][kol] = 7
    elif tab[wier][kol] < 5 and tab[wier][kol]>0:
        tab[wier][kol] = 8

def TEST(tab):
    suma = 0
    for i in range(1,11):
        for j in range(1,11):
            if tab[i][j] > 0 and tab[i][j] < 5:
                suma += 1
    return suma

def Komunikat(TK,TG,ref):
    tk = TEST(TK)
    tg = TEST(TG)
    if tk == tg and tk == 0:
        ref[0] = True
        print(cls+bgred+blue+"Remis",end=normal)
        ref[1] = jeszcze()
    if tk == 0:
        ref[0] = True
        print(cls+bgred+blue+"Wygral Gracz",end=normal)
        ref[1] = jeszcze()
    if tg == 0:
        ref[0] = True
        print(cls+bgred+blue+"Wygral Komputer",end=normal)
        ref[1] = jeszcze()

def zapisz(tab1,tab2):
    plik = open("plansza.txt","w")
    for i in range(1,11):
        for j in range(1,11):
            plik.write(str(tab1[i][j])+"\n")
            plik.write(str(tab2[i][j])+"\n")
    plik.close
def odczyt(tab1,tab2):
    plik = open("plansza.txt","r")
    text = plik.read()
    lista = text.split("\n")
    lista = lista[:-1]
    for i in range(1,11):
        for j in range(1,11):
            tab1[i][j] = int(lista[((i-1)*10+j-1)*2])
            tab2[i][j] = int(lista[((i-1)*10+j-1)*2+1])
    plik.close

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
    TG = [row[:] for row in tablica]
    TK = [row[:] for row in tablica]
    print(cls+"\033[?25l")
    re = [True]
    losowanie = True
    print("czy chesz wczytac zapis?(t/n)")
    if(getin()=='t'):
        try:
            odczyt(TG,TK)
            losowanie = False
            print(cls)
            plansza(TG, 3, 2)
            plansza(TK, 31,2)
        except:
            print("nie ma pliku program zostanie zamknięty")
            getch()
            return
    while(re[0] == True):
        if(losowanie):
            zeruj(TG)
            zeruj(TK)
            lost(TG)
            lost(TK)
            plansza(TG, 3, 2)
            plansza(TK, 31,2)
            losowanie = False
        gotoxy(3, 1)
        print("Plansza Gracz Statki: "+str(TEST(TG)))
        gotoxy(31, 1)
        print("Plansza Komputera Statki: "+str(TEST(TK)))
        gotoxy(3, 17)
        print("Nacisznij [Q] w dowolnym momencie gry aby wyjsc z programu.")
        SG(TK,re)
        zapisz(TG,TK)
        SK(TG)
        plansza(TG,3,2)
        plansza(TK,31,2)
        Komunikat(TK ,TG,[losowanie,re])

if __name__ == "__main__":
    main()
