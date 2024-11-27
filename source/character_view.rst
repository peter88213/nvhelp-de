Figureneigenschaften
====================

Die Ansicht der Figureneigenschaften öffnet sich im rechten Fenster,
wenn Sie eine Figur auswählen.

.. figure:: _images/character_view01.png
   :alt: Screenshot

Titel und Beschreibung
----------------------

Titel und Beschreibung werden als beschreibbare "Karteikarte" dargestellt.

Die Bearbeitung des Titels können Sie mit der Eingabetaste beenden.
Änderungen an der Beschreibung werden übernommen, sobald mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.

Vollst. Name
------------

Der Titel der Figur, wie er auf der Karteikarte steht,
dient an verschiedenen Stellen im Programm als Kurzname.
Den vollständigen Namen können Sie hier gesondert eingeben.
Die Bearbeitung können Sie mit der Eingabetaste beenden.

alias
-----

Dieses Eingabefeld ist für alternative Namen.
Die Bearbeitung können Sie mit der Eingabetaste beenden.

Tags
----

Tags sind ein frei benutzbares Werkzeug,
um Figuren in der Baumansicht zu kennzeichnen.
Tags müssen nicht anderswo definiert werden, sie werden einfach,
durch Semikolons getrennt, ins Eingabefeld eingetragen.
Die Bearbeitung können Sie mit der Eingabetaste beenden.

.. caution::
   Achten Sie auf eine einheitliche Schreibweise, 
   falls Sie Tags mehrmals verwenden wollen.

Hauptfigur
----------

Mit dem **Hauptfigur**-Auswahlfeld können Sie den Status der Figur ändern.

.. note::
   Der Figurenstatus dient nur zur visuellen Unterscheidung.
   Er hat keine Auswirkung auf die Programmfunktion.
   Sie können ihn einsetzen, um Perspektivfiguren 
   oder Figuren mit eigener Plotlinie zu kennzeichnen.


Biographie
----------

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/character_view02.png
   :alt: Screenshot

Geburtsdatum/Sterbedatum
   Format: *JJJJ-MM-TT*, entsprechend ISO 8601.

Die Bearbeitung von Geburts- und Sterbedatum können Sie mit der
Eingabetaste beenden.
Änderungen an der Biographie werden übernommen, wenn mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.

.. hint::
   Dieses Eingabefeld kann beliebige Figurendaten speichern, 
   die Ihnen wichtig erscheinen.   
   Falls "Biographie" nicht die passende Kategorie für Sie ist, 
   können Sie den Bezeichner in den 
   `Bucheigenschaften <book_view.html#umbenennungen>`__ ändern.
   Die Eingabefelder für Geburts- und Sterbedatum bleiben dabei 
   erhalten.      
    


Ziele
-----

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/character_view03.png
   :alt: Screenshot

Änderungen an den Zielen werden übernommen, wenn mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.

.. hint::
   Dieses Eingabefeld kann beliebige Figurendaten speichern, 
   die Ihnen wichtig erscheinen.   
   Falls "Ziele" nicht die passende Kategorie für Sie ist, 
   können Sie den Bezeichner in den 
   `Bucheigenschaften <book_view.html#umbenennungen>`__ ändern. 

Links
-----

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/book_view13.png
   :alt: Screenshot

Das ist eine Liste für Links zu Bildern und Recherche-Dokumenten.

Obwohl *novelibre* Daten zu Figuren, Schauplätzen und Gegenständen
verwalten kann, ist es nicht die richtige Anwendung für
umfangreichen Weltenbau.
Dafür sollte man leistungsfähigere Softwareprogramme verwenden,
zum Beispiel `Zim Desktop Wiki
<https://zim-wiki.org/>`__.
Dazu kann *novelibre* Hyperlinks zu den Textdateien erzeugen,
welche Sie schnell zu den richtigen Stellen im Wiki führen.

Oder Sie haben einige Bilder gesammelt, die Sie beim Schreiben inspirieren.
Dann erzeugen Sie einfach Links zu diesen Bildern und lassen Sie
*novelibre* diese mit Ihrem System-Bildbetrachter öffnen.

.. tip::
   Wenn Sie mehrere Bilder z.B. zu einer Figur in einem Ordner
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
         
         Windows Explorer Screenshot


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
         
         Windows Explorer Screenshot

.. |Hinzufügen| image:: _images/add.png
.. |Goto| image:: _images/goto.png
.. |Entfernen| image:: _images/remove.png




"Haftmerker"
------------

Der gelbe Texteingabebereich ist für Notizen.
Änderungen werden übernommen, wenn mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.

Wenn der "Haftmerker" einer Figur Text enthält,
erscheint in the Baumansicht ein "N" als Hinweis.

.. note::
   Die "Haftmerker" sind nur für die Arbeit mit *novelibre* gedacht.
   Sie werden nicht beim Dokumentenexport berücksichtigt.
   Allerdings erscheinen sie in der `Figurenliste`_.

.. _Figurenliste: characters_menu.html#exportieren-character-list-spreadsheet

Navigationsschaltflächen
------------------------

- **Zurück** bewegt die Auswahl auf die vorhergehende Figur im Baum.
- **Vor** bewegt die Auswahl auf die nachfolgende Figur im Baum.
