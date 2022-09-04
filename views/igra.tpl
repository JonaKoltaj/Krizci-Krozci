%rebase('base.tpl', title="KrizciKrozci")
#nared tuki krajse pa si zorganiziri kvadrate (a more bit usak kvadrat posebi??)
plosca = <table>
  <tr>
    <td>
        <button type="submit" name="move" value="0">
            kvadrat
        </button>
    </td>
    <td>
        <button type="submit" name="move" value="1">
            kvadrat
        </button>
    </td>
    <td>
        <button type="submit" name="move" value="2">
            kvadrat
        </button>
    </td>
  </tr>
  <tr>
    <tr>
    <td>
        <button type="submit" name="move" value="3">
            kvadrat
        </button>
    </td>
    <td>
        <button type="submit" name="move" value="4">
            kvadrat
        </button>
    </td>
    <td>
        <button type="submit" name="move" value="5">
            kvadrat
        </button>
    </td>
  </tr>
  <tr>
    <tr>
    <td>
        <button type="submit" name="move" value="6">
            kvadrat
        </button>
    </td>
    <td>
        <button type="submit" name="move" value="7">
            kvadrat
        </button>
    </td>
    <td>
        <button type="submit" name="move" value="8">
            kvadrat
        </button>
    </td>
  </tr>
</table>


% if stanje != model.ZMAGA and stanje != model.PORAZ:
  <form action="" method="post">
  <input name="crka" autofocus> <input type="submit" value="ugibaj">
  </form>

% elif stanje == model.ZMAGA:
Čestitke, zmagali ste! Bi želeli igrati še enkrat?
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% elif stanje == model.PORAZ:
Več sreče prihodnjič, geslo je bilo <b>{{celo_geslo}}</b>.<br>
Bi želeli igrati še enkrat?
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% end