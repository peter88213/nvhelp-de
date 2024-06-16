Bucheigenschaften
=================

.. |ico01| image:: _images/viewBook.png
   :alt: Buch

The Bucheigenschaften-Ansicht öffnet sich im rechten Fenster, wenn Sie
im Baum "Buch" wählen, oder wenn Sie in der Werkzeugleiste auf |ico01|
klicken. Nach dem Öffnen eines *novelibre*-Projekts sehen Sie diese Ansicht.

.. figure:: _images/book_view01.png
   :alt: novelibre Screenshot


Titel, Beschreibung und Autor
-----------------------------

Titel und Beschreibung erscheinen auf einer "Karteikarte" zum Bearbeiten.

Die Bearbeitung von Buchtitel und Autorkönnen Sie mit der Eingabetaste beenden.
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

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

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

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/book_view03.png
   :alt: novelibre Screenshot

Kapitel/Teile automatisch nummerieren, wenn der Baum aktualisiert wird.
   Ist dieses Auswahlfeld angekreuzt, werden alle Kapitel/Teile jedes
   Mal automatisch nummeriert, wenn `der Baum aktualisiert wird
   <file_menu.html#baum-aktualisieren>`__.
   Die Titel werden dann durch ein ``Präfix-Nummer-Suffix``-Muster
   (ohne die Bindestriche) ersetzt.

   .. hint::
      Wahlweise können Sie einzelne Kapitel/Teile über die 
      `Kapitel/Teil-Eigenschaften 
      <chapter_view.html#dieses-kapitel-nicht-automatisch-nummerieren-part>`__.
      von der automatischen Nummerierung ausschließen,   

Die Eingabe von Präfix und Suffixkönnen Sie mit der Eingabetaste beenden.

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

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/book_view04.png
   :alt: novelibre Screenshot

*novelibre* bietet einige vorgefertigte Felder für Abschnitte und Figuren,
um Informationen zu speichern, die beim Schreiben zur Hand sein sollten.
Wenn die voreingestellten Kategorien nicht in Ihr individuelles
Story-Planungskonzept passen, können Sie diese Felder umbenennen.
Die Bearbeitung der Kategorienkönnen Sie mit der Eingabetaste beenden.

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

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/book_view05.png
   :alt: novelibre Screenshot

