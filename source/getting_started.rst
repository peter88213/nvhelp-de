Erste Schritte
==============

Von Null beginnen
-----------------

Wenn Sie *novelibre* starten, indem Sie eine *.novx* Datei auf das Symbol ziehen,
wird dieses Projekt geöffnet. Andernfalls wird das Projekt der letzten
Sitzung automatisch wieder geöffnet, falls es eines gibt.

Nehmen wir an, dass beides nicht der Fall ist, z. B. wenn das Programm
zum allerersten Mal nach der Installation aufgerufen wird.
Nehmen wir außerdem an, dass wir noch keine Vorbereitungen getroffen haben,
d.h. wir haben weder ein angefangenes Werk noch eine Gliederung irgendeiner Art.
Zunächst legen wir mit **Datei > Neu > Leeres Projekt** ein neues leeres Projekt an.

.. figure:: _images/getting_started01.png
   :alt: novelibre Screenshot
   
Ein Dateiauswahldialog öffnet sich und fragt nach dem Dateinamen und dem Speicherort
des neuen Projekts.

.. tip::
   Es ist von Vorteil, einen eigenen Ordner für das Projekt anzulegen, 
   da alle exportierten Dokumente auch hier gespeichert werden. 
   Dazu gehören auch Hilfsdateien wie Zeitleisten oder projektbezogene 
   Konfigurationsdateien für Werkzeuge und Plugins. 

Es ist nicht obligatorisch, aber wir sollten dann einen Titel
und einen Autorennamen eingeben, vielleicht auch eine Beschreibung unserer Idee.
Um gleich loslegen zu können, verschieben wir die restlichen
Projekteinstellungen auf später.

.. figure:: _images/getting_started02.png
   :alt: novelibre Screenshot
   
Wir brauchen mindestens einen Abschnitt, um mit dem Schreiben beginnen zu können.
Und dieser muss zu einem Kapitel gehören. Also erstellen wir jetzt das erste
Kapitel mit **Kapitel > Hinzufügen**.

.. figure:: _images/getting_started03.png
   :alt: novelibre Screenshot
   
Nachdem das Kapitel erstellt wurde, setzt *novelibre* den Fokus auf den
Kapitel-Titel am oberen Rand des rechten Fensters.
Überschreiben wir den vorgegebenen Titel.

.. figure:: _images/getting_started04.png
   :alt: novelibre Screenshot
   
.. hint::
   Wenn sie sich dafür entscheiden, *novelibre* `die Kapitel automatisch 
   nummerieren zu lassen <book_view.html#automatische-nummerierung>`__,
   können Sie das überspringen und den voreingestellten Titel stehenlassen. 

Es gibt nun mehrere Möglichkeiten, einen Abschnitt hinzuzufügen.
In diesem Beispiel klicken wir mit der rechten Maustaste auf das Kapitel
und wählen **Abschnitt Hinzufügen**.

.. figure:: _images/getting_started05.png
   :alt: novelibre Screenshot


Gleich mit dem Manuskript beginnen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sobald der neue Abschnitt in der Baumansicht erscheint,
können wir ein Manuskript exportieren.
Klicken Sie einfach auf die Schaltfläche |Manuskript exportieren| in der Werkzeugleiste.

.. |Manuskript exportieren| image:: _images/Manuscript.png

.. figure:: _images/getting_started06.png
   :alt: novelibre Screenshot
   
Fertig! *Writer* sollte sich nun mit dem Manuskript öffnen.
Fangen Sie einfach an, Ihren Roman innerhalb des Textrahmens zu schreiben.

.. figure:: _images/getting_started07.png
   :alt: Libreoffice Screenshot
   
Wir können nun mit *Writer* weiterarbeiten,  `wie auf der folgenden Seite
beschrieben <writing.html>`__, und während des Schreibens neue Abschnitte
und Kapitel erzeugen.

.. tip::
   You can now work on the Manuskript document "on the seat of your pants"
   until it makes sense for  you to transfer the whole thing back to 
   *novelibre* in order to create an overview and set up your project 
   organization there.
   
   However, I recommend doing this at least daily at the end of your writing 
   session and exporting a new Manuskript document the next day. 
   Then you won't get behind with entering the section Titels und Inhalt 
   descriptions, and you will get your chapters numbered, if desired. 
   In addition, *novelibre* then saves entries in the daily word count log.
   
   
Eine Kapitelstruktur anlegen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer to make a plan first before you start writing, *novelibre* is
the right tool for you.
Then you don't start *Writer* with an empty Manuskript, but first create
a framework of empty chapters for which you enter content information.
Or können Sie leave it at one chapter for the time being and create empty sections
in it, which können Sie later distribute to chapters.
The results of this preliminary work can be exported as text documents in the
form of synopses, e.g on
`chapter <chapter_menu.html#kapitelbeschreibungen-zum-bearbeiten-exportieren>`__ or
`section <section_menu.html#abschnittsbeschreibungen-zum-bearbeiten-exportieren>`__ level.


Eine dramaturgische Struktur aufbauen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

However können Sie also start on a more abstract level and first create and
describe stages like acts or steps in order to later insert the sections as
scenes.
For this, you first create at least one chapter. Then create your stages.

.. figure:: _images/getting_started08.png
   :alt: novelibre Screenshot

The system is described on the `Plotting with novelibre <plotting.html>`__
page.
There you also can learn how to set up multiple strands or character arcs.

.. tip::
   Mit the `nv_templates plugin
   <https://github.com/peter88213/nv_templates/>`__ können Sie have 
   *novelibre* set up your new project with a pre-made structure like the
   "Drei-Akt-Modell" or "Save The Cat". 


Ein Handlungsraster anlegen
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to outline your novel using a `plot grid
<plotting.html#handlungsraster-plot-grid>`__ können Sie do this with
*novelibre*:

1. Create an empty new project as described above.
2. Hinzufügen a single chapter.
3. Select this chapter, then `add multiple sections
   <section_menu.html#mehrere-abschnitte-hinzufugen>`__.
4. If you need a number of new sections above the limit,
   repeat step 3.
   However, it is recommended to start with a few sections
   that are easier to distribute to the chapters to be created later.
   You can extend the plot grid over time.
5. Create the `Plotlinien <plot_menu.html#plotlinie-hinzufugen>`__ you need.
6. `Exportieren a plot grid <plot_menu.html#handlungsraster-plot-grid-zum-bearbeiten-exportieren>`__
   and fill the table cells.
7. `Importieren <import_menu.html>`__ the plot grid.
8. `Hinzufügen more chapters <chapter_menu.html#hinzufugen>`__ and
   `move the sections <desktop.html#move-tree-elements>`__
   to them.

-----------------


Mit einem angefangenen Werk beginnen
------------------------------------

Let's assume that you have already written an extensive novel Manuskript with
*Writer* and now want to continue with *novelibre*.
In this case you first make sure to set it up in a way, *novelibre* can
recognize its parts, chapters, and sections.

.. important::
   How to set up a work in progress for import
      A work in progress must not have any third level heading.
      
      -  *Heading 1* → Teil Titel.
      -  *Heading 2* → Kapitel Titel.
      -  ``* * *`` → Abschnitt divider (not needed for the first section in a
         chapter).
      -  Alle other text is considered section content.

.. caution::
   Formatting that is not `supported with novelibre 
   <basic_concepts.html#text-formatieren>`__ is lost.
   The same applies to images. 
   So if your work depends on a sophisticated layout that is beyond 
   *novelibre's* capabilities, consider using comments as reminders 
   as you write. That will help you doing the special formatting at 
   the end, when you prepare the finished novel for publication. 
   If this is not enough, *novelibre* may not be  the right tool for you.
      
When your Manuskript is ready, create your new project
with **Datei > Neu > Aus ODT erzeugen...**.

.. figure:: _images/getting_started09.png
   :alt: novelibre Screenshot

A file selection dialog opens and asks for the *ODT* document. The new project
will be created in the same directory and named after the Manuskript file, but
with the *.novx* extension.

.. caution::
   Once your novel is imported into *novelibre*, your initial *ODT* document is no
   longer needed. So if you want to keep it, you best move it elsewhere, so that
   it is not overwritten by an `exported document 
   <export_menu.html#manuskript-zum-drucken-nur-exportieren>`__ later on. 

.. tip::
   After importing an extensive piece of work, you may have a whole lot
   of sections that need to be named and described. 
   A `plot grid <plotting.html#handlungsraster-plot-grid>`__ might be a great help for
   doing this. 



Mit einer Gliederung beginnen
-----------------------------

Instead of a work in progress, you also can import an outline made with *Writer*
into *novelibre* to get a novel project with empty, but named and described
chapters and sections.
At first glance, an outline looks the same as a work in progress, but it has
third level headings for the sections, indicating their Titels. If *novelibre*
finds third-level headings, it considers all body text to be description.
In this case, formatting doesn't matter.

.. important::
   How to set up an outline for import
      An outline has at least one third level heading.
      
      -  *Heading 1* → Teil Titel.
      -  *Heading 2* → Kapitel Titel.
      -  *Heading 3* → Abschnittstitel.
      -  Alle other text is considered to be chapter/section description.

When your Manuskript is ready, create your new project
with **Datei > Neu > Aus ODT erzeugen...**.

.. figure:: _images/getting_started09.png
   :alt: novelibre Screenshot

A file selection dialog opens and asks for the *ODT* document. The new project
will be created in the same directory and named after the Manuskript file, but
with the *.novx* extension.

.. caution::
   Once your novel is imported into *novelibre*, your initial *ODT* document is no
   longer needed. So if you want to keep it, you best move it elsewhere, so that
   it is not overwritten by an `exported document 
   <export_menu.html#manuskript-zum-drucken-nur-exportieren>`__ later on. 
      