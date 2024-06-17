Schauplätze-Menü
================

**Schauplatzfunktionen**

.. figure:: _images/locations_menu01.png
   :alt: novelibre Screenshot

Hinzufügen
----------

**Einen neuen Schauplatz erzeugen**

Mit **Schauplätze > Hinzufügen**
können Sie einen `Schauplatz <basic_concepts.html#figuren-und-erzahlwelt>`__
in den Baum einfügen.

- Wenn ein Schauplatz ausgewählt ist, wird der neue Schauplatz dahinter platziert.
- Andernfalls wird der neue Schauplatz an den Schluss gesetzt.
- Der neue Schauplatz hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.


Importieren
-----------

**Importieren locations from another project**

Mit **Schauplätze > Importieren**
können Sie import a selection of locations from another project.
First you select an XML file containing the location data.
Then you select the locations you want to add to the current project.

.. hint::
   To create an XML-Schauplatzdatei for the current project, 
   use **Exportieren > Figuren/Schauplätze/Gegenstände-Datendateien**.


Schauplatzbeschreibungen zum Bearbeiten exportieren
---------------------------------------------------

**Ein ODT-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Gegenstände > Schauplatzbeschreibungen zum Bearbeiten exportieren**
können Sie ein Textdokument erzeugen, das eine
location descriptions that can be edited with *Writer* and reimported.
Der Dateinamenszusatz lautet ``_locations_tmp``.


Schauplatzliste exportieren (Tabelle)
-------------------------------------

**Ein ODS-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Gegenstände > Schauplatzliste exportieren (Tabelle)**
können Sie ein Tabellenkalkulationsdokument mit einer Schauplatzliste erzeugen.
Dieses Dokument kann mit *Calc* bearbeitet und zu *novelibre*
zurückgespielt werden.
Der Dateinamenszusatz lautet ``_loclist_tmp``.

.. note::
   Sie können Zeilen und Spalten umordnen, verbergen oder löschen, 
   ohne dass es Auswirkungen auf den Re-Import hat. 
   Nur die erste Zeile und die erste Spalte, die standardmäßig verborgen 
   sind, dürfen nicht verändert werden, weil sie die Strukturinformationen 
   für den Import enthalten. 


Liste anzeigen
--------------

**Einen HTML-Report mit Schaupatzdaten anzeigen**

Mit **Schauplätze > Liste anzeigen**
können Sie create a list-formatted HTML file that contains
a location list,
and launch your system’s web browser for displaying it.

.. note::
   The report is a temporary file, auto-gelöscht on program exit.
   If needed können Sie have your web browser save or print it.

