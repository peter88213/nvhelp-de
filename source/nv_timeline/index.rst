|external-link| `English <https://peter88213.github.io/nvhelp-en/nv_timeline/>`__

.. |external-link| image:: ../_images/external-link.png

-----------------

===========
nv_timeline
===========

**Benutzerhandbuch**

.. hint::
   Die deutsche Übersetzung des *nv_timeline*-Benutzerhandbuchs ist noch in Arbeit.
   Im Zweifelsfall könnnen Sie von dieser Seite aus zur englischen Version 
   des Benutzerhandbuchs wechseln (Link s.o.).

Diese Seite gilt für die neueste Ausgabe von `nv_timeline
<https://github.com/peter88213/nv_timeline/>`__.
Sie können sie mit **Hilfe > Timeline-Plugin Online-Hilfe** öffnen.


Das Plugin installieren
-----------------------

- Entpacken Sie die heruntergeladene Zip-Datei in einen neuen Ordner.
- Gehen Sie in diesen Ordner und führen Sie **setup.pyw** aus. Damit installieren Sie das Plugin.

Das Plugin fügt dem *novelibre*-Hauptmenü
den Eintrag **Timeline** hinzu,
außerdem dem **Datei > Neu**-Untermenü den Eintrag **Aus Timeline erzeugen...**,
und dem **Hilfe**-Menü den Eintrag **Timeline-Plugin Online-Hilfe**.


Befehlsreferenz
---------------

Timeline > Information
~~~~~~~~~~~~~~~~~~~~~~

Damit bekommen Sie Informationen über ein bestehendes *Timeline*-Projekt angezeigt,
falls vorhanden.
Das Dateidatum des *Timeline*- wird mit dem des *novelibre*-Projekts verglichen.


Timeline > Den Zeitstrahl erzeugen oder aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit wird ein existierender Zeitstrahl aus dem *novelibre*-Projekt aktualisiert.
Ein fehlender Zeitstrahl wird neu erzeugt.


Timeline > Das Projekt aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit wird das *novelibre*-Projekt aus einem existierenden Zeitstrahl aktualisiert.


.. important::
   Vergessen Sie nicht, den Zeitstrahl vor dem Synchronisieren mit *novelibre* 
   abzuspeichern.
   Da *nv_timeline* die *.timeline*-Datei liest, bleiben ungesicherte Änderungen 
   unberücksichtigt.
   Im Zweifelsfall beenden Sie *Timeline*, bevor Sie mit *novelibre* synchronisieren.


Timeline > Den Zeitstrahl bearbeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Den Zeitstrahl zum Projekt mit *Timeline* öffnen, falls vorhanden.
Je nach Konfiguration (siehe unten) wird das Projekt automatisch gesperrt.

Datei > Neu > Aus Timeline erzeugen...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit öffnen Sie einen Dateiauswahldialog, um eine *.timeline*-Datei auszuwählen.
Falls noch kein *novelibre*-Projekt mit dem gleichen Dateinamen existiert,
wird das aktuelle Projekt geschlossen und ein neues aus dem Zeitstrahl erzeugt.


Benutzerdefinierte Konfiguration
--------------------------------

Sie können die Voreinstellungen mit einer Konfigurationsdatei überschreiben.
Denken Sie aber immer daran, dass fehlerhafte Einträge zu
Programmstörungen oder unlesbaren *Timeline*-Projekten führen können.
Be always aware that faulty entries may cause program errors or
Falls Sie zwischendurch eine Konfiguration ändern,
können zuvor synchronisierte Projekte eventuell  nicht mehr zusammenpassen.

Globale Konfiguration
~~~~~~~~~~~~~~~~~~~~~

Sie können eine optionale globale Konfigurationsdatei
namens ``nv_timeline.ini``
im Konfigurationsverzeichnis der Installation ablegen.
Sie wird auf jedes Projekt angewendet.
Ihre Einträge überschreiben die Voreinstellungen von *nv_timeline*.
Dies ist der Pfad unter Windows:
``c:\Users\<user name>\.novx\config\nv_timeline.ini``

Das Setup-Skript installiert eine Musterkonfigurationsdatei
mit den voreingestellten Werten von *nv_timeline*
Sie können sie ändern oder löschen.

Lokale Projektkonfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sie können eine optionale Projekt-Konfigurationsdatei namens
``nv_timeline.ini`` in Ihrem Projektverzeichnis ablegen,
d.h. in dem Ordner, der Ihre *novelibre*- und *Timeline*-Projektdateien
enthält.
Sie gilt dann nur für das Projekt.
Ihre Einträge überschreiben sowohl die Voreinstellungen von
*nv_timeline* als auch die globale Konfiguration, falls vorhanden.


Wie man eine Konfigurationsdatei erstellt oder anpasst
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die *nv_timeline*-Distribution wird mit einer Beispielkonfigurationsdatei
geliefert, die sich im Unterordner ``sample`` befindet.
Sie enthält die Standardeinstellungen und Optionen von *nv_timeline*.
Diese Datei wird auch während der Installation automatisch in den
globalen Konfigurationsordner kopiert.
Am besten erstellen Sie eine Kopie und bearbeiten sie.

