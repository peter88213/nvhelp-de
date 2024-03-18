Erste Schritte
==============

Von Null beginnen
-----------------

If you start *novelibre* by dragging a *.novx* file onto the icon,
that project will be opened. Otherwise, the project from the last
session will be automatically reopened, if there is one.

Let's assume that neither is the case, for example when the program
is called up for the very first time after installation.
Let's also assume that we have not yet made any preparations, i.e.
we have neither a work in progress nor an outline of any kind. First
of all, we create a new empty project with **Datei > Neu > Leeres Projekt**.

.. figure:: _images/getting_started01.png
   :alt: novelibre screenshot
   
A file selection dialog opens and asks for the file name and location
of the new project.

.. tip::
   It is advantageous to create a separate folder for the project, as 
   all exported documents are also stored here. This also includes 
   auxiliary files such as timelines or project-related configuration 
   files for tools and plugins. 

It is not mandatory, but we should then enter a Titel and the author's
name. Perhaps also a description of our idea. To get started right away,
we will postpone the remaining project settings until later.

.. figure:: _images/getting_started02.png
   :alt: novelibre screenshot
   
We need at least one section in order to get space to begin writing.
And this must belong to a chapter. So we now create the first
chapter with **Kapitel > Hinzufügen**.

.. figure:: _images/getting_started03.png
   :alt: novelibre screenshot
   
After the chapter is created, *novelibre* sets the focus on the chapter
Titel entry at the top of the right pane. Let's overwrite the default
Titel.

.. figure:: _images/getting_started04.png
   :alt: novelibre screenshot
   
.. hint::
   If you decide to have *novelibre* `auto-number the chapters 
   <book_view.html#automatische-nummerierung>`__, you can skip this and keep the
   default chapter Titel. 

There are several ways to add a section now. In this example, we
right-click on the chapter, and select **Hinzufügen section**.

.. figure:: _images/getting_started05.png
   :alt: novelibre screenshot


Gleich mit dem Manuskript beginnen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As soon as the new section appears in the Baumansicht, we can export a
Manuskript. Just click on the |Exportieren Manuskript| toolbar icon.

.. |Exportieren Manuskript| image:: _images/Manuscript.png

.. figure:: _images/getting_started06.png
   :alt: novelibre screenshot
   
Fertiggestellt! *Writer* should now appear with the Manuskript open.
Just start writing your novel within the text boundary.

.. figure:: _images/getting_started07.png
   :alt: Libreoffice screenshot
   
We can now continue working with *Writer* `as described on the next
page <writing.html>`__, creating new sections and chapters as we write.

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
Or you can leave it at one chapter for the time being and create empty sections
in it, which you can later distribute to chapters.
The results of this preliminary work can be exported as text documents in the
form of synopses, e.g on
`chapter <chapter_menu.html#kapitelbeschreibungen-zum-bearbeiten-exportieren>`__ or
`section <section_menu.html#abschnittsbeschreibungen-zum-bearbeiten-exportieren>`__ level.


Eine dramaturgische Struktur aufbauen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

However, you can also start on a more abstract level and first create and
describe stages like acts or steps in order to later insert the sections as
scenes.
For this, you first create at least one chapter. Then create your stages.

.. figure:: _images/getting_started08.png
   :alt: novelibre screenshot

The system is described on the `Plotting with novelibre <plotting.html>`__
page.
There you also can learn how to set up multiple strands or character arcs.

.. tip::
   Mit the `nv_templates plugin
   <https://github.com/peter88213/nv_templates/>`__ you can have 
   *novelibre* set up your new project with a pre-made structure like the
   "Drei-Akt-Modell" or "Save The Cat". 


Ein Handlungsraster anlegen
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to outline your novel using a `plot grid
<plotting.html#handlungsraster-(plot-grid)>`__, you can do this with
*novelibre*:

1. Create an empty new project as described above.
2. Hinzufügen a single chapter.
3. Select this chapter, then `add multiple sections
   <section_menu.html#mehrere-abschnitte-hinzufügen>`__.
4. If you need a number of new sections above the limit,
   repeat step 3.
   However, it is recommended to start with a few sections
   that are easier to distribute to the chapters to be created later.
   You can extend the plot grid over time.
5. Create the `Plotlinien <plot_menu.html#plotlinie-hinzufügen>`__ you need.
6. `Exportieren a plot grid <export_menu.html#handlungsraster-(plot-grid)-zum-bearbeiten>`__
   and fill the table cells.
7. `Importieren <import_menu.html>`__ the plot grid.
8. `Hinzufügen more chapters <chapter_menu.html#hinzufügen>`__ and
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
   :alt: novelibre screenshot

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
   A `plot grid <plotting.html#handlungsraster-(plot-grid)>`__ might be a great help for
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
   :alt: novelibre screenshot

A file selection dialog opens and asks for the *ODT* document. The new project
will be created in the same directory and named after the Manuskript file, but
with the *.novx* extension.

.. caution::
   Once your novel is imported into *novelibre*, your initial *ODT* document is no
   longer needed. So if you want to keep it, you best move it elsewhere, so that
   it is not overwritten by an `exported document 
   <export_menu.html#manuskript-zum-drucken-nur-exportieren>`__ later on. 
      