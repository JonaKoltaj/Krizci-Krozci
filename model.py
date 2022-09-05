import json
import random

DATOTEKA_S_STANJEM = "stanje.json"

NEOZNACENO = "n"
KRIZEC = "x"
KROG = "o"
ZMAGA = "w"
PORAZ = "l"
NEDOLOCENO = "nd"
POLNO = "f"

class Kvadrat:
    
    #na zacetku je izid nedoloceno, potem pa ali zmaga ali poraz
    #simboli je slovar {polje:simbol}, kjer je polje 0 do 8, simbol pa krizec/krog/neoznaceno
    def __init__(self, izid=None, simboli=None):
        if simboli is None:
            self.simboli = []
            for i in range(9):
                self.simboli[i] = NEOZNACENO
        else:
            self.simboli = simboli
        if izid is None:
            self.izid = NEDOLOCENO
        else:
            self.izid = izid
    
    #seznam nezasedenih polj       
    def nezasedena_polja(self):
        nezasedena = []
        for i in range(9):
            if self.simboli[i] == NEOZNACENO:
                nezasedena.append(i)
        return nezasedena
        
    #polje je neka stevilka od 0 do 8 in tam se simbol zamenja z krizcem
    #uporabnik bo mel na voljo samo nezasedena polja
    def izberi_polje(self, polje):
        self.simboli[polje] = KRIZEC
    
    #izmed nezasedenih nakljucno izberemo
    def odziv(self):
        polje = random.choice(self.nezasedena_polja())
        self.simboli[polje] = KROG
        
    #preverimo najprej ce use ujema ksna od vrstic, pol ksn od stolpcev, pol ksn na diagonali
    def getizid(self):
        if self.izid != NEDOLOCENO: return self.izid
        else:
            izid = {KRIZEC:ZMAGA, KROG:PORAZ}
            for i in [KRIZEC, KROG]:
                #vrstice 012, 345, 678
                for j in range(0,9,3):
                    if self.simboli[j] == self.simboli[j+1] == self.simboli[j+2] == i:
                        self.izid = izid[i]
                        return izid[i]
                #stolpci 036, 147, 258
                for j in range(3):
                    if self.simboli[j] == self.simboli[j+3] == self.simboli[j+6] == i:
                        self.izid = izid[i]
                        return izid[i]
                #diagonali
                if self.simboli[0] == self.simboli[4] == self.simboli[8] == i or self.simboli[2] == self.simboli[4] == self.simboli[6] == i:
                    self.izid = izid[i]
                    return izid[i]

    #preverimo, ce je ze use zasedeno
    def je_polno(self):
        polno = 0
        if self.nezasedena_polja() == []:
            spolno += 1
        return polno


class Igra:

    #kvadrati je seznam 9 kvadratov (po vrsti), zacnemo z praznimi kvadrati
    def __init__(self, kvadrati=None, trenutni_kvadrat=None):
        if kvadrati is None:
            self.kvadrati = []
            for i in range(9):
                self.kvadrati[i] = Kvadrat()
        else:
            self.kvadrati = kvadrati
        self.trenutni_kvadrat = trenutni_kvadrat
    
    #izberes polje v trenutnem kvadatu
    def izberi(self, polje):
        self.kvadrati[self.trenutni_kvadrat].izberi_polje(polje)
        
    #odziv racunalnika
    def odziv(self):
        self.kvadrati[self.trenutni_kvadrat].odziv()

    #izid celotne igre
    def izid(self):
        for i in [ZMAGA, PORAZ]:
            #vrstice 012, 345, 678
            for j in range(0,9,3):
                if self.kvadrati[j].getizid() == self.kvadrati[j+1].getizid() == self.kvadrati[j+2].getizid() == i:
                    return i
            #stolpci 036, 147, 258
            for j in range(3):
                if self.kvadrati[j].getizid() == self.kvadrati[j+3].getizid() == self.kvadrati[j+6].getizid() == i:
                    return i
            #diagonali
            if self.kvadrati[0].getizid() == self.kvadrati[4].getizid() == self.kvadrati[8].getizid() == i or self.kvadrati[2].getizid() == self.kvadrati[4].getizid() == self.kvadrati[6].getizid() == i:
                return i
    
def nova_igra():
    kvadrati = []
    for i in range(9):
        kvadrati.append(Kvadrat())
    return Igra(kvadrati)
            
class KrizciKrozci:
    datoteka_s_stanjem = DATOTEKA_S_STANJEM

    #zacnemo s praznim seznamom iger (ki je potem oblike {id igre: (igra, stanje)})
    def __init__(self):
        self.igre = {}

    #zaporedna stevilka igre
    def prost_id_igre(self):
        if not self.igre:
            return 0
        else:
            return int(max(self.igre.keys())) + 1
    
    #nova igra se zapise v urejen par (igra, nedoloceno), kjer je igra "prazna" plosca kvadratov
    def nova_igra(self):
        i = self.prost_id_igre()
        igra = nova_igra()
        self.igre[i] = (igra, NEDOLOCENO)
        return i
    
    #v trenutnem kvadratu (indeks od 0 do 8) izberemo polje (indeks od 0 do 8)
    def izberi_polje(self, i, polje):
        igra, stanje = self.igre[i]
        igra = igra.izberi(polje)
        self.igre[i] = (igra, stanje)
        
    #racunalnik se odzove
    def odziv_(self, i):
        igra, stanje = self.igre[i]
        igra = self.odziv()
        self.igre[i] = (igra, stanje)

    #najprej pretvorimo kvadrati v ustrezno obliko kvadrati_igre = [Kvadrat(), Kvadrat(),...], da je ustrezen atribut Igre
    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as d:
            zapis = json.load(d)
        for id_igre, (kvadrati, stanje) in zapis.items():
            kvadrati_igre =[]
            for (izid, simboli) in kvadrati:
                kvadrati_igre.append(Kvadrat(izid, simboli))
            self.igre[id_igre] = (Igra(kvadrati_igre), stanje)

    #zapis je slovar {id_igre: (kvadrati, stanje)}, kjer je kvadrati seznam parov[(izid, simboli)]
    def zapisi_igre_v_datoteko(self):
        zapis = {}
        for id_igre, (igra, stanje) in self.igre.items():
            kvadrati = []
            for kvadrat in igra.kvadrati:
                kvadrati.append((kvadrat.izid, kvadrat.simboli))
            zapis[id_igre] = (kvadrati, stanje)
        with open(self.datoteka_s_stanjem, "w") as d:
            json.dump(zapis, d)