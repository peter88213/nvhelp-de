|external-link| `English <https://peter88213.github.io/nvhelp-en/nv_collection/>`__

.. |external-link| image:: ../_images/external-link.png

-----------------

=============
nv_collection
=============

**Benutzerhandbuch**

.. hint::
   Die deutsche Übersetzung des *novelibre*-Benutzerhandbuchs ist noch in Arbeit.
   Im Zweifelsfall könnnen Sie von dieser Seite aus zur englischen Version 
   des Benutzerhandbuchs wechseln (Link s.o.).

Diese Seite gilt für die neueste Ausgabe von `nv_collection
<https://github.com/peter88213/nv_collection/>`__.
Sie können sie mit **Hilfe > Sammlung-Plugin Online-Hilfe** öffnen.


Das Plugin installieren
-----------------------

- Entpacken Sie die heruntergeladene Zip-Datei in einen neuen Ordner.
- Gehen Sie in diesen Ordner und führen Sie **setup.pyw** aus. Damit installieren Sie das Plugin.

The plugin adds a **Sammlung** entry to the *novelibre* **Datei**-Menü,
and a **Sammlung-Plugin Online-Hilfe** entry to the **Hilfe**-Menü.


Die Sammlungen-Verwaltung aufrufen
----------------------------------

Öffnen the collection manager from the Hauptmenü:
**Datei > Sammlung**.


Eine Sammlung öffnen
--------------------

By default, the latest collection selected is preset.
You can change it with **Datei > Öffnen**.


Eine neue Sammlung ereugen
--------------------------

Mit **Datei > Neu** können Sie erzeugen a neu collection.
This will close the current collection and open a file dialog
asking for the location and file name of the collection to erzeugen.
Once you specified a valid file path, a blank collection appears.


Eine neue Serie erzeugen
------------------------

Mit **Serie > Hinzufügen** können Sie add a neu Serie.
Bearbeiten the Serie’ title and description in the right window.


Bücher zur Sammlung hinzufügen
------------------------------

To add the current novelibre-Projekt as a book to the collection,
use **Buch > Aktuelles Projekt zur Sammlung hinzufügen**.
If a Serie is selected, the book is added as a part of this Serie.


Die Buchbeschreibung aktualisieren
----------------------------------

To aktualisieren the book description from the current project,
use **Buch > Buchdaten aus aktuellem Projekt aktualisieren**.

.. caution::
   Be sure not to change the book title, because it is used as identifier.

To aktualisieren the current project description from the book,
use **Buch > Aktualisieren project data from the selected project**.


Bücher aus der Sammlung entfernen
---------------------------------

To remove the selected book from the collection,
use **Buch > Ausgewähltes Buch aus der Sammlung entfernen**.


Serien ünd Bücher veschieben
----------------------------

Drag and drop while pressing the ``Alt`` key.

.. caution::
   Be aware, there is no "Undo" feature.


Bücher entfernen
----------------

To remove a book from the collection,
either select the book and hit the ``Entf``-Taste,
or use **Buch > Ausgewähltes Buch aus der Sammlung entfernen**.

.. note::
   When removing a book from the collection, 
   the project file associated is kept on disc.


Eine Serie löschen
------------------

To delete a Serie,
either select the Serie and hit the ``Entf``-Taste,
or use **Serie > Ausgewählte Serie entfernen, aber die Bücher behalten**.

.. note::
   When deleting a collection, the Bücher are kept by default.

To delete the selected Serie and remove all its Bücher from the
collection,
use **Serie > Entfernen selected Serie**.


Beenden
-------

-  Under Windows können Sie exit with **Datei > Beenden** or ``Alt``-``F4``.
-  Otherwise können Sie exit with **Datei > Beenden** or ``Strg``-``Q``.
