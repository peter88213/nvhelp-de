Daten speichern
===============

*novelibre* speichert den gesamten Romantext sowie alle Metadaten eines Romanprojekts
in einer einzigen Textdatei mit der Dateiendung ``.novx`` ab.
Die im Lauf der Arbeit erzeugten Text- und Tabellendokumente gelten als temporäre Dateien,
da ihre Inhalte aus der entsprechenden *novx*-Projektdatei wiederhergestellt werden können,
solange diese durch rechtzeitigen Reimport aktuell gehalten wird.
Wenn also ein bestimmter Bearbeitungsstand gesichert werden soll,
genügt diese eine Projektdatei.
Hinzu kommen möglicherweise noch weitere Dateien wie Zeitleisten oder ein Projekt-Wiki.


Änderungsanzeige
----------------

Wenn Sie im Verlauf einer *novelibre*-Sitzung das Projekt verändern, ändert sich die Farbe
der Fußleiste zu Goldgelb, um zu zeigen, dass es ungespeicherte Änderungen gibt.
Diese Änderungsanzeige bleibt erhalten, bis Sie das Projekt speichern
oder einen früheren Bearbeitungsstand wiederherstellen.

.. hint::
   Die Änderungsanzeige bleibt aus technischen Gründen auch dann erhalten, 
   wenn Sie alle Änderungen rückgängig machen. Sie zeigt also nicht wirklich 
   einen geänderten Bearbeitungsstand an, sondern, dass seit dem letzten Speichern 
   etwas geändert wurde. 

Um alle Änderungen seit dem letzten Speichern zu verwerfen, können Sie Über den Menübefehl
`Neu laden <file_menu.html#neu-laden>`__ den zuletzt gespeicherten Stand wiederherstellen.

Sicherungsdateien
-----------------

*novelibre* ist darauf ausgelegt, seine Daten so gut wie möglich zu sichern.
Die aktuellen Dateien werden weder überschrieben noch komplett gelöscht,
stattdessen werden Sicherungskopien mit der Dateiendung ``.bak`` erzeugt.
Auf diese Weise steht auch der vorletzte Bearbeitungsstand noch zur Verfügung
und kann sogar mittels des Menübefehls
`Sicherungskopie wiederherstellen <file_menu.html#sicherungskopie-wiederherstellen>`__
wiederhergestellt werden.

.. hint::
   *novelibre* legt solche *bak*-Sicherungskopien nicht nur für *novx*-Dateien an, 
   sondern auch für die temporären Text- und Tabellendokumente und für 
   Dateien, die z.B. über Plugins synchronisiert werden, wie Zeitleisten.   

Optional können Sie *novelibre* auch dazu veranlassen, bei jedem Abspeichern
eine Kopie der Projektdatei in einem
`benutzerdefinierten Sicherungsverzeichnis <tools_menu.html#sicherungseinstellungen>`__
abzulegen.
In diesem Sicherungsverzeichnis sollte nicht gearbeitet werden,
deshalb erhalten die Sicherungskopien dort einen Dateinamenszusatz,
den Sie beim Wiederherstellen manuell entfernen müssen.


-----------------


Bemerkungen zum Dateiformat
---------------------------

*novx*-Dateien sind Textdateien, die für Menschen lesbar sind und im Prinzip
mit beliebigen Texteditoren angezeigt und bearbeitet werden können.
Der Text und die Daten sind mit Hilfe von XML-Markierungen gegliedert,
wodurch die Datei auch für Computer verständlich wird.

Die Definition des *novx*-XML-Formats ist hier zu finden:

https://peter88213.github.io/novxlib-docs/

Die Informationen sind für Computerexperten gedacht, welche die vielfältigen
Standard-Techniken zum Lesen und zur Verarbeitung von XML-Dateien anwenden möchten.
Als Romanautor und gewöhnlicher Benutzer müssen Sie sich um all das nicht kümmern.
Sie können jedoch beruhigt sein, dass es um die Speicherung Ihrer Arbeitsergebnisse
keinerlei Geheimnisse gibt.

Allerdings gibt es auch für Sie einen Aspekt zu beachten, nämlich den der Dateiversion.
Es kann vorkommen, dass *novelibre* um Leistungsmerkmale erweitert wird,
die es erforderlich machen, auch das *novx*-Dateiformat zu erweitern.
Das wird dann in der Änderungshistorie vermerkt.
In solchen Fällen wird die Versionsnummer des *novx*-Dateiformats hochgezählt.
Diese Versionsnummer ist in der *novx*-Datei hinterlegt und wird von *novelibre*
jedesmal beim Öffnen eines Projekts geprüft.
Wenn *novelibre* auf eine Dateiversion stößt, die mit einer neueren Programmversion
erzeugt wurde, bedeutet das, dass dieses Projekt Informationen enthalten könnte,
welche das aktuell laufende Programm nicht kennt, und die deshalb beim erneuten
Speichern verlorengehen könnten.
Aus diesem Grund wird *novelibre* eine solche Datei nicht öffnen
und eine entsprechende Fehlermeldung in der Statuszeile anzeigen.

.. important::
   Um solche Probleme auszuschließen, stellen Sie einfach sicher, dass Sie, falls Sie 
   auf mehreren Computern arbeiten, überall die selbe Programmversion von *novelibre*
   installiert haben. 
   Am besten die aktuelle Ausgabe. 



