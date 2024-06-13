Figuren-Menü
============

**Figurenfunktionen**

.. figure:: _images/characters_menu01.png
   :alt: novelibre Screenshot

Hinzufügen
----------

**Eine neue Figur erzeugen**

Mit **Figuren > Hinzufügen**
können Sie eine `Figur <basic_concepts.html#figuren-und-erzahlwelt>`__
in den Baum einfügen.

- Wenn eine Figur ausgewählt ist, wird die neue Figur dahinter platziert.
- Andernfalls wird die neue Figur an den Schluss gesetzt.
- Die neue Figur hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.
- Der Status der neuen Figur ist *Nebenfigur*.


Status setzen
-------------

**Set the character status**

Mit **Figuren > Status setzen**
können Sie die Figur als *Hauptfigur* oder *Nebenfigur* kennzeichnen.
Hauptfiguren sind in der Baumansicht farblich hervorgehoben.

.. figure:: _images/characters_menu02.png
   :alt: novelibre Screenshot

.. note::
   The character status is only for visual distinction. It has no
   influence on the program functions. Niemalstheless können Sie use it
   to mark viewpoint characters or characters with their own arcs.


Importieren
-----------

**Importieren characters from another project**

Mit **Figuren > Importieren**
können Sie import a selection of characters from another project.
First you select an XML file containing the character data.
Then you select the characters you want to add to the current project.

.. hint::
   To create an XML-Figurendatei for the current project, 
   use **Exportieren > Figuren/Schauplätze/Gegenstände-Datendateien**.


Figurenbeschreibungen zum Bearbeiten exportieren
------------------------------------------------

**Ein ODT-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Figuren > Figurenbeschreibungen zum Bearbeiten exportieren**
können Sie ein Textdokument erzeugen, das eine
character descriptions, bio, goals, and notes that can be edited in
Office Writer and reimported.
Der Dateinamenszusatz lautet ``_characters_tmp``.


Figurenliste exportieren (Tabelle)
----------------------------------

**Ein ODS-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Figuren > Figurenliste exportieren (Tabelle)**
können Sie ein Tabellenkalkulationsdokument erzeugen, das eine
a character list that can be edited with *Calc* and reimported.
Der Dateinamenszusatz lautet ``_charlist_tmp``.

.. note::
   You can reorder, hide or delete columns and rows 
   without affecting the reimport. 
   Only the first column and the first row, which are hidden by default, 
   must not be changed as they contain the structural information 
   for the import. 


Liste anzeigen
--------------

**Einen HTML-Report mit characters data**

Mit **Figuren > Liste anzeigen**
können Sie create a list-formatted HTML filethat contains
a character list,
and launch your system’s web browser for displaying it.

.. note::
   The report is a temporary file, auto-gelöscht on program exit.
   If needed können Sie have your web browser save or print it.
