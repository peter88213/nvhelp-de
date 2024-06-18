Baumansicht Kontextmenü
=======================

Wenn sie im linken Fenster auf ein Projektbaumelement rechtsklicken,
öffnet sich ein passendes Kontextmenü.

.. hint::
   Ausgegraute Elemente sind nicht verfügbar, z.B. wegen "Projektsperre".


Buch-Kontextmenüeinräge
-----------------------

.. figure:: _images/context_menu01.png
   :alt: novelibre Screenshot

Abschnitt hinzufügen
~~~~~~~~~~~~~~~~~~~~

Einen neuen Abschnitt erzeugen.

- Der neue Abschnitt wird an die nächste freie Stelle nach der Auswahl gesetzt.
- Der neue Abschnitt hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.

Eigenschaften eines neuen Abschnitts:
   -  Typ: *Normal*
   -  Fertigstellungsstatus: *Gliederung*
   -  Keine Perspektivfigur zugewiesen
   -  Keine Plotlinie zugewiesen
   -  Keine Tags
   -  Keine Angaben zu Datum, Zeit und Dauer


Kapitel hinzufügen
~~~~~~~~~~~~~~~~~~

Ein neues Kapitel erzeugen.

- Das neue Kapitel wird an die nächste freie Stelle nach der Auswahl gesetzt.
- Das neue Kapitel hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.


Teil hinzufügen
~~~~~~~~~~~~~~~

Einen neuen Teil erzeugen.

- Der neue Teil wird auf Kapitelebene an der nächsten freien Position
  nach der Auswahl platziert.
- Im Projektbaum ist der Teil auf der selben Ebene wie die Kapitel,
  so dass die Kapitel nicht Kinder des Teils sind.
  Damit ist es einfacher, die Teilegrenzen zu verschieben.
- Der neue Teil hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.


Stadium einfügen
~~~~~~~~~~~~~~~~

Ein neues Stadium am nächsten freien Platz nach der Auswahl einfügen.

- Das neue Stadium hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.
- Standardmäßig ist das neue Stadium auf der zweiten Ebene.


Ebene ändern
~~~~~~~~~~~~

Die Ebene eines Kapitels oder Stadiums ändern.

-  **Erste Ebene** wandelt ein Kapitel in einen Teil um.
-  **Zweite Ebene** wandelt einen Teil in ein Kapitel um.


Löschen
~~~~~~~

Das ausgewählte Baumelement mit allen seinen Kindern löschen.

- Teile und Kapitel werden gelöscht.
- Abschnitte weerden als "unbenutzt" markiert und ins "Papierkorb"-Kapitel verschoben.
- Einen Teil zu löschen, hat keinen Einfluss auf die nachgeordneten Kapitel.
- Wird ein Kapitel gelöscht, verschiebt das seine Abschnitte ins "Papierkorb" Kapitel.
- Das "Papierkorb"-Kapitel wird bei Bedarf automatisch erzeugt.
- Löscht man das "Papierkorb"-Kapitel, werden auch die enthaltenen Abschnitte unwiederbringlich gelöscht.


Typ wählen
~~~~~~~~~~

Den `Typ <basic_concepts.html#teil-kapitel-abschnittstypen>`__
des ausgewählten Kapitels oder Abschnitts einstellen.
Dieser kann *Normal* oder *Unbenutzt* sein.

.. note::
   Wenn man den Typ eines Kapitels zu *Unbenutzt* ändert, 
   werden auch seine Abschnitte *Unbenutzt*.

Status setzen
~~~~~~~~~~~~~

Den `Fertigstellungsstatus <basic_concepts.html#abschnitts-status>`__
des ausgewählten Abschnitts ändern.

.. hint::
   Wählen Sie einen Elternknoten aus, um den Status mehrerer Abschnitte zu ändern.


Mit dem vorhergehenden zusammenfassen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Zwei Abschnitte zusammenfassen, falls sie zum selben Kapitel gehören,
den selben Typ haben und die selbe Perspektivfigur.

- Neuer Titel = Titel des vorhergehenden Abschnitts & Titel des
  ausgewählten Abschnitts.
- Die Abschnittsinhalte werden miteinander verbunden und durch einen
  Absatzumbruch getrennt.
- Beschreibungen werden miteinander verbunden und durch einen
  Absatzumbruch getrennt.
- Zielangaben werden miteinander verbunden und durch einen
  Absatzumbruch getrennt.
- Konfliktangaben werden miteinander verbunden und durch einen
  Absatzumbruch getrennt.
- Ausgangsangaben werden miteinander verbunden und durch einen
  Absatzumbruch getrennt.
- Notizen werden miteinander verbunden und durch einen
  Absatzumbruch getrennt.
- Figurenlisten werden kombiniert.
- Schauplatzlisten werden kombiniert.
- Gegenstandslisten werden kombiniert.
- Plotlinienzuweisungen werden kombiniert.
- Plotpunktzuweisungen, falls vorhanden, werden zum verbundenen Abschnitt verschoben.
- Abschnittsdauern werden addiert.

.. caution::
   Denken Sie daran, dass es keine Rückgängig-Funktion gibt.

Kapitelebene anzeigen
~~~~~~~~~~~~~~~~~~~~~

Verbirgt die Abschnitte durch Einklappen des Baums,
sodass nur Teile und Kapitel sichtbar sind.


Aufklappen
~~~~~~~~~~

Zeigt einen ganzen Ast, indem das ausgewählte Baumelement aufgeklappt wird.


Einklappen
~~~~~~~~~~

Verbirgt die Kindelemente des ausgewählten Baumelements.


Alles aufklappen
~~~~~~~~~~~~~~~~

Zeigt den ganzen Baum.


Alle einklappen
~~~~~~~~~~~~~~~

Verbirgt alle Baumelemente außer den Hauptkategorien.


Figuren/Schauplätze/Gegenstände-Kontextmenüeinträge
---------------------------------------------------

.. figure:: _images/context_menu02.png
   :alt: novelibre Screenshot

Hinzufügen
~~~~~~~~~~

Figur/Schauplatz/Gegenstand erzeugen.

- Das neue Element wird hinter dem gewählten platziert.
- Das neue Element hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.
- Der Status einer neuen Figur ist *Nebenfigur*.

Manuskript nach Perspektive gefiltert exportieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ein `Manuskript <export_menu.html#manuskript-zum-bearbeiten>`__
mit den Abschnitten exportieren,
welche die ausgewählte Figur als Perspektivfigur haben.

Zusammenfassung nach Perspektive gefiltert exportieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die `Beschreibungen
<section_menu.html#abschnittsbeschreibungen-zum-bearbeiten-exportieren>`__
derjenigen Abschnitte exportieren,
welche die ausgewählte Figur als Perspektivfigur haben.


Löschen
~~~~~~~

Figur/Schauplatz/Gegenstand löschen.

.. caution::
   Denken Sie daran, dass es keine Rückgängig-Funktion gibt.

Status setzen
~~~~~~~~~~~~~

Kennzeichnet die ausgewählte Figur als *Hauptfigur* oder *Nebenfigur*.
Hauptfiguren sind in der Baumansicht farblich hervorgehoben.

.. note::
   Der Figurenstatus dient nur zur visuellen Unterscheidung.
   Er hat keine Auswirkung auf die Programmfunktion.
   Sie können ihn einsetzen, um Perspektivfiguren 
   oder Figuren mit eigener Plotlinie zu kennzeichnen.

.. hint::
   Wählen Sie den Wurzelknoten *Figuren* aus, um den Status 
   für alle Figuren gleichzeitig zu setzen.

Plotlinien-Kontextmenüeinträge
------------------------------

.. figure:: _images/context_menu03.png
   :alt: novelibre Screenshot

Plotlinie hinzufügen
~~~~~~~~~~~~~~~~~~~~

Eine neue Plotlinie erzeugen.

- Wenn eine Plotlinie ausgewählt ist, wird die neue Plotlinie dahinter platziert.
- Andernfalls wird die neue Plotlinie an den Schluss gesetzt.
- Die neue Plotlinie hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.

Plotpunkt hinzufügen
~~~~~~~~~~~~~~~~~~~~

Einen neuen Plotpunkt erzeugen.

- Wenn ein Plotpunkt ausgewählt ist, wird der neue Plotpunkt dahinter platziert.
- Wenn eine Plotlinie ausgewählt ist, wird der neue Plotpunkt an letzter Stelle platziert.
- Der neue Plotpunkt hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.

Manuskript nach Plotlinie gefiltert exportieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ein `Manuskript <export_menu.html#manuskript-zum-bearbeiten>`__
mit den Abschnitten exportieren,
welche zur ausgewählten Plotlinie gehören.

Zusammenfassung nach Plottlinie gefiltert exportieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die `Beschreibungen
<section_menu.html#abschnittsbeschreibungen-zum-bearbeiten-exportieren>`__
derjenigen Abschnitte exportieren,
welche zur ausgewählten Plotlinie gehören.

Löschen
~~~~~~~

Plotlinie/Plotpunkt löschen.

.. caution::
   Denken Sie daran, dass es keine Rückgängig-Funktion gibt.
   Wenn Sie eine Plotlinie löschen, löschen sie gleichzeitig
   ihre Plotpunkte.
   
   
Projektnotizen-Kontextmenüeinträge
----------------------------------

Projektnotiz hinzufügen
~~~~~~~~~~~~~~~~~~~~~~~

Eine Projektnotiz erzeugen.

- Wenn eine Projektnotiz ausgewählt ist, wird die neue Projektnotiz
  dahinter platziert.
- Andernfalls wird die neue Projektnotiz an den Schluss gesetzt.
- Die neue Projektnotiz hat einen automatisch erzeugten Titel.
  Sie können ihn im rechten Bereich der Arbeitsfläche ändern.

Löschen
~~~~~~~

Die ausgewählte Projektnotiz löschen.

