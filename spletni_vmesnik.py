import bottle, model

SKRIVNOST = ":)"

krizcikrozci = model.KrizciKrozci()
krizcikrozci.nalozi_igre_iz_datoteke()

@bottle.get("/")
def indeks():
    return bottle.template("views/index.tpl")

@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = krizcikrozci.nova_igra()
    bottle.response.set_cookie('id_igre', id_igre, path="/", secret=SKRIVNOST)
    krizcikrozci.zapisi_igre_v_datoteko()
    return bottle.redirect("/igra/")

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    igra, stanje = krizcikrozci.igre[id_igre]
    plosca = igra.kvadrati()
    kvadrat = igra.simboli()

    return bottle.template("views/igra.tpl", {'stanje': stanje, 'model': model, 'plosca': plosca, 'kvadrat': kvadrat})

@bottle.post("/igra/")
def izberi():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    button = bottle.request.forms.move
    krizcikrozci.izberi_polje(id_igre, button)
    krizcikrozci.zapisi_igre_v_datoteko()
    return bottle.redirect("/igra/")


bottle.run(reloader=True, debug=True)