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
ZACETEK = "z"

class Kvadrat:
    
    #na zacetku je izid nedoloceno, potem pa ali zmaga ali poraz
    #simboli je slovar {polje:simbol}, kjer je polje 0 do 8, simbol pa krizec/krog/neoznaceno
    #lahko so usa mesta zapolnjena ne glede na izid, ce so polna je variable=1, ce ne pa =0
    def __init__(self, izid=None, simboli=None):
        if simboli is None:
            simboli = {}
            for i in range(9):
                self.simboli[i] = NEOZNACENO
        else:
            self.simboli = simboli
        if izid is None:
            self.izid = NEDOLOCENO
        else:
            self.izid = izid
    
    #seznam nezasedenih polj (da lah pol ko bom buttone delala sam disabelam use zasedene)        
    def nezasedena_polja(self):
        nezasedena = []
        for i in range(9):
            if self.simboli[i] == NEOZNACENO:
                nezasedena.append(i)
        return nezasedena
        
    #polje je neka stevilka od 0 do 8 in tam se simbol zamenja z krizcem
    #uporabnik bo meu na voljo samo nezasedena polja
    def izberi_polje(self, polje):
        self.simboli[polje] = KRIZEC
    
    #izmed nezasedenih randomly izberemo 
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

    #kvadrati je seznam 9 kvadratov (po vrsti), zacnemo z default kvadrati
    def __init__(self, kvadrati=None):
        if kvadrati is None:
            self.kvadrati = []
            for i in range(9):
                self.kvadrati[i] = Kvadrat()
        else:
            self.kvadrati = kvadrati
            
    #kvadrat v katerem trenutno igramo, podan s stevilkami od 0 do 8
    #ce je zacetek igre mi imputamo kvadrat, ce ne pa nas preusmeri
    def trenutni_kvadrat(self, kvadrat):
        pass
    
    #izberes polje v trenutnem kvadatu
    def izberi(self, kvadrat, polje):
        self.kvadrati[kvadrat].izberi_polje(polje)
        
    #odziv racunalnika
    def odziv(self):
        kvadrat = random.choice(range(9))
        self.kvadrati[kvadrat].odziv()

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
            
class KrizciKrozci:
    datoteka_s_stanjem = DATOTEKA_S_STANJEM

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if not self.igre:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        i = self.prost_id_igre()
        igra = self.nova_igra()
        self.igre[i] = (igra, ZACETEK)
        return i
    
    def izberi_polje(self, i, polje):
        igra, stanje = self.igre[i]
        stanje = igra.izberi(polje).odziv()
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
            for i in igra.kvadrati:
                kvadrati.append((igra.kvadrati[i].izid, igra.kvadrati[i].simboli))
            zapis[id_igre] = (kvadrati, stanje)
        with open(self.datoteka_s_stanjem, "w") as d:
            json.dump(zapis, d)