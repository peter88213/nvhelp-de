Exportieren-Menü
================

**Dateiexport**

.. figure:: _images/export_menu01.png
   :alt: novelibre Screenshot

Manuskript zum Bearbeiten
-------------------------

**Ein ODT-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Exportieren >  Manuskript zum Bearbeiten**
können Sie ein Textdokument erzeugen, das in Abschnitte aufgeteilt ist
(im Navigator sichtbar).
Der Dateinamenszusatz lautet ``_Manuskript_tmp``.

- Nur "normale" Kapitel und Abschnitte werden exportiert.
  Kapitel und Abschnitte vom Typ "unbenutzt" werden ausgelassen.
- Abschnittstitel sind unsichtbar, erscheinen aber im *Navigator*.
- Kapitel und Abschnitte können weder umgeordnet noch gelöscht werden.
- Mit *Writer* können Sie Abschnitte aufteilen, indem sie Überschriften
  oder einen Abschnitstrenner einfügen:

   - *Überschrift 1* → Titel des neuen Teils.
     Wahlweise können Sie, durch ``|`` getrennt, eine Beschreibung anhängen.
   - *Überschrift 2* → Titel des neuen Kapitels
     Wahlweise können Sie, durch ``|`` getrennt, eine Beschreibung anhängen.
   - ``###`` → Abschnittstrenner.
     Wahlweise können Sie  an den Trenner einen Abschnittstitel, und,
     durch ``|`` getrennt, eine Beschreibung anhängen.

   .. important:: 
      Dokumente mit aufgeteilten Abschnitten werden nach dem Reimport
      zu *novelibre* automatisch gelöscht.

- Textauszeichnungen: Fett- und Kursivschreibung werden reimportiert.
  Andere Auszeichnungen wie Unterstreichung oder Durchstreichung gehen verloren.


Manuskript für fremde Textverarbeitung
--------------------------------------

**Ein ODT-Dokument exportieren, das bearbeitet und zurückgelesen werden kann**

Mit **Exportieren >  Manuskript für fremde Textverarbeitung**
können Sie ein Textdokument mit sichtbaren Abschnittsamarkierungen erzeugen.
Der Dateinamenszusatz lautet ``_proof_tmp``.

.. note::
   Dieses Dokument behält seine Abschnittsinformationen auch dann, 
   wenn es in andere Dateiformate konvertiert wird und umgekehrt.
   Das sollte mit verbreiteten kommerziellen Textverarbeitungsprogrammen
   funktionieren, auch mit webbasierten Textverarbeitungen wie Google Docs. 


- Nur "normale" Kapitel und Abschnitte werden exportiert.
  Kapitel und Abschnitte vom Typ "unbenutzt" werden ausgelassen.
- Das Dokument enthält Kapitel- und Abschnittsüberschriften.
  Änderungen daran werden jedoch nicht reimportiert.
- Das Dokument enthält Abschnittsmarkierungen in der Form ``[scx]``.
  **Ändern Sie nichts an den Zeilen mit Abschnittsmarkierungen**
  sonst können Sie das geänderte Dokument nicht in *novelibre* reimportieren.
- Kapitel und Abschnitte können weder umgeordnet noch gelöscht werden.
- Mit *Writer* können Sie Abschnitte aufteilen, indem sie Überschriften
  oder einen Abschnitstrenner einfügen:

   - *Überschrift 1* → Titel des neuen Teils.
     Wahlweise können Sie, durch ``|`` getrennt, eine Beschreibung anhängen.
   - *Überschrift 2* → Titel des neuen Kapitels
     Wahlweise können Sie, durch ``|`` getrennt, eine Beschreibung anhängen.
   - ``###`` → Abschnittstrenner.
     Wahlweise können Sie  an den Trenner einen Abschnittstitel, und,
     durch ``|`` getrennt, eine Beschreibung anhängen.

   .. important:: 
      Dokumente mit aufgeteilten Abschnitten werden nach dem Reimport
      zu *novelibre* automatisch gelöscht.

-  Textauszeichnungen: Fett- und Kursivschreibung werden reimportiert.
   Andere Auszeichnungen wie Unterstreichung oder Durchstreichung gehen verloren.


Manuskript zum Drucken (nur Export)
-----------------------------------

**Ein ODT-Dokument exportieren**

Mit **Exportieren >  Manuskript zum Drucken (nur Export)**
können Sie ein Textdokument zum weiteren Gebrauch erzeugen,
z.B. als endgültiges Dokument, wenn sie mit *novelibre* fertig sind.

.. hint::
   Im Gegensatz zum editierbaren Manuskript ist dieses Dokument nicht intern
   in Abschnitte unterteilt. 
   Das soll die weitere Verarbeitung und Formatierung erleichtern.


- Das Dokument wird im selben Dateiverzeichnis wie das Projekt platziert.
- Der **Dateiname**: ``<Projektname>.odt``.
- Nur "normale" Kapitel und Abschnitte werden exportiert.
  Kapitel und Abschnitte vom Typ "unbenutzt" werden ausgelassen.
