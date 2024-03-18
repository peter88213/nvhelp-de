Plot-Menü
=========

**Plot elements operation**

.. figure:: _images/plot_menu01.png
   :alt: novelibre screenshot

Plotlinie hinzufügen
--------------------

**Hinzufügen a new Plotlinie to the story**

Mit **Plot > Hinzufügen Plotlinie**,
you can add a Projektnotiz to the tree .

.. note::

   -  If a Plotlinie is selected, the new item is placed after the selected one.
   -  Otherwise, the new Plotlinie is placed at the last position.
   -  The new Plotlinie has an auto-generated Titel. You can change it in the
      right pane.

Plotpunkt hinzufügen
--------------------

**Hinzufügen a new Plotpunkt to the selected Plotlinie**

Mit **Plot > Plotpunkt hinzufügen**,
you can add a plot point to a Plotlinie.

.. note::

   - If a plot point is selected, the new plot point is placed after the selected one.
   - If a Plotlinie is selected, the new plot point is placed at the last position.
   - Otherwise, no new plot point is generated.
   - The new plot point has an auto-generated Titel. You can change it in
     the right pane.

Stadium einfügen
----------------

**Insert a stage between the sections**

Mit **Plot > Stadium einfügen**,
you can insert a stage after the selected chapter or section.

.. hint::
   By default, the new stage is on the second level. 
   You can change the level to first (see below).

Ebene ändern
------------

**Change the level of the selected stages**

Mit **Plot > Ebene ändern**,
you can change the level of the selected stages.

.. figure:: _images/plot_menu02.png
   :alt: novelibre screenshot

-  **Erste Ebene** is displayed in bold face.
-  **Zweite Ebene** is displayed in regular font.

.. note::
   The stage level is only for visual distinction. It has no
   influence on the program functions. 

Plot-Beschreibung exportieren
-----------------------------

**Exportieren an ODT document**

Mit **Plot > Plot-Beschreibung exportieren**,
you can create a text document that contains
stages, Plotlinien, and plot points, each with description.
Der Dateinamenszusatz lautet ``_plot``.


Plot-Liste exportieren (Tabelle)
--------------------------------

**Exportieren an ODS document**

Mit **Plot > Plot-Liste exportieren (Tabelle)**,
you can create a spreadsheet with a row for each section
and a column for each Plotlinie.
Associations between Plotlinien and sections are color-highlighted.
Plotpunkt Titels are displayed.
Der Dateinamenszusatz lautet ``_plotlist``.

.. hint::
   The Plotlinie Titels and the section Titels are hyperlinked to 
   the respective descriptions in other exported documents, if any.

.. figure:: _images/plot_menu04.png
   :alt: LibreOffice screenshot

   LibreOffice screenshot. Note the hyperlink from the Plotlinie Titel in the
   plot list (left) to the Plotlinie in the plot description (right). 

.. important::
   Hyperlinks in ODS spreadsheets are absolute within the file system, 
   so they might not work after moving the location of your project file
   to another folder or computer. In this case, you will have to 
   export the spreadsheet anew.  

Plot-Liste anzeigen
-------------------

**Show an HTML report with plot elements**

Mit **Plot > Plot-Liste anzeigen**,
You can create a list-formatted HTML file that contains
a plot list similar to the ODS plot list (see above),
but without any hyperlinks,
and launch your system’s web browser for displaying it.

.. figure:: _images/plot_menu03.jpg
   :alt: Edge browser screenshot

   Edge browser screenshot

.. note::
   The report is a temporary file, auto-gelöscht on program exit.
   If needed, you can have your web browser save or print it.

