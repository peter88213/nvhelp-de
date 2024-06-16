Abschnittseigenschaften
=======================

Die Ansicht der Abschnittseigenschaften öffnet sich im rechten Fenster,
wenn Sie im Baum einen Abschnitt wählen.


.. figure:: _images/section_view01.png
   :alt: Screenshot

Titel und Beschreibung
----------------------

Titel und Beschreibung werden als beschreibbare "Karteikarte" dargestellt.

Die Bearbeitung des Titels können Sie mit der Eingabetaste beenden.
Änderungen an der Beschreibung werden übernommen, sobald mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.


Tags
----

Tags sind ein frei benutzbares Werkzeug,
um Abschnitte in der Baumansicht zu kennzeichnen.
Tags müssen nicht anderswo definiert werden, sie werden einfach,
durch Semikolons getrennt, ins Eingabefeld eingetragen.
Die Bearbeitungkönnen Sie mit der Eingabetaste beenden.

.. caution::
   Achten Sie auf eine einheitliche Schreibweise, 
   falls Sie Tags mehrmals verwenden wollen.

Perspektive
-----------

Der Kurzname der Perspektivfigur wird in der Baumansicht angezeigt.
Sie können ihn aus einer Drop-down-Liste auswählen, die alle
Figuren in der selben Reihenfolge wie in der Baumansicht enthält.

Unbenutzt
---------

Mit dem **Unbenutzt** Auswahlfeld können Sie change the `section type
<basic_concepts.html#teil-kapitel-abschnittstypen>`__.

An den vorherigen Abschnitt anhängen
------------------------------------

Wenn dieses Feld angekreuzt ist, erhalten exportierte
Dokumente keinen Abschnittstrenner vor dem ausgewählten
Abschnitt.
Der Abschnitt beginnt dann einfach mit einem neuen Absatz.

Plot
----

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/section_view04.png
   :alt: Screenshot

Plotlinien
~~~~~~~~~~

Hier können Sie den ausgewählten Absatz den Plotlinien zuweisen,
zu denen er beiträgt.
Die zugewiesenen Plotlinien werden in einer Liste dargestellt,
in der Reihenfolge der Zuweisung zum Abschnitt.

.. tip::
   Einen bequemeren Weg um Plotlinienzuweisungen zu verwalten und
   zu überblicken, bietet das 
   `nv_matrix plugin <https://github.com/peter88213/nv_matrix/>`__. 
   
   Sie können einen Abschnitt auch einer Plotlinie zuweisen, 
   indem Sie im `Handlungsraster <plotting.html#handlungsraster-plot-grid>`__
   Text ins entsprechende Plotliniennotizen-Feld eintragen.
   
Hinzufügen Plotlinie assignment
   When clicking on |Hinzufügen|, the "Auswahlmodus"
   is activated, and the cursor changes to a "plus" shape. By clicking
   on a Plotlinie, it will be related with the section.

   .. hint::
      You can exit the "Auswahlmodus" without selecting an element by
      clicking on the highlighted status bar, or by pressing the ``Esc``
      key. 

Plotlinie entfernen assignment
   When clicking on |Entfernen| or pressing the ``Entf``-Taste,
   the selected Plotlinie is removed from the list.

Ansicht the related element
   When double-clicking on a Plotlinie, or clicking on |Goto|,
   the selected Plotlinie is opened and its properties are displayed.

   .. hint::
      You can go back to the initially selected section with |Go Back|. 

Plotlinie notes
   You can enter section-related notes for the Plotlinie selected
   in the list of related Plotlinien. These notes appear in the
   `plot grid <plotting.html#handlungsraster-plot-grid>`__ where you also can
   edit them.



Plotpunkte
~~~~~~~~~~

The plot points assigned with the selected section are displayed
along with their Plotlinien.

.. hint::
   To change or clear the plot point assignment, go to the
   `plot point's properties <point_view.html#assigned-section>`__.


Szene
-----

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/section_view03.png
   :alt: Screenshot

.. figure:: _images/section_view08.png
   :alt: Screenshot

Es gibt eine verbreitete Theorie für "absatzstarke Autoren",
nach der Romane am besten in Szenen unterteilt werden,
wobei sich "Aktionsszenen" und "Reaktionsszenen", oder
"Szenen" und "Folgen" wechselseitig ablösen.
Falls Sie so etwas umsetzen wollen, können Sie das hier tun.

Falls das nichts für Sie ist, Sie aber eine andere Methode anwenden wollen,
um ihre Szenen dramaturgisch zu gliedern,
können sie den Abschnitt als **Andere** einstellen,
um `frei benannte <book_view.html#umbenennungen>`_
Textfelder zu erhalten.

.. figure:: _images/section_view06.png
   :alt: Screenshot
   
   Beispiel für eine vom Standard abweichende Szenenkategorie

Andererseits ist nicht jeder Abschnitt eine Szene, auf welche
die pben erwähnten Kategorien zutreffen.
Abschnitte können auch anderweitig charkterisiert werden,
zum Beispiel als narrative Zusammenfassung, Dialog, Beschreibung
oder Erklärung.
Wenn also ein Abschnitt nicht szenisch ist, können Sie ihn als
**Keine Szene** einstellen,
um `frei benannte <book_view.html#umbenennungen>`_
Textfelder zu erhalten.

