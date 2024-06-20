|external-link| `English <https://peter88213.github.io/nvhelp-en/nv_editor/>`__

.. |external-link| image:: ../_images/external-link.png

-----------------

=========
nv_editor
=========

**Benutzerhandbuch**

.. hint::
   Die deutsche Übersetzung des *novelibre*-Benutzerhandbuchs ist noch in Arbeit.
   Im Zweifelsfall könnnen Sie von dieser Seite aus zur englischen Version 
   des Benutzerhandbuchs wechseln (Link s.o.).

Diese Seite gilt für die neueste Ausgabe von `nv_editor
<https://github.com/peter88213/nv_editor/>`__.
Sie können sie mit **Hilfe > Editor-Plugin Online-Hilfe** öffnen.


Das Plugin installieren
-----------------------

- Entpacken Sie die heruntergeladene Zip-Datei in einen neuen Ordner.
- Gehen Sie in diesen Ordner und führen Sie **setup.pyw** aus. Damit installieren Sie das Plugin.

Das Plugin fügt dem *novelibre*-**Abschnitt**-Menü
den Eintrag **Bearbeiten** hinzu,
und dem **Hilfe**-Menü den Eintrag **Editor-Plugin Online-Hilfe**.


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
-  Auswahl erweitern mit ``⇧``-``Pfeil``.
-  Auswahl bis zum nächsten Wort erweitern mit ``Strg``-``⇧``-``Pfeil``.
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
-  ``Strg``-``Y``stellt den zuletzt rückgängig genachten Bearbeitungsschritt wieder her.
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
-  Der Editor lädt den neuen Abschnitt.


Einen Abschnitt erzeugen
------------------------

Mit **Datei > Abschnitt erzeugen** or ``Strg``-``Alt``-``N``,
können Sie erzeugen a section.

-  Der neue Abschnitt is placed after the currently edited section.
-  Der neue Abschnitt is of the same type as the currently edited section.
-  Der Editor lädt den neuen Abschnitt.

Wortzählung
-----------

-  The section word count is displayed at the status bar at the bottom
   of the window.
-  By default, word count is aktualisierend manually, either by pressing the
   ``F5`` key, or via the **Wortzählung > Aktualisieren**-Menü entry.
-  The word count can be aktualisierend "live", i.e. just while entering text.
   This is enabled via the **Wortzählung > Laufende Aktualisierung einschalten**-Menü
   entry.
-  Live aktualisieren is disabled by the **Wortzählung > Laufende Aktualisierung ausschalten**
   Menüeintrag.

.. note::
   Live updating the word count is resource intensive and may slow down
   the program when editing big sections. This is why it’s disabled by
   default.


Änderungen übernehmen
---------------------

Mit ``Strg``-``S``,
können Sie apply changes to the section.
Then "Modified" status is displayed in *novelibre*.

-  If the project is locked in *novelibre*, you will be asked to unlock
   it before changes can be applied.

.. note::
   Before applying changes, the program checks the editor content for
   XML validity. Malformed XML will not be accepted. 


Das Editorfenster schließen
---------------------------

-  To close the editor window, click on the **Schließen** button,
   or just close the window.
-  Under Windows können Sie optionally exit with **Abschnitt > Beenden**
   or ``Alt``-``F4``.
-  Otherwise können Sie optionally exit with **Abschnitt > Beenden**
   or ``Strg``-``Q``.
-  When closing the editor window, you will be asked for applying changes.


