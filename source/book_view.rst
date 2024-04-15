Bucheigenschaften
=================

.. |ico01| image:: _images/viewBook.png
   :alt: Buch

The Bucheigenschaften-Ansicht öffnet sich im rechten Fenster, wenn man
im Baum "Buch" wählt, oder wenn man in der Werkzeugleiste auf |ico01|
klickt. Nach dem Öffnen eines *novelibre*-Projekts sieht man diese Ansicht.

.. figure:: _images/book_view01.png
   :alt: novelibre Screenshot


Titel, Beschreibung und Autor
-----------------------------

Titel und Beschreibung erscheinen auf einer "Karteikarte" zum Bearbeiten.

Die Bearbeitung von Buchtitel und Autor kann mit der Eingabetaste beendet werden.
Änderungen an der Beschreibung werden übernommen, sobald mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.

After exporting the book to an *ODT* document, Titel and description
appear in the document properties.

.. figure:: _images/book_view08.png
   :alt: Screenshot

   LibreOffice Writer Screenshot

Diese Eigenschaften sind beispielsweise zu sehen, wenn der Mauszeiger im
Windows Explorer über dem Dokument steht.

.. figure:: _images/book_view09.png
   :alt: Screenshot
   
   Windows 10 Explorer Screenshot
   


Sprache des Dokuments
---------------------

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/book_view02.png
   :alt: novelibre Screenshot

- Sprachencode entsprechend ISO 639-1
- Ländercode entsprechend ISO 3166-2

Diese Information steuert die Rechtschreibprüfung für Exportdokumente.

.. figure:: _images/book_view10.png
   :alt: LibreOffice Writer Screenshot

   LibreOffice Writer Screenshot

Ist die Einstellung nicht gesetzt, wird das Systemgebietsschema
als Standardeinstellung verwendet.

.. hint::
   Sie können die Sprache des Dokuments auch mit *Writer* einstellen 
   oder ändern, dann wird sie beim Import übernommen. 

	.. figure:: _images/book_view11.png
	   :alt: LibreOffice Writer Screenshot
	   
	   LibreOffice Writer Screenshot


Automatische Nummerierung
-------------------------

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/book_view03.png
   :alt: novelibre Screenshot

Kapitel/Teile automatisch nummerieren, wenn der Baum aktualisiert wird.
   Ist dieses Auswahlfeld angekreuzt, werden alle Kapitel/Teile jedes
   Mal automatisch nummeriert, wenn `der Baum aktualisiert wird
   <file_menu.html#baum-aktualisieren>`__.
   Die Titel werden dann durch ein ``Präfix-Nummer-Suffix``-Muster
   (ohne die Bindestriche) ersetzt.

   .. hint::
      Wahlweise kann man einzelne Kapitel/Teile über die 
      `Kapitel/Teil-Eigenschaften 
      <chapter_view.html#dieses-kapitel-nicht-automatisch-nummerieren-part>`__.
      von der automatischen Nummerierung ausschließen,   

Die Eingabe von Präfix und Suffix kann mit der Eingabetaste beendet werden.

.. note::
   Bitte auch ein Leerzeichen zur Trennung von Präfix oder Suffix
   von der Kapitel- oder Teilenummer vorsehen!

Römische Kapitelnummern
   Für die automatische Nummerierung sind arabische Ziffern wie "1", "2", "3" ...
   voreingestellt.
   Wenn dieses Auswahlfeld angekreuzt ist, werden stattdessen römische Ziffern
   wie "I", "II", "III", "IV" ... verwendet.

Kapitelnummern per Teil
   Per Voreinstellung werden die Kapitel über die Teile hinweg fortlaufend nummeriert.
   Wenn dieses Auswahlfeld angekreuzt ist, beginnt die Kapitelzählung in jedem Teil
   erneut mit "1"


Umbenennungen
-------------

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/book_view04.png
   :alt: novelibre Screenshot

*novelibre* provides some ready-made fields for sections and characters
to store information that should be at hand when writing.
If the default categories do not fit into your individual story planning
concept kann man rename these fields.
Editing the categories kann mit der Eingabetaste beendet werden.

