%rebase('base.tpl', title="KrizciKrozci")
#nared tuki krajse pa si zorganiziri kvadrate (a more bit usak kvadrat posebi??) disable pa enable!!
kvadrat = <table>
  <tr>
    <td>
        <form action="" method="post"><button type="submit" name="move" value="0"></button></form>
    </td>
    <td>
        <form action="" method="post"><button type="submit" name="move" value="1"></button></form>
    </td>
    <td>
        <form action="" method="post"><button type="submit" name="move" value="2"></button></form>
    </td>
  </tr>
  <tr>
    <tr>
    <td>
        <form action="" method="post"><button type="submit" name="move" value="3"></button></form>
    </td>
    <td>
        <form action="" method="post"><button type="submit" name="move" value="4"></button></form>
    </td>
    <td>
        <form action="" method="post"><button type="submit" name="move" value="5"></button></form>
    </td>
  </tr>
  <tr>
    <tr>
    <td>
        <form action="" method="post"><button type="submit" name="move" value="6"></button></form>
    </td>
    <td>
        <form action="" method="post"><button type="submit" name="move" value="7"></button></form>
    </td>
    <td>
        <form action="" method="post"><button type="submit" name="move" value="8"></button></form>
    </td>
  </tr>
</table>

plosca = <table>
  <tr>
    <td>
        kvadrat
    </td>
    <td>
        kvadrat
    </td>
    <td>
        kvadrat
    </td>
  </tr>
  <tr>
    <tr>
    <td>
        kvadrat
    </td>
    <td>
        kvadrat
    </td>
    <td>
        kvadrat
    </td>
  </tr>
  <tr>
    <tr>
    <td>
        kvadrat
    </td>
    <td>
        kvadrat
    </td>
    <td>
        kvadrat
    </td>
  </tr>
</table>


% if stanje != model.ZMAGA and stanje != model.PORAZ:
  <form action="" method="post">
  <input name="move"> <input type="submit" value="izberi">
  </form>

% elif stanje == model.ZMAGA:
Čestitke, zmagali ste! Bi želeli igrati še enkrat?
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% elif stanje == model.PORAZ:
Več sreče prihodnjič:(
Bi želeli igrati še enkrat?
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% end