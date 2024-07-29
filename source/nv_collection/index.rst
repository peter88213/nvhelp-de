|external-link| `English <https://peter88213.github.io/nvhelp-en/nv_collection/>`__

.. |external-link| image:: ../_images/external-link.png

-----------------

=============
nv_collection
=============

**Benutzerhandbuch**

Diese Seite gilt für die neueste Ausgabe von `nv_collection
<https://github.com/peter88213/nv_collection/>`__.
Sie können sie mit **Hilfe > Sammlung-Plugin Online-Hilfe** öffnen.

Wenn Sie mehrere *novelibre*-Projekte haben, können Sie sie als Bücher
in einer Sammlung verwalten, auch nach Serien gegliedert.
Eine Sammlung ermöglicht Ihnen den schnellen Zugriff auf Ihre Projekte.

Das Plugin fügt dem *novelibre*-**Datei**-Menü
den Eintrag **Sammlung** hinzu,
und dem **Hilfe**-Menü den Eintrag **Sammlung-Plugin Online-Hilfe**.


Das Plugin installieren
-----------------------

- Starten Sie entweder die heruntergeladene Datei
  **nv_collection_vx.x.x.pyzw** durch Doppelklick (Windows/Linux-Desktop),
- oder führen Sie ```python nv_collection_vx.x.x.pyzw``` (Windows),
  bzw. ```python3 nv_collection_vx.x.x.pyzw``` (Linux) auf der Kommandozeile aus.

*"x.x.x"* ist dabei die Versionsnummer.

.. important::
   Viele Webbrowser erkennen den Download als ausführbare Datei
   und bieten an, sie direkt zu öffnen. 
   Damit wird die Installation gestartet.
   
   Abhängig von Ihren Sicherheitseinstellungen kann es allerdings 
   auch passieren, dass Ihr Browser den Download der ausführbaren 
   Datei zunächst verweigert. 
   In diesem Fall ist Ihre Bestätigung oder eine zusätzliche Handlung 
   erforderlich. 
   Falls das nicht geht, können Sie auf den Download der zip-Datei
   ausweichen. 
 
 
Die Sammlungsverwaltung aufrufen
--------------------------------

Sie können die Sammlungsverwaltung über das *novelibre*-Dateimenü aufrufen:
**Datei > Sammlung**.


Eine Sammlung öffnen
--------------------

Standardmäßig ist die Sammlung der letzten Sitzung voreingestellt.
Sie können das mit **Datei > Öffnen** ändern.


Eine neue Sammlung ereugen
--------------------------

Mit **Datei > Neu** können Sie eine neue Sammlung erzeugen.
Das wird die aktuelle Sammlung schließen und einen
Dateiauswahldialog öffnen, der nach Ort und Dateiname
der neuen Sammlung fragt.
Sobald Sie einen gültigen Dateipfad angegeben haben,
erscheint eine leere Sammlung.


Eine neue Serie erzeugen
------------------------

Mit **Serie > Hinzufügen** können Sie eine neue Serie erzeugen.
Bearbeiten Sie den Titel und die Beschreibung der Serie
im rechten Fenster der Dateiverwaltung.


Bücher zur Sammlung hinzufügen
------------------------------

Um das aktuelle *novelibre*-Projekt als Buch zur Sammlung hinzuzufügen,
rufen Sie **Buch > Aktuelles Projekt zur Sammlung hinzufügen** auf.
Ist eine Serie ausgewählt, wird das Buch als Teil dieser Serie
hinzugefügt.


Die Buchbeschreibung aktualisieren
----------------------------------

Um die Buchbeschreibung aus dem aktuellen *novelibre*-Projekt zu übernehmen,
rufen Sie **Buch > Buchdaten aus aktuellem Projekt aktualisieren** auf.

.. caution::
   Ändern Sie nicht den Buchtitel, denn er dient zur Identifikation.

Um die Beschreibung des ausgewählten Buchs in das *novelibre*-Projekt
zu übernehmen,
rufen Sie **Buch > Projektdaten aus ausgewähltem Buch aktualisieren** auf.


Bücher aus der Sammlung entfernen
---------------------------------

um das ausgewählte Buch aus der Sammlung zu entfernen,
rufen Sie **Buch > Ausgewähltes Buch aus der Sammlung entfernen** auf.


Serien ünd Bücher veschieben
----------------------------

Bei gedrückter ``Alt``-Taste mit der Maus ziehen.

.. caution::
   Denken Sie daran, es gibt keine "Rückgängig"-Funktion.


Bücher entfernen
----------------

Um ein Buch aus der Sammlung zu entfernen,
wählen Sie es aus und drücken entweder die ``Entf``-Taste,
oder rufen Sie **Buch > Ausgewähltes Buch aus der Sammlung entfernen** auf.

.. note::
   Wenn Sie ein Buch aus der Sammlung entfernen, 
   bleibt die dazugehörige Projektdatei auf der Festplatte erhalten.


Eine Serie löschen
------------------

Um eine Serie zu löschen,
wählen Sie sie aus und und drücken entweder die ``Entf``-Taste,
oder rufen Sie **Serie > Ausgewählte Serie entfernen, aber die Bücher behalten** auf.

.. note::
   Wenn Sie eine Serie löschen, bleiben die Bücher standardmäßig erhalten.

Um eine Serie zu löschen und alle enthaltenen Bücher aus der Sammlung zu entfernen,
rufen Sie **Serie > Ausgewählte Serie mitsamt den Büchern entfernen** auf.


Beenden
-------

- Beenden Sie die Sammlungsverwaltung mit **Datei > Beenden**.
- Unter Windows können Sie die Sammlungsverwaltung wahlweise mit ``Alt``-``F4`` beenden.
- Andernfalls  können Sie die Sammlungsverwaltung wahlweise mit ``Strg``-``Q`` beenden.