- Teiletitel erscheinen als Überschriften auf erster Ebene.
- Kapiteltitel erscheinen als Überschriften auf zweiter Ebene.
- Abschnitte sind durch ``* * *`` getrennt.
- Die erste Zeile des jeweils ersten Absatzes ist nicht eingezogen.
- Vom zweiten Absatz an beginnen die Absätze mit eingezogener Erstzeile.
- Abschnitte, die mit
  `An den vorherigen Abschnitt anhängen
  <section_view.html#an-den-vorherigen-abschnitt-anhangen>`__ markiert sind,
  erscheinen als fortlaufende Absätze.
- Dem erste Absatz jedes Kapitels ist die Absatzvorlage *Kapitelanfang* 
  zugewiesen, die standardmäßig dem Textkörper ohne Einzug gleicht. 
  Wenn Sie diese Vorlage verändern, können Sie den Kapitelanfängen ein
  besonderes Aussehen verleihen, z.B. mit Initialen.

.. tip::
   Falls Sie in Ihrem fertigen Dokument anstelle der drei-Sternchen-Abschnittstrenner 
   lieber einfache Leerzeilen wollen, 
   lässt sich das durch "Suchen und Ersetzen" bewerkstelligen.
   Besonders komfortabel geht das mit einem Makro, das in der
   `novelibre-tools 
   <https://github.com/peter88213/novelibre-tools/>`__-Erweiterung enthalten ist.



Kurzzusammenfassung (nur Export)
--------------------------------

**Ein ODT-Dokument exportieren**

Mit **Exportieren >  Kurzzusammenfassung (nur Export)**
können Sie ein Textdokument erzeugen, das eine
**kurze Zusammenfassung** mit den Titeln
der Teile, Kapitel und Abschnitte enthält.
Der Dateinamenszusatz lautet ``_brf_synopsis``.

- Nur "normale" Kapitel und Abschnitte werden exportiert.
  Kapitel und Abschnitte vom Typ "unbenutzt" werden ausgelassen.
- Teiletitel erscheinen als Überschriften auf erster Ebene.
- Kapiteltitel erscheinen als Überschriften auf zweiter Ebene.
- Abschnittstitel erscheinen als normale Absätze.


Querverweise (nur Export)
-------------------------

**Ein ODT-Dokument exportieren**

Mit **Exportieren >  Querverweise (nur Export)**
können Sie ein Textdokument erzeugen, das
Querverweise mit Hyperlinks enthält.
Der Dateinamenszusatz lautet ``_xref``.

Die Querverweise sind:

-  Abschnitte pro Figur,
-  Abschnitte pro Schauplatz,
-  Abschnitte pro Gegenstand,
-  Abschnitte pro Tag,
-  Figuren pro Tag,
-  Schauplätze pro Tag,
-  Gegenstände pro Tag.


Figuren/Schauplätze/Gegenstände-Datendateien
--------------------------------------------

**XML-Dateien exportieren, die in anderen Projekten importiert werden können**

Mit **Exportieren >  Figuren/Schauplätze/Gegenstände-Datendateien**
können Sie einen Satz XML-Dateien mit den Figuren, Schauplätzen und
Gegenständen des Projekts inklusive ihrer Eigenschaften enthält.
Mit diesen Dateien können Sie Figuren, Schauplätze und
Gegenstände in ein anderes Projekt transferieren.

.. hint::
   Um XML-Datendateien aus einem anderen Projekt zu importieren, 
   rufen Sie im **Figuren**, **Schauplätze** oder 
   **Gegenstände**-Menü **Importieren** auf.


Optionen
--------

**Projektunabhängige Programmeinstellungen**

Mit **Exportieren >  Optionen**
können Sie einen Dialog für Einstellungen zum Dokumentenexport öffnen.

.. figure:: _images/export_menu02.png
   :alt: novelibre Screenshot


Vor dem Öffnen exportierter Dokumente nachfragen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dieses Auswahlfeld steuert das Verhalten beim Dokumentenexport.

- Wenn angekreuzt, werden Sie gefragt, ob *novelibre* neu erzeugte
  Dokumente in *Writer* oder *Calc* öffnen soll.

- Wenn nicht angekreuzt, wird *novelibre* neu erzeugte
  Dokumente in *Writer* oder *Calc* ohne Rückfrage öffnen.


Nach dem Dokumentenexport zum Editieren das Projekt sperren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dieses Auswahlfeld steuert das Verhalten beim Öffnen von Dokumenten zur Bearbeitung.

- Wenn angekreuzt, wird *novelibre* das `Projekt automatisch sperren
  <basic_concepts.html#projekt-sperre>`__, wenn es *Writer* oder *Calc* aufruft.

- Wenn nicht angekreuzt, wird *novelibre* das Projekt nicht sperren,
  wenn es *Writer* oder *Calc* aufruft.
