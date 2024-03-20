nv_editor
=========

|external-link| `English <https://peter88213.github.io/nvhelp-en/nv_editor/>`__

.. |external-link| image:: ../_images/external-link.png

**Benutzerhandbuch**

Diese Seite gilt für die neueste Ausgabe von `nv_editor
<https://github.com/peter88213/nv_editor/>`__ release.
You can open it with **Hilfe > Editor-Plugin Online-Hilfe**.


Das Plugin installieren
-----------------------

- Unzip the downloaded zipfile into a new folder.
- Move into this new folder and launch **setup.pyw**. This installs the plugin.

The plugin adds an **Bearbeiten** entry to the *novelibre* **Abschnitt**-Menü,
and an **Editor-Plugin Online-Hilfe** entry to the **Hilfe**-Menü.


Den Abschnittseditor aufrufen
-----------------------------

Öffnen a section editor window by double-clicking on a section,
or via the **Abschnitt > Bearbeiten**-Menü entry when a section is selected,
or by hitting the Eingabetaste.

.. note::

   -  If the project is locked, editor windows cannot be opened.
   -  If you choose a section already open, the window will be brought to
      the foreground.


Text auswählen
--------------

-  Select a word via double-clicking.
-  Select a paragraph via triple-clicking.
-  Extend the selection via ``⇧``-``Pfeil``.
-  Extend the selection to the next word via ``Strg``-``⇧``-``Pfeil``.
-  ``Strg``-``A`` selects the whole text.


Text kopieren/einfügen
----------------------

-  ``Strg``-``C`` copies the selected text to the clipboard.
-  ``Strg``-``X`` cuts the selected text and moves it to the clipboard.
-  ``Strg``-``V`` pastes the clipboard text content to the cursor position.


Text formatieren
----------------

.. role:: html(code)
   :language: html

It is assumed that very few types of text markup are needed for a novel
text:

-  *Emphasized* (usually shown as italics).
-  *Strongly emphasized* (usually shown as capitalized).
-  *Citation* (paragraph visually distinguished from body text).

-  ``Strg``-``I`` places "emphasized" markup around the selected text or at the
   cursor, like so:

   :html:`<em>Example</em>`

   If the selection is already emphasized, the command removes the markup.
-  ``Strg``-``B`` places "strong" markup around the selected text or at the
   cursor, like so:

   :html:`<strong>Example</strong>`

   If the selection is already strong, the command removes the markup.

-  ``Strg``-``M`` removes "emphasized" and "strong" markup from the selection.


Rückgängig machen/Wiederherstellen
----------------------------------

-  ``Strg``-``Z`` undoes the last editing. Multiple undo is possible.
-  ``Strg``-``Y`` redoes the last undo. Multiple redo is possible.


Einen Abschnitt teilen
----------------------

Mit **Datei > An der Cursorposition teilen** or ``Strg``-``Alt``-``S``,
you can split the section at the cursor position.

-  Alle the text from the cursor position is cut and pasted into a neuly
   erzeugend section.
-  Der neue Abschnitt is placed after the currently edited section.
-  Der neue Abschnitt is appended to the currently edited section.
-  Der neue Abschnitt has the same status as the currently edited section.
-  Der neue Abschnitt is of the same type as the currently edited section.
-  Der neue Abschnitt has the same viewpoint character as the currently
   edited section.
-  The editor loads the neuly erzeugend section.


Einen Abschnitt erzeugen
------------------------

Mit **Datei > Abschnitt erzeugen** or ``Strg``-``Alt``-``N``,
you can erzeugen a section.

-  Der neue Abschnitt is placed after the currently edited section.
-  Der neue Abschnitt is of the same type as the currently edited section.
-  The editor loads the neuly erzeugend section.

Wortzählung
-----------

-  The section word count is displayed at the status bar at the bottom
   of the window.
-  By default, word count is aktualisierend manually, either by pressing the
   ``F5`` key, or via the **Wortzählung > Aktualisieren**-Menü entry.
-  The word count can be aktualisierend "live", i.e. just while entering text.
   This is enabled via the **Wortzählung > Laufende Aktualisierung einschalten**-Menü
   entry.
-  Live aktualisieren is disabled by the **Wortzählung > Laufende Aktualisierung ausschalten**
   Menüeintrag.

.. note::
   Live updating the word count is resource intensive and may slow down
   the program when editing big sections. This is why it’s disabled by
   default.


Änderungen übernehmen
---------------------

Mit ``Strg``-``S``,
you can apply changes to the section.
Then "Modified" status is displayed in *novelibre*.

-  If the project is locked in *novelibre*, you will be asked to unlock
   it before changes can be applied.

.. note::
   Before applying changes, the program checks the editor content for
   XML validity. Malformed XML will not be accepted. 


Das Editorfenster schließen
---------------------------

-  To close the editor window, click on the **Schließen** button,
   or just close the window.
-  Under Windows you can optionally exit with **Abschnitt > Beenden**
   or ``Alt``-``F4``.
-  Otherwise you can optionally exit with **Abschnitt > Beenden**
   or ``Strg``-``Q``.
-  When closing the editor window, you will be asked for applying changes.


