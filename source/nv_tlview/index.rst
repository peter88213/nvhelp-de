|external-link| `English <https://peter88213.github.io/nvhelp-en/nv_tlview/>`_

.. |external-link| image:: ../_images/external-link.png

-----------------

=========
nv_tlview
=========

**Benutzerhandbuch**

.. hint::
   Die deutsche Übersetzung des *nv_tlview*-Benutzerhandbuchs ist noch in Arbeit.
   Im Zweifelsfall könnnen Sie von dieser Seite aus zur englischen Version 
   des Benutzerhandbuchs wechseln (Link oben).

Diese Seite gilt für die neueste Ausgabe von `nv_tlview
<https://github.com/peter88213/nv_tlview/>`__.
Sie können sie mit **Hilfe > Zeitleistenansicht Online-Hilfe** öffnen.

*nv_tlview* ist ein Plugin, das Abschnitte mit Datums- und Zeitangaben
in einer Zeitleiste anzeigt.

Das Plugin fügt dem *novelibre*-**Extras**-Menü
den Eintrag **Zeitleistenansicht** hinzu,
und dem **Hilfe**-Menü den Eintrag **Zeitleistenansicht Online-Hilfe**.
Die Werkzeugleiste erhält eine |Zeitline| Schaltfläche.

.. |Zeitline| image:: _images/tlview.png

.. figure:: _images/screen01.png
   :alt: novelibre Screenshot


Das Plugin installieren
-----------------------

- Starten Sie entweder die heruntergeladene Datei
  **nv_tlview_vx.x.x.pyzw** durch Doppelklick (Windows/Linux-Desktop),
- oder führen Sie ```python nv_tlview_vx.x.x.pyzw``` (Windows),
  bzw. ```python3 nv_tlview_vx.x.x.pyzw``` (Linux) auf der Kommandozeile aus.

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
 
 
Bedienung
---------


Die Zeitleistenansicht öffnen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Öffnen Sie die Zeitleistenansicht entweder über das Hauptmenü: **Extras > Zeitleistenansicht**,
- oder über die |Zeitline|-Schaltfläche in der Werkzeugleiste.


Scrollen mit dem Mausrad
~~~~~~~~~~~~~~~~~~~~~~~~

- Scrollen Sie die Zeitleiste horizontal mit dem Mausrad bei gedrückter Umschalttaste.
- Scrollen Sie die Zeitleiste vertikal mit dem Mausrad.
- Den Zeitmaßstab vergrößern oder verkleinern Sie mit dem Mausrad bei gedrückter ``Strg``-Taste.
- Die Abstandsgrenzen für das Stapeln verändern Sie mit dem Mausrad bei gleichzeitig
  gedrückter ``Strg``- und Umschalttaste.


Selecting a section in the *novelibre* project tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Wählen Sie einen Abschnitt, indem sie auf einen Eintrag in der Zeitleiste doppelklicken.
  Das bringt das Anwendungsfenster von *novelibre* in den Vordergrund.


Command reference
-----------------


"Gehe zu"-Menü
~~~~~~~~~~~~~~

Erstes Ereignis
   Damit verschieben Sie die Zeitleiste so, dass
   das früheste Ereignis in der Nähe des linken Rands erscheint.

Letztes Ereignis
   Damit verschieben Sie die Zeitleiste so, dass
   das späteste Ereignis in der Nähe des rechten Rands erscheint.

Ausgewählter Abschnitt
   Damit verschieben Sie die Zeitleiste so, dass
   der im *novelibre*-Projektbaum ausgewählte Abschnitt
   in der Mitte des Fensters erscheint.


"Maßstab"-Menü
~~~~~~~~~~~~~~

Stunden
   Damit stellen Sie den Maßstab auf eine Stunde pro Skalenstrich ein.

Tage
   Damit stellen Sie den Maßstab auf einen Tag pro Skalenstrich ein.

Jahre
   Damit stellen Sie den Maßstab auf ein Jahr pro Skalenstrich ein.

Ans Fenster anpassen
   Damit stellen Sie den Maßstab und die Position so ein,
   dass alle Abschnitte mit gültiger Datum/Zeitinformation ins Fenster passen.


"Ersetzungen"-Menü
~~~~~~~~~~~~~~~~~~

