Am Manuskript schreiben
=======================

Writer als Texteditor aufrufen
------------------------------

.. note::
   Das folgende Beispiel beschreibt den Arbeitsablauf für das
   Bearbeiten des Manuskripts mit LibreOffice. 
   Dasselbe gilt auch für OpenOffice.
   
   Andere Textverarbeitungsprogramme, die versprechen, das 
   *ODT*-Dateiformat zu unterstützen, werden generell nicht empfohlen.

Sobald Ihr Romanprojekt mindestens einen Abschnitt hat, können
Sie mit dem Schreiben beginnen. 
Dazu speichern Sie Ihr Projekt und exportieren Ihren Roman in die
*Writer*-Textverarbeitung. Das geht entweder mit
**Exportieren > Manuskript zum Bearbeiten**, oder indem Sie
in der Werkzeugleiste auf das Symbol |Exportieren Manuskript| klicken.

.. hint::
   - Wenn Sie den Menübefehl verwenden, können Sie *novelibre* ein 
     Manuskript erzeugen und nach einer Nachfrage mit *Writer*
     öffnen lassen.
   - Wenn Sie auf das Symbol in der Werkzeugleiste klicken, 
     wird *Writer* sofort nach dem Export aufgerufen. 


.. figure:: _images/writing01.png
   :alt: novelibre Screenshot
   
   novelibre Screenshot

Falls Sie das schon einmal gemacht haben, und es immer noch ein 
Manuskriptdokument von der letzten Sitzung gibt, werden Sie nun gefragt, 
ob Sie damit weiterarbeiten wollen. Falls ja, wählen Sie "Bestehendes öffnen".

.. figure:: _images/writing02.png
   :alt: novelibre Screenshot
   
   novelibre Screenshot

Falls Sie "Überschreiben" wählen, erzeugt *novelibre* ein neues Manuskriptdokument.
"Abbruch" bricht den Exportvorgang ab und bringt Sie zum Arbeitsbereich zurück. 


.. hint::
   *novelibre* prüft, ob ein existierendes Manuskript neuer oder älter 
   als die Projektdatei ist, und schlägt eine Auswahl vor, indem es die 
   passende Schaltfläche aktiviert. Sie können das mit der Eingabetaste 
   akzeptieren. Wenn Ihre Auswahl dem Vorschlag entspricht, sehen Sie
   in der Statusleiste eine grüne Meldung. Andernfalls ist die Meldung rot, 
   nur zur Erinnerung. 

If you started the export using the **Exportieren**-Menü command, you may
be asked whether you want to open the newly created document, depending
of your `Exportieren settings <export_menu.html#optionen>`__.

.. figure:: _images/writing03.png
   :alt: novelibre Screenshot
   
   novelibre Screenshot
   
If you answer "yes", *Writer* will be launched with
the Manuskript document. Otherwise, the document is just
kept for future use.

Depending on your `Exportieren settings <export_menu.html#optionen>`__,
*novelibre* now may `lock the project <basic_concepts.html#projekt-sperre>`__,
so that it can't be accidentally modified with *novelibre* while
worked on in *Writer*.

.. note::
   *novelibre* starts your standard application for files with the *.odt* 
   extension. Usually, the setting is made by LibreOffice or ÖffnenOffice
   during installation.

After you change to *Writer*, you see the whole novel in
a layout that is similar to the "standard Manuskript format". The
*Navigator* (open with ``F5``) shows the chapter and section Titels
in the *Headings* area. Double click on a heading to move the cursor
to that location. You can now write within the frames that define
the sections.

.. figure:: _images/writing04.png
   :alt: LibreOffice Writer Screenshot
   
   LibreOffice Writer Screenshot: Note that the text boundaries are 
   made visible here, which is `highly recommended 
   <preparations.html#setting-up-writer>`__.
   
.. note::
   The section Titels displayed in the Navigator are invisible 
   in the workspace so that they do not disrupt the flow of writing, 
   and the impression of an original Manuskript page is retained. 
 

Änderungen zu novelibre zurückschreiben
---------------------------------------

At the end of the writing session, save the changes, exit the *Writer*
word processor, and return to *novelibre*. Simply click on the
|Änderungen am Manuskript übernehmen| toolbar icon, and your latest changes will
appear.

.. note::
   The toolbar icon mentioned above is only for the Manuskript. If 
   you want to apply changes made in other documents like character
   sheets or synopses, use the `Importieren-Menü <import_menu.html>`__. 

   .. figure:: _images/writing09.png
      :alt: novelibre Screenshot
      
      novelibre Screenshot: The Manuskript entry is highlighted in 
      green, because the file is newer than the open project. 


Mit Writer neue Abschnitte anlegen
----------------------------------

If you need a new section while writing, you don't have to switch
to *novelibre*. Simply start a new line with a special marker
``###``. Wahlweise können Sie add a section Titel, and, separated
by ``|``, a section description. Alle other metadata is intended
to be entered in *novelibre* later.

.. tip::
   As of *novelibre* version 3.0.2 können Sie use ``####`` to create
   an `appended section 
   <section_view.html#an-den-vorherigen-abschnitt-anhangen>`__. 

The following example shows how to split an existing section:

.. figure:: _images/writing05.png
   :alt: LibreOffice Writer Screenshot
   
   LibreOffice Writer Screenshot: Notice the highlighted section marker

Zurück in *novelibre*, you see the new section. It has got a Titel,
but no other metadata.

.. figure:: _images/writing06.png
   :alt: novelibre Screenshot
   
   *novelibre* Screenshot: Notice the selected new section 


Mit Writer neue Kapitel anlegen
-------------------------------

If you need a new chapter while writing, you don't have to switch to
*novelibre*. Simply start a new line *within the edited section*
with a second-level heading.

.. important::
   *novelibre* only re-imports text within section defining frames. 
   Technically, it always splits sections when creating new chapters 
   or sections from the Manuskript.
   
   You also cannot move chapters within *Writer*. If you 
   want to rearrange chapters or sections, do it with *novelibre*.  
   

The following example shows how to add a chapter with *Writer*:

.. figure:: _images/writing07.png
   :alt: LibreOffice Writer Screenshot
   
   LibreOffice Writer Screenshot: It doesn't matter what the new
   chapter is Titeld

Zurück in *novelibre*, you see a new chapter and a new section. Since
the chapters are auto-numbered in this example project, the new
chapter Titel already fits, while the new section's Titel should
be adjusted manually.

.. figure:: _images/writing08.png
   :alt: novelibre Screenshot: Notice the selected new chapter
   
   novelibre Screenshot

.. |Exportieren Manuskript| image:: _images/Manuscript.png
.. |Änderungen am Manuskript übernehmen| image:: _images/updateFromManuscript.png
