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

*novelibre* bietet einige vorgefertigte Felder für Abschnitte und Figuren,
um Informationen zu speichern, die beim Schreiben zur Hand sein sollten.
Wenn die voreingestellten Kategorien nicht in Ihr individuelles
Story-Planungskonzept passen, können Sie diese Felder umbenennen.
Die Bearbeitung der Kategorien kann mit der Eingabetaste beendet werden.

"Keine Szene"-Felder
   Die Überschriftersetzungen für *Handlungsfortschritt*, *Charakterisierung* und *Weltenbau*
   kommen zur Anwendung, wenn Sie im `"Szene"-Fenster
   <section_view.html#szene>`__ eines Abschnitts **Keine Szene** auswählen.
   Diese Kategorien gelten dann für alle Abschnitte,
   die keine Szenen darstellen.

"Andere Szene"-Felder
   Die Überschriftersetzungen für *Eröffnung*, *Emotionaler Höhepunkt* und *Ende*
   kommen zur Anwendung, wenn Sie im `"Szene"-Fenster
   <section_view.html#szene>`__ eines Abschnitts **Andere** auswählen.
   Diese Kategorien gelten dann für alle Abschnitte,
   die andere Szenen als "Aktion" und "Reaktion" darstellen.

"Figur"-Felder
   Falls Sie für Ihre Figuren andere Kategorien als
   `Biographie <character_view.html#biographie>`__
   und `Ziele <character_view.html#ziele>`__ wollen,
   können Sie diese Kategorien hier benennen.
   Sie gelten dann für alle Figuren gleichermaßen.

   .. note::
      If you rename the *Biographie* frame, it will keep the Birth/death date
      entries anyway.      


Erzählzeit
----------

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/book_view05.png
   :alt: novelibre Screenshot

Um den Überblick über die erzählte Zeit zu behalten, kann man
jedem Abschnitt `Datums- und Zeitinformationen <section_view.html#datum-zeit>`__
zuordnen.
Das Datum kann man spezifisch *(JJJJ-MM-TT)* oder unspezifisch (Anzahl der
Tage, z.B. seit Beginn) eingeben.

Bezugsdatum
   Das Bezugsdatum ist optional. Es kann dazu dienen, unspezifische
   Datumsangaben in spezifische umzuwandeln, oder umgekehrt.
   Mit Hilfe des Referenzdatums können Zeitleisten-Plugins
   aus Abschnitten ohne spezifischem Datum Ereignisse erzeugen.

   Format: *JJJJ-MM-TT*, entsprechend ISO 8601.

   .. hint::
      Selbst wenn Sie keine spezifischen Datumsangaben in Ihrer 
      Geschichte benötigen, kann es hilfreich sein, ein Referenzdatum
      anzugeben. 
      Auf diese Weise wird der Wochentag zusammen mit dem 
      `unspezifischen Datum <section_view.html#beginn>`__, angezeigt, 
      und für die `Figuren im Abschnitt <section_view.html#beziehungen>`__ 
      können Sie das Alter abrufen, sofern Sie ein Geburtsdatum angegeben haben.   

Datum in Tage umwandeln
   Damit können Sie spezifische Abschnitts-Datumsangaben in Tage,
   bezogen auf das Referenzdatum, umwandeln.

Tage in Datum umwandeln
   Damit können Sie unspezifische Abschnitts-Datumsangaben
   (auf das Referenzdatum bezogene Tage) in
   spezifische Datumsangaben umwandeln.

.. note::
   Bei umfangreichen Romanen kann die Umwandlung eine Zeitlang dauern, 
   je nach Leistungsfähigkeit Ihres Systems.
   Solange die Konvertierung läuft, zeigt die angeklickte Schaltfläche
   *"Bitte warten ..."* an.  

.. hint::
   Die oben beschriebenen Befehle konvertieren alle datierten 
   Abschnitte auf einmal. 
   Wenn Sie nur einzelne Abschnitte umwandeln wollen, gehen Sie einfach
   zu den `Abschnittseigenschaften <section_view.html#beginn>`__.
   

Schreibfortschritt
------------------

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/book_view06.png
   :alt: novelibre Screenshot

Mit *novelibre* können Sie sich ein Ziel für die Wörterzahl setzen und
Ihren Fortschritt verfolgen.

.. note::
   Unabhängig von den hier gemachten Einstellungen können Sie 
   die Wortzahl jederzeit in der Statuszeile sehen.

