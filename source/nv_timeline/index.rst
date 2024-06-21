|external-link| `English <https://peter88213.github.io/nvhelp-en/nv_timeline/>`__

.. |external-link| image:: ../_images/external-link.png

-----------------

===========
nv_timeline
===========

**Benutzerhandbuch**

.. hint::
   Die deutsche Übersetzung des *novelibre*-Benutzerhandbuchs ist noch in Arbeit.
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

- Informationen über ein bestehendes *Timeline*-Projekt anzeigen, falls vorhanden.
  Das Dateidatum des *Timeline*- und des *novelibre*-Projekts vergleichen.

Timeline > Die Zeitleiste erzeugen oder aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Falls eine Zeitleiste existiert, aktualisiere sie aus *novelibre*,
andernfalls erzeuge eine neue Zeitleiste.

Timeline > Das Projekt aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aktualisiere das *novelibre*-Projekt aus der Zeitleiste, falls vorhanden.


.. important::
   Vergessen Sie nicht, die Zeitleiste vor dem Synchronisieren mit *novelibre* 
   abzuspeichern.
   Da *nv_timeline* die *.timeline*-Datei liest, bleiben ungesicherte Änderungen 
   unberücksichtigt.
   Im Zweifelsfall beenden Sie *Timeline*, bevor Sie mit *novelibre* synchronisieren.


Timeline > Die Zeitleiste bearbeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Zeitleiste zum Projekt mit *Timeline* öffnen, falls vorhanden.
Je nach Konfiguration (siehe unten) wird das Projekt automatisch gesperrt.

Datei > Neu > Aus Timeline erzeugen...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit öffnen Sie einen Dateiauswahldialog, um eine *.timeline*-Datei auszuwählen.
Falls noch kein *novelibre*-Projekt mit dem gleichen Dateinamen existiert,
wird das aktuelle Projekt geschlossen und ein neues aus der Zeitleiste erzeugt.


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

Sie können eine optionale globale Konfigurationsdatei im
Konfigurationsverzeichnis der Installation ablegen.
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
d.h. in den Ordner, der Ihre *novelibre*- und *Timeline*-Projektdateien
enthält.
Sie gilt dann nur für das Projekt.
Ihre Einträge überschreiben sowohl die Voreinstellungen von
*nv_timeline* als auch die globale Konfiguration, falls vorhanden.


Wie man eine Konfigurationsdatei erstellt oder anpasst
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die *nv_timeline* distribution comes with a sample Konfiguration
file located in the ``sample`` Unterverzeichnis. It contains
*nv_timeline*’s default settings and options. This file is also
automatically copied to the global Konfiguration Ordner during
installation. You best make a copy and edit it.

-  The SETTINGS section comprises the program "constants". If you change
   them, the program might behave differently than described in the
   documentation. So only touch them if you are clear about the
   consequences.
-  Comment lines begin with a ``#`` number sign. In the example, they
   refer to the code line immediately above.

This is the Konfiguration explained:

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

Just delete your global and local Konfigurationsdateis.


Konventionen
------------

Allgemein
~~~~~~~~~

-  The *novelibre*-Projekt file and the Timeline file are located in the
   same directory.
-  They have the same file name and differ in the file extension.
-  Either a timeline or a *novelibre*-Projekt is generated from the other
   file for the first time. After that, the two files can be
   synchronized against each other.
-  **Please keep in mind:** Synchronizing means overwriting target data
   with source data. Since *nv_timeline* works in both directions,
   there is always a danger of confusing source and target, thus losing
   changes. So if the program asks you for confirmation to overwrite a
   file, better check if it’s actually the target file.


Auf der Seite von *novelibre*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Only normal sections are synchronized with Timeline, or exported to
   Timeline. Unbenutzt sections will not show up in the timeline.
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

-  A section ID is a string looking like "sc1". It is auto-generated and
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

-  Abschnitt events that begin before 0001-01-01 in the timeline, will not
   be synchronized with *novelibre*, because *novelibre* can not handle
   these dates.
-  The same applies to the section duration in this case, i.e. the event
   duration in Timeline and the section duration in *novelibre* may
   differ.
-  If a section event ends after 9999-12-31 in the timeline, the section
   duration is not synchronized with *novelibre*.

