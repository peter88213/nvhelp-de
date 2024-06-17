Plot-Menü
=========

**Plotelementfunktionen**

.. figure:: _images/plot_menu01.png
   :alt: novelibre Screenshot

Plotlinie hinzufügen
--------------------

**Eine neue Plotlinie erzeugen**

Mit **Plot > Plotlinie hinzufügen**
können eine Plotlinie
in den Baum einfügen.


.. note::

   -  If a Plotlinie is selected, the new item is placed after the selected one.
   -  Otherwise, the new Plotlinie is placed at the last position.
   -  The new Plotlinie has an auto-generated Titel. You can change it in the
      right pane.

Plotpunkt hinzufügen
--------------------

**Einen neuen Plotpunkt erzeugen**

Mit **Plot > Plotpunkt hinzufügen**
können Sie einer Plotlinie einen Plotpunkt hinzufügen.

.. note::

   - If a plot point is selected, the new plot point is placed after the selected one.
   - If a Plotlinie is selected, the new plot point is placed at the last position.
   - Otherwise, no new plot point is generated.
   - The new plot point has an auto-generated Titel. You can change it in
     the right pane.

Stadium einfügen
----------------

**Insert a stage between the sections**

Mit **Plot > Stadium einfügen**
können Sie ein Stadium hinter dem ausgewählten Kapitel oder Abschnitt einfügen.

.. hint::
   By default, the new stage is on the second level. 
   You can change the level to first (see below).

Ebene ändern
------------

**Change the level of the selected stages**

Mit **Plot > Ebene ändern**
können Sie change the level of the selected stages.

.. figure:: _images/plot_menu02.png
   :alt: novelibre Screenshot

-  **Erste Ebene** is displayed in bold face.
-  **Zweite Ebene** is displayed in regular font.

.. note::
   The stage level is only for visual distinction. It has no
   influence on the program functions. 


Handlungsraster (Plot grid) zum Bearbeiten exportieren
------------------------------------------------------

**Ein ODS-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Plot > Handlungsraster (Plot grid) zum Bearbeiten exportieren**
können Sie ein Tabellenkalkulationsdokument erzeugen, wie im Kapitel
`Mit novelibre plotten <plotting.html#handlungsraster-plot-grid>`__ beschrieben,
mit einer Zeile pro Abschnitt und folgenden Spalten:

- The sequential section number as a hyperlink to the section in the
  Manuskript (falls vorhanden)
- Erzähldatum
- Erzählzeit
- Tag
- Abschnittstitel
- Abschnittsbeschreibung
- Perspektive
- One column per Plotlinie with the section's Plotlinie notes
- Tags
- Szene
- Ziel/Reaktion/(benutzerdefiniert)
- Konflikt/Dilemma/(benutzerdefiniert)
- Ausgang/Entscheidung/(benutzerdefiniert)
- Abschnittsnotizen

.. note::
   Only "normal" sections appear in the plot grid. 
   Abschnitte of the "Unbenutzt" type are omitted.

Der Dateinamenszusatz lautet ``_grid_tmp``.

.. note::
   Sie können Zeilen und Spalten umordnen, verbergen oder löschen, 
   ohne dass es Auswirkungen auf den Re-Import hat. 
   Nur die erste Zeile und die erste Spalte, die standardmäßig verborgen 
   sind, dürfen nicht verändert werden, weil sie die Strukturinformationen 
   für den Import enthalten. 


Erzählstruktur-Beschreibung zum Bearbeiten exportieren
------------------------------------------------------

**Ein ODT-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Plot > Erzählstruktur-Beschreibung zum Bearbeiten exportieren**,
können Sie ein Textdokument erzeugen, das
all stages, each with description.
File name suffix is ``_structure_tmp``.

.. hint::
   This is also a full synopsis, with the emphasis on the dramaturgical structure.


Plotlinienbeschreibungen zum Bearbeiten exportieren
---------------------------------------------------

**Ein ODT-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Plot > Plotlinienbeschreibungen zum Bearbeiten exportieren**,
können Sie ein Textdokument erzeugen, das
stages, plot lines, and plot points, each with description.
The plot points are linked to the manuscript and to the section descriptions.
File name suffix is ``_plotlines_tmp``.


Plot-Liste exportieren (Tabelle)
--------------------------------

**Ein ODS-Dokument exportieren**

Mit **Plot > Plot-Liste exportieren (Tabelle)**
können Sie ein Tabellendokument
mit einer Zeile pro Abschnitt und einer Spalte pro Plotlinie
erzeugen.
Associations between Plotlinien and sections are color-highlighted.
Plotpunkt Titels are displayed.
Der Dateinamenszusatz lautet ``_plotlist``.

.. hint::
   The Plotlinie Titels and the section Titels are hyperlinked to 
   the respective descriptions in other exported documents, if any.

.. figure:: _images/plot_menu04.png
   :alt: LibreOffice Screenshot

   LibreOffice Screenshot. Note the hyperlink from the Plotlinie Titel in the
   plot list (left) to the Plotlinie in the plot description (right). 

.. important::
   Hyperlinks in ODS spreadsheets are absolute within the file system, 
   so they might not work after moving the location of your project file
   to another folder or computer. In this case, you will have to 
   export the spreadsheet anew.  

Plot-Liste anzeigen
-------------------

**Einen HTML-Report mit Plot-elementen anzeigen**

Mit **Plot > Plot-Liste anzeigen**
You can create a list-formatted HTML file that contains
a plot list similar to the ODS plot list (see above),
but without any hyperlinks,
and launch your system’s web browser for displaying it.

.. figure:: _images/plot_menu03.jpg
   :alt: Edge browser Screenshot

   Edge browser Screenshot

.. note::
   The report is a temporary file, auto-gelöscht on program exit.
   If needed können Sie have your web browser save or print it.

