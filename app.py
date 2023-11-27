#Checking the winner if the input match with 8 valid conditions
def isWinner(tab):
    cIdx = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)]]
    for i in cIdx:
        x = ' X '
        o = ' O '
        oCount = 0
        xCount = 0
        for j in i:
            r,c = j
            if tab[r][c] == x:
                xCount += 1
            elif tab[r][c] == o:
                oCount += 1
        if oCount == 3 or xCount == 3:
            return True
    return False

def isValidEntry(tab,loc):
    r,c = loc
    return tab[r][c] == " _ "

def update(tab,loc,symbol):
    r,c = loc
    tab[r][c] = " {} ".format(symbol)

def show(tab):
    for r in tab:
        print("[",end="")
        for c in r:
            print(c,end="")
        print("]")
    print('-----------')

table = [[" _ "," _ "," _ "],[" _ "," _ "," _ "],[" _ "," _ "," _ "]]

i = 0
winner = False
show(table)
while(i<9 and not winner):
    validEntry = False
    while(not validEntry):
        idx = input("ENTER LOCATION(R(0-2)/C(0-2)): ")
        row = int(idx[0])
        column = int(idx[1])
        validEntry = isValidEntry(table,(row,column))
        if not validEntry:
            print("Already Filled, Please Enter another Location")
    if i%2 == 0:
        update(table,(row,column),'X')
    else:
        update(table,(row,column),'O')
    show(table)
    winner = isWinner(table)
    if(winner):
        print("Hurray, We have a WINNER!!!!!!!!!!!")
    i += 1
else:
    if i == 9 and not winner:
        print("Game Over Without a WINNER!!!!!!!!!")