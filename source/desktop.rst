Der Arbeitsbereich
==================


Der Arbeitsbereich von *novelibre* ist in drei Fenster unterteilt:

.. figure:: _images/desktop01.png
   :alt: Desktop

   Desktop


Projektbaum
-----------

Der Projektbaum im linken Fenster zeigt die Organisation des Projekts.

- Die Elemente des Baums sind entsprechend des Abschnittstyps eingefärbt
  (siehe `Grundlegende Konzepte <basic_concepts.html#teil-kapitel-abschnittstypen>`__).
  Abschnitte vom Typ *Normal* sind farblich hervorgehoben, je nach dem, welcher
  Farbgebungsmodus eingestellt ist (siehe *Optionen*
  im `Ansicht-Menü <view_menu.html#farbgebungsmodus>`__).
- Die Anordnung der Spalten kann geändert werden (siehe *Optionen* im
  `Ansicht-Menü <view_menu.html#spalten>`__).
- Beim Rechtsklick auf ein Baumelement öffnet sich ein `Kontextmenü
  <tree_context_menu.html>`__ mit verschiedenen Auswahlmöglichkeiten.
- Der Typ der Kapitel und Abschnitte kann ebenso wie der Fertigstellungs-
  status der Abschnitte über das Kontextmenü geändert werden.


Projektbaumstruktur
~~~~~~~~~~~~~~~~~~~

- Der **Buch**-Zweig umfasst die Teile, Kapitel und Abschnitte, die zum
  Romanmanuskript gehören.
- Die **Figuren/Schauplätze/Gegenstände**-Zweige enthalten Beschreibungen
  der Weltenbau-Elemente, die zu den Buchabschnitten in Beziehung gesetzt
  werden können.
- Der **Plotlinien**-Zweig umfasst die Plotlinien und Plotpunkte.
- Der **Projektnotizen**-Zweig enthält alle Projektnotizen.


Arbeiten im Projektbaum
~~~~~~~~~~~~~~~~~~~~~~~

Sich durch den Baum bewegen
   *novelibre* hat einen Browservelauf der ausgewählten Baumelemente.
   Damit kann man sich vor- und zurückbewegen, zum Beispiel zwischen einem
   Abschnitt und den Figuren, die in ihm vorkommen.

   -  |Gehe zurück| geht einen Knoten zurück in im Browserverlauf.
   -  |Gehe vor| geht einen Knoten vor in im Browserverlauf.

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
- Abschnitte werden als "unbenutzt" gekennzeichnet und ins
  "Papierkorb"-Kapitel verschoben.
-  Deleting a part has no effect on its subordinate chapters.
-  Deleting a chapter moves its sections to the "Papierkorb" chapter.
-  The "Papierkorb" chapter is created automatically, if needed.
-  When deleting the "Papierkorb" chapter, all its sections are gelöscht.


Textbetrachter
--------------

Der **Textbetrachter** im mitleren Fenster shows the part/chapter/section
contents with their Titels as headings.

-  You can open or close the Textbetrachter with **Ansicht > Toggle Text
   viewer**, or ``Strg``-``T``, or clicking on |Textbetrachter anzeigen/verbergen|.
-  On opening, the windows shows the text, where the tree is selected.
-  When changing the tree selection, the text moves along.
-  However, the text can be scrolled independently with the verical
   scrollbar, or the mousewheel.
-  You can select text with the mouse, and copy it to the clipboard with
   ``Strg``-``C``.
-  You cannot edit the text. For this, you might want to install an
   editor plugin, such as
   `nv_editor <https://github.com/peter88213/nv_editor/>`__.
-  Abschnitt text is color-coded according to the section type (see `Basic
   concepts <basic_concepts.html#teil-kapitel-abschnittstypen>`__).
-  Mit the **Markup anzeigen** checkbox, XML markup can be shown/hidden.


Eigenschaften
-------------

The `Eigenschaften <properties.html>`__ im rechten Fenster show properties
and metadata of the element selected in the project tree.

-  The project settings can be made in the *Buch* properties view.
-  You can open or close the element properties window with **Ansicht >
   Eigenschaften anzeigen/verbergen** or ``Strg``-``Alt``-``T``, or clicking on
   |Eigenschaften anzeigen/verbergen|.
-  On opening, the windows shows the editable properties of the selected
   element.
-  You can detach or dock the element properties window with **Ansicht >
   Eigenschaften abtrennen/andocken** or ``Strg``-``Alt``-``D``.
-  On closing the detached window, the properties are docked again.

On large screens, you can arrange *novelibre* and *Writer* with detached
windows.

.. figure:: _images/full_desktop.png
   :alt: Writer and novelibre screen arrangement
   
   Example: Arranging LibreOffice (middle) with detached Navigator (upper left) 
   and novelibre (lower left) with detached Eigenschaften (right) 


.. |Gehe zurück| image:: _images/goBack.png
.. |Gehe vor| image:: _images/goForward.png
.. |Textbetrachter anzeigen/verbergen| image:: _images/viewer.png
.. |Eigenschaften anzeigen/verbergen| image:: _images/properties.png


Menüleiste
----------

The bar at the top is the-Menü bar with the main-Menü,
which is documented in the `Befehlsreferenz <command_reference.html>`__.


Werkzeugleiste
--------------

The second bar from the top is the toolbar with
`Schaltflächen for frequently used actions <toolbar.html>`__.


Statusleiste
------------

The second bar from the bottom is the status bar. It normally displays project
statistics, such as word count. These are overwritten with program messages
when necessary.

- Messages on a green background indicate successful actions.
- Messages on a red background indicate errors or warnings.

.. tip::
   You can restore the normal view at any time by clicking on the status bar.
   

Fußzeile
--------

The footer bar at the bottom displays the project file path and the file date.

Change notification
   If there are unsaved changes, the footer bar is highlighted in goldenrod.

Project lock
   If the project is locked, the footer bar is displayed in reversed colors.


