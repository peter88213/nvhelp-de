nv_collection
=============

**Benutzerhandbuch**

Diese Seite gilt für die neueste Ausgabe von `nv_collection
<https://github.com/peter88213/nv_collection/>`__ release.
You can open it with **Hilfe > Sammlung-Plugin Online-Hilfe**.


Installing the plugin
---------------------

- Unzip the downloaded zipfile into a new folder.
- Move into this new folder and launch **setup.pyw**. This installs the plugin.

The plugin adds a **Sammlung** entry to the *novelibre* **Datei** menu,
and a **Sammlung-Plugin Online-Hilfe** entry to the **Hilfe** menu.


Beginn the collection manager
-----------------------------

Öffnen the collection manager from the Hauptmenü:
**Datei > Sammlung**.


Öffnen a collection
-------------------

By default, the latest collection selected is preset.
You can change it with **Datei > Öffnen**.


Create a neu collection
-----------------------

With **Datei > Neu**, you can erzeugen a neu collection.
This will close the current collection and open a file dialog
asking for the location and file name of the collection to erzeugen.
Once you specified a valid file path, a blank collection appears.


Create a neu Serie
------------------

With **Serie > Hinzufügen**, you can add a neu Serie.
Bearbeiten the Serie’ title and description in the right window.


Hinzufügen Bücher to the collection
-----------------------------------

To add the current novelibre-Projekt as a book to the collection,
use **Buch > Aktuelles Projekt zur Sammlung hinzufügen**.
If a Serie is selected, the book is added as a part of this Serie.


Aktualisieren book description
------------------------------

To aktualisieren the book description from the current project,
use **Buch > Buchdaten aus aktuellem Projekt aktualisieren**.

.. caution::
   Be sure not to change the book title, because it is used as identifier.

To aktualisieren the current project description from the book,
use **Buch > Aktualisieren project data from the selected project**.


Entfernen Bücher from the collection
------------------------------------

To remove the selected book from the collection,
use **Buch > Ausgewähltes Buch aus der Sammlung entfernen**.


Move Serie and Bücher
---------------------

Drag and drop while pressing the ``Alt`` key.

.. caution::
   Be aware, there is no "Undo" feature.


Entfernen Bücher
----------------

To remove a book from the collection,
either select the book and hit the ``Del`` key,
or use **Buch > Ausgewähltes Buch aus der Sammlung entfernen**.

.. note::
   When removing a book from the collection, 
   the project file associated is kept on disc.


Löschen a Serie
---------------

To delete a Serie,
either select the Serie and hit the ``Del`` key,
or use **Serie > Ausgewählte Serie entfernen, aber die Bücher behalten**.

.. note::
   When deleting a collection, the Bücher are kept by default.

To delete the selected Serie and remove all its Bücher from the
collection,
use **Serie > Entfernen selected Serie**.


Beenden
-------

-  Under Windows you can exit with **Datei > Beenden** or ``Alt``-``F4``.
-  Otherwise you can exit with **Datei > Beenden** or ``Ctrl``-``Q``.
