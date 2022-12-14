%import json
%rebase('base.tpl', title="KrizciKrozci")

<form action="" method="post">
  <table>
      %for Vrstica in range(3):
      <tr>
          %for Stolpec in range(3):
          <td>
              <!--ce je bil kvadrat zmagan/zgubljen, ga oznacimo kot takega-->
              <table class=
              %if igra.kvadrati[3*Vrstica + Stolpec].getizid() == model.ZMAGA:
                "krizec"
              %elif igra.kvadrati[3*Vrstica + Stolpec].getizid() == model.PORAZ:
                "krozec"
              %end
                >
                  %for vrstica in range(3):
                  <tr>
                      %for stolpec in range(3):
                      <td>
                          <!--vsi gumbi razen tisti v trenutnem kvadratu in vsi tisti ki so ze zapolnjeni so disabled-->
                          <!--ce smo ze zmagali ali zgubili ne moremo vec pritisniti gumba-->
                          <button type="submit" name="move" value="{{Vrstica}},{{Stolpec}},{{vrstica}},{{stolpec}}"
                          %if 3*Vrstica + Stolpec != igra.trenutni_kvadrat and igra.trenutni_kvadrat is not None:
                          disabled
                          %elif 3*vrstica + stolpec not in igra.kvadrati[3*Vrstica + Stolpec].nezasedena_polja():
                          disabled
                          %elif stanje == model.ZMAGA or stanje == model.PORAZ:
                          disabled
                          %end
                          >
                          {{igra.kvadrati[3*Vrstica + Stolpec].simboli[3*vrstica + stolpec]}}
                          </button>
                      </td>
                      %end
                  </tr>
                  %end
              </table>
          </td>
          %end
      </tr>
      %end
  </table>
</form>

%if stanje == model.ZMAGA:
Čestitke, zmagali ste!
Bi želeli igrati še enkrat?
  <form action="/nova_igra/" method="post">
    <input type="submit" value="Nova Igra"></input>
  </form>

% elif stanje == model.PORAZ:
Več sreče prihodnjič:(
Bi želeli igrati še enkrat?
  <form action="/nova_igra/" method="post">
    <input type="submit" value="Nova Igra"></input>
  </form>

%elif stanje == model.IZENACENO:
Izenačeno!
Bi želeli igrati še enkrat?
  <form action="/nova_igra/" method="post">
    <input type="submit" value="Nova Igra"></input>
  </form>

% end

<style>
  button {
    width: 2em;
    height: 2em;
    background-color: rgba(255, 255, 255, 0.5);
  }
  button:disabled {
    color:black
  }
  .krizec {
    background-image: url("/img/krizec.png");
    background-size: contain;
  }
  .krozec {
    background-image: url("/img/krozec.png");
    background-size: contain;
  }
</style> 