from copy import deepcopy
from random import randint
from time import sleep
import os

clear = lambda: os.system('cls')

class Herni_pole:

    def __init__(self, rozmery_pole):
        self._rozmery = rozmery_pole
        self._prostredek = rozmery_pole // 2 + 1
        self._polickaCil = ((rozmery_pole - 1) * 4) - 1
        self._sloupec1 = 0
        self._sloupec2 = 0
        i = 0
        self.herni_pole = [['#' for i in range(rozmery_pole+2)] for j in range(rozmery_pole+2)]
        for i in range(rozmery_pole + 1):
            if i > 0 and i < rozmery_pole + 1:
                for j in range(rozmery_pole + 1):
                    if j > 0 and j < rozmery_pole + 1:
                        self.herni_pole[i][j] = " "
                    if j > self._prostredek - 2 and j < self._prostredek + 2:
                        self.herni_pole[i][j] = "□"
                        if self._sloupec1 == 0: 
                            self._sloupec1 = j
                        elif self._sloupec2 == 0:
                            self._sloupec2 = j + 1
                    if i > self._prostredek - 2 and i < self._prostredek + 2 and j > 0:
                        self.herni_pole[i][j] = "□"
                    if j > self._prostredek - 1 and j < self._prostredek + 1 and 1 < i < rozmery_pole:
                        self.herni_pole[i][j] = bcolors.Zluta + "▲" + bcolors.End
                        if i > 4 and i < self._prostredek:
                            self.herni_pole[i][j] = " "
                        if i > self._prostredek and i < self._rozmery - 3:
                            self.herni_pole[i][j] = " "
                    if j > self._prostredek - 1 and j < self._prostredek + 1 and self._prostredek < i < rozmery_pole:
                        self.herni_pole[i][j] = bcolors.Modra + "▲" + bcolors.End
                        if i > 4 and i < self._prostredek:
                            self.herni_pole[i][j] = " "
                        if i > self._prostredek and i < self._rozmery - 3:
                            self.herni_pole[i][j] = " "
                    if i > self._prostredek - 1 and i < self._prostredek + 1 and 1 < j < rozmery_pole:
                        self.herni_pole[i][j] = bcolors.Zelena + "▲" + bcolors.End
                        if j > 4 and j < self._prostredek:
                            self.herni_pole[i][j] = " "
                        if j > self._prostredek and j < self._rozmery - 3:
                            self.herni_pole[i][j] = " "
                    if i > self._prostredek - 1 and i < self._prostredek + 1 and self._prostredek < j < rozmery_pole:
                        self.herni_pole[i][j] = bcolors.Cervena + "▲" + bcolors.End
                        if j > 4 and j < self._prostredek:
                            self.herni_pole[i][j] = " "
                        if j > self._prostredek and j < self._rozmery - 3:
                            self.herni_pole[i][j] = " "
                    if i == self._prostredek and j == self._prostredek:
                        self.herni_pole[i][j] = bcolors.Ruzova + "Ω" + bcolors.End
        self._zelenySpawnR = self._sloupec1
        self._zelenySpawnS = 1
        self._CervenySpawnR = self._sloupec2
        self._CervenySPawnS = self._rozmery
        self._KuleSpawnR = 1
        self._KuleSpawnS = self._sloupec2
        self._ZaludySpawnR = self._rozmery
        self._ZaludySPawnS = self._sloupec1
        self.grid = deepcopy(self.herni_pole)

    def spawn_players(self):
        self.herni_pole[1][1] = "♠"
        self.herni_pole[1][2] = "♠"
        self.herni_pole[2][1] = "♠"
        zeleny1._radek = 1
        zeleny1._sloupec = 2
        zeleny2._radek = 2
        zeleny2._sloupec = 1
        zeleny3._radek = 1
        zeleny3._sloupec = 1

        self.herni_pole[self._rozmery][self._rozmery] = "♥"
        self.herni_pole[self._rozmery][self._rozmery - 1] = "♥"
        self.herni_pole[self._rozmery - 1][self._rozmery] = "♥"
        cerveny1._radek = self._rozmery
        cerveny1._sloupec = self._rozmery - 1
        cerveny2._radek = self._rozmery - 1
        cerveny2._sloupec = self._rozmery
        cerveny3._radek = self._rozmery
        cerveny3._sloupec = self._rozmery

        if players > 2:
            self.herni_pole[1][self._rozmery] = "♦"
            self.herni_pole[1][self._rozmery - 1] = "♦"
            self.herni_pole[2][self._rozmery] = "♦"
            kule1._radek = 1
            kule1._sloupec = self._rozmery - 1
            kule2._radek = 2
            kule2._sloupec = self._rozmery
            kule3._radek = 1
            kule3._sloupec = self._rozmery

            if players > 3:
                self.herni_pole[self._rozmery][1] = "♣"
                self.herni_pole[self._rozmery - 1][1] = "♣"
                self.herni_pole[self._rozmery][2] = "♣"
                zaludy1._radek = self._rozmery
                zaludy1._sloupec = 2
                zaludy2._radek = self._rozmery - 1
                zaludy2._sloupec = 1
                zaludy3._radek = self._rozmery
                zaludy3._sloupec = 1
        
    def spawn_powerUps(self):
        self.herni_pole[self._sloupec1][self._sloupec1] = bcolors.Ruzova + "■" + bcolors.End
        self.herni_pole[self._sloupec1][self._sloupec2] = bcolors.Ruzova + "■" + bcolors.End
        self.herni_pole[self._sloupec2][self._sloupec1] = bcolors.Ruzova + "■" + bcolors.End
        self.herni_pole[self._sloupec2][self._sloupec2] = bcolors.Ruzova + "■" + bcolors.End

    #Přetvoření do defaultní mapy
    def cleargrid(self):
        self.herni_pole = deepcopy(self.grid)

    #Zakreslení objektů do defaultní mapy
    def draw_gui(self):
        clear()
        self.cleargrid()
        if powerup1._spawned == True:
            self.herni_pole[powerup1._radek][powerup1._sloupec] = bcolors.Ruzova + "■" + bcolors.End
        if powerup2._spawned == True:
            self.herni_pole[powerup2._radek][powerup2._sloupec] = bcolors.Ruzova + "■" + bcolors.End
        if powerup3._spawned == True:
            self.herni_pole[powerup3._radek][powerup3._sloupec] = bcolors.Ruzova + "■" + bcolors.End
        if powerup4._spawned == True:
            self.herni_pole[powerup4._radek][powerup4._sloupec] = bcolors.Ruzova + "■" + bcolors.End
        self.herni_pole[zeleny1._radek][zeleny1._sloupec] = bcolors.Zelena + "♠" + bcolors.End
        self.herni_pole[zeleny2._radek][zeleny2._sloupec] = bcolors.Zelena + "♠" + bcolors.End
        self.herni_pole[zeleny3._radek][zeleny3._sloupec] = bcolors.Zelena + "♠" + bcolors.End
        self.herni_pole[cerveny1._radek][cerveny1._sloupec] = bcolors.Cervena + "♥" + bcolors.End
        self.herni_pole[cerveny2._radek][cerveny2._sloupec] = bcolors.Cervena + "♥" + bcolors.End
        self.herni_pole[cerveny3._radek][cerveny3._sloupec] = bcolors.Cervena + "♥" + bcolors.End
        if players > 2:
            self.herni_pole[kule1._radek][kule1._sloupec] = bcolors.Zluta + "♦" + bcolors.End
            self.herni_pole[kule2._radek][kule2._sloupec] = bcolors.Zluta + "♦" + bcolors.End
            self.herni_pole[kule3._radek][kule3._sloupec] = bcolors.Zluta + "♦" + bcolors.End
            if players > 3:
                self.herni_pole[zaludy1._radek][zaludy1._sloupec] = bcolors.Modra + "♣" + bcolors.End
                self.herni_pole[zaludy2._radek][zaludy2._sloupec] = bcolors.Modra + "♣" + bcolors.End
                self.herni_pole[zaludy3._radek][zaludy3._sloupec] = bcolors.Modra + "♣" + bcolors.End
        for radek in self.herni_pole:
            print(" ".join(radek))

