%rebase('base.tpl', title="KrizciKrozci")

  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  <h2>Navodila</h2>
  <p>Plošča je sestavljena iz 3x3 kvadratov, kvadrat pa iz 3x3 polj, na katerih izbiramo simbole. Igrate kot križec, vaš cilj pa je zmagati, tako da na veliki plošči dobite tri križce v vrsto. To se zgodi, ko na treh kvadratih v vrsti zmagate (tako da tam dobite tri križce v vrsto). Igra poteka tako, da začnete vi (na kateremkoli kvadratu), potem igra avtomatičen in naključen odziv (krožec), ki igra v kvadratu istega indeksa kot polje v kvadratu ki ste ga izbrali vi. Nadaljujete na kvadratu z indeksom polja, ki ga je izbral odziv v svojem kvadratu. Če ste poslani na kvadrat, ki je že zapolnjen, lahko izberete katerokoli prosto polje na plošči.</p>

  <style>
    h2 {
      font-family: 'Patrick Hand', cursive;
      font-size: 2em;
      margin-top: 50px;
    }
    p {
      font-family: 'Patrick Hand', cursive;
      max-width: 500px;
    }
  </style>