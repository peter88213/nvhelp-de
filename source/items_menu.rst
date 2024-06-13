Gegenstände-Menü
================

**Gegenstandsfunktionen**

.. figure:: _images/items_menu01.png
   :alt: novelibre Screenshot

Hinzufügen
----------

**Einen neuen Gegenstand erzeugen**

Mit **Gegenstände > Hinzufügen**
können Sie einen `Gegenstand <basic_concepts.html#figuren-und-erzahlwelt>`__
in den Baum einfügen.

- Wenn ein Gegenstand ausgewählt ist, wird der neue Gegenstand dahinter platziert.
- Andernfalls wird der neue Gegenstand an den Schluss gesetzt.
- Der neue Gegenstand hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.


Importieren
-----------

**Importieren items from another project**

Mit **Gegenstände > Importieren**
können Sie import a selection of items from another project.
First you select an XML file containing the item data.
Then you select the items you want to add to the current project.

.. hint::
   To create an XML-Gegenstandsdatei for the current project, 
   use **Exportieren > Figuren/Schauplätze/Gegenstände-Datendateien**.


Gegenstandsbeschreibungen zum Bearbeiten exportieren
----------------------------------------------------

**Ein ODT-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Gegenstände > Gegenstandsbeschreibungen zum Bearbeiten exportieren**
können Sie ein Textdokument erzeugen, das eine
item descriptions that can be edited with *Writer* and reimported.
Der Dateinamenszusatz lautet ``_items_tmp``.


Gegenstandsliste exportieren (Tabelle)
--------------------------------------

**Ein ODS-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Gegenstände > Gegenstandsliste exportieren (Tabelle)**
können Sie ein Tabellenkalkulationsdokument erzeugen, das eine
an item list that can be edited with *Calc* and reimported.
Der Dateinamenszusatz lautet ``_itemlist_tmp``.

.. note::
   You can reorder, hide or delete columns and rows 
   without affecting the reimport. 
   Only the first column and the first row, which are hidden by default, 
   must not be changed as they contain the structural information 
   for the import. 


Liste anzeigen
--------------

**Einen HTML-Report mit Gegenstandsdaten anzeigen**

Mit **Gegenstände > Liste anzeigen**
können Sie create a list-formatted HTML file that contains
an item list,
and launch your system’s web browser for displaying it.

.. note::
   The report is a temporary file, auto-gelöscht on program exit.
   If needed können Sie have your web browser save or print it.
