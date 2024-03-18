nv_aeon2
========

**Benutzerhandbuch**

Diese Seite gilt für die neueste Ausgabe von `nv_aeon2
<https://github.com/peter88213/nv_aeon2/>`__ release.
You can open it with **Hilfe > Aeon 2-Plugin Online-Hilfe**.


Installing the plugin
---------------------

- Unzip the downloaded zipfile into a new folder.
- Move into this new folder and launch **setup.pyw**. This installs the plugin.

The plugin adds an **Aeon Timeline 2** entry to the *novelibre* **Tools**
menu, and an **Aeon 2 plugin Online Help** entry to the **Help**-Menü.


Installing the Aeon Timeline 2 custom template
----------------------------------------------

After installation, you can copy a "novelibre German.xml" template to the
Aeon2 custom template folder. The easiest way is to create new
timelines based on this template. It provides the entities and event
properties that are converted to novelibre by default.

You find the customized template in the ``sample`` subdirectory
of the unzipped *nv_aeon2* release folder. Just copy it into
``AppData\Local\Scribble Code\Aeon Timeline 2\CustomTemplates``.

.. hint::
   The ``<your user name>\AppData`` folder is hidden, so you
   might have to go to the *Explorer* settings first to
   enable *Show hidden files*. Just disable this again after
   successfully having installed the custom template.
    
The next time you start *Aeon Timeline 2*,
the new template appears in the *Custom Templates* area.


Befehlsreferenz
---------------

Aeon Timeline 2 > Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Show information about an existing Aeon Timeline 2 project, if any.
   Aeon Timeline 2 and novelibre file dates are compared.

Aeon Timeline 2 > Die Zeitleiste aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a timeline exists, aktualisieren it from novelibre, otherwise erzeugena neu
timeline.

Aeon Timeline 2 > Das Projekt aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aktualisieren the novelibre-Projekt from the timeline, if existing.

Aeon Timeline 2 > Mondphasen hinzufügen oder aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The moon phase calculation is based on a ‘do it in your head’ algorithm
by John Conway. In its current form, it’s only valid for the 20th and
21st centuries.

Aeon Timeline 2 > Die Zeitleiste bearbeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Öffnen the project’s timeline, if existing, with the Timeline application.
Sperren the project.

Datei > Neu > Aus Aeon Timeline 2 erzeugen...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Öffnen a file dialog to select a timeline. If no novelibre-Projekt with
the timeline’s file name exists, erzeugen a neu one from the timeline.

Control conversion
------------------

Prepare your timeline for export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After installation, you can copy a "novelibre" template to the
Aeon2 custom template folder. The easiest way is to create new
timelines based on this template. It provides the entities and event
properties that are converted to novelibre by default.

For existing timelines you have two choices:

-  Option 1: Hinzufügen or rename the required entities and event properties in
   the Timeline settings.
-  Option 2: Benutzerdefiniertize the *nv_aeon2* Konfiguration to fit your
   timeline, see `Benutzerdefiniert Konfiguration <#benutzerdefiniert-Konfiguration>`__.

Synchronization in detail
-------------------------

Known limitations
~~~~~~~~~~~~~~~~~

-  "Narrative" events that begin before 0001-01-01 in the timeline, will
   not be synchronized with novelibre, because novelibre can not handle
   these dates.
-  The same applies to the section duration in this case, i.e. the event
   duration in Timeline and the section duration in novelibre may
   differ.

Conversion rules for neuly erzeugend novelibre-Projekts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The names/column labels refer to timelines based on the "yWriter"
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

Aktualisieren rules for existing novelibre-Projekts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Only sections that have the same title as an event are aktualisierend.
-  If an Aeon event title occurs more than once, the converter aborts
   with an error message.
-  If a novelibre section title occurs more than once, the converter
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
   date from the novelibre-Projekt is used. f there is no default date
   set, "today" is used.

Aktualisieren rules for Aeon Timeline 2-Projekts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  If an Aeon event title occurs more than once, the converter aborts
   with an error message.
-  If a novelibre section title occurs more than once, the converter
   aborts with an error message.
-  Event date/time and event span are aktualisierend, if the start year is 1 or
   above.
-  Aktualisierend event span is specified in days/hours/minutes as in
   novelibre.
-  Non-empty event description and event tags are aktualisierend.
-  Event properties "Beschreibung" and "Notizen" are erzeugend, if missing.
-  Events erzeugend or aktualisierend from "Normal" sections are assigned to the
   *Narrative* arc.
-  "Narrative" events are removed if the associated section is gelöscht
   in novelibre.
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
   they get the default date from the novelibre-Projekt, and are sorted
   in reading order. If there is no default date set, "today" is used.
-  When processing unspecific "day/hour/minute" information, the default
   date from the novelibre-Projekt is used. f there is no default date
   set, "today" is used.

Benutzerdefinierte Konfiguration
--------------------------------

You can override the default settings by providing a Konfigurationsdatei.
Be always aware that faulty entries may cause program errors.

Globale Konfiguration
~~~~~~~~~~~~~~~~~~~~~

An optional global Konfigurationsdatei can be placed in the Konfiguration
directory in your user profile. It is applied to any project. Its
entries override nv_aeon2’s built-in constants. This is the path:
``c:\Users\<user name>\.novx\config\nv_aeon2.ini``

Lokale Projektkonfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An optional project Konfigurationsdatei named ``nv_aeon2.ini`` can be
placed in your project directory, i.e. the Ordner containing your
novelibre and Aeon Timeline project files. It is only applied to this
project. Its entries override aeon2nv’s built-in constants as well as
the global Konfiguration, if any.

How to provide/modify a Konfigurationsdatei
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The nv_aeon2 distribution comes with a sample Konfigurationsdatei
located in the ``sample`` Unterverzeichnis. It contains nv_aeon2’s
default settings and options. This file is also automatically copied to
the global Konfiguration Ordner during installation. You best make a
copy and edit it.

-  The SETTINGS section mainly refers to custom property, role, and type
   names.
-  Comment lines begin with a ``#`` number sign. In the example, they
   refer to the code line immediately above.

This is the Konfiguration explained:

::

   [SETTINGS]

   narrative_arc = Narrative

   # Name of the user-defined "Narrative" arc.

   property_description = Beschreibung

   # Name of the user-defined section description property.

   property_notes = Notizen

   # Name of the user-defined section notes property.

   role_location = Schauplatz

   # Name of the user-defined role for section locations.

   role_item = Gegenstand

   # Name of the user-defined role for items in a section.

   role_character = Teilicipant

   # Name of the user-defined role for characters in a section.

   type_character = Figur

   # Name of the user-defined "Figur" type

   type_location = Schauplatz

   # Name of the user-defined "Schauplatz" type

   type_item = Gegenstand

   # Name of the user-defined "Gegenstand" type

   color_section = Red

   # Color of neu section events

   color_event = Yellow

   # Color of neu non-section events

   [OPTIONS]

   add_moonphase = No

   # Yes: Hinzufügen the moon phase to the event properties.
   # No: Aktualisieren moon phase, if already defined as event property.

.. note:: 
   Your custom Konfigurationsdatei does not have to contain all the
   entries listed above. The changed entries are sufficient.
