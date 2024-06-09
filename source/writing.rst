Am Manuskript schreiben
=======================

Writer als Texteditor aufrufen
------------------------------

.. note::
   Das folgende Beispiel beschreibt den Arbeitsablauf für das
   Bearbeiten des Manuskripts mit LibreOffice. 
   Dasselbe gilt auch für OpenOffice.
   
   Andere Textverarbeitungsprogramme, die versprechen, das 
   *ODT*-Dateiformat zu unterstützen, werden generell nicht empfohlen.

Sobald Ihr Romanprojekt mindestens einen Abschnitt hat, können
Sie mit dem Schreiben beginnen. 
Dazu speichern Sie Ihr Projekt und exportieren Ihren Roman in die
*Writer*-Textverarbeitung. Das geht entweder mit
**Exportieren > Manuskript zum Bearbeiten**, oder indem Sie
in der Werkzeugleiste auf das Symbol |Exportieren Manuskript| klicken.

.. hint::
   - Wenn Sie den Menübefehl verwenden, können Sie *novelibre* ein 
     Manuskript erzeugen und nach einer Nachfrage mit *Writer*
     öffnen lassen.
   - Wenn Sie auf das Symbol in der Werkzeugleiste klicken, 
     wird *Writer* sofort nach dem Export aufgerufen. 


.. figure:: _images/writing01.png
   :alt: novelibre Screenshot
   
   novelibre Screenshot

Falls Sie das schon einmal gemacht haben, und es immer noch ein 
Manuskriptdokument von der letzten Sitzung gibt, werden Sie nun gefragt, 
ob Sie damit weiterarbeiten wollen. Falls ja, wählen Sie "Bestehendes öffnen".

.. figure:: _images/writing02.png
   :alt: novelibre Screenshot
   
   novelibre Screenshot

Falls Sie "Überschreiben" wählen, erzeugt *novelibre* ein neues Manuskriptdokument.
"Abbruch" bricht den Exportvorgang ab und bringt Sie zum Arbeitsbereich zurück. 


.. hint::
   *novelibre* prüft, ob ein existierendes Manuskript neuer oder älter 
   als die Projektdatei ist, und schlägt eine Auswahl vor, indem es die 
   passende Schaltfläche aktiviert. Sie können das mit der Eingabetaste 
   akzeptieren. Wenn Ihre Auswahl dem Vorschlag entspricht, sehen Sie
   in der Statusleiste eine grüne Meldung. Andernfalls ist die Meldung rot, 
   nur zur Erinnerung. 

Falls Sie den Export über den Menübefehl **Exportieren** eingeleitet haben,
kann es sein, dass Sie entsprechend Ihren  `Exportoptionen <export_menu.html#optionen>`__
gefragt werden, ob Sie das neu erzeugte Dokument öffnen wollen. 

.. figure:: _images/writing03.png
   :alt: novelibre Screenshot
   
   novelibre Screenshot
   
Wenn Sie mit "Ja" antworten, wird *Writer* mit dem Manuskriptdokument gestartet. 
Andernfalls wird das Dokument einfach für den späteren Gebrauch aufbewahrt.

Abhängig von Ihren `Exportoptionen <export_menu.html#optionen>`__
kann *novelibre* jetzt `das Projekt sperren <basic_concepts.html#projekt-sperre>`__,
damit Sie es nicht versehentlich ändern, solange es in *Writer* in Bearbeitung ist.

.. note::
   *novelibre* ruft Ihre Standardanwendung für Dateien mit der Endung
   *.odt* auf. 
   Üblicherweise trägt sich LibreOffice oder OpenOffice bei der 
   Installation selbst als Standardanwendung ein.  

Nachdem Sie zu *Writer* gewechselt haben, sehen Sie Ihren ganzen Roman
als "Normseiten" formatiert. 
Der *Navigator* (mit ``F5`` geöffnet) zeigt im *Überschriften*-Bereich
die Kapitel- und Abschnittstitel an. Per Doppelklick auf eine dieser 
Überschriften springen Sie an den jeweiligen Ort. 
Nun können Sie innerhalb der Textbegrenzungen, die die Abschnitte
definieren, losschreiben. 


.. figure:: _images/writing04.png
   :alt: LibreOffice Writer Screenshot
   
   LibreOffice Writer Screenshot: Beachten Sie, dass die Textbegrenzungen
   hier angezeigt werden, was `sehr zu empfehlen 
   <preparations.html#die-abschnitte-im-manuskript-sichtbar-machen>`__ ist.
   