class bcolors:
    Ruzova = '\033[95m'
    Modra = '\033[94m'
    Zelena = '\033[92m'
    Zluta = '\033[93m'
    Cervena = '\033[91m'
    End = '\033[0m'

class Figurka:

    def __init__(self, poradi, team, barvicka ,spawnR, spawnS, spawnPoleR, spawnPoleS, fronta):
        self._barva = team
        self._barvicka = barvicka
        self._fronta = fronta
        self._poradi = poradi
        self._mana = 0
        self._power = 0
        self._radek = 0
        self._sloupec = 0
        self._vzdalenost = 0
        self._radekAcc = 0
        self._sloupecAcc = 0
        self._vzdalenostAcc = 0
        self._spawnR = spawnR
        self._spawnS = spawnS
        self._spawnPoleR = spawnPoleR
        self._spawnPoleS = spawnPoleS
        self._spawned = False
        self._cil = False
    
    #Move funkce
    def move(self, cisloKostka, figurka, fronta):  
        figurka._radekAcc = figurka._radek
        figurka._sloupecAcc = figurka._sloupec

        while cisloKostka > 0:
            #Move funkce v poli
            if figurka._radek == hraci_pole._prostredek - 1 and figurka._sloupec < hraci_pole._prostredek - 1:
                self.updatePos(0, 1)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.powerCheck(figurka, powerup1)
                    self.dokonceniKola(figurka)
                    break
            if figurka._radek <= hraci_pole._prostredek - 1 and figurka._sloupec == hraci_pole._prostredek - 1 and figurka._radek != 1:
                self.updatePos(-1, 0)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
            if figurka._radek == 1 and figurka._sloupec <= hraci_pole._prostredek:
                if figurka._vzdalenost == hraci_pole._polickaCil:
                    figurka._cil = True
                    activePlayers.remove(figurka)
                    figurka._spawned = False
                    fronta.dequeue()
                    self.updatePos(1, 0)
                else:
                    self.updatePos(0, 1)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
            if figurka._sloupec == hraci_pole._prostredek + 1 and figurka._radek < hraci_pole._prostredek - 1:
                self.updatePos(1, 0)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.powerCheck(figurka, powerup2)
                    self.dokonceniKola(figurka)
                    break
            if figurka._radek == hraci_pole._prostredek - 1 and figurka._sloupec > hraci_pole._prostredek and figurka._sloupec != hraci_pole._rozmery:
                self.updatePos(0, 1)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
            if figurka._sloupec == hraci_pole._rozmery and figurka._radek <= hraci_pole._prostredek:
                if figurka._vzdalenost == hraci_pole._polickaCil:
                    figurka._cil = True
                    activePlayers.remove(figurka)
                    figurka._spawned = False
                    fronta.dequeue()
                    self.updatePos(0, -1)
                else:
                    self.updatePos(1, 0)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
            if figurka._radek == hraci_pole._prostredek + 1 and figurka._sloupec > hraci_pole._prostredek + 1:
                self.updatePos(0, -1)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.powerCheck(figurka, powerup3)
                    self.dokonceniKola(figurka)
                    break
            if figurka._sloupec == hraci_pole._prostredek + 1 and figurka._radek > hraci_pole._prostredek and figurka._radek != hraci_pole._rozmery:
                self.updatePos(1, 0)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
            if figurka._radek == hraci_pole._rozmery and figurka._sloupec >= hraci_pole._prostredek:
                if figurka._vzdalenost == hraci_pole._polickaCil:
                    figurka._cil = True
                    activePlayers.remove(figurka)
                    figurka._spawned = False
                    fronta.dequeue()
                    self.updatePos(-1, 0)
                else:
                    self.updatePos(0, -1)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
            if figurka._sloupec == hraci_pole._prostredek - 1 and figurka._radek > hraci_pole._prostredek and figurka._radek != hraci_pole._prostredek + 1:
                self.updatePos(-1, 0)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.powerCheck(figurka, powerup4)
                    self.dokonceniKola(figurka)
                    break
            if figurka._radek == hraci_pole._prostredek + 1 and figurka._sloupec > 1 and figurka._sloupec < hraci_pole._prostredek:
                self.updatePos(0, -1)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
            if figurka._sloupec == 1 and figurka._radek >= hraci_pole._prostredek:
                if figurka._vzdalenost == hraci_pole._polickaCil:
                    figurka._cil = True
                    activePlayers.remove(figurka)
                    figurka._spawned = False
                    fronta.dequeue()
                    self.updatePos(0, 1)
                else:
                    self.updatePos(-1, 0)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
                
            #Move funkce v domečku
            if figurka._sloupec >= 1 and figurka._radek == hraci_pole._prostredek and figurka._sloupec <= hraci_pole._prostredek - 1 and figurka._vzdalenost > hraci_pole._polickaCil:
                self.updatePos(0, 1)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
            if figurka._radek >= 1 and figurka._sloupec == hraci_pole._prostredek and figurka._radek <= hraci_pole._prostredek and figurka._vzdalenost > hraci_pole._polickaCil:
                self.updatePos(1, 0)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
            if figurka._sloupec > hraci_pole._prostredek and figurka._radek == hraci_pole._prostredek and figurka._sloupec >= hraci_pole._prostredek - 1 and figurka._vzdalenost > hraci_pole._polickaCil:
                self.updatePos(0, -1)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
            if figurka._radek > hraci_pole._prostredek and figurka._sloupec == hraci_pole._prostredek and figurka._radek >= hraci_pole._prostredek + 1 and figurka._vzdalenost > hraci_pole._polickaCil:
                self.updatePos(-1, 0)
                cisloKostka = cisloKostka - 1
                hraci_pole.draw_gui()
                hodilJste()
                sleepCas()
                if cisloKostka == 0:
                    self.dokonceniKola(figurka)
                    break
        self._vzdalenostAcc = 0

    def dokonceniKola(self, figurka):
        self.selfDespawn(figurka, figurka._barvicka)
        self.despawnCheck(figurka, activePlayers)
        hraci_pole.draw_gui()
        hodilJste()
        sleepCas()
 
    #Přidání powerupu figurce
    def powerCheck(self, figurka, powerup):
        if powerup._spawned == True and powerup._radek == figurka._radek and powerup._sloupec == figurka._sloupec:
            figurka._power = figurka._power + 1
            powerup._spawned = False
    
    #Updatování pozice figurky
    def updatePos(self, r, s):
        self._vzdalenostAcc = self._vzdalenostAcc + 1
        self._vzdalenost = self._vzdalenost + 1
        self._sloupec = self._sloupec + s
        self._radek = self._radek + r

    #Updatování pozice figurky, pokud by figurka stoupla na figurku stejné barvy
    def downPos(self, r, s, v, fronta):
        self._vzdalenost = self._vzdalenost - v
        if self._cil == True:
            fronta._items.append(self)
            self._cil = False
            activePlayers.append(self)
        self._spawned = True
        self._sloupec = s
        self._radek = r
    
    #Oznámení o pokusu vyhození figurky figurkou stejné barvy
    def selfDespawnWarn(self, figurka):
        self.downPos(figurka._radekAcc, figurka._sloupecAcc, figurka._vzdalenostAcc, figurka._fronta)
        hraci_pole.draw_gui()
        print("Nesmíš se vyhodit, tvoje kolo se přeskakuje!")
        sleep(3)
    
    #Zjišťování zda se na cílovém políčku nachází figurka stejné barvy
    def selfDespawn(self, figurka, barvicka):
        if barvicka == "♠":
            if figurka._radek == zeleny1._radek and figurka._sloupec == zeleny1._sloupec and figurka != zeleny1:
                self.selfDespawnWarn(figurka)
            elif figurka._radek == zeleny2._radek and figurka._sloupec == zeleny2._sloupec and figurka != zeleny2:
                self.selfDespawnWarn(figurka)
            elif figurka._radek == zeleny3._radek and figurka._sloupec == zeleny3._sloupec and figurka != zeleny3:
                self.selfDespawnWarn(figurka)
        elif barvicka == "♥":
            if figurka._radek == cerveny1._radek and figurka._sloupec == cerveny1._sloupec and figurka != cerveny1:
                self.selfDespawnWarn(figurka)
            elif figurka._radek == cerveny2._radek and figurka._sloupec == cerveny2._sloupec and figurka != cerveny2:
                self.selfDespawnWarn(figurka)
            elif figurka._radek == cerveny3._radek and figurka._sloupec == cerveny3._sloupec and figurka != cerveny3:
                self.selfDespawnWarn(figurka)
        elif barvicka == "♦":
            if figurka._radek == kule1._radek and figurka._sloupec == kule1._sloupec and figurka != kule1:
                self.selfDespawnWarn(figurka)
            elif figurka._radek == kule2._radek and figurka._sloupec == kule2._sloupec and figurka != kule2:
                self.selfDespawnWarn(figurka)
            elif figurka._radek == kule3._radek and figurka._sloupec == kule3._sloupec and figurka != kule3:
                self.selfDespawnWarn(figurka)
        elif barvicka == "♣":
            if figurka._radek == zaludy1._radek and figurka._sloupec == zaludy1._sloupec and figurka != zaludy1:
                self.selfDespawnWarn(figurka)
            elif figurka._radek == zaludy2._radek and figurka._sloupec == zaludy2._sloupec and figurka != zaludy2:
                self.selfDespawnWarn(figurka)
            elif figurka._radek == zaludy3._radek and figurka._sloupec == zaludy3._sloupec and figurka != zaludy3:
                self.selfDespawnWarn(figurka)

    #Zjištění zda figurka vyhodila jinou figurku
    def despawnCheck(self, figurka, active):
        delka = len(active)
        for x in range(delka):
            if active[x]._sloupec == figurka._sloupec and active[x]._radek == figurka._radek and figurka != active[x]:
                self.despawnWarn(active[x])
                break

    #Oznámení o vyhození figurky
    def despawnWarn(self, vyhozenej):
        self.despawn(vyhozenej)
        hraci_pole.draw_gui()
        print("Vyhodil si hráče " + vyhozenej._barvicka + "!")
        sleep(3)

    #Updatování pozice vyhozené figurky
    def despawn(self, vyhozenej):
        vyhozenej._spawned = False
        vyhozenej._vzdalenost = 0
        vyhozenej._mana = 0
        vyhozenej._power = 0
        vyhozenej._radek = vyhozenej._spawnR
        vyhozenej._sloupec = vyhozenej._spawnS
        activePlayers.remove(vyhozenej)
        for x in range(len(zelenyFronta._items)):
            if zelenyFronta._items[x] == vyhozenej:
                zelenyFronta._items.remove(vyhozenej)
                break
        for x in range(len(cervenyFronta._items)):
            if cervenyFronta._items[x] == vyhozenej:
                cervenyFronta._items.remove(vyhozenej)
                break
        for x in range(len(kuleFronta._items)):
            if kuleFronta._items[x] == vyhozenej:
                kuleFronta._items.remove(vyhozenej)
                break
        for x in range(len(zaludyFronta._items)):
            if zaludyFronta._items[x] == vyhozenej:
                zaludyFronta._items.remove(vyhozenej)
                break

class Powerup:

    def __init__(self, r, s):
        self._radek = r
        self._sloupec = s
        self._spawned = True

class Kostka:

    def __init__(self):
        self._hozeneCislo = 0
    
    def hodit(self):
        self._hozeneCislo = randint(1, 6)
        #self._hozeneCislo = int(input("Cislo: "))
        print("Hodil jste: " + str(self._hozeneCislo))
        return self._hozeneCislo

class Fronta:

    def __init__(self, items = None):
        if items == None:
            self._items = []

    #Řadící algoritmus
    def enqueue(self):
        memory = ""
        last = 0
        try:
            memory = self._items[0]
        except:
            return
        for x in range(len(self._items) - 1):
            self._items[x] = self._items[x + 1]
            last = last + 1
        if memory != "":
            self._items[last] = memory

    #Vyhození figurky z fronty
    def dequeue(self):
        self._items.pop(0)

    def printstr(self):
        for x in range(len(self._items)):
            print(str(self._items[x]._sloupec) + " " + str(self._items[x]._radek))

def hodilJste():
    print("Hodil jste: " + str(kostka._hozeneCislo))

#spawn funkce pro objekty
def spawn(figurka):
    if hraci_pole.herni_pole[figurka._spawnPoleR][figurka._spawnPoleS] == "□" or figurka._barvicka:
        if figurka._barvicka == hraci_pole.herni_pole[figurka._spawnPoleR][figurka._spawnPoleS]:
            print("Nesmíš se vyhodit, tvoje kolo se přeskakuje!")
            sleep(3)
        else:
            hraci_pole.herni_pole[figurka._radek][figurka._sloupec] = " "
            hraci_pole.herni_pole[figurka._spawnPoleR][figurka._spawnPoleS] = figurka._barvicka
            figurka._spawned = True
            figurka._radek = figurka._spawnPoleR
            figurka._sloupec = figurka._spawnPoleS
            figurka._fronta._items.append(figurka)
            activePlayers.append(figurka)
            figurka._fronta.enqueue()
            figurka.despawnCheck(figurka, activePlayers)
    else:
        hraci_pole.herni_pole[figurka._radek][figurka._sloupec] = " "
        hraci_pole.herni_pole[figurka._spawnPoleR][figurka._spawnPoleS] = figurka._barvicka
        figurka._spawned = True
        figurka._radek = figurka._spawnPoleR
        figurka._sloupec = figurka._spawnPoleS
        figurka._fronta._items.append(figurka)
        activePlayers.append(figurka)
        figurka._fronta.enqueue()
        figurka.despawnCheck(figurka, activePlayers)