-  Der Abschnitt SETTINGS enthält die Programm-"Konstanten".
   Wenn Sie sie ändern, kann es sein, dass sich das Programm
   anders als in der Dokumentation beschrieben verhält.
   Deshalb sollten Sie sie nur anfassen, wenn Sie sich über
   die Konsequenzen im Klaren sind.
-  Kommentarzeilen beginnen mit einem Rautenzeichen ``#``.
   Im Beispiel beziehen sie sich auf die unmittelbar darüberliegende
   Codezeile.

Das ist die Konfiguration mit Erklärungen:

::

   [SETTINGS]

   section_label = Abschnitt

   # Ereignisse mit diesem Label werden in ein neu erzeugtes
   # novelibre-Projekt als Abschnitte übernommen. 

   section_color = 170,240,160

   # Die Farbe für Ereignisse, die novelibre-Abschnitten entsprechen.

   new_event_spacing = 1

   # Anzahl der Tage, die zwischen Ereignissen
   # mit automatisch erzeugten Datum liegen.  


   [OPTIONS]
   
   lock_on_export = No
   
   # Yes:Das novelibre-Projekt beim Start von Timeline automatisch sperren.
   # No: Das Projekt beim Start von Timeline nicht automatisch sperren.

Wie man die Konfiguration auf die Standardeinstellungen zurücksetzt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Löschen Sie einfach Ihre globalen und lokalen Konfigurationsdateien.


Konventionen
------------

Allgemein
~~~~~~~~~

- Die *novelibre*-Projektdatei und die *Timeline*-Datei befinden
  sich im selben Verzeichnis.
- Sie haben den selben Dateinamen, aber unterschiedliche Erweiterungen.
- Beim ersten Mal wird entweder ein *Timeline*- oder ein *novelibre*-Projekt
  aus dem jeweils anderen erzeugt. Danach können die beiden miteinander
  synchronisiert werden.

.. caution:: 
   Synchronisieren heißt Zieldaten mit Quelldaten 
   überschreiben. 
   Da *nv_timeline* in beide Richtungen arbeitet,
   besteht immer die Gefahr, Quelle und Ziel zu verwechseln und so 
   Änderungen zu verlieren. 
   Wenn Sie also nach einer Bestätigung gefragt werden, 
   eine Datei zu überschreiben, 
   prüfen Sie besser noch einmal nach, ob es sich dabei tatsächlich
   um  das gewünschte Ziel handelt. 


Auf der Seite von *novelibre*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Nur normale Abschnitte werden mit *Timeline* synchronisiert oder zu
  *Timeline* exportiert.
  Unbenutzte Abschnitte erscheinen nicht auf dem Zeitstrahl.
-  Abschnitte with an unspecific time stamp (day, hours, minutes) are
   synchronized with the timeline, if a reference date is set.
-  Changes to the section date/time affect the event start date/time
   during synchronization.
-  Changes to the section title affect the event text during
   synchronization.
-  Changes to the section description affect the event description
   during synchronization.
-  Changes to the section type may add or remove the corresponding event
   during synchronization.
-  Hinzufügening or removing sections will add or remove the corresponding
   event during synchronization.


Auf der Seite von Timeline
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  A section ID is a string looking like "sc1". It is auto-generated und
   must not be changed manually.
-  Only events with a label containing the string "Abschnitt" (user input)
   or a section ID (auto-generated) are exported as sections to a neu
   *novelibre*-Projekt.
-  When creating a neu *novelibre*-Projekt from a timeline the first time,
   "Abschnitt" labels are replaced with section ID labels.
-  If a neu *novelibre*-Projekt is generated again with the same timeline,
   the section ID labels may change.
-  Only events with a label containing a section ID are synchronized
   with an existing *novelibre*-Projekt.
-  Changes to the event start date/time affect the section date/time
   during synchronization.
-  Changes to the event text affect the section title during
   synchronization.
-  Changes to the event description affect the section description
   during synchronization.
-  The section structure of an existing *novelibre*-Projekt can not be
   changed in Timeline. Hinzufügening/removing events, or adding/removing
   section IDs from event labels will *not* add or remove the
   corresponding section during synchronization.
-  When creating events from sections without date/time information, the
   dates are automatically generated with a one-day difference, starting
   from the *novelibre*-Projekt’s reference date.

Bekannte Einschränkungen
~~~~~~~~~~~~~~~~~~~~~~~~

-  Ereignisse, die auf dem Zeitstrahl vor dem Datum 0001-01-01
   liegen, können nicht mit *novelibre* synchronisiert werden,
   weil *novelibre* damit nicht umgehen kann.
-  The same applies to the section duration in this case, i.e. the event
   duration in Timeline und the section duration in *novelibre* may
   differ.
-  If a section event ends after 9999-12-31 in the timeline, the section
   duration is not synchronized with *novelibre*.

