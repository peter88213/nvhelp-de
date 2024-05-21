Abschnittseigenschaften
=======================

The Abschnitt properties view öffnet sich im rechten Fenster when you
select a section in the tree.


.. figure:: _images/section_view01.png
   :alt: Screenshot

Titel und Beschreibung
----------------------

Titel und Beschreibung werden als beschreibbare "Karteikarte" dargestellt.

Die Bearbeitung des Titels kann mit der Eingabetaste beendet werden.
Änderungen an der Beschreibung werden übernommen, sobald mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.


Tags
----

Tags are a very freely usable tool for labeling sections in the
Baumansicht. Tags do not have to be defined elsewhere, but simply
entered in the input field separated by semicolons.
Die Bearbeitung kann mit der Eingabetaste beendet werden.

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

Mit te **Unbenutzt** Auswahlfeld kann man change the `section type
<basic_concepts.html#teil-kapitel-abschnittstypen>`__.

An den vorherigen Abschnitt anhängen
------------------------------------

When ticked, there will be no section divider inserted above
the selected section in exported documents. The section
just starts a new paragraph.


Plot
----

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/section_view04.png
   :alt: Screenshot

Plotlinien
~~~~~~~~~~

Hier kann man assign the selected section to the Plotlinien it belongs to.
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


Szene
-----

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/section_view03.png
   :alt: Screenshot

There is a popular theory for "selling writers" that suggests novels
are best divided into scenes, alternating between "action scenes" and
"reaction scenes", or "scenes" and "sequels". If you want to implement
something like this to ensure suspense kann man do so here.

If this is not for you, but you would like to use a different method
to set up a dramaturgical scene micro-structure kann man set the section
to **Andere** and get three `freely named <book_view.html#umbenennungen>`_
text fields.

.. figure:: _images/section_view06.png
   :alt: Screenshot
   
   Example of a non-standard scene category

On the other hand, not every section is a scene to which the categories
mentioned above appliy. Sections can be characterized by mode of discourse 
(e.g. Narration, Dramatic action, Dialogue, Description, Exposition).
So if a section is not staged, you can set the section to **Keine Szene**,
and get three `freely named <book_view.html#umbenennungen>`_
text fields.

.. figure:: _images/section_view07.png
   :alt: Screenshot
   
   Example of a non-staged section category


Beziehungen
-----------

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/section_view02.png
   :alt: Screenshot

If you want to associate characters, locations, and items with the
section kann man do it here by adding the element to a list of
relationships.

Alter anzeigen
   If a section is dated kann man call up the ages of the related
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

Hier kann man enter information about the selected section's narrative time.
Die Bearbeitung kann mit der Eingabetaste beendet werden.

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
      If necessary kann man convert all sections at once in the 
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

Der gelbe Texteingabebereich ist für Notizen.
Änderungen werden übernommen, wenn mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.

Wenn der "Haftmerker" einers Abschnitts Text enthält,
erscheint in the Baumansicht ein "N" als Merker.

Wenn ein Kapitelzweig mit Abschnitten, die notizen enthalten,
eingeklappt wird, erscheint das "N" in der Kapitelzeile.

.. note::
   Die "Haftmerker" sind nur für die Arbeit mit *novelibre* gedacht.
   Sie werden nicht beim Dokumentenexport berücksichtigt.
   Allerdings erscheinen sie in der `Abschnittsliste`_.

.. _Abschnittsliste: section_menu.html#exportieren-section-list-spreadsheet

Navigationsschaltflächen
------------------------

- **Zurück** moves the selection to the previous section in the tree.
- **Vor** moves the selection to the next section in the tree.