#Funkce pro zjištění výherce
def win():
    winString = ""
    if zeleny1._cil == True and zeleny2._cil == True and zeleny3._cil == True:
        winString = bcolors.Zelena + "♠" + bcolors.End
    elif cerveny1._cil == True and cerveny2._cil == True and cerveny3._cil == True:
        winString = bcolors.Cervena + "♥" + bcolors.End
    elif kule1._cil == True and kule2._cil == True and kule3._cil == True:
        winString =  bcolors.Zluta + "♦" + bcolors.End
    elif zaludy1._cil == True and zaludy2._cil == True and zaludy3._cil == True:
        winString = bcolors.Modra + "♣" + bcolors.End
    return winString

#Funkce pro vrácení figurky, která je  pořadí
def poradiVypis(fronta, sFronta):
    if sFronta._items[0]._spawned == False and sFronta._items[1]._spawned == False and sFronta._items[2]._spawned == False:
        return sFronta._items[0]
    elif fronta._items[0]._spawned == True:
        return fronta._items[0]
    elif fronta._items[1]._spawned == True:
        return fronta._items[1]
    elif fronta._items[2]._spawned == True:
        return fronta._items[2]

#Funkce, která vrací ještě dostupné figurky
def dostupny(sFronta):
    if sFronta._items[0]._spawned == False and sFronta._items[0]._cil == False:
        return sFronta._items[0]
    elif sFronta._items[1]._spawned == False and sFronta._items[1]._cil == False:
        return sFronta._items[1]
    elif sFronta._items[2]._spawned == False and sFronta._items[2]._cil == False:
        return sFronta._items[2]