Schreibfortschritt protokollieren
   Per Voreinstellung speichert *novelibre* täglich Protokolleinträge
   mit den Wörterzahlen ab.
   Sie können das abschalten, indem Sie den Haken im Auswahlfeld
   **Schreibfortschritt protokollieren** entfernen.

   .. hint::
      Sie können das Protokoll Ihres täglichen Schreibfortschritts
      betrachten, wenn Sie das `nv_progress-Plugin 
      <https://github.com/peter88213/nv_progress/>`__ installieren.

Wörter zu schreiben
   Hier können Sie eine Zahl (Ohne Dezimaltrenner oder Leerzeichen)
   eingeben, die Ihr Schreibziel in Wörtern angibt.
   Die Eingabe kann mit der Eingabetaste beendet werden.

Anfangswert
   Hier können Sie eine Zahl (Ohne Dezimaltrenner oder Leerzeichen)
   eingeben, welche die Anfangs-Wörterzahl für Ihr Schreibziel angibt.
   Die Eingabe kann mit der Eingabetaste beendet werden.

Aktuelle Wortzahl als Anfangswert setzen
   Klicken Sie auf diese Schaltfläche, um die aktuelle Wörterzahl in das
   **Anfangswert**-Feld einzutragen.

Wörter geschrieben
   Hier wird die Differenz zwischen Ihrer derzeitigen Wörterzahl
   und dem Anfangswert angezeigt.
   Der Prozentwert bezieht sich auf Ihr Schreibziel.

Arbeitsphase
   Diese Einstellung wird für den `Farbgebungsmodus "Arbeitsphase"
   <view_menu.html#farbgebungsmodus>`__ benötigt.

   - Abschnitte mit dem selben Fertigstellungsstatus wie die eingestellte
     Arbeitsphase sind schwarz.
   - Abschnitte, die der eingestellten Arbeitsphase vorauseilen, sind grün.
   - Abschnitte, die der eingestellten Arbeitsphase hinterherhinken, sind magenta.


Links
-----

Dieses Fenster mit Klick auf den Titel öffnen oder schließen.

.. figure:: _images/book_view13.png
   :alt: Screenshot
   
This is a list for image and research document links.

Although *novelibre* holds some character/location/item data, it is
not the right application for extensive world building. For this,
you may want to use more powerful software, like `Zim Desktop Wiki
<https://zim-wiki.org/>`__. In this case, *novelibre* allows you to
create links to the text files that will take you quickly to the right
places in the wiki.

Or you have collected some images that could inspire you when writing.
Then simply create links to these images to open them with your
system's standard image viewer.

.. tip::
   If you have collected several images for a character in a folder 
   that your standard image viewer can browse through, a single link 
   to any image file is sufficient.  
   
The links are displayed in a list in the order they are entered.

Link hinzufügen
   When clicking on |Hinzufügen|, a file selection dialog opens. The selected
   file will be added to the link list.

   .. hint::
      By default, the dialog shows image files. For other file types, 
      change the selector in the lower right corner. 
      
      .. figure:: _images/filePicker01.png
         :alt: Screenshot
         
         Windows 10 Explorer Screenshot


Link entfernen
   When clicking on |Entfernen| or pressing the ``Entf``-Taste,
   the selected link is removed from the list.

Link öffnen
   When double-clicking on a link, or clicking on |Goto|,
   the link is opened with the standard application for the link's file type.

   .. hint::
      If you want to open certain linked files with another application than the 
      standard application kann man provide a *novelibre* "launcher" setting. 
      For this, just create a text file named **launchers.ini** in the 
      ``.novx/config``  directory (where all configuration files are stored). 
      Here you can assign applications to the file extensions. 
      
      Zim desktop wiki pages are a special case. 
      For this, the Zim program is assigned to the `.zim` extension. 
      
      This example shows a setting that makes *novelibre* open text files
      with the *Zim Desktop Wiki* application instead of the standard text 
      editor: 
      
      ::
     
         [SETTINGS]
         .zim = C:/Program Dateis (x86)/Zim Desktop Wiki/zim.exe 
         
      .. figure:: _images/launchers.png
         :alt: Screenshot
         
         Windows 10 Explorer Screenshot

.. |Hinzufügen| image:: _images/add.png
.. |Goto| image:: _images/goto.png
.. |Entfernen| image:: _images/remove.png



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

