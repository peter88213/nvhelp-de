Der Arbeitsbereich
==================


Der Arbeitsbereich von *novelibre* ist in drei Fenster unterteilt:

.. figure:: _images/desktop01.png
   :alt: Arbeitsbereich

   Arbeitsbereich


Projektbaum
-----------

Der Projektbaum im linken Fenster zeigt die Organisation des Projekts.

- Die Elemente des Baums sind entsprechend des Abschnittstyps eingefärbt
  (siehe `Grundlegende Konzepte <basic_concepts.html#teil-kapitel-abschnittstypen>`__).
  Abschnitte vom Typ *Normal* sind farblich hervorgehoben, je nach dem, welcher
  Farbgebungsmodus eingestellt ist (siehe *Optionen*
  im `Ansicht-Menü <view_menu.html#farbgebungsmodus>`__).
- Die Reihenfolge der Spalten kann geändert werden (siehe *Optionen* im
  `Ansicht-Menü <view_menu.html#spalten>`__).
- Beim Rechtsklick auf ein Baumelement öffnet sich ein `Kontextmenü
  <tree_context_menu.html>`__ mit verschiedenen Auswahlmöglichkeiten.
- Der Typ der Kapitel und Abschnitte kann ebenso wie der Fertigstellungsstatus
  der Abschnitte über das Kontextmenü geändert werden.


Projektbaumstruktur
~~~~~~~~~~~~~~~~~~~

- Der **Buch**-Zweig umfasst die Teile, Kapitel und Abschnitte, die zum
  Romanmanuskript gehören.
- Die **Figuren/Schauplätze/Gegenstände**-Zweige enthalten Beschreibungen
  der Weltenbau-Elemente, die zu den Buchabschnitten in Beziehung gesetzt
  werden können.
- Der **Plotlinien**-Zweig umfasst die `Plotlinien und Plotpunkte
  <plotting.html#plotlinien-definieren>`__.
- Der **Projektnotizen**-Zweig enthält `Projektnotizen
  <project_note_view.html>`__.


Arbeiten im Projektbaum
~~~~~~~~~~~~~~~~~~~~~~~

Sich durch den Baum bewegen
   *novelibre* hat einen Browservelauf der ausgewählten Baumelemente.
   Damit kann man sich vor- und zurückbewegen, zum Beispiel zwischen einem
   Abschnitt und den Figuren, die in ihm vorkommen.

   - |Gehe zurück| geht einen Knoten zurück in im Browserverlauf.
   - |Gehe vor| geht einen Knoten vor in im Browserverlauf.

   .. hint::
      Unter Windows sollten die "Vor" und "Zurück"-Maustasten (falls 
      vorhanden) ebenfalls funktionieren.  


Baumelemente verschieben
^^^^^^^^^^^^^^^^^^^^^^^^

Bei gedrückter ``Alt``-Taste mit der Maus ziehen.

.. caution::
   Bitte daran denken, dass es keine "Rückgängig"-Funktion gibt.


Baumelemente löschen
^^^^^^^^^^^^^^^^^^^^

Das zu löschende Element auswählen und die ``Entf``-Taste drücken.

- Teile und Kapitel werden gelöscht.
- Abschnitte werden als "unbenutzt" gekennzeichnet und in den
  "Papierkorb" verschoben.
- Einen Teil zu löschen, hat keinen Einfluss auf nachgeordnete
  Kapitel.
- Wird ein Kapitel gelöscht, werden dessen Abschnitte in den
  "Papierkorb" verschoben.
- Das "Papierkorb"-Kapitel wird automatisch erstellt, wenn es gebraucht wird.
- Wird das "Papierkorb"-Kapitel gelöscht, löscht das auch die enthaltenen Abschnitte.


Textbetrachter
--------------

Der **Textbetrachter** im mittleren Fenster zeigt die Inhalte der Teile,
Kapitel und Abschnitte mit deren Titeln als Überschriften.

- Mit **Ansicht > Textbetrachter anzeigen/verbergen** oder ``Strg``-``T``
  oder Klick auf |Textbetrachter anzeigen/verbergen| kann man das mittlere
  Fenster mit dem Textbetrachter öffnen und schließen.
