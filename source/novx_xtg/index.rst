|external-link| `English <https://peter88213.github.io/nvhelp-en/novx_xtg/>`__

.. |external-link| image:: ../_images/external-link.png

-----------------

========
novx_xtg
========

**Benutzerhandbuch**

.. hint::
   Die deutsche Übersetzung des *novx_xtg*-Benutzerhandbuchs ist noch in Arbeit.
   Im Zweifelsfall könnnen Sie von dieser Seite aus zur englischen Version 
   des Benutzerhandbuchs wechseln (Link oben).

Diese Seite gilt für die neueste Ausgabe von `novx_xtg
<https://github.com/peter88213/novx_xtg/>`__.

Das Python-Skript *novx_xtg.py* durchläuft alle Kapitel und Abschnitte
eines *novelibre*-Projekts und füllt XTG-Vorlagen aus.

Das Programm installieren
-------------------------

- Starten Sie entweder die heruntergeladene Datei
  **novx_xtg_vx.x.x.pyzw** durch Doppelklick (Windows/Linux-Desktop),
- oder führen Sie ```python novx_xtg_vx.x.x.pyzw``` (Windows),
  bzw. ```python3 novx_xtg_vx.x.x.pyzw``` (Linux) auf der Kommandozeile aus.

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
 
 
Gebrauchsanweisung
------------------

Vorgesehene Benutzung
~~~~~~~~~~~~~~~~~~~~~

Das Installationsprogramm fordert Sie auf, eine Verknüpfung
auf dem Desktop anzulegen.
Die können das Programm dann aufrufen, indem Sie mit der Maus eine
*.novx*-Datei auf das Symbol ziehen.


Auf der Kommandozeile
~~~~~~~~~~~~~~~~~~~~~

Wahlweise können Sie auch

- das Programm von der Kommandozeile aus aufrufen und das *novelibre*-Projekt
  als Parameter übergeben, oder
- das Programm aus einer Batchdatei heraus aufrufen.

Aufruf: ``novx_xtg.pyw [--silent] Quelldatei``


Positionsbezogene Parameter:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Quelldatei``

Der Dateipfad der *novelibre*-Projektdatei.


Optionale Parameter:
^^^^^^^^^^^^^^^^^^^^

``--silent``  Fehlermeldungen und Nachfragen unterdrücken.

---


Allgemein
---------

Über XTG
~~~~~~~~

The XTG file format uses the *XPress Tags* language, the knowledge of which is assumed. You can
download the manual *A Guide to XPress Tags* for your program version from the *Quark* web site.


novelibre Textauszeichnungen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bold and italics are supported. Other highlighting such as
underline and strikethrough are lost.


Anführungszeichen und Interpunktion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is assumed that quotation marks and punctuation marks are already set correctly; this is best done in advance with a word processor, e.g. via novelibre's "proof read" function.


Konfiguration
-------------

- Place a subfolder named **novx_xtg** in the novelibre project folder. It contains the configuration file
  and all template files as listed below to be applied to this project. The best way is to copy the provided sample folder and customize the contained files with a text editor according to your needs.

- If there is no configuration data in the project file, data stored in `c:\Users\<user name>\.novx\novx_xtg\config` is used prior  to the script's default configuration data.

- If a template file or a configuration entry is missing, *novx_xtg* uses the lower priority source as a fallback.


.. hint::
   Sie finden einen Musterkonfigurationsordner mit Vorlagen und
   den voreingestellten Werten von *novx_xtg* im
   *novelibre*-Installationsverzeichnis unter
   
   ``c:\Users\<Benutzername>\.novx\novx_xtg\sample\``
   
   Am besten erstellen Sie eine Kopie und bearbeiten sie.


Konfigurationsdatei
~~~~~~~~~~~~~~~~~~~

Das ist die Konfigurationsdatei mit Erklärungen:

::

   [STYLES]
   first_paragraph = @Text body:
   
   # XPress tag for paragraphs preceded by a heading or a blank line.
   
   indented_paragraph = @Text body indent:
   
   # XPress tag for indented paragraphs.
   
   other_paragraph = @First line indent:
   
   # XPress tag for regular paragraphs.
   
   italic = <@Emphasis>
   
   # XPress tag opening italic sections. 
   
   italic0 = <@$p>
   
   # XPress tag closing italic sections.
   
   bold = <@Strong emphasis>
   
   # XPress tag opening bold sections.
   
   bold0 = <@$p>
   
   # XPress tag closing bold sections.
   
   acronym =
   
   # XPress tag opening acronyms.
    
   acronym0 = 
   
   # XPress tag closing acronyms.
   
   figure =
   
   # XPress tag opening figure groups.
   
   figure0 = 
   
   # XPress tag closing figure groups.
   
   [OPTIONS]
   
   adjust_digits = Yes
   
   # If Yes, adjust digit-separating blanks.
   
   space_points = Yes
   
   # If Yes, space digit-separating points.
   
   per_chapter = No
   
   # If Yes, create one XTG file for each chapter.
   # If No, create one XTG file for the entire document.



Formatmarkierungen
^^^^^^^^^^^^^^^^^^

- **textbody** - The QX paragraph style applied to all paragraphs in a section, except the first. The first paragraph's style can be set in the section level templates.
- **italic** - The opening tag to replace novelibre's *italic* formatting.
- **italic0** - The closing tag to replace novelibre's *italic* formatting.
- **bold** - The opening tag to replace novelibre's *bold* formatting.
- **bold0** - The closing tag to replace novelibre's *bold* formatting.
- **acronym** - The opening tag to format sequences of uppercase characters (e.g. set a slightly smaller font size).
- **acronym0** - The closing tag to format sequences of uppercase characters.
- **figure** - The opening tag to format figures (e.g. switch the font to get "osf" text figures).
- **figure0** - The closing tag to format figures.

