|external-link| `English <https://peter88213.github.io/nvhelp-en/scap_novx/>`__

.. |external-link| image:: ../_images/external-link.png

-----------------

=========
scap_novx
=========

**Benutzerhandbuch**

.. hint::
   Die deutsche Übersetzung des *scap_novx*-Benutzerhandbuchs ist noch in Arbeit.
   Im Zweifelsfall könnnen Sie von dieser Seite aus zur englischen Version 
   des Benutzerhandbuchs wechseln (Link oben).


Diese Seite gilt für die neueste Ausgabe von `scap_novx
<https://github.com/peter88213/scap_novx/>`__.

Das Python-Skript *scap_novx.py* erzeugt ein *novelibre*-Projekt aus einer
*Scapple*-Gliederung.


Gebrauchsanweisung
------------------

Vorgesehene Benutzung
~~~~~~~~~~~~~~~~~~~~~

Das mitgelieferte Installationsskript fordert Sie auf, eine Verknüpfung
auf dem Desktop anzulegen.
Die können das Programm dann aufrufen, indem Sie mit der Maus eine
*.scap*-Datei auf das Symbol ziehen.


Auf der Kommandozeile
~~~~~~~~~~~~~~~~~~~~~

Wahlweise können Sie auch

- das Programm von der Kommandozeile aus aufrufen und die *Scapple*-Datei als
  Parameter übergeben, oder
- das Programm aus einer Batchdatei heraus aufrufen.

Aufruf: ``scap_novx.py [--silent] Quelldatei``


Positionsbezogene Parameter:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Quelldatei``

Der Dateipfad der *Scapple*-Gliederungsdatei.


Optionale Parameter:
^^^^^^^^^^^^^^^^^^^^

``--silent``  Fehlermeldungen und Nachfragen unterdrücken.


Funktionsweise
--------------

*scap_novx* erzeugt eine neue *novelibre*-Projektdatei im selben Verzeichnis und
mit dem selben Namen wie die Scapple-Quelldatei, doch mit der Erweiterung `.novx``.


.. note::
   Falls das *novelibre*-Projekt bereits existiert, wird es nicht überschrieben. 
   Stattdessen werden XML-Figuren-, Schauplatz- und Gegenstandsdateien erzeugt, 
   die in jedes *novelibre*-Projekt importiert werden können. 


Konvertierungsregeln
--------------------

- Notes with a shadow are converted to sections.
- Notes with a shadow and "cloud" border are converted to "Notes" sections.
- Sections are ordered by their position in the Scapple diagram (from top left to bottom right).
- Notes with a "cloud" border without shadow are converted to section and character notes.
- Notes with a square border are converted to tags.
- Notes with red text are converted to major characters.
- Notes with purple text are converted to minor characters.
- Notes with blue text are converted to locations.
- Notes with green text are converted to items.
- Assign characters/locations/items to a section by connecting the corresponding notes.
- Assign tags to sections/characters/locations/items by connecting the corresponding notes.
- Assign a viewpoint character to a section by creating an arrow pointing from the character to the section. If a section is pointed to by several characters, or by no character, the viewpoint is random.


Wie man Einträge für den Export kennzeichnet
--------------------------------------------

Stile importieren (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The scap_novx distribution comes with a sample Scapple project *styles.scap* including all required styles. You can either use this diagram as a template, or import the styles into your own Scapple diagram.

.. figure:: _images/import_styles.png
   :alt: Screenshot

   Screenshot: Import styles dialog
   
In the file picker dialog, select ``<unzipped scap_novx release folder>\sample\styles.scap``. Then können Sie apply the styles via context menu.

.. figure:: _images/apply_styles.png
   :alt: Screenshot
   
   Screenshot: Apply style menu


Abschnitte kennzeichnen
~~~~~~~~~~~~~~~~~~~~~~~

Either apply the "Section" style, if any, via context menu, or tick "Shadow" in the Inspector to mark the note as section.

.. figure:: _images/mark_section.png
   :alt: Screenshot
   
   Screenshot: Set note shadow
   

Notizen kennzeichnen
~~~~~~~~~~~~~~~~~~~~

Either apply the "Note" style, if any, via context menu, or make the note's border style "Cloud" in the Inspector.


Tags kennzeichnen
~~~~~~~~~~~~~~~~~

Either apply the "Tag" style, if any, via context menu, or make the note's border style "Square" in the Inspector.


Schauplätze kennzeichnen
~~~~~~~~~~~~~~~~~~~~~~~~

Either apply the "Location" style, if any, via context menu, or tick the big blue field above the text color swatch in the Inspector.

.. figure:: _images/mark_location.png
   :alt: Screenshot
   
   Screenshot: Set text color


Hauptfiguren kennzeichnen
~~~~~~~~~~~~~~~~~~~~~~~~~

Either apply the "Major character" style, if any, via context menu, or tick the big red field above the text color swatch in the Inspector.


Nebenfiguren kennzeichnen
~~~~~~~~~~~~~~~~~~~~~~~~~

Either apply the "Minor character" style, if any, via context menu, or tick the big purple field above the text color swatch in the Inspector.


Gegenstände kennzeichnen
~~~~~~~~~~~~~~~~~~~~~~~~

Either apply the "Item" style, if any, via context menu, or tick the big green field above the text color swatch in the Inspector.


Benutzerdefinierte Konfiguration
--------------------------------

You can override the default settings by providing a configuration file. Be always aware that faulty entries may cause program errors.


Globale Konfiguration
~~~~~~~~~~~~~~~~~~~~~

An optional global configuration file can be placed in the configuration directory in your user profile. It is applied to any project. Its entries override scap_novx's built-in constants. This is the path:
``c:\Users\<user name>\.novx\scap_novx\scap_novx.ini``

The setup script installs a sample configuration file containing scap_novx's default values. You can modify or delete it.


Lokale Projektkonfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An optional project configuration file ``scap_novx.ini2novx.ini`` can be placed in your project directory, i.e. the folder containing your novelibre and Timeline project files. It is only applied to this project. Its entries override scap_novx's built-in constants as well as the global configuration, if any.


Wie man eine Konfigurationsdatei erstellt oder anpasst
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The scap_novx distribution comes with a sample configuration file located in the ``sample`` subfolder. It contains scap_novx's default settings and options. This file is also automatically copied to the global configuration folder during installation. You best make a copy and edit it.

- The SETTINGS section mainly refers to colors, i.e. The text colors that mark the characters/locations/items in Scapple. If you change them, the program might behave differently than described in the description of the conversion rules below.
- The OPTIONS section comprises options for regular program execution.
- Comment lines begin with a ``#`` number sign. In the example, they refer to the code line immediately above.

This is the configuration explained:

::

   [SETTINGS]

   location_color = 0.0 0.0 1.0

   # RGB text color that marks the locations in Scapple.

   item_color = 0.0 0.5 0.0

   # RGB text color that marks the items in Scapple.

   major_chara_color = 1.0 0.0 0.0

   # RGB text color that marks the major racters in Scapple.

   minor_chara_color = 0.5 0.0 0.5

   # RGB text color that marks the minor characters in Scapple.

   [OPTIONS]

   export_sections = Yes

   # Yes: create sections from Scapple notes.

   export_characters = Yes

   # Yes: create characters from Scapple notes.

   export_locations = Yes

   # Yes: create location from Scapple notes.

   export_items = Yes

   # Yes: create items from Scapple notes.



Installationspfad
-----------------

The setup script installs *scap_novx.py* in the user profile.
This is the installation path on Windows:

``c:\Users\<user name>\.novx\scap_novx``