- Beim Öffnen zeigt der Textbetrachter den Text an der Stelle des aktuell
  gewählten Abschnitts an.
- Wird die Auswahl im Baum geändert, bewegt sich der angezeigte Text mit.
- Allerdings kann man den Text auch unabhängig davon mit dem Mausrad oder
  dem Scrollbalken scrollen.
- Man kann Text mit der Maus auswählen und mit ``Strg``-``C`` in die
  Zwischenablage kopieren.
- Man kann den Text nicht im Betrachter bearbeiten.
  Für so etwas benötigt man ein Editor-Plugin, wie zum Beispiel
  `nv_editor <https://github.com/peter88213/nv_editor/>`__.
- Der Abschnittstext ist entsprechend dem Abschnittstyp eingefärbt
  (siehe `Gtundlegende Konzepte <basic_concepts.html#teil-kapitel-abschnittstypen>`__).
- Mit dem Auswahlfeld **Markup anzeigen** kann man das XML-Markup
  anzeigen oder verbergen.


Eigenschaften
-------------

Die `Eigenschaften-Ansicht <properties.html>`__ im rechten Fenster zeigt
Eigenschaften und Metadaten des ausgewählten Baumelements an.

- Projekteinstellungen werden mit den *Buch*-Eigenschaften vorgenommen.
- Mit **Ansicht > Eigenschaften anzeigen/verbergen** oder ``Strg``-``Alt``-``T``
  oder Klick auf |Eigenschaften anzeigen/verbergen| kann man das rechte Fenster
  mit den Eigenschaften öffnen und schließen.
- Beim Öffnen zeigt das Fenster die Eigenschaften des aktuell gewählten
  Baumelements an.
- Mit **Ansicht > Eigenschaften abtrennen/andocken** oder ``Strg``-``Alt``-``D``
  kann man das Eigenschaftsfenster abtrennen und wieder andocken.
- Schließt man das abgetrennte Eigenschaftsfenster, wird es wieder angedockt.

Auf großen Bildschirmen kann man *novelibre* und *Writer* mit abgekoppelten
Fenstern anordnen.

.. figure:: _images/full_desktop.png
   :alt: Bildschirmanordnung von Writer und novelibre 
   
   Beispiel: LibreOffice (Mitte) mit abgetrenntem Navigator (oben links),
   und novelibre (unten links) mit abgetrennten Eigenschaften (rechts) 


.. |Gehe zurück| image:: _images/goBack.png
.. |Gehe vor| image:: _images/goForward.png
.. |Textbetrachter anzeigen/verbergen| image:: _images/viewer.png
.. |Eigenschaften anzeigen/verbergen| image:: _images/properties.png


Menüleiste
----------

Die Leiste ganz oben ist die Menüleiste mit dem Hauptmenü,
das in der `Befehlsreferenz <command_reference.html>`__
dokumentiert ist.


Werkzeugleiste
--------------

Die zweite Leiste von oben ist die Werkzeugleiste mit den
`Schaltflächen für häufige Vorgänge <toolbar.html>`__.


Statusleiste
------------

Die zweite Leiste von unten ist die Statusleiste.
Normalierweise zeigt sie statistische Angaben zum Projekt,
wie zum Beispiel die Wortzahl.
Bei Bedarf werden sie mit Meldungen des Programms überschrieben.

- Meldungen vor grünem Hintergrund zeigen erfolgreiche Vorgänge an.
- Meldungen vor rotem Hintergrund zeigen Warnungen oder Fehlermeldungen an.

.. tip::
   Die Normalansicht kann man jederzeit durch Klicken auf die 
   Statusleiste wiederherstellen.
   

Fußleiste
---------

Die Fußleiste ganz unten zeigt den Pfad und das Speicherdatum der Projektdatei an.

Änderungsanzeige
   Wenn es ungesicherte Änderungen gibt, ist die Fußleiste goldgelb.

Projektsperre
   Ist das Projekt gesperrt, wird die Fußleiste invertiert angezeigt.