.. note::
   Die Abschnittstitel, wie sie im Navigator zu sehen sind, 
   sind im Arbeitsbereich unsichtbar, so dass sie nicht den 
   Schreibfluss stören, und der Eindruck einer Original-Manuskriptseite
   gewahrt bleibt. 
 

Änderungen zu novelibre zurückschreiben
---------------------------------------

Nach Beendigung der Schreibsitzung speichern Sie die Änderungen ab, 
verlassen die *Writer*-Textverarbeitung, und kehren zu *novelibre* zurück.
Klicken Sie einfach in der Werkzeugleiste auf die Schaltfläche 
|Änderungen am Manuskript übernehmen|, 
und Ihre letzten Änderungen werden im Textbetrachter erscheinen. 

.. note::
   Das oben erwähnte Werkzeugleistensymbol gilt nur für das Manuskript. 
   Wenn Sie Änderungen aus anderen Dokumenten übernehmen wollen, 
   z.B. aus Figurenbeschreibungen, Zusammenfassungen oder dem Handlungsraster, 
   benutzen Sie das `Importieren-Menü <import_menu.html>`__. 



Mit Writer neue Abschnitte anlegen
----------------------------------

Wenn Sie während des Schreibens einen neuen Abschnitt brauchen, 
müssen Sie deswegen nicht zu *novelibre* zurückkehren. 
Beginnen Sie einfach eine neue Zeile mit der speziellen Markierung
``###``. Wahlweise können Sie einen Abschnittstitel anhängen, 
und, durch ``|`` getrennt, auch eine Abschnittsbeschreibung.
Andere Metadaten sind dann bei Bedarf später in *novelibre* einzugeben. 

.. tip::
   Sie können ``####`` benutzen, um einen `angehängten Abschnitt 
   <section_view.html#an-den-vorherigen-abschnitt-anhangen>`__
   zu erzeugen. 

Das folgende Beispiel zeigt, wie Sie einen bestehenden Abschnitt aufteilen:

.. figure:: _images/writing05.png
   :alt: LibreOffice Writer Screenshot
   
   LibreOffice Writer Screenshot: Beachten Sie die gekennzeichnete
   Abschnittsmarkierung.

In *novelibre* sehen Sie dann den neuen Abschnitt. Er hat einen Titel,
doch keine anderen Metadaten.

.. figure:: _images/writing06.png
   :alt: novelibre Screenshot
   
   *novelibre* Screenshot: Beachten Sie den ausgewählten Abschnitt.


Mit Writer neue Kapitel anlegen
-------------------------------

Wenn Sie während des Schreibens ein neuens Kapitel brauchen, 
müssen Sie deswegen nicht zu *novelibre* zurückkehren. 
Weisen Sie einfach einer neuen Zeile 
*innerhalb des laufenden Abschnitts* das Format **Überschrift 2** zu.

.. important::
   *novelibre* importiert nur Text innerhalb der Rahmen zurück, 
   welche die Abschnitte definieren. 
   Technisch teilt es immer Abschnitte auf, wenn es aus dem Manuskript
   neue Kapitel oder Abschnitte erzeugt.
  
   Sie können mit *Writer* auch keine Kapitel verschieben. 
   Falls Sie Kapitel oder Abschnitte umsortieren wollen, 
   tun Sie es mit *novelibre*.
   
Das folgende Beispiel zeigt, wie man mit *Writer*  ein Kapitel hinzufügt:

.. figure:: _images/writing07.png
   :alt: LibreOffice Writer Screenshot
   
   LibreOffice Writer Screenshot: Es kommt nicht darauf an, wie ein 
   neues Kapitel in *Writer* betitelt wird.

In *novelibre* sehen Sie dann sowohl ein neues Kapitel als auch einen 
neuen Abschnitt. 
Weil die Kapitel in diesem Beispiel automatisch nummeriert werden, 
passt die neue Kapitelüberschrift bereits, wohingegen der neue Abschnittstitel
noch manuell angepasst werden sollte.


.. figure:: _images/writing08.png
   :alt: novelibre Screenshot: Notice the selected new chapter
   
   novelibre Screenshot

.. |Exportieren Manuskript| image:: _images/Manuscript.png
.. |Änderungen am Manuskript übernehmen| image:: _images/updateFromManuscript.png