Optionen
^^^^^^^^

- **adjust_digits** - Replace regular spaces between digits with thin spaces.
- **space_points** - Insert a thin space after each point that separates digits.
- **per_chapter** - Generate one XTG file per chapter. The file names consist of the chapter's number and title. the files are written to the XTG_Chapters subdirectory.

You can define styles in ``fileHeader.XTG``, but it is preferable to use the names of styles that already exist in the QX book project instead.


Vorlagenliste
-------------

Project level templates
~~~~~~~~~~~~~~~~~~~~~~~

- **fileHeader.XTG** - This template must contain at least the version code and encoding indication.

Chapter level templates
~~~~~~~~~~~~~~~~~~~~~~~

- **partTemplate.XTG** - Chapter header; applied to chapters marked "section beginning".
- **chapterTemplate.XTG** - Chapter header; applied to all "used" and "normal" chapters unless a "part template" exists.


Section level templates
~~~~~~~~~~~~~~~~~~~~~~~

- **firstSectionTemplate.XTG** - Applied  to sections at the beginning of the chapter.
- **sectionTemplate.XTG** - Applied to "used" sections within "normal" chapters.
- **sectionDivider.XTG** - Section divider placed between sections.
- **appendedSectionTemplate.XTG** - Applied to sections to be appended to the previous section.


Platzhalter
-----------

Syntax
~~~~~~

There are two options:

1. $Placeholder
2. ${Placeholder}


"Project template" placeholders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **$Title** - Project title
- **$Desc** - Project description
- **$AuthorName** - Author's name
- **$Language** - Language code acc. to ISO 639-1
- **$Country** - Country code acc. to ISO 3166-2
- **$CustomPlotProgress** - Custom "Plot progress" field title
- **$CustomCharacterization** - Custom "Characterization" field title
- **$CustomWorldBuilding** - Custom "World building" field title
- **$CustomGoal** - Custom "Goal" field title
- **$CustomConflict** - Custom "Conflict" field title
- **$CustomOutcome** - Custom "Outcome" field title
- **$CustomChrBio** - Custom character "Bio" field title
- **$CustomChrGoals** - Custom character "Goals" field title

"Chapter template" placeholders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **$ID** - Chapter ID,
- **$ChapterNumber** - Chapter number (in sort order),
- **$Title** - Chapter title
- **$Desc** - Chapter description
- **$Notes** - Chapter notes
- **$ProjectName** - URL-coded file name without suffix and extension
- **$ProjectPath** - URL-coded fpath to the project directory
- **$Language** - Language code acc. to ISO 639-1
- **$Country** - Country code acc. to ISO 3166-2
- **$ManuscriptSuffix** - File name suffix of the manuscript

"Section template" placeholders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **$ID** - Section ID,
- **$SectionNumber** - Section number (in sort order),
- **$Title** - Section title
- **$Desc** - Section description
- **$WordCount** - Section word count
- **$WordsTotal** - Accumulated word count including the current section
- **$Status** - Section status (Outline, Draft etc.)
- **$SectionContent** - Section content
- **$Date** - Specific section date (yyyy-mm-dd)
- **$Time** - Time section begins: (hh:mm)
- **$OdsTime** - Time section begins: (PThhHmmMssS)
- **$Day** - Day section begins
- **$ScDate** - Date or day (localized)
- **$DateYear** - Year
- **$DateMonth** - Month (number)
- **$DateDay** - Day (number)
- **$DateWeekday** - Day of the week (name)
- **$MonthName** - Month (name)
- **$LastsDays** - Amount of time section lasts: days
- **$LastsHours** - Amount of time section lasts: hours
- **$LastsMinutes** - Amount of time section lasts: minutes
- **Duration** - Combination of days and hours and minutes
- **$Scene** - The sections's kind of scene, if any
- **$Goal** - The section protagonist's goal
- **$Conflict** - The section conflict
- **$Outcome** - The section outcome
- **$Tags** - Comma-separated list of section tags
- **$Characters** - Comma-separated list of characters assigned to the section
- **$Viewpoint** - Viewpoint character
- **$Locations** - Comma-separated list of locations assigned to the section
- **$Items** - Comma-separated list of items assigned to the section
- **$Notes** - Section notes
- **$ProjectName** - URL-coded file name without suffix and extension
- **$ProjectPath** - URL-coded fpath to the project directory
- **$Language** - Language code acc. to ISO 639-1
- **$Country** - Country code acc. to ISO 3166-2
- **$ManuscriptSuffix** - File name suffix of the manuscript
- **$SectionsSuffix** - File name suffix of the section descriptions
- **$CustomPlotProgress** - Custom "Plot progress" field title
- **$CustomCharacterization** - Custom "Characterization" field title
- **$CustomWorldBuilding** - Custom "World building" field title
- **$CustomGoal** - Custom "Goal" field title
- **$CustomConflict** - Custom "Conflict" field title
- **$CustomOutcome** - Custom "Outcome" field title


Installationspfad
-----------------

Das Setup-Skript kopiert *scap_novx.py* an einen definierten Ort.
Unter Windows ist das der folgende Ordner:

``c:\Users\<Benutzername>\.novx\novx_xtg``