#Funkce pro zjištění, zda se figurka může hýbat
def moveDostupnost(figurka):
    if kostka._hozeneCislo + figurka._vzdalenost > hraci_pole._polickaCil + 3:
        if input("Ajajaj, přehodil si, tvoje kolo se přeskakuje!") == "q":
            quit()
    else:
        figurka.move(kostka._hozeneCislo, figurka, figurka._fronta)

#Funkce pro vykonání dashe
def dash(figurka):
    if figurka._mana == 3:
        if input("Chceš využít dash? (y/n) (Posunutí o 3 pole) ") == "y":
            figurka._mana = 0
            if 3 + figurka._vzdalenost > hraci_pole._polickaCil + 3:
                if input("Ajajaj, přehodil si, tvoje kolo se přeskakuje!") == "q":
                    quit()
            else:
                figurka.move(3, figurka, figurka._fronta)
    elif figurka._mana != 3:
        figurka._mana = figurka._mana + 1
    figurka._fronta.enqueue()

#Funkce pro vykonání powerupu
def power(figurka):
    if figurka._power > 0:
        if input("Chceš využít powerup? (y/n) (Posunutí o 1-6 polí) ") == "y":
            figurka._power = figurka._power - 1
            posun = int(input("O kolik polí (1-6) se chcete posunout? "))
            if posun > 0 and posun < 7:
                figurka.move(posun, figurka, figurka._fronta)
            else:
                print("Zadal si jiné číslo než 1-6, ztrácíš powerup!")
                sleep(3)                

def sleepCas():
    sleep(0.3)
    #sleep(0)


print(f"Vítá tě hra Boosted člověče nezlob se!\n")
print("Tato hra má stejná pravidla jako klasické člověče nezlob se, až na pár vyjímek.")
print("1: Každý hráč má pouze tři figurky.")
print(f"2: Nevybíráš si jakou figurkou budeš tahat, ale pořadí určuje prioritní fronta,\n   nejdříve hraje figurka jedna, poté dva, poté tři a tato rotace se opakuje.")
print("3: Pokud stoupneš na svojí figurku, tvé kolo se přeskakuje.")
print("4. Pokud hodíš 6 neházíš znovu a máš na výběr, zda chceš spawnout figurku.")
print("5. Pokud nemáš žádnou spawnutou figurku (nebo jsou v cíli), házíš třikrát.")
print("6: Pokud vstoupíš do domečku (▲), tvá figurka se stává nehratelnou.")
if input("Stiskni tlačítko pro pokračování! ") == "q":
    quit()
clear()
print("Tato boosted verze má také své vlastní prvky, jako jsou powerupy, dashe a mana.")
print(f"1: Powerupy (■) se nachází čtyři na každé mapě, pokud na toto políčko stoupneš,\n   tvá figurka získá powerup. Můžeš sebrat i všechny čtyři powerupy za jednu\n   figurku. Po sebrání powerupu máš možnost hrát znovu a sám si zvolit číslo (1-6)\n   o kolik se tvá figurka posune. Tato možnost se ti nabídne každé kolo, dokud jí\n   nevyužiješ nebo s figurkou nedojdeš do domečku.")
print(f"2: Mana je atribut každé figurky. Mana se ti nabije o jeden bod při každém tahu\n   figurky. Maximální počet many je tři. Při dosažení tohoto limutu získáš šanci\n   využít dash. Tato šance se ti nabídne také každé kolo.")
print("3: Dash je schopnost figurky se posunout o 3 políčka.")
if input("Stiskni tlačítko pro pokračování! ") == "q":
    quit()
clear()
print("Hru můžeš kdykoliv ukončit stisknutím tlačítka q.")
players = int(input("Kolik hráčů bude hrát? (2-4) "))
if players < 2 or players > 4:
    print("Zadal si jiné číslo než 2-4! Hra se ukončí.")
    sleep(5)
    quit()
rozmery_pole = int(input("Jakou chceš velikost mapy? (11-99) (pouze lichá čísla) "))
if rozmery_pole < 11 or rozmery_pole > 99:
    print("Zadal si jiné číslo než 11-99! Hra se ukončí.")
    sleep(5)
    quit()
if rozmery_pole % 2 != 1:
    print("Zadal jsi sudé číslo! Hra se ukončí.")
    sleep(5)
    quit()

winZeleny = False
winCerveny = False
winKule = False
winZaludy = False
cilAcc = 0
pocetHodu = 0
kostka = Kostka()
hraci_pole = Herni_pole(rozmery_pole)
zelenyFronta = Fronta()
zeleny1 = Figurka(1, "zeleny", bcolors.Zelena + "♠" + bcolors.End, 1, 2, hraci_pole._zelenySpawnR, hraci_pole._zelenySpawnS, zelenyFronta)
zeleny2 = Figurka(2, "zeleny", bcolors.Zelena + "♠" + bcolors.End, 2, 1, hraci_pole._zelenySpawnR, hraci_pole._zelenySpawnS, zelenyFronta)
zeleny3 = Figurka(3, "zeleny", bcolors.Zelena + "♠" + bcolors.End, 1, 1, hraci_pole._zelenySpawnR, hraci_pole._zelenySpawnS, zelenyFronta)
cervenyFronta = Fronta()
cerveny1 = Figurka(1, "cerveny", bcolors.Cervena + "♥" + bcolors.End, rozmery_pole, rozmery_pole - 1, hraci_pole._CervenySpawnR, hraci_pole._CervenySPawnS, cervenyFronta)
cerveny2 = Figurka(2, "cerveny", bcolors.Cervena + "♥" + bcolors.End, rozmery_pole - 1, rozmery_pole, hraci_pole._CervenySpawnR, hraci_pole._CervenySPawnS, cervenyFronta)
cerveny3 = Figurka(3, "cerveny", bcolors.Cervena + "♥" + bcolors.End, rozmery_pole, rozmery_pole, hraci_pole._CervenySpawnR, hraci_pole._CervenySPawnS, cervenyFronta)
kuleFronta = Fronta()
kule1 = Figurka(1, "kule", bcolors.Zluta + "♦" + bcolors.End, 1, rozmery_pole - 1, hraci_pole._KuleSpawnR, hraci_pole._KuleSpawnS, kuleFronta)
kule2 = Figurka(2, "kule", bcolors.Zluta + "♦" + bcolors.End, 2, rozmery_pole, hraci_pole._KuleSpawnR, hraci_pole._KuleSpawnS, kuleFronta)
kule3 = Figurka(3, "kule", bcolors.Zluta + "♦" + bcolors.End, 1, rozmery_pole, hraci_pole._KuleSpawnR, hraci_pole._KuleSpawnS, kuleFronta)
zaludyFronta = Fronta()
zaludy1 = Figurka(1, "zaludy", bcolors.Modra + "♣" + bcolors.End, rozmery_pole, 2, hraci_pole._ZaludySpawnR, hraci_pole._ZaludySPawnS, zaludyFronta)
zaludy2 = Figurka(2, "zaludy", bcolors.Modra + "♣" + bcolors.End, rozmery_pole - 1, 1, hraci_pole._ZaludySpawnR, hraci_pole._ZaludySPawnS, zaludyFronta)
zaludy3 = Figurka(3, "zaludy", bcolors.Modra + "♣" + bcolors.End, rozmery_pole, 1, hraci_pole._ZaludySpawnR, hraci_pole._ZaludySPawnS, zaludyFronta)
sZelenyFronta = Fronta()
sCervenyFronta = Fronta()
sKuleFronta = Fronta()
sZaludyFronta = Fronta()
sZelenyFronta._items.append(zeleny1)
sZelenyFronta._items.append(zeleny2)
sZelenyFronta._items.append(zeleny3)
sCervenyFronta._items.append(cerveny1)
sCervenyFronta._items.append(cerveny2)
sCervenyFronta._items.append(cerveny3)
sKuleFronta._items.append(kule1)
sKuleFronta._items.append(kule2)
sKuleFronta._items.append(kule3)
sZaludyFronta._items.append(zaludy1)
sZaludyFronta._items.append(zaludy2)
sZaludyFronta._items.append(zaludy3)
sKdoHraje = Fronta()
kdoHraje = Fronta()
sKdoHraje._items.append(sZelenyFronta)
sKdoHraje._items.append(sCervenyFronta)
kdoHraje._items.append(zelenyFronta)
kdoHraje._items.append(cervenyFronta)
if players > 2:
    sKdoHraje._items.append(sKuleFronta)
    kdoHraje._items.append(kuleFronta)
    if players > 3:
        sKdoHraje._items.append(sZaludyFronta)
        kdoHraje._items.append(zaludyFronta)
activePlayers = []
powerup1 = Powerup(hraci_pole._sloupec1, hraci_pole._sloupec1)
powerup2 = Powerup(hraci_pole._sloupec1, hraci_pole._sloupec2)
powerup3 = Powerup(hraci_pole._sloupec2, hraci_pole._sloupec2)
powerup4 = Powerup(hraci_pole._sloupec2, hraci_pole._sloupec1)
hraci_pole.spawn_players()
hraci_pole.spawn_powerUps()
hraci_pole.draw_gui()
kolo = 0

#Funkce pro samotný běh hry
if input("Začít hru? ") != "q":
    while (zeleny1._cil == False or zeleny2._cil == False or zeleny3._cil == False) and (cerveny1._cil == False or cerveny2._cil == False or cerveny3._cil == False) and (kule1._cil == False or kule2._cil == False or kule3._cil == False) and (zaludy1._cil == False or zaludy2._cil == False or zaludy3._cil == False):
        cilAcc = 0
        hraci_pole.draw_gui()
        if input("Na tahu je " + poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo])._barvicka + ". [" + str(poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo])._radek) + "][" + str(poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo])._sloupec) + "] P: " + str(poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo])._power) + " M: " + str(poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo])._mana) + "/3 Hodit kostkou? ") != "q":
            if sKdoHraje._items[kolo]._items[0]._spawned == False and sKdoHraje._items[kolo]._items[1]._spawned == False and sKdoHraje._items[kolo]._items[2]._spawned == False:
                while pocetHodu < 3:
                    kostka.hodit()
                    pocetHodu = pocetHodu + 1
                    if kostka._hozeneCislo > 5:
                        spawn(dostupny(sKdoHraje._items[kolo]))
                        hraci_pole.draw_gui()
                        if input("Vaše figurka byla spawnuta! Hodit kostkou? ") != "q":
                            poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo]).move(kostka.hodit(), poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo]), poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo])._fronta)
                            power(sKdoHraje._items[kolo]._items[0])
                            poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo])._mana = 1
                            kdoHraje._items[kolo].enqueue()
                            break
                        else:
                            quit()
                    if pocetHodu < 3:
                        if input("Hodit kostkou znovu? ") == "q":
                            quit()
                pocetHodu = 0
            else:
                kostka.hodit()
                if kostka._hozeneCislo == 6:
                    if sKdoHraje._items[kolo]._items[0]._spawned == False and sKdoHraje._items[kolo]._items[0]._cil == False or sKdoHraje._items[kolo]._items[1]._spawned == False and sKdoHraje._items[kolo]._items[1]._cil == False or sKdoHraje._items[kolo]._items[2]._spawned == False and sKdoHraje._items[kolo]._items[2]._cil == False:
                        hraci_pole.draw_gui()
                        if input("Hodil jste 6! Chcete spawnout další figurku? (y/n) ") == "y":
                            if sKdoHraje._items[kolo]._items[0]._spawned == False and sKdoHraje._items[kolo]._items[0]._cil == False:
                                spawn(dostupny(sKdoHraje._items[kolo]))
                                hraci_pole.draw_gui()
                            elif sKdoHraje._items[kolo]._items[1]._spawned == False and sKdoHraje._items[kolo]._items[1]._cil == False:
                                spawn(dostupny(sKdoHraje._items[kolo]))
                                hraci_pole.draw_gui()
                            elif sKdoHraje._items[kolo]._items[2]._spawned == False and sKdoHraje._items[kolo]._items[2]._cil == False:
                                spawn(dostupny(sKdoHraje._items[kolo]))
                                hraci_pole.draw_gui()
                        else:
                            poradi = poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo])
                            moveDostupnost(poradi)
                            if poradi._cil == False:
                                power(poradi)
                                dash(poradi)
                    else:
                        poradi = poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo])
                        moveDostupnost(poradi)
                        if poradi._cil == False:
                            power(poradi)
                            dash(poradi)
                else:
                    poradi = poradiVypis(kdoHraje._items[kolo], sKdoHraje._items[kolo])
                    moveDostupnost(poradi)
                    if poradi._cil == False:
                        power(poradi)
                        dash(poradi)
        else:
            quit()
        hraci_pole.draw_gui()
        cilAcc = 0
        sleep(0.5)
        if kolo < players - 1:
            kolo = kolo + 1
        else:
            kolo = 0
    if input("Vyhrál: " + win() + "! Pro ukončení stikni klávesu.") == "q":
        quit()
else:
    quit()