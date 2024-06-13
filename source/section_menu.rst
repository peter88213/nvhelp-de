Abschnitt-Menü
==============

**Abschnittsfunktionen**

.. figure:: _images/section_menu01.png
   :alt: novelibre Screenshot

Hinzufügen
----------

**Einen neuen Abschnitt erzeugen**

Mit **Abschnitt > Hinzufügen**
können Sie einen `Abschnitt <basic_concepts.html#abschnitte>`__
in den Baum einfügen.

- Der neue Abschnitt wird an die nächste freie Stelle nach der Auswahl gesetzt,
  falls möglich.
- Andernfalls wird kein Abschnitt erzeugt.
- Der neue Abschnitt hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.

Eigenschaften eines neuen Abschnitts:
   -  Typ: *Normal*
   -  Fertigstellungsstatus: *Gliederung*
   -  Keine Perspektivfigur zugewiesen
   -  Keine Plotlinie zugewiesen
   -  Keine Tags
   -  Keine Angaben zu Datum, Zeit und Dauer


Mehrere Abschnitte hinzufügen
-----------------------------

**Hinzufügen new sections in bulk**

.. figure:: _images/section_menu04.png
   :alt: novelibre Screenshot

Mit **Abschnitt > Mehrere Abschnitte hinzufügen**
können Sie add up to 20 sections to the tree.

- You will be prompted to enter the number of new sections.
- The number of sections to be added at once is limited to 20.
- The new sections are placed at the next free position after the selection, if
  possible.
- Otherwise, no new section is generated.


Typ wählen
----------

**Set the type of the selected section**

Mit **Abschnitt > Typ wählen**
können Sie set the `type <basic_concepts.html#teil-kapitel-abschnittstypen>`__
of the selected section to *Normal* or *Unbenutzt* .

.. figure:: _images/section_menu02.png
   :alt: novelibre Screenshot

.. hint::

   Type change for multiple sections:
      - Either select multiple sections, or
      - select a chapter.


Status setzen
-------------

**Set the section completion status**

.. figure:: _images/section_menu03.png
   :alt: novelibre Screenshot

Mit **Abschnitt > Status setzen**
können Sie set the `completion status
<basic_concepts.html#abschnitts-status>`__
of the selected section to *Gliederung*, *Entwurf*, *1. Überarbeitung*, *2. Überarbeitung*,
or *Fertiggestellt*.

.. hint::

   Status change for multiple sections:
      -  Either select multiple sections, or
      -  select a parent node (chapter or Buch)


Abschnittsbeschreibungen zum Bearbeiten exportieren
---------------------------------------------------

**Ein ODT-Dokument exportieren**

Mit **Abschnitt > Abschnittsbeschreibungen zum Bearbeiten exportieren**
können Sie ein Textdokument erzeugen, das eine
**vollständige Inhaltsangabe** mit Teile-/Kapitelüberschriften
und Abschnittsbeschreibungen enthält,
die bearbeitet und zurückgeschrieben werden können.
Der Dateinamenszusatz lautet ``_sections_tmp``.


Abschnittsliste (nur Exportieren)
---------------------------------

**Ein ODS-Dokument exportieren**

Mit **Abschnitt > Abschnittsliste (nur Exportieren)**
können Sie ein Tabellenkalkulationsdokument
mit einer Reihe pro Abschnitt erzeugen, welche die
folgenden Daten umfasst:

- Abschnitts-ID (eingeklappt)
- Abschnittsnummer (Hyperlink zum Manuskript)
- Titel
- Beschreibung
- Perspektivfigur
- Datum
- Zeit
- Tag
- Dauer
- Tags
- Abschnittsnotizen
- Szene
- Ziel
- Konflikt
- Ausgang
- Fertigstellungsstatus
- Fortlaufende Wortzählung
- Wortzahl des Abschnitts
- Figuren
- Schauplätze
- Gegenstände

.. note::
   Only "normal" sections appear in the section list. 
   Abschnitte of the "Unbenutzt" type are omitted.

Der Dateinamenszusatz lautet ``_sectionlist``.