Abschnitt fields
   The heading replacements for *Ziel*, *Konflikt*, and *Ausgang* are
   used when you set the `Aktion/Reaktion frame
   <section_view.html#aktion-reaction>`__ to **Benutzerdefiniert**.
   You can do this individually for each section.

Figur fields
   If you want other categories than `Biographie <character_view.html#biographie>`__
   and `Ziele <character_view.html#ziele>`__ for your characters, you
   can enter them here. They will then apply to all characters.

   .. note::
      If you rename the *Biographie* frame, it will keep the Birth/death date
      entries anyway.      


Erzählzeit
----------

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/book_view05.png
   :alt: novelibre Screenshot

To get an overview of the course of the narrative time kann man enter
date/time information `for each section <section_view.html#datum-time>`__.
The date can be specific *(YYYY-MM-DD)* or unspecific (number of days,
e.g. from the beginning of the story).

Bezugsdatum
   The reference date is optional. It can be used to convert relative dates
   into absolute dates, or vice versa. The timeline software plugins may
   use the reference date for creating events from sections that have no
   date or an unspecific one.

   Format: *YYYY-MM-DD*, according to ISO 8601.

   .. hint::
      Even if you don't need specific dates for your story, specifying
      a reference date might be helpful. Thus, a day of the week
      can be displayed along with the `unspecific date 
      <section_view.html#beginn>`__, and ages can be calculated for 
      `related characters <section_view.html#beziehungen>`__.  

Datum in Tage umwandeln
   This transforms specific section dates into days, related to the
   reference date.

Tage in Datum umwandeln
   This transforms unspecific section dates into specific ones, using
   the reference date.

.. note::
   For large novels, the conversion may take some time, depending on 
   your system. During the conversion time, the clicked Schaltfläche will 
   display *"Bitte warten ..."*.  

.. hint::
   The commands above convert all dated sections at once. If you want to 
   do the conversion for single sections, just go to the 
   `Abschnitt properties view <section_view.html#beginn>`__.
   

Schreibfortschritt
------------------

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/book_view06.png
   :alt: novelibre Screenshot

Mit *novelibre* kann man set a word count target and track your
writing progress.

.. note::
   Regardless of the entries made here kann man see the word count 
   in the status bar at any time. 

Schreibfortschritt protokollieren
   By default, *novelibre* stores a log entry with the word counts
   for each day on which you edit the project. You can prevent
   this by unticking the **Schreibfortschritt protokollieren** Auswahlfeld.

   .. hint::
      For viewing the daily progress log, you may want to 
      install the `nv_progress plugin 
      <https://github.com/peter88213/nv_progress/>`__.

Wörter zu schreiben
   Hier kann man enter a number (without decimal points or separators)
   indicating your writing goal in words.
   The entry kann mit der Eingabetaste beendet werden.

Anfangswert
   Hier kann man enter a number (without decimal points or separators)
   indicating the word count you want to start from.
   The entry kann mit der Eingabetaste beendet werden.

Aktuelle Wortzahl als Anfangswert setzen
   Click this Schaltfläche to enter your current word count in the **Beginning
   count** field.

Wörter geschrieben
   Here the difference between your actual word count and the starting
   count is displayed. The percentage refers to the words to write.

Arbeitsphase
   This setting is for the Baumansicht `"Arbeitsphase" coloring mode
   <view_menu.html#farbgebungsmodus>`__.

   - Abschnitte with the same completion status as the selected work
     phase are black.
   - Abschnitte that are ahead of the selected work phase are green.
   - Abschnitte that are behind the selected work phase are magenta.


Buchumschlag-Miniaturbild
-------------------------

A cover thumbnail is displayed with the book properties if you
provide a PNG image file with the project name along with the *.novx*
file. The recommended image width is 100 to 200 pixels.

.. figure:: _images/book_view12.png
   :alt: Windows 10 Explorer Screenshot
   
   Windows 10 Explorer Screenshot
   
.. figure:: _images/book_view07.jpg
   :alt: novelibre Screenshot

   novelibre Screenshot

