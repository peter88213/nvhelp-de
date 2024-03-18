Abschnitt-Menü
==============

**Abschnitt operation**

.. figure:: _images/section_menu01.png
   :alt: novelibre screenshot

Hinzufügen
----------

**Hinzufügen a new section**

Mit **Abschnitt > Hinzufügen**,
you can add a `section <basic_concepts.html#abschnitte>`__ to the tree.

- The new section is placed at the next free position after the selection, if
  possible.
- Otherwise, no new section is generated.
- The new section has an auto-generated Titel. You can change it in
  the right pane.

Eigenschaften of a new section:
   -  *Normal* type
   -  *Gliederung* completion status
   -  No viewpoint character assigned
   -  No Plotlinie or tag assigned
   -  No date/time set


Mehrere Abschnitte hinzufügen
-----------------------------

**Hinzufügen new sections in bulk**

.. figure:: _images/section_menu04.png
   :alt: novelibre screenshot

Mit **Abschnitt > Mehrere Abschnitte hinzufügen**,
you can add up to 20 sections to the tree.

- You will be prompted to enter the number of new sections.
- The number of sections to be added at once is limited to 20.
- The new sections are placed at the next free position after the selection, if
  possible.
- Otherwise, no new section is generated.


Typ wählen
----------

**Set the type of the selected section**

Mit **Abschnitt > Typ wählen**,
you can set the `type <basic_concepts.html#teil-kapitel-abschnittstypen>`__
of the selected section to *Normal* or *Unbenutzt* .

.. figure:: _images/section_menu02.png
   :alt: novelibre screenshot

.. hint::

   Type change for multiple sections:
      - Either select multiple sections, or
      - select a chapter.


Status setzen
-------------

**Set the section completion status**

.. figure:: _images/section_menu03.png
   :alt: novelibre screenshot

Mit **Abschnitt > Status setzen**,
you can set the `completion status
<basic_concepts.html#abschnitts-status>`__
of the selected section to *Gliederung*, *Entwurf*, *1. Überarbeitung*, *2. Überarbeitung*,
or *Fertiggestellt*.

.. hint::

   Status change for multiple sections:
      -  Either select multiple sections, or
      -  select a parent node (chapter or Buch)


Abschnittsbeschreibungen zum Bearbeiten exportieren
---------------------------------------------------

**Exportieren an ODT document**

Mit **Abschnitt > Abschnittsbeschreibungen zum Bearbeiten exportieren**
kann man ein neues OpenDocument-Textdokument (odt) erzeugen,
das eine **vollständige Inhaltsangabe** mit Teile-/Kapitelüberschriften
und Abschnittsbeschreibungen enthält,
die bearbeitet und zurückgeschrieben werden können.
Der Dateinamenszusatz lautet ``_sections_tmp``.


Abschnittsliste (nur Exportieren)
---------------------------------

**Exportieren an ODS document**

Mit **Abschnitt > Abschnittsliste (nur Exportieren)**
kann man eine neue OpenDocument-Tabelle (ods)
mit einer Reihe pro Abschnitt erzeugen, welche die
folgenden Daten umfasst:

- Die Abschnitts-ID als hyperlink zum Abschnitt im Manuskript
  (falls vorhanden)
- Abschnittstitel
- Abschnittsbeschreibung
- Erzähldatum
- Erzählzeit
- Tags
- Abschnittsnotizen
- A/R
- Ziel
- Konflikt
- Ausgang
- Fortlaufende Abschnittsnummer
- Fortlaufende Wortzählung
- Wortzahl des Abschnitts
- Figuren
- Schauplätze
- Gegenstände

.. note::
   Only "normal" sections appear in the section list. 
   Abschnitts of the "Unbenutzt" type are omitted.

Der Dateinamenszusatz lautet ``_sectionlist``.

