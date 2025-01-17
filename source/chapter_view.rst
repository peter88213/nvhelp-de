Kapitel/Teil-Eigenschaften
==========================

Die Ansicht der Kapitel/Teil-Eigenschaften öffnet sich im rechten Fenster,
wenn Sie ein Kapitel oder einen Teil auswählen.

.. hint::
   Mit Hilfe des **Ebene ändern**-Eintrags im Kontextmenü, dem 
   **Teil**-Menü oder dem **Kapitel**-Menü 
   können Sie jedes Kapitel in einen Teil umwandeln, oder umgekehrt.

.. image:: _images/chapter_view01.png
   :alt: Screenshot

Titel und Beschreibung
----------------------

Titel und Beschreibung werden als beschreibbare "Karteikarte" dargestellt.

Die Bearbeitung des Titels können Sie mit der Eingabetaste beenden.
Änderungen an der Beschreibung werden übernommen, sobald mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.

.. note::
   
   Entsprechend Ihrer Vorgabe in den 
   `Bucheigenschaften <book_view.html#automatische-nummerierung>`_
   wird *novelibre* den Titel spätestens bei der nächsten Aktualisierung 
   des Projektbaums ändern. 
   Deshalb brauchen Sie den Kapitel- oder Teiletitel nicht einzugeben, 
   falls die automatische Nummerierung auf der entsprechenden Ebene 
   aktiviert und das aktuelle Kapitel bzw. der aktuelle Teil 
   nicht von der Nummerierung ausgenommen ist (siehe unten). 


Unbenutzt
---------

Mit dem **Unbenutzt**-Auswahlfeld können Sie den
`Kapiteltyp <basic_concepts.html#teil-kapitel-abschnittstypen>`__
ändern.


Dieses Kapitel/diesen Teil nicht automatisch nummerieren
--------------------------------------------------------

Wenn dieses Auswahlfeld angekreuzt ist, wird das ausgewählte Kapitel von der
`automatischen Nummerierung <book_view.html#automatische-nummerierung>`_
ausgenommen, und der von Ihnen manuell eingegebene Titel bleibt erhalten.


Links
-----

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. image:: _images/book_view13.png
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
      
      .. image:: _images/filePicker01.png
         :alt: Screenshot
         

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
         
      .. image:: _images/launchers.png
         :alt: Screenshot
         

.. |Hinzufügen| image:: _images/add.png
.. |Goto| image:: _images/goto.png
.. |Entfernen| image:: _images/remove.png



"Haftmerker"
------------

Der gelbe Texteingabebereich ist für Notizen.
Änderungen werden übernommen, wenn mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.

Wenn der "Haftmerker" eines Plotpunkts Text enthält,
erscheint in the Baumansicht ein "N" als Hinweis.


Navigationsschaltflächen
------------------------

Kapitelansicht
   - **Zurück** bewegt die Auswahl auf das vorhergehende Kapitel im Baum.
   - **Vor** bewegt die Auswahl auf das nachfolgende Kapitel im Baum.

Teileansicht
   - **Zurück** bewegt die Auswahl auf den vorhergehenden Teil im Baum.
   - **Vor** bewegt die Auswahl auf den nachfolgenden Teil im Baum.
