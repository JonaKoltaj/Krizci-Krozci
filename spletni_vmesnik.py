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

    return bottle.template("views/igra.tpl", {'stanje': stanje, 'model': model, 'plosca': plosca})

@bottle.post("/igra/")
def ugibaj():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    #kaj je bottle.request.forms??
    polje = bottle.request.forms.polje
    krizcikrozci.izberi_polje(id_igre, polje)
    krizcikrozci.zapisi_igre_v_datoteko()
    return bottle.redirect("/igra/")

@bottle.get("/img/<picture>")
def slike(picture):
    return bottle.static_file(picture, root="img")


bottle.run(reloader=True, debug=True)