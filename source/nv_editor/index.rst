|external-link| `English <https://peter88213.github.io/nvhelp-en/nv_editor/>`__

.. |external-link| image:: ../_images/external-link.png

-----------------

=========
nv_editor
=========

**Benutzerhandbuch**

Diese Seite gilt für die neueste Ausgabe von `nv_editor
<https://github.com/peter88213/nv_editor/>`__.
Sie können sie mit **Hilfe > Editor-Plugin Online-Hilfe** öffnen.

Mit dem Abschnittseditor können Sie auf die Schnelle einzelne
Abschnitte bearbeiten und aufteilen.
Der Editor bietet einen Zugriff auf die interne Auszeichnung,
die HTML ähnelt.


Das Plugin installieren
-----------------------

- Starten Sie entweder die heruntergeladene Datei
  **nv_editor_vx.x.x.pyzw** durch Doppelklick (Windows/Linux-Desktop),
- oder führen Sie ```python nv_editor_vx.x.x.pyzw``` (Windows),
  bzw. ```python3 nv_editor_vx.x.x.pyzw``` (Linux) auf der Kommandozeile aus.

*"x.x.x"* ist dabei die Versionsnummer.

Das Plugin fügt dem *novelibre*-**Abschnitt**-Menü
den Eintrag **Bearbeiten** hinzu,
und dem **Hilfe**-Menü den Eintrag **Editor-Plugin Online-Hilfe**.


.. important::
   Viele Webbrowser erkennen den Download als ausführbare Datei
   und bieten an, sie direkt zu öffnen. 
   Damit wird die Installation gestartet.
   
   Abhängig von Ihren Sicherheitseinstellungen kann es allerdings 
   auch passieren, dass Ihr Browser den Download der ausführbaren 
   Datei zunächst verweigert. 
   In diesem Fall ist Ihre Bestätigung oder eine zusätzliche Handlung 
   erforderlich. 
   Falls das nicht geht, können Sie auf den Download der zip-Datei
   ausweichen. 
 
 
Den Abschnittseditor aufrufen
-----------------------------

Siw öffnen ein Editorfenster,
indem Sie im Projektbaum auf einen Abschnitt doppelklicken,
oder über den **Abschnitt > Bearbeiten**-Menüeintrag, wenn ein Abschnitt ausgewählt ist,
oder mit der Eingabetaste.

.. note::
   
   - Wenn das Projekt gesperrt ist, können keine Editorfenster geöffnet werden.
   - Wenn Sie einen Abschnitt auswählen, für den bereits ein Editorfenster offen ist, 
     wird dieses Fenster in den Vordergrund gebracht.


Text auswählen
--------------

-  Wortauswahl durch Doppelklick.
-  Absatzauswahl durch Dreifachklick.
-  Auswahl erweitern mit ``Umschalttaste``-``Pfeil``.
-  Auswahl bis zum nächsten Wort erweitern mit ``Strg``-``Umschalttaste``-``Pfeil``.
-  ``Strg``-``A`` wählt den gesamten Text aus.


Text kopieren/einfügen
----------------------

-  ``Strg``-``C`` kopiert den ausgewählten Text in die Zwischenablage.
-  ``Strg``-``X`` verschiebt den ausgewählten Text in die Zwischenablage.
-  ``Strg``-``V`` Fügt den Text aus der Zwischenablage an der Cursorposition ein.


Text formatieren
----------------

.. role:: html(code)
   :language: html


-  ``Strg``-``I`` umschließt den ausgewählten Text mit "Betont"-Markup,
   so wie hier:

   :html:`<em>Beispiel</em>`

   Falls die Auswahl bereits betont ist, wird das Markup entfernt.

-  ``Strg``-``B`` umschließt den ausgewählten Text mit "Stark betont"-Markup,
   so wie hier:

   :html:`<strong>Beispiel</strong>`

   Falls die Auswahl bereits stark betont ist, wird das Markup entfernt.

-  ``Strg``-``M`` entfernt "Betont" und "Stark betont"-Markup
   rund um die Auswahl.


Rückgängig machen/Wiederherstellen
----------------------------------

-  ``Strg``-``Z`` macht den letzten Bearbeitungsschritt rückgängig.
   Auch mehrfach möglich.
-  ``Strg``-``Y`` stellt den zuletzt rückgängig genachten Bearbeitungsschritt wieder her.
   Auch mehrfach möglich.


Einen Abschnitt teilen
----------------------

Mit **Datei > An der Cursorposition teilen** or ``Strg``-``Alt``-``S``,
können Sie den Abschnitt an der Corsorposition teilen.

-  Der gesamte Text ab der Cursorposition wird in einen neu erzeugten Abschnitt verschoben.
-  Der neue Abschnitt wird nach dem aktuell bearbeiteten Abschnitt platziert.
-  Der neue Abschnitt wird an den aktuell bearbeiteten Abschnitt
   `angehängt <../section_view.html#an-den-vorherigen-abschnitt-anhangen>`__.
-  Der neue Abschnitt hat denselben Fertigstellungstatus wie der aktuell bearbeitete.
-  Der neue Abschnitt ist vom selben Typ wie der aktuell bearbeitete.
-  Der neue Abschnitt hat dieselbe Perspektivfigur wie der aktuell bearbeitete.
-  Der Editor wechselt zum neuen Abschnitt.


Einen Abschnitt erzeugen
------------------------

Mit **Datei > Abschnitt erzeugen** or ``Strg``-``Alt``-``N``,
können Sie einen neuen Abschnitt erzeugen.

-  Der neue Abschnitt wird nach dem aktuell bearbeiteten Abschnitt platziert.
-  Der neue Abschnitt ist vom selben Typ wie der aktuell bearbeitete.
-  Der Editor wechselt zum neuen Abschnitt.

Wortzählung
-----------

-  Die Wortanzahl des bearbeiteten Abschnitts wird in der Statusleiste
   unten im Fenster angezeigt.
-  Standardmäßig wird die Wortzahl manuell aktualisiert,
   entweder durch Drücken der Taste ``F5``,
   oder über den Menübefehl **Wortzählung > Aktualisieren**.
-  Die Wortzahl kann auch laufend während der Texteingabe aktualisiert werden.
   Das wird über den Menüeintrag **Wortzählung > Laufende Aktualisierung einschalten**
   freigeschaltet.
-  Die laufende Wortzählung kann über **Wortzählung > Laufende Aktualisierung ausschalten**
   ausgeschaltet werden.

.. note::
   Die laufende Aktualisierung der Wortzahl kostet Rechenleistung
   und kann das Programm bei der Bearbeitung großer Abschnitte verlangsamen.
   Deshalb ist sie standardmäßig ausgeschaltet.


Änderungen übernehmen
---------------------

Mit ``Strg``-``S``,
können Sie die Änderungen für den Abschnitt übernehmen.
Dann zeigt *novelibre* den "Geändert"-Status an.

-  Falls das Projekt in *novelibre* gesperrt ist,
   werden Sie aufgefordert, es zu entsperren, bevor Änderungen übernommen werden.

.. note::
   Bevor es Änderungen übernimmt, prüft das Programm den Editorinhalt
   auf XML-Validität. Missgebildetes XML wird nicht akzeptiert.


Das Editorfenster schließen
---------------------------

-  Um die Bearbeitung zu beenden, klicken Sie auf die Schaltfläche **Schließen**,
   oder Sie wählen den Menüeintrag **Abschnitt > Beenden**,
   oder Sie schließen einfach das Fenster.
-  Unter Windows können Sie die Bearbeitung wahlweise mit ``Alt``-``F4`` beenden.
-  Andernfalls  können Sie die Bearbeitung wahlweise mit ``Strg``-``Q`` beenden.
-  Wenn Sie das Editorfenster schließen, werden Sie gegebenenfalls
   gefragt, ob Sie Änderungen übernehmen wollen.