Benutze 00:00 für fehlende Zeiten
   - Wenn dieses Feld angekreuzt ist,
     wird "00:00" für Abschnitte ohne Zeitangaben verwendet.
     Dies hat keinen Einfluss auf die Eigenschaften des Abschnitts.
   - Wenn dieses Feld nicht angekreuzt ist,
     werden Abschnitte ohne Zeitangabe nicht angezeigt.


Tage in Datum umwandeln
   - Wenn dieses Feld angekreuzt ist,
     erhalten Abschnitte mit unspezifischem Datum ein spezifisches für die Anzeige
     sofern ein Bezugsdatum angegeben ist.
     Dies hat keinen Einfluss auf die Eigenschaften des Abschnitts.
   - Wenn dieses Feld nicht angekreuzt ist,
     werden Abschnitte ohne spezifisches Datum nicht anzezeigt.


Benutze Bezugsdatum für fehlende Datumsangaben
   - Wenn dieses Feld angekreuzt ist,
     erhalten Abschnitte ohne Datum oder Tag das Bezugsdatum (sofern vorhanden)
     für die Anzeige.
     Dies hat keinen Einfluss auf die Eigenschaften des Abschnitts.
   - Wenn dieses Feld nicht angekreuzt ist,
     werden Abschnitte ohne Datum oder Tag nicht anzezeigt.


"Kaskadieren"-Menü
~~~~~~~~~~~~~~~~~~

The section marks are stacked on the timeline canvas, so that they would not
overlap or cover the title of previous sections.
If the stacking algorithm does not seem good enough to you,
you can adjust its limits.

Dicht
   Arrange consecutive events behind each other, even if they are close together.

Aufgelockert
   Arrange consecutive events in a stack, even if they are some distance apart.

Normal
   Reset the cascading to default.

.. hint::
   You can fine-tune the stacking limits with ``Shift``-``Strg``-``Mousewheel``.



"Hilfe"-Menü
~~~~~~~~~~~~

Online-Hilfe
   Diese Hilfeseite im Webbrowser öffnen.
   Dasselbe wie ``F1``.


Schaltflächen in der Werkzeugleiste am unteren Rand
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|rewindLeft| Eine Bildschirmseite zurück
   Shift the timeline to go about one screen width back in time.

|arrowLeft| Zurückscrollen
   Shift the timeline to go 1/5 screen width back in time.
   You can move it more precisely with the mouse wheel.

|goToFirst| Gehe zum ersten Ereignis
   Shift the timeline so that the earliest event
   is positioned near the left edge of the window.

|goToSelected| Gehe zum ausgewählten Abschnitt
   Shift the timeline so that the section selected in the *novelibre* project tree
   is positioned in the center of the window.

|goToLast| Gehe zum letzten Ereignis
   Shift the timeline so that the latest event
   is positioned near the right edge of the window.

|arrowRight| Vorscrollen
   Shift the timeline to go 1/5 screen width forward in time.
   You can move it more precisely with the mouse wheel.

|rewindRight| Eine Bildschirmseite nach vorne
   Shift the timeline to go about one screen width forward in time.

|arrowDown| Den Zeitmaßstab verkleinern
   Reduce the time scale in major steps.
   Fine scaling is meant to be done with the mouse wheel.

|fitToWindow| Ans Fenster anpassen
   This sets the scale and moves the timeline, so that all sections with
   valid or substituted date/time information fit into the window.

|arrowUp| Den Zeitmaßstab vergrößern
   Increase the time scale in major steps.
   Fine scaling is meant to be done with the mouse wheel.

Schließen
   Das Zeitleistenfenster schließen.
   Dasselbe wie ``Strg``-``Q`` (Linux)
   oder ``Alt``-``F4`` (Windows).


.. |rewindLeft| image:: _images/rewindLeft.png
.. |arrowLeft| image:: _images/arrowLeft.png
.. |goToFirst| image:: _images/goToFirst.png
.. |goToLast| image:: _images/goToLast.png
.. |arrowRight| image:: _images/arrowRight.png
.. |rewindRight| image:: _images/rewindRight.png
.. |goToSelected| image:: _images/goToSelected.png
.. |arrowDown| image:: _images/arrowDown.png
.. |fitToWindow| image:: _images/fitToWindow.png
.. |arrowUp| image:: _images/arrowUp.png

