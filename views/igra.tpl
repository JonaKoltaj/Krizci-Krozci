%import json
%rebase('base.tpl', title="KrizciKrozci")

% if stanje != model.ZMAGA and stanje != model.PORAZ:
  <form action="" method="post">
    <table>
        %for Vrstica in range(3):
        <tr>
            %for Stolpec in range(3):
            <td>
                <table>
                    %for vrstica in range(3):
                    <tr>
                        %for stolpec in range(3):
                        <td>
                            <input type="submit" name="move" value="{{Vrstica}},{{Stolpec}},{{vrstica}},{{stolpec}}">
                            {{igra.kvadrati[3*Vrstica + Stolpec].simboli[3*vrstica + stolpec]}}
                            </input>
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