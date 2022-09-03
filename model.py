from curses import noecho
import json
import random
DATOTEKA_S_STANJEM = "stanje.json"

NEOZNACENO = "n"
KRIZEC = "x"
KROG = "o"
MALI_ZMAGA = "mz"
MALI_PORAZ = "mp"
MALI_IZENACENO = "mi"
IZENACENO = "I"
PORAZ = "P"
ZMAGA = "Z"

class Kvadrat:
    #mamo slovar {polje:simbol}, tko nm je podan kvadratek
    def __init__(self, simboli=None):
        if simboli is None:
            simboli = {}
            for i in range(9):
                self.simboli[i] = NEOZNACENO
        else:
            self.simboli = simboli
    
    #seznam zasedenih polj (da lah pol ko bom buttone delala sam disabelam use zasedene)        
    def zasedena_polja(self):
        zasedena = []
        for i in range(9):
            if self.simboli[i] != NEOZNACENO:
                zasedena.append(i)
        return zasedena
        
    #polje je neka stevilka od 0 do 8 in tam se simbol zamenja z krizcem
    #(a morm ze zdej kej rect o nezasedenosti polja al bom pol to sam z buttoni uredila)
    def izberi_polje(self, polje):
        self.simboli[polje] = KRIZEC
    
    #izmed nezasedenih randomly izberemo 
    def odziv(self):
        nezasedena = []
        for i in range(9):
            if i not in self.zasedena_polja:
                nezasedena.append(i)
        polje = random.choice(nezasedena)
        self.simboli[polje] = KROG
        
    #preverimo najprej ce use ujema ksna od vrstic, pol ksn od stolpcev, pol ksn na diagonali
    #na konc se prevermo ce so ze usa mesta zasedena   
    def izid(self):
        izid = {KRIZEC:MALI_ZMAGA, KROG:MALI_PORAZ}
        for i in [KRIZEC, KROG]:
            for j in range(0,9,3):
                if self.simboli[j] == self.simboli[j+1] == self.simboli[j+2] == i:
                    return izid[i]
            for j in range(3):
                if self.simboli[j] == self.simboli[j+3] == self.simboli[j+6] == i:
                    return izid[i]
            if self.simboli[0] == self.simboli[4] == self.simboli[8] == i or self.simboli[2] == self.simboli[4] == self.simboli[6] == i:
                return izid[i]
        prazna_mesta = 0
        for i in range(9):
            if self.simboli[i] == NEOZNACENO:
                prazna_mesta += 1
        if prazna_mesta == 0:
            return MALI_IZENACENO
                
            
                
            
            
            
            

class Igra:
    
    def __init__(self, izbrana_polja, odzivi):
        self.izbrana_polja = izbrana_polja
        self.odzivi = odzivi