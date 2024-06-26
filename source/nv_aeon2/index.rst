|external-link| `English <https://peter88213.github.io/nvhelp-en/nv_aeon2/>`__

.. |external-link| image:: ../_images/external-link.png

-----------------

========
nv_aeon2
========

**Benutzerhandbuch**

.. hint::
   Die deutsche Übersetzung des *nv_aeon2*-Benutzerhandbuchs ist noch in Arbeit.
   Im Zweifelsfall könnnen Sie von dieser Seite aus zur englischen Version 
   des Benutzerhandbuchs wechseln (Link oben).

Diese Seite gilt für die neueste Ausgabe von `nv_aeon2
<https://github.com/peter88213/nv_aeon2/>`__.
Sie können sie mit **Hilfe > Aeon 2-Plugin Online-Hilfe** öffnen.


Das Plugin installieren
-----------------------

- Entpacken Sie die heruntergeladene Zip-Datei in einen neuen Ordner.
- Gehen Sie in diesen Ordner und führen Sie **setup.pyw** aus. Damit installieren Sie das Plugin.

Das Plugin fügt dem *novelibre*-Hauptmenü
den Eintrag **Aeon Timeline 2** hinzu,
außerdem dem **Datei > Neu**-Untermenü den Eintrag **Aus Aeon Timeline 2 erzeugen...**,
und dem **Hilfe**-Menü den Eintrag **Aeon 2-Plugin Online-Hilfe**.


Die Aeon Timeline 2 Benutzervorlage installieren
------------------------------------------------

Nach der Installation können Sie eine Vorlagendatei namens
"novelibre German.xml" in den Aeon 2-Ordner für Benutzervorlagen kopieren.
Es ist dann einfach, neue Zeitleisten aus dieser Vorlage zu erzeugen.
Sie stellt die Entities und Properties bereit, die standardmäßig
mit *novelibre* synchronisiert werden.

Sie finden die Benutzervorlage im Unterverzeichnis
``sample`` des entpackten *nv_aeon2* Release-Verzeichnisses.
Kopieren Sie sie einfach in das folgende Verzeichnis:
``AppData\Local\Scribble Code\Aeon Timeline 2\CustomTemplates``.

.. hint::
   Der Ordner ``<Benutzername>\AppData`` ist verborgen,
   deshalb müssen Sie eventuell zuerst zu den 
   *Explorer*-Einstellungen gehen und *Verborgene Dateien anzeigen*
   erlauben. 
   Nachdem Sie die Benutzervorlage erfolgreich installiert haben, 
   können Sie das wieder zurückstellen. 
    
Wenn Sie *Aeon Timeline 2* das nächste Mal aufrufen, erscheint
die Benutzervorlage im Bereich *Custom Templates* zur Auswahl.


Befehlsreferenz
---------------

Aeon Timeline 2 > Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit bekommen Sie Informationen über ein bestehendes *Aeon Timeline 2*-Projekt angezeigt,
falls vorhanden.
Das Dateidatum des *Aeon Timeline 2*- wird mit dem des *novelibre*-Projekts verglichen.


Aeon Timeline 2 > Den Zeitstrahl aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit wird ein existierender Zeitstrahl aus dem *novelibre*-Projekt aktualisiert.


Aeon Timeline 2 > Das Projekt aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit wird das *novelibre*-Projekt aus einem existierenden Zeitstrahl aktualisiert.


Aeon Timeline 2 > Mondphasen hinzufügen oder aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Berechnung der Mondphase beruht auf einem überschlägigen Verfahren
von John Conway.
In ihrer derzeitigen Ausführung ist sie nur für das 20. und 21. Jahrhundert
gültig.


Aeon Timeline 2 > Den Zeitstrahl bearbeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Den Zeitstrahl zum Projekt mit *Aeon Timeline 2* öffnen, falls vorhanden.
Je nach Konfiguration (siehe unten) wird das Projekt automatisch gesperrt.


Datei > Neu > Aus Aeon Timeline 2 erzeugen...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit öffnen Sie einen Dateiauswahldialog, um eine *.aeonzip*-Datei auszuwählen.
Falls noch kein *novelibre*-Projekt mit dem gleichen Dateinamen existiert,
wird das aktuelle Projekt geschlossen und ein neues aus dem Zeitstrahl erzeugt.


Die Konvertierung steuern
-------------------------

Den Zeitstrahl für den Export vorbereiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nach der Installation können Sie eine "novelibre"-Vorlage
in das *Aeon Timeline 2*-Benutzervorlagenverzeichnis kopieren.
Es ist am einfachsten, neue Zeitstrahlen mit Hilfe dieser Vorlage zu erzeugen.
Sie stellt diejenigen *Entities* und *Event Properties* bereit,
die standardmäßig mit *novelibre* synchronisiert werden.

für existierende Zeitstrahlen haben Sie zwei Möglichkeiten zur Auswahl:

-  Option 1: Fügen Sie in *Aeon Timeline 2*
   die erforderlichen *Entities* und *Event Properties* hinzu
   oder benennen Sie sie um.
-  Option 2: Passen Sie die Konfiguration von *nv_aeon2* an,
   damit sie zum Zeitstrahl passt, siehe
   `Benutzerdefinierte Konfiguration <#benutzerdefinierte-konfiguration>`__.


Die Synchronisierung im Einzelnen
---------------------------------

Bekannte Einschränkungen
~~~~~~~~~~~~~~~~~~~~~~~~

-  Ereignisse, die auf dem Zeitstrahl vor dem Datum 0001-01-01
   liegen, können nicht mit *novelibre* synchronisiert werden,
   weil *novelibre* damit nicht umgehen kann.
-  The same applies to the section duration in this case, i.e. the event
   duration in Timeline and the section duration in *novelibre* may
   differ.


Konvertierungsregeln für neu erzeugte novelibre-Projekte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The names/column labels refer to timelines based on the "novelibre"
template.

-  If an Aeon event title occurs more than once, the program aborts with
   an error message.
-  Events assigned to the "Narrative" arc are converted to regular
   sections.
-  Neue Abschnitte are put into a neu chapter named "Neue Abschnitte".
-  Alle sections are sorted chronologically.
-  The section status is "Gliederung".
-  The event title is used as section title (\*).
-  The start date is used as section date/time, if the start year is 1
   or above.
-  The section duration is calculated, if the start year is 1 or above.
-  Event tags are converted to section tags, if any (\*).
-  "Beschreibungs" are imported as section descriptions, if any (\*).
-  "Notizen" are used as section notes, if any (\*).
-  "Teilicipants" are imported as characters, if any (\*).
-  "Schauplätze" are imported, if any (\*).
-  "Gegenstände" are imported, if any (\*).


Aktualisierungsregeln für bestehende novelibre-Projekte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Only sections that have the same title as an event are aktualisierend.
-  If an Aeon event title occurs more than once, the converter aborts
   with an error message.
-  If a *novelibre* section title occurs more than once, the converter
   aborts with an error message.
-  Abschnitte are marked "unused" if the associated event is gelöscht in
   Aeon.
-  Abschnitt date, section time, and section duration are aktualisierend.
-  Non-empty section description and section tags are aktualisierend.
-  Notizen of events with a matching title are appended to the section
   notes.
-  The start date is overwritten, if the start year is 1 or above.
-  The section duration is overwritten, if the start year is 1 or above.
-  Neu "Normal" type sections are erzeugend from "Narrative" events, if
   missing.
-  Neue Abschnitte are put into a neu chapter named "Neue Abschnitte".
-  Neu plot lines, characters, locations, and items are added, if assigned to
   "Narrative" events.
-  Arc, character, location, and item relationships are aktualisierend, if the
   entity names match.
-  When processing unspecific "day/hour/minute" information, the default
   date from the *novelibre*-Projekt is used. f there is no default date
   set, "today" is used.


Aktualisierungsregeln für Aeon Timeline 2-Projekte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  If an Aeon event title occurs more than once, the converter aborts
   with an error message.
-  If a *novelibre* section title occurs more than once, the converter
   aborts with an error message.
-  Event date/time and event span are aktualisierend, if the start year is 1 or
   above.
-  Aktualisierend event span is specified in days/hours/minutes as in
   *novelibre*.
-  Non-empty event description and event tags are aktualisierend.
-  Event properties "Beschreibung" and "Notizen" are erzeugend, if missing.
-  Events erzeugend or aktualisierend from "Normal" sections are assigned to the
   *Narrative* arc.
-  "Narrative" events are removed if the associated section is gelöscht
   in *novelibre*.
-  Entity types "Arc", "Figur", "Schauplatz", and "Gegenstand" are erzeugend,
   if missing.