Um den Überblick über die erzählte Zeit zu behalten, können Sie
jedem Abschnitt `Datums- und Zeitinformationen <section_view.html#datum-zeit>`__
zuordnen.
Das Datum können Sie spezifisch *(JJJJ-MM-TT)* oder unspezifisch (Anzahl der
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

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/book_view06.png
   :alt: novelibre Screenshot

Mit *novelibre* können Sie sich ein Ziel für die Wortanzahl setzen und
Ihren Fortschritt verfolgen.

.. note::
   Unabhängig von den hier gemachten Einstellungen können Sie 
   die Wortanzahl jederzeit in der Statuszeile sehen.

Schreibfortschritt protokollieren
   Per Voreinstellung speichert *novelibre* täglich Protokolleinträge
   mit den Wortanzahlen ab.
   Sie können das abschalten, indem Sie den Haken im Auswahlfeld
   **Schreibfortschritt protokollieren** entfernen.

   .. hint::
      Sie können das Protokoll Ihres täglichen Schreibfortschritts
      betrachten, wenn Sie das `nv_progress-Plugin 
      <https://github.com/peter88213/nv_progress/>`__ installieren.

Wörter zu schreiben
   Hier können Sie eine Zahl (ohne Dezimaltrenner oder Leerzeichen)
   eingeben, die Ihr Schreibziel in Wörtern angibt.
   Die Eingabekönnen Sie mit der Eingabetaste beenden.

Anfangswert
   Hier können Sie eine Zahl (ohne Dezimaltrenner oder Leerzeichen)
   eingeben, welche die Anfangs-Wortanzahl für Ihr Schreibziel angibt.
   Die Eingabekönnen Sie mit der Eingabetaste beenden.

Aktuelle Wortzahl als Anfangswert setzen
   Klicken Sie auf diese Schaltfläche, um die aktuelle Wortanzahl in das
   **Anfangswert**-Feld einzutragen.

Wörter geschrieben
   Hier wird die Differenz zwischen Ihrer derzeitigen Wortanzahl
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

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/book_view13.png
   :alt: Screenshot

Das ist eine Liste für Links zu Bildern und Recherche-Dokumenten.

Obwohl *novelibre* Daten zu Figuren, Schauplätzen und Gegenständen
verwalten kann, ist es nicht die richtige Anwendung für
umfangreichen Weltenbau.
Dafür sollten Sie leistungsfähigere Softwareprogramme verwenden,
zum Beispiel `Zim Desktop Wiki
<https://zim-wiki.org/>`__.
Dazu kann *novelibre* Hyperlinks zu den Textdateien erzeugen,
welche Sie schnell zu den richtigen Stellen im Wiki führen.

Oder Sie haben einige Bilder gesammelt, die Sie beim Schreiben inspirieren.
Dann erzeugen Sie einfach Links zu diesen Bildern und lassen Sie
*novelibre* diese mit Ihrem System-Bildbetrachter öffnen.

.. tip::
   Wenn sie mehrere Bilder z.B. zu einer Figur in einem Ordner
   gesammelt haben, den Ihr Standard-Bildbetrachter durchsuchen kann,
   ist ein einziger Link auf eines dieser Bilder ausreichend.
   
Die Links werden in einer Liste angezeigt, und zwar in der Reihenfolge
der Eingabe.

Link hinzufügen
   Wenn Sie auf |Hinzufügen| klicken, öffnet sich ein Dateiauswahldialog.
   Die ausgewählte Datei wird der Linkliste hinzugefügt.

   .. hint::
      Der Dialog zeigt zunächst nur Bilddateien.
      Für andere Dateitypen ändern Sie die Auswahl in der unteren 
      rechten Ecke. 
      
      .. figure:: _images/filePicker01.png
         :alt: Screenshot
         
         Windows 10 Explorer Screenshot


Link entfernen
   Wenn Sie auf |Entfernen| klicken oder die ``Entf``-Taste drücken,
   wird der ausgewählte Link von der Liste entfernt.


Link öffnen
   Wenn Sie auf einen Link doppelklicken, oder auf |Goto| klicken,
   Wird die Datei, auf die der Link verweist, mit der Standardanwendung
   für ihren Typ geöffnet.

   .. hint::
      Falls Sie bestimmte verlinkte Dateien mit einer anderen Anwendung
      als der System-Standardanwendung öffnen wollen, 
      können Sie eine "Programmstarter"-Einstellung vornehmen. 
      Dafür erzeugen Sie einfach eine Textdatei namens **launchers.ini**
      im Verzeichnis ``.novx/config`` (wo alle Konfigurationsdateien liegen).
      Hier in können Sie Erweiterungen Anwendungsprogramme zuordnen.  

      Zim Desktop-Wiki-Seiten sind ein Sonderfall.
      Dafür ordnen Sie die `.zim`-Erweiterung dem Zim-Programm zu.

      Dieses Beispiel zeigt eine Einstellung, die *novelibre* Textdateien
      mit der *Zim Desktop Wiki*-anwendung öffnen lässt, 
      statt mit dem Standard-Texteditor:    
      
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

Eine Buchumschlag-Vorschau wird zusammen mit den Bucheigenschaften
angezeigt, wenn Sie im Projektverzeichnis eine PNG-Bilddatei
mit dem selben Namen wie das Projekt bereitstellen.
Die empfohlene Bildbreite ist 100 bis 200 Pixel.

.. figure:: _images/book_view12.png
   :alt: Windows 10 Explorer Screenshot
   
   Windows 10 Explorer Screenshot
   
.. figure:: _images/book_view07.jpg
   :alt: novelibre Screenshot

   novelibre Screenshot