.. figure:: _images/section_view07.png
   :alt: Screenshot
   
   Beispiel für eine nicht-szenische Abschnittskategorie


Beziehungen
-----------

Dieses Fenster öffnen oder schließen Sie mit Klick auf den Titel.

.. figure:: _images/section_view02.png
   :alt: Screenshot

Wenn Sie Figuren, Schauplätze und Gegenstände mit dem Abschnitt
in Verbindung bringen wollen, können sie das hier tun, indem
Sie das jeweilige Element einer Liste von Beziehungen hinzufügen.

Alter anzeigen
   Wenn ein Abschnitt ein Datum hat, können Sie das Alter der
   verbundenen Figuren abrufen, die ein
   `Geburtsdatum <character_view.html#biographie>`__ haben.

Hinzufügen Relationship
   Wenn Sie auf |Hinzufügen| klicken, wird der "Auswahlmodus"
   is activated, and the cursor changes to a "plus" shape. By clicking
   on a character/location/item, this element will be related with the
   section.

   .. hint::
      You can exit the "Auswahlmodus" without selecting an element by
      clicking on the highlighted status bar, or by pressing the ``Esc``
      key. 

Entfernen Relationship
   When clicking on |Entfernen| or pressing the ``Entf``-Taste,
   the selected relationship is removed from the list.

Ansicht the related element
   When double-clicking on a related element, or clicking on |Goto|,
   the selected element is opened and its properties are displayed.

   .. hint::
      You can go back to the initially selected section with |Go Back|. 

.. hint::
   A convenient way to manage and keep track of relationships is offered 
   by the `nv_matrix plugin 
   <https://github.com/peter88213/nv_matrix/>`__. 


.. |Hinzufügen| image:: _images/add.png
.. |Goto| image:: _images/goto.png
.. |Entfernen| image:: _images/remove.png
.. |Go back| image:: _images/goBack.png


Datum/Zeit
----------

Hier können Sie enter information about the selected section's narrative time.
Die Bearbeitungkönnen Sie mit der Eingabetaste beenden.

.. hint::
   Dedicated timeline software offers a more convenient way of entering date/time 
   and duration information. So if chronology is important to your story, you
   might want to take a look at the `Timeline plugin 
   <https://github.com/peter88213/nv_timeline/>`__, or the 
   `Aeon Timeline 2 plugin <https://github.com/peter88213/nv_aeon2/>`__.

.. figure:: _images/section_view05.png
   :alt: Screenshot

Beginn
~~~~~~

If the selected section is a scene, this is when it starts:

Datum
   Format: *YYYY-MM-DD*, according to ISO 8601.

Zeit
   Format: *hh:mm*, according to ISO 8601.

Tag
   Format: Any number. Tag "0" is the `reference date
   <book_view.html#erzahlzeit>`_, if set.

.. note::
   Alle entries are optional. You can either enter a date, or a day. 
   
Datum/Zeit löschen
   This will reset *Datum*, *Zeit*, and *Tag* simultaneously.

Erzeugen
   This generates date and time from the date/time/duration data of the
   `previous section <Navigationsschaltflächen_>`_, so the selected section
   follows directly the previous one.

Datum/Tag umwandeln
   If the `reference date <book_view.html#erzahlzeit>`__ is set,
   The unspecific *Tag* can be transformed into a specific *Datum*,
   and vice versa.

   .. hint::
      If necessary können Sie convert all sections at once in the 
      `Buch properties view <book_view.html#erzahlzeit>`__.
   

Dauer
~~~~~

Tage
   Any number should be accepted.

Stunden
   If a number greater than 24 is entered, the number of days
   will be automatically increased.

Minuten
   If a number greater than 60 is entered, the number of hours
   will be automatically increased.

Dauer löschen
   This will reset *Tage*, *Stunden*, and *Minuten* simultaneously.

Erzeugen
   This generates the duration from the date/time data of the
   `next section <Navigationsschaltflächen_>`_, so the next section
   follows directly the current one.


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
   Wenn sie auf einen Link doppelklicken, oder auf |Goto| klicken,
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


"Haftmerker"
------------

Der gelbe Texteingabebereich ist für Notizen.
Änderungen werden übernommen, wenn mit der Maus
irgendwo außerhalb des Texteingabefelds geklickt wird.

Wenn der "Haftmerker" einers Abschnitts Text enthält,
erscheint in the Baumansicht ein "N" als Merker.

Wenn ein Kapitelzweig mit Abschnitten, die notizen enthalten,
eingeklappt wird, erscheint das "N" in der Kapitelzeile.

.. note::
   Die "Haftmerker" sind nur für die Arbeit mit *novelibre* gedacht.
   Sie werden nicht beim Dokumentenexport berücksichtigt.
   Allerdings erscheinen sie in der `Abschnittsliste`_.

.. _Abschnittsliste: section_menu.html#exportieren-section-list-spreadsheet

Navigationsschaltflächen
------------------------

- **Zurück** moves the selection to the previous section in the tree.
- **Vor** moves the selection to the next section in the tree.
