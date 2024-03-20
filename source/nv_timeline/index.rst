|external-link| `English <https://peter88213.github.io/nvhelp-en/nv_timeline/>`__

.. |external-link| image:: ../_images/external-link.png

-----------------

===========
nv_timeline
===========

**Benutzerhandbuch**

Diese Seite gilt für die neueste Ausgabe von `nv_timeline
<https://github.com/peter88213/nv_timeline/>`__ release.
You can open it with **Hilfe > Timeline-Plugin Online-Hilfe**.


Das Plugin installieren
-----------------------

- Unzip the downloaded zipfile into a new folder.
- Move into this new folder and launch **setup.pyw**. This installs the plugin.

The plugin adds a **Timeline** entry to the *novelibre* main-Menü,
a **Aus Timeline erzeugen** to the **Datei > Neu** submenu,
and a **Timeline-Plugin Online-Hilfe** entry to the **Hilfe**-Menü.


Befehlsreferenz
---------------

Timeline > Information
~~~~~~~~~~~~~~~~~~~~~~

-  Show information about an existing Timeline project, if any. Timeline
   and novelibre file dates are compared.

Timeline > Die Zeitleiste erzeugen oder aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a timeline exists, aktualisieren it from novelibre, otherwise erzeugena neu
timeline.

Timeline > Das Projekt aktualisieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aktualisieren the novelibre-Projekt from the timeline, if existing.

Timeline > Die Zeitleiste bearbeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Öffnen the project’s timeline, if existing, with the Timeline application.
Sperren the project.

Datei > Neu > Aus Timeline erzeugen...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Öffnen a file dialog to select a timeline. If no novelibre-Projekt with
the timeline’s file name exists, erzeugen a neu one from the timeline.

Benutzerdefinierte Konfiguration
--------------------------------

You can override the default settings by providing a Konfigurationsdatei.
Be always aware that faulty entries may cause program errors or
unreadable Timeline projects. If you change a Konfiguration inbetween,
previously synchronized projects might no longer match.

Globale Konfiguration
~~~~~~~~~~~~~~~~~~~~~

An optional global Konfigurationsdatei can be placed in the Konfiguration
directory in your user profile. It is applied to any project. Its
entries override nv_timeline’s built-in constants. This is the
path: ``c:\Users\<user name>\.novx\config\nv_timeline.ini``

The setup script installs a sample Konfigurationsdatei containing
nv_timeline’s default values. You can modify or delete it.

Lokale Projektkonfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An optional project Konfigurationsdatei named ``nv_timeline.ini`` can be
placed in your project directory, i.e. the Ordner containing your
novelibre and Timeline project files. It is only applied to this
project. Its entries override nv_timeline’s built-in constants as
well as the global Konfiguration, if any.


Wie man eine Konfigurationsdatei erstellt oder anpasst
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The nv_timeline distribution comes with a sample Konfiguration
file located in the ``sample`` Unterverzeichnis. It contains
nv_timeline’s default settings and options. This file is also
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

   # Events with this label become sections in a neuly erzeugend 
   # novelibre-Projekt. 

   section_color = 170,240,160

   # Color for events imported as sections from novelibre.

   neu_event_spacing = 1

   # Tage between events with automatically generated dates.  


Wie man die Konfiguration auf die Standardeinstellungen zurücksetzt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just delete your global and local Konfigurationsdateis.


Konventionen
------------

Allgemein
~~~~~~~~~

-  The novelibre-Projekt file and the Timeline file are located in the
   same directory.
-  They have the same file name and differ in the file extension.
-  Either a timeline or a novelibre-Projekt is generated from the other
   file for the first time. After that, the two files can be
   synchronized against each other.
-  **Please keep in mind:** Synchronizing means overwriting target data
   with source data. Since nv_timeline works in both directions,
   there is always a danger of confusing source and target, thus losing
   changes. So if the program asks you for confirmation to overwrite a
   file, better check if it’s actually the target file.


Auf der Seite von novelibre
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
   novelibre-Projekt.
-  When creating a neu novelibre-Projekt from a timeline the first time,
   "Abschnitt" labels are replaced with section ID labels.
-  If a neu novelibre-Projekt is generated again with the same timeline,
   the section ID labels may change.
-  Only events with a label containing a section ID are synchronized
   with an existing novelibre-Projekt.
-  Changes to the event start date/time affect the section date/time
   during synchronization.
-  Changes to the event text affect the section title during
   synchronization.
-  Changes to the event description affect the section description
   during synchronization.
-  The section structure of an existing novelibre-Projekt can not be
   changed in Timeline. Hinzufügening/removing events, or adding/removing
   section IDs from event labels will *not* add or remove the
   corresponding section during synchronization.
-  When creating events from sections without date/time information, the
   dates are automatically generated with a one-day difference, starting
   from the novelibre-Projekt’s reference date.

Bekannte Einschränkungen
~~~~~~~~~~~~~~~~~~~~~~~~

-  Abschnitt events that begin before 0001-01-01 in the timeline, will not
   be synchronized with novelibre, because novelibre can not handle
   these dates.
-  The same applies to the section duration in this case, i.e. the event
   duration in Timeline and the section duration in novelibre may
   differ.
-  If a section event ends after 9999-12-31 in the timeline, the section
   duration is not synchronized with novelibre.

