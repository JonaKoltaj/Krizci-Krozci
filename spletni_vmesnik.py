import bottle, model

SKRIVNOST = ":)"

krizcikrozci = model.KrizciKrozci()
krizcikrozci.nalozi_igre_iz_datoteke()

#odpre zacetno stran
@bottle.get("/")
def indeks():
    return bottle.template("views/index.tpl")

#zacne novo igro in jo zapise v datoteko pod primernim indeksom
@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = krizcikrozci.nova_igra()
    bottle.response.set_cookie('id_igre', id_igre, path="/", secret=SKRIVNOST)
    krizcikrozci.zapisi_igre_v_datoteko()
    return bottle.redirect("/igra/")

#igra je prikazana z 9x9 plosco narejeno iz gumbov, ki jih uporabnik pritisne da igra
@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    igra, stanje = krizcikrozci.igre[id_igre]
    igre = krizcikrozci.igre

    return bottle.template("views/igra.tpl", {'stanje': stanje, 'model': model, 'igra': igra, 'id_igre': id_igre, 'igre': igre})

#ko igralec pritisne gumb, se izpisejo koordinate gumba in ustrezno spremenijo znak na tem mestu
@bottle.post("/igra/")
def izberi():
    #zapisemo koordinate v obliki stevilk od 0 do 8 za tako kvadrat kot polje
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    button = bottle.request.forms.move
    koordinate = button.split(",")
    kvadrat = 3*int(koordinate[0]) + int(koordinate[1])
    polje = 3*int(koordinate[2]) + int(koordinate[3])
    #spremenimo znak na tem polju
    krizcikrozci.izberi_polje(id_igre, kvadrat, polje)
    #odziv racunalnika
    krizcikrozci.odziv(id_igre)
    krizcikrozci.zapisi_igre_v_datoteko()
    return bottle.redirect("/igra/")

@bottle.get("/img/<picture>")
def slike(picture):
    return bottle.static_file(picture, root="img")

bottle.run(reloader=True, debug=True)