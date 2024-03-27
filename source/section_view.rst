Abschnittseigenschaften
=======================

The Abschnitt properties view öffnet sich im rechten Fenster when you
select a section in the tree.


.. figure:: _images/section_view01.png
   :alt: Screenshot

Titel und Beschreibung
----------------------

Titel und Beschreibung are displayed in an editable "Karteikarte".

The editing of the Titel can be completed by pressing the Eingabetaste.
Changes to the description are applied when the mouse is clicked
anywhere outside the text input field.


Tags
----

Tags are a very freely usable tool for labeling sections in the
Baumansicht. Tags do not have to be defined elsewhere, but simply
entered in the input field separated by semicolons.
Editing can be completed by pressing the Eingabetaste.

.. caution::
   If you want to use a tag more than once, make sure you use 
   the same spelling in the different places. 

Perspektive
-----------

The viewpoint character's short name is displayed in the Baumansicht.
You can select it from a drop-down list containing all characters
in the Baumansicht's sort order.

Unbenutzt
---------

Mit te **Unbenutzt** Auswahlfeld, you can change the `section type
<basic_concepts.html#teil-kapitel-abschnittstypen>`__.

An den vorherigen Abschnitt anhängen
------------------------------------

When ticked, there will be no section divider inserted above
the selected section in exported documents. The section
just starts a new paragraph.


Plot
----

Aufklappen or collapse this frame by clicking on the label.

.. figure:: _images/section_view04.png
   :alt: Screenshot

Plotlinien
~~~~~~~~~~

Here you can assign the selected section to the Plotlinien it belongs to.
The assigned Plotlinien are displayed in a list in the order they are
assigned to the section.

.. tip::
   A more convenient way to manage and keep track of Plotlinie assignments is 
   offered by the `nv_matrix plugin 
   <https://github.com/peter88213/nv_matrix/>`__. 
   
   You can also assign a section to a Plotlinie by entering text
   in the corresponding *Plotlinie notes* cell of the 
   `plot grid <plotting.html#handlungsraster-plot-grid>`__. 

Hinzufügen Plotlinie assignment
   When clicking on |Hinzufügen|, the "Pick mode"
   is activated, and the cursor changes to a "plus" shape. By clicking
   on a Plotlinie, it will be related with the section.

   .. hint::
      You can exit the "Pick mode" without selecting an element by
      clicking on the highlighted status bar, or by pressing the ``Esc``
      key. 

Plotlinie entfernen assignment
   When clicking on |Entfernen| or pressing the ``Entf``-Taste,
   the selected Plotlinie is removed from the list.

Ansicht the related element
   When double-clicking on a Plotlinie, or clicking on |Goto|,
   the selected Plotlinie is opened and its properties are displayed.

   .. hint::
      You can go back to the initially selected section with |Go Back|. 

Plotlinie notes
   You can enter section-related notes for the Plotlinie selected
   in the list of related Plotlinien. These notes appear in the
   `plot grid <plotting.html#handlungsraster-plot-grid>`__ where you also can
   edit them.



Plotpunkte
~~~~~~~~~~

The plot points assigned with the selected section are displayed
along with their Plotlinien.

.. hint::
   To change or clear the plot point assignment, go to the
   `plot point's properties <point_view.html#assigned-section>`__.


Aktion/Reaktion
---------------

Aufklappen or collapse this frame by clicking on the label.

.. figure:: _images/section_view03.png
   :alt: Screenshot

There is a popular theory for "selling writers" that suggests novels
are best divided into scenes, alternating between "action scenes" and
"reaction scenes", or "scenes" and "sequels". If you want to implement
something like this to ensure suspense, you can do so here.

If this is not for you, but you would like to use a different method
to set up a dramaturgical scene micro-structure, you can set the section
to **Benutzerdefiniert** and get three `freely named <book_view.html#umbenennungen>`_
text fields.

.. figure:: _images/section_view06.png
   :alt: Screenshot
   
   Example of a user-defined scene category

.. note::
   The "Ziel/Konflikt/Ausgang" data is only for working with *novelibre*.
   It is not meant to be exported into a document.
   However, it all appears in the `section list`_.

Beziehungen
-----------

