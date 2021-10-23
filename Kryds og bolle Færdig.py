import random
hvilken_tur= 'X'
er_spilletslut = False
hvem_starter=None
spillerens_identitet=''

xPos=[]
oPos=[]

succesfuldetræk=[
    [1,2,3],
    [1,5,9],
    [2,5,8],
    [3,6,9],
    [4,5,6],
    [7,8,9],
    [3,5,7],
    [1,4,7],
]
spillepladen = [
   [' ','|',' ','|',' '],
   ['-','+','-','+','-'],
   [' ','|',' ','|',' '],
   ['-','+','-','+','-'],
   [' ','|',' ','|',' '],
]
spillerens_identitet = ''
def hvis_plade():
    print('')
    print('================================================================')
    for i in range(len(spillepladen)):
        for j in range(len(spillepladen)):
            print(spillepladen[i][j],end='')
        print('\n')
    print('================================================================')

def returnerHvilkenRækkeOgKolonneDerÆndres(placering):
    #key er en integer og value er en tupple. man skal se det som par, som hedder key-value pairs.
    # der er to parametre placering og træk hvor placeringen er en plads på brættet fra 1 til 9. trækket er så X eller O
    return {
        1 : (0,0),
        2 : (0,2),
        3 : (0,4),
        4 : (2,0),
        5 : (2,2),
        6 : (2,4),
        7 : (4,0),
        8 : (4,2),
        9 : (4,4)
    } [placering]


def valgtePlaceringErTom(randomTal):
    return (randomTal not in xPos and randomTal not in oPos)

def placer_træk(placering,træk):
    xPos.append(placering) if træk == 'X' else oPos.append(placering)
    tupel=returnerHvilkenRækkeOgKolonneDerÆndres(placering)
    #dette er manual funktion : spillepladen[2][2]='x'
    spillepladen[tupel[0]][tupel[1]]=træk # her automatiseres valget, hvor der findes indeksene og træk kan indsættes.
    global hvilken_tur
    if hvilken_tur == 'O':
        hvilken_tur = 'X'
    else:
        hvilken_tur = 'O'
    hvis_plade()



def computerLavTræk():
    # Ændrer 'X' til det modsatte af spillerens valgte identitet
    randomTal = random.randrange(1, 10)
    placer_træk(randomTal, 'O' if spillerens_identitet == 'X' else 'X') if valgtePlaceringErTom(randomTal) else computerLavTræk()


while hvem_starter==None:
    try:
        hvem_starter = int(input("Hvem skal starte?. Tryk 1 hvis du vil starte og tryk 2 hvis computeren skal starte! "))
        spillerens_identitet = 'X' if hvem_starter==1 else 'O'
    except:
        print("det var vist ikke et tal du skrev der. prøv igen")
        continue


def checkHvemDerHarVundet():
    global er_spilletslut
    for i in range(len(succesfuldetræk)):
        if all(element in xPos for element in succesfuldetræk[i]):
            if spillerens_identitet == 'X':
                print("Vinderen er fundet. Fedt du vinder over computeren !")
            else:
                 print("Nederen at du taber til computeren")
                 er_spilletslut = True
    for i in range(len(succesfuldetræk)):
        if all(element in oPos for element in succesfuldetræk[i]):
            if spillerens_identitet == 'O':
                print("Vinderen er fundet. Fedt du vinder over computeren !")
            else:
                 print("Nederen at du taber til computeren")
                 er_spilletslut = True



while er_spilletslut == False:
    if len(xPos)+len(oPos) == 9:
        print("ingen spiller vandt")
        er_spilletslut = True
        break
    if hvilken_tur==spillerens_identitet:
        try:
            placering= int(input('vælg et tal fra 1-9 alt efter hvor du vil placere din brik: '))
            if placering <1 or placering >9:
                raise TypeError("tallet skal være imellem 1 og 9")
            if valgtePlaceringErTom(placering):
                placer_træk(placering,spillerens_identitet)
            else:
                raise TypeError("placeringen er ikke tom!")
# typeerror er når man prøver at gøre noget som i realiteten ikke er tilladt.
        except TypeError as e:
            print("")
            print(e)
            continue
        except ValueError:# hvis det ikke er et tal så bliver følgende printet, og valuerror bliver raised.
            print("")
            print("Det ikke et tal")

    else:
        computerLavTræk()
    checkHvemDerHarVundet()



