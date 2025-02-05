Abschnitt-Menü
==============

**Abschnittsfunktionen**

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
   -  Keine Schlagwörter
   -  Keine Angaben zu Datum, Zeit und Dauer


Mehrere Abschnitte hinzufügen
-----------------------------

**Mehrere neue Abschnitte auf einmal erzeugen**

Mit **Abschnitt > Mehrere Abschnitte hinzufügen**
können Sie dem Baum bis zu 20 Abschnitte hinzufügen.

- Sie werden nach der Anzahl der neuen Abschnitte gefragt.
- Die Anzahl der neuen Abschnitte ist auf 20 begrenzt.
- Die neuen Abschnitte werden an die nächste freie Stelle nach
  der Auswahl gesetzt, falls möglich.
- Andernfalls wird kein Abschnitt erzeugt.


Typ wählen
----------

**Den Typ der ausgewählten Abschnitte ändern**

Mit **Abschnitt > Typ wählen**
können Sie den `Typ <basic_concepts.html#teil-kapitel-abschnittstypen>`__
der ausgewählten Abschnitte zu *Normal* oder *Unbenutzt* ändern.

.. hint::

   Um den Typ für mehrere Abschnitte gleichzeitig zu ändern:
      - Entweder mehrere Abschnitte auswählen, oder
      - das Kapitel auswählen.


Status setzen
-------------

**Den Fertigstellungsstatus des Abschnitts ändern**

Mit **Abschnitt > Status setzen**
können Sie den `Fertigstellungsstatus
<basic_concepts.html#abschnitts-status>`__
der ausgewählten Abschnitte zu *Gliederung*, *Entwurf*,
*1. Überarbeitung*, *2. Überarbeitung*
oder *Fertiggestellt* setzen.

.. hint::

   Um den Status für mehrere Abschnitte gleichzeitig zu ändern:
      - Entweder mehrere Abschnitte auswählen, oder
      - einen Elternknoten (Kapitel oder Buch) auswählen.


Abschnittsbeschreibungen zum Bearbeiten exportieren
---------------------------------------------------

**Ein ODT-Dokument exportieren**

Mit **Abschnitt > Abschnittsbeschreibungen zum Bearbeiten exportieren**
können Sie ein Textdokument erzeugen, das eine
**vollständige Inhaltsangabe** mit Teile-/Kapitelüberschriften
und Abschnittsbeschreibungen enthält.
Dieses Dokument kann mit *Writer* bearbeitet und zu *novelibre*
zurückgespielt werden.
Der Dateinamenszusatz lautet ``_sections_tmp``.


Abschnittsliste (nur Export)
----------------------------

**Ein ODS-Dokument exportieren**

Mit **Abschnitt > Abschnittsliste (nur Export)**
können Sie ein Tabellenkalkulationsdokument
mit einer Zeile pro Abschnitt und den folgenden Spalten:

- Abschnitts-ID (eingeklappt)
- Abschnittsnummer (Hyperlink zum Manuskript)
- Titel
- Beschreibung
- Perspektivfigur (Kurzname)
- Datum
- Zeit
- Tag
- Dauer
- Schlagwörter
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
   Nur "normale" Abschnitte erscheinen in der Abschnittsliste. 
   Abschnitte vom Typ "unbenutzt" werden ausgelassen.

Der Dateinamenszusatz lautet ``_sectionlist``.

Mit ``Strg``-Klick auf eine Abschnittsnummer können Sie zum entsprechenden
Abschnitt im Manuskript springen.
Wenn Sie diese Tabelle jedoch bearbeiten, lassen sich die Änderungen
(im Gegensatz zum `Handlungsraster
<plot_menu.html#handlungsraster-plot-grid-zum-bearbeiten-exportieren>`__)
nicht zu *novelibre* zurückspielen.
Die Abschnittsliste ist mehr dazu gedacht, die Metadaten des Schreibprojekts
zu extrahieren, zum Beispiel, falls man *novelibre* nicht weiterverwenden will.


Zeittafel anzeigen
------------------

**Einen HTML-Report mit einer Zeittafel anzeigen**

Mit **Abschnitt > Zeittafel anzeigen**
erzeugen Sie eine als Tabelle formatierte HTML-Seite
mit einer Zeittafel
und starten Ihren System-Webbrowser zur Anzeige.

In der Zeittafel sind die datierten "normalen" Abschnitte
in chronologischer Reihenfolge aufgeführt.
Die Spalten umfassen neben Datum/Zeit und Dauer den Abschnittstitel, die Beschreibung,
Schauplätze und Figuren sowie Plotlinien mit Plotnotizen.

.. note::
   Der Report ist eine temporäre Datei, die bei 
   Programmbeendigung automatisch gelöscht wird.
   Lassen Sie sie bei Bedarf von Ihrem Browser 
   sichern oder ausdrucken.