-  A "Narrative" arc is erzeugend, if missing.
-  A "Storyline" arc role is erzeugend, if missing.
-  Neu arcs, characters, locations, and items are added, if assigned to
   sections.
-  Arc, character, location, and item relationships are aktualisierend, if the
   entity names match.
-  When creating events from sections without date/time, they get the
   actual date and are sorted in reading order.
-  When creating events from sections without any date/time information,
   they get the default date from the *novelibre*-Projekt, and are sorted
   in reading order. If there is no default date set, "today" is used.
-  When processing unspecific "day/hour/minute" information, the default
   date from the *novelibre*-Projekt is used. f there is no default date
   set, "today" is used.


Benutzerdefinierte Konfiguration
--------------------------------

Sie können die Voreinstellungen mit Hilfe einer Konfigurationsdatei überschreiben.
Denken Sie aber immer daran, dass fehlerhafte Einträge den Programmablauf stören können.


Globale Konfiguration
~~~~~~~~~~~~~~~~~~~~~

Sie können eine optionale globale Konfigurationsdatei
namens ``nv_aeon2.ini``
im Konfigurationsverzeichnis der Installation ablegen.
Sie wird auf jedes Projekt angewendet.
Ihre Einträge überschreiben die Voreinstellungen von *nv_aeon2*.
Dies ist der Pfad unter Windows:
``c:\Users\<Benutzername>\.novx\config\nv_aeon2.ini``

Das Setup-Skript installiert eine Musterkonfigurationsdatei
mit den voreingestellten Werten von *nv_aeon2*
Sie können sie ändern oder löschen.


Lokale Projektkonfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sie können eine optionale Projekt-Konfigurationsdatei namens
``nv_aeon2.ini`` in Ihrem Projektverzeichnis ablegen,
d.h. in dem Ordner, der Ihre *novelibre*- und
*Aeon Timeline 2*-Projektdateien enthält.
Sie gilt dann nur für das Projekt.
Ihre Einträge überschreiben sowohl die Voreinstellungen von
*nv_aeon2* als auch die globale Konfiguration, falls vorhanden.


Wie man eine Konfigurationsdatei erstellt oder anpasst
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die *nv_aeon2*-Distribution wird mit einer Beispielkonfigurationsdatei
geliefert, die sich im Unterordner ``sample`` befindet.
Sie enthält die Standardeinstellungen und Optionen von *nv_aeon2*.
Diese Datei wird auch während der Installation automatisch in den
globalen Konfigurationsordner kopiert.
Am besten erstellen Sie eine Kopie und bearbeiten sie.

-  The SETTINGS section mainly refers to custom property, role, and type
   names.
-  Kommentarzeilen beginnen mit einem Rautenzeichen ``#``.
   Im Beispiel beziehen sie sich auf die unmittelbar darüberliegende
   Codezeile.

Das ist die Konfiguration mit Erklärungen:

::

   [SETTINGS]
   
   narrative_arc = Romanhandlung
   
   # Name of the user-defined "Narrative" arc.
   
   property_description = Beschreibung
   
   # Name of the user-defined scene description property.
   
   property_notes = Notizen
   
   # Name of the user-defined scene notes property.
   
   property_moonphase = Mondphase
   
   # Name of the user-defined moon phase property.
   
   role_location = Schauplatz
   
   # Name of the user-defined role for scene locations.
   
   role_item = Item
   
   # Name of the user-defined role for items in a scene.
   
   role_character = Anwesend
   
   # Name of the user-defined role for characters in a scene.
   
   type_character = Figur
   
   # Name of the user-defined "Character" type
   
   type_location = Ort
   
   # Name of the user-defined "Location" type
   
   type_item = Gegenstand
   
   # Name of the user-defined "Item" type
   
   color_scene = Red
   
   # Color of new scene events
   
   color_event = Yellow
   
   # Color of new non-scene events
   
   [OPTIONS]
   
   add_moonphase = Yes
   
   # Yes: Add the moon phase to the event properties.
   # No: Update moon phase, if already defined as event property.
   
   lock_on_export = No
   
   # Yes: Lock the novelibre project when opening the timeline.
   # No: Do not lock the novelibre project when opening the timeline.
   

.. note:: 
   Your custom Konfigurationsdatei does not have to contain all the
   entries listed above. The changed entries are sufficient.