Aufklappen or collapse this frame by clicking on the label.

.. figure:: _images/section_view02.png
   :alt: Screenshot

If you want to associate characters, locations, and items with the
section, you can do it here by adding the element to a list of
relationships.

Alter anzeigen
   If a section is dated, you can call up the ages of the related
   characters who have `birth dates <character_view.html#biographie>`__.

Hinzufügen Relationship
   When clicking on |Hinzufügen|, the "Pick mode"
   is activated, and the cursor changes to a "plus" shape. By clicking
   on a character/location/item, this element will be related with the
   section.

   .. hint::
      You can exit the "Pick mode" without selecting an element by
      clicking on the highlighted status bar, or by pressing the ``Esc``
      key. 

Entfernen Relationship
   When clicking on |Entfernen| or pressing the ``Entf``-Taste,
   the selected relationship is removed from the list.

Ansicht the related element
   When double-clicking on a related element, or clicking on |Goto|,
   the selected element is opened and its properties are displayed.

   .. hint::
      You can go back to the initially selected section with |Go Back|. 

.. hint::
   A convenient way to manage and keep track of relationships is offered 
   by the `nv_matrix plugin 
   <https://github.com/peter88213/nv_matrix/>`__. 


.. |Hinzufügen| image:: _images/add.png
.. |Goto| image:: _images/goto.png
.. |Entfernen| image:: _images/remove.png
.. |Go back| image:: _images/goBack.png


Datum/Zeit
----------

Here you can enter information about the selected section's narrative time.
Editing can be completed by pressing the Eingabetaste.

.. hint::
   Dedicated timeline software offers a more convenient way of entering date/time 
   and duration information. So if chronology is important to your story, you
   might want to take a look at the `Zeitline plugin 
   <https://github.com/peter88213/nv_timeline/>`__, or the 
   `Aeon Zeitline 2 plugin <https://github.com/peter88213/nv_aeon2/>`__.

.. figure:: _images/section_view05.png
   :alt: Screenshot

Beginn
~~~~~~

If the selected section is a scene, this is when it starts:

Datum
   Format: *YYYY-MM-DD*, according to ISO 8601.

Zeit
   Format: *hh:mm*, according to ISO 8601.

Tag
   Format: Any number. Tag "0" is the `reference date
   <book_view.html#erzahlzeit>`_, if set.

.. note::
   Alle entries are optional. You can either enter a date, or a day. 
   
Datum/Zeit löschen
   This will reset *Datum*, *Zeit*, and *Tag* simultaneously.

Erzeugen
   This generates date and time from the date/time/duration data of the
   `previous section <Navigationsschaltflächen_>`_, so the selected section
   follows directly the previous one.

Datum/Tag umwandeln
   If the `reference date <book_view.html#erzahlzeit>`__ is set,
   The unspecific *Tag* can be transformed into a specific *Datum*,
   and vice versa.

   .. hint::
      If necessary, you can convert all sections at once in the 
      `Buch properties view <book_view.html#erzahlzeit>`__.
   

Dauer
~~~~~

Tage
   Any number should be accepted.

Stunden
   If a number greater than 24 is entered, the number of days
   will be automatically increased.

Minuten
   If a number greater than 60 is entered, the number of hours
   will be automatically increased.

Dauer löschen
   This will reset *Tage*, *Stunden*, and *Minuten* simultaneously.

Erzeugen
   This generates the duration from the date/time data of the
   `next section <Navigationsschaltflächen_>`_, so the next section
   follows directly the current one.


"Haftmerker"
------------

The yellow text area is for notes. Changes are applied
when the mouse is clicked anywhere outside the text input field.

When the "sticky note" of a section contains text, an "N" is
displayed in the Baumansicht as a reminder. If the branch of a chapter
with sections containing notes is collapsed, the "N" is displayed
in the chapter row.

.. note::
   The "sticky notes" are only for working with *novelibre*.
   They are not meant to be exported into a document.
   However, they appear in the `section list`_.

.. _section list: section_menu.html#exportieren-section-list-spreadsheet

Navigationsschaltflächen
------------------------

- **Zurück** moves the selection to the previous section in the tree.
- **Vor** moves the selection to the next section in the tree.
