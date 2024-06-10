Datei-Menü
==========

**Dateioperationen**

.. figure:: _images/file_menu01.png
   :alt: novelibre Screenshot

Neu
---

**Ein neues Romanprojekt anlegen**

Mit **Datei > Neu**  können Sie ein neues Projekt erstellen.
Damit öffnen Sie zunächst ein Untermenü.

.. note::
   Das Untermenü kann durch Plugins erweitert werden, 
   um mehr Dateiformate anzubieten, 
   aus denen ein *novelibre*-Projekt erzeugt werden kann.

.. figure:: _images/file_menu02.png
   :alt: novelibre Screenshot

Leeres Projekt
   -  Damit schließen Sie das laufende Projekt und erzeugen ein 
      leeres Projekt.
   -  Ein Dateiauswahldialog fragt nach Speicherort und Dateinamen 
      des neuen Projekts.
      Falls Sie diesen Dialog abbrechen, können Sie den Dateinamen 
      auch später beim Abspeichern vergeben.


Aus ODT erzeugen...
   -  Damit schließen Sie das laufende Projekt und erhalten einen 
      Dateiauswahldialog, der nach einem ODT-Dokument fragt, aus dem 
      das neue Projekt erzeugt werden soll.
   -  Das neu angelegte Projekt wird automatisch im selben Verzeichnis wie
      das ODT-Dokument abgelegt. Es hat den Dateinamen des Dokuments und 
      die Erweiterung *.novx*.
   -  Falls im Verzeichnis bereits ein Projekt mit dem Namen des ODT-Dokuments 
      existiert, wird kein neues Projekt angelegt. 
   -  Falls Sie ein zuvor exportiertes Dokument auswählen, das zu einem existierenden
      Projekt gehört, wird dieses Projekt aktualisiert und geladen. 
   -  Das ODT-Dokument kann entweder ein `angefangenes Werk
      <getting_started.html#mit-einem-angefangenen-werk-beginnen>`__,
      sein, d.h. ein Romanmanuskript mit Kapitelüberschriften und Abschnitten,
      oder eine `Gliederung <getting_started.html#mit-einer-gliederung-beginnen>`__,
      welche die Kapitel- und Abschnittsstruktur mit den Titeln und 
      Beschreibungen enthält. 


Öffnen...
---------

**Ein Romanprojekt öffnen**

Mit **Datei > Öffnen** oder ``Strg``-``O``
können Sie eine existierende Projektdatei öffnen.

.. note::
   Wenn Sie ein Projekt öffnen, wied das aktuell geladene Projekt geschlossen. 
   Falls es noch ungesicherte Änderungen gibt, werden Sie Zum Abspeichern aufgefordert.


Neu laden
---------

**Das Romanprojekt neu laden**

Mit **Datei > Neu laden** oder ``Strg``-``R``
können Sie das Projekt im Arbeitsspeicher 
mit der zuletzt gesicherten Version überschreiben.

.. tip::
   Auf diese Weise können Sie Änderungen der aktuellen Sitzung rückgängig machen.

.. note::
   Falls die Projektdatei seit dem letzten Öffnen oder Abspeichern 
   auf der Festplatte geändert wurde, erhalten Sie eine Warnmeldung.


Sicherungskopie wiederherstellen
--------------------------------

**Die zuletzt erzeugte Sicherungskopie wiederherstellen**

Mit **Datei > Sicherungskopie wiederherstellen** or ``Strg``-``B``
können Sie das Projekt im Arbeitsspeicher 
mit der zuletzt erzeugten Sicherungsdatei überschreiben.
Sie erhalten eine Warnung, dass Änderungen verlorengehen.

.. hint::
   Nach dem Wiederherstellen der Sicherungskopie gibt es keine Sicherungsdatei 
   mehr im Projektverzeichnis.
   Eine neue wird erzeugt, sobald Sie das Projekt speichern.


Baum aktualisieren
------------------

**Enforce tree refresh after making changes**

Mit **Datei > Baum aktualisieren** or ``F5``
können Sie refresh the tree.

-  "Normal" sections that have been moved to an "Unbenutzt" chapter are
   made "Unbenutzt".
-  Teils and chapters are renumbered according to the `Automatische Nummerierung
   settings <book_view.html#automatische-nummerierung>`__.
-  The "Papierkorb" chapter is moved to the end of the book, if necessary.


Sperren
-------

**Protect the project while edited outsides**

Mit **Datei > Sperren** or ``Strg``-``L``
können Sie `lock <basic_concepts.html#projekt-sperre>`__ the project.

.. note::
   Alle changes must be saved before locking the project.


Entsperren
----------

**Make the project editable**

Mit **Datei > Entsperren** or ``Strg``-``U``
können Sie unlock the project.


Projektordner öffnen
--------------------
**Launch the file manager**

Mit **Datei > Projektordner öffnen** or ``Ctrl-P``
können Sie launch the file manager with the current project folder .
This might come in handy, if you wish to delete files,
open your project with another application, and so on.

.. hint::
   In case you edit the project "outsides", consider locking it before.


Style sheet kopieren
--------------------

**Provide a css style sheet in the project folder**

Mit **Datei > Style sheet kopieren**
können Sie copy the style sheet *novx.css* into the current project folder.
This allows you to view the *.novx* project file with a web browser.

.. figure:: _images/file_menu01.jpg
   :alt: Edge browser Screenshot

   Edge browser Screenshot

.. hint::

   Depending on your web browser and your operating system, the
   *content type* resp. *MIME type* of *.novx* files must be registered as
   *"text/xml"*. Under Windows, yo can do this by running the
   ``<home>\.novx\add_novelibre.reg`` script.


Manuskript verwerfen
--------------------

**Verwerfen the current Manuskript by renaming it**

Mit **Datei > Manuskript verwerfen**
können Sie add the *.bak* extension to the `current Manuskript
<export_menu.html#manuskript-zum-bearbeiten>`__.
This may help to avoid confusion about changes made with *novelibre* and
*Writer*.

.. hint::
   You can also discard any previously exported document "for editing"
   via the `Importieren dialog <import_menu.html>`__. 


Speichern
---------

**Das projekt speichern**

Mit **Datei > Speichern** oder ``Strg``-``S``
können Sie das Projekt speichern.
Dabei wird automatisch eine Sicherungskopie des letzten Stands erzeugt.

.. note::
   Falls die Projektdatei seit dem letzten Öffnen oder Abspeichern 
   auf der Festplatte geändert wurde, erhalten Sie eine Warnmeldung.


Speichern unter...
------------------

**Das Projekt unter einem anderen Namen/an einem anderen Ort speichern.**

Mit **Datei > Speichern unter...** or ``Strg``-``⇧``-``S``
können Sie das Projekt unter einem anderen Dateinamen oder an einem anderen 
Ort speichern.
Es öffenet sich ein Dateiauswahldialog, um den neuen Dateipfad und den
Dateinamen anzugeben. 

.. note::
   Ihr laufendes Projekt bleibt in dem Zustand, wie es zuletzt gespeichert 
   wurde. 
   Zwischenzeitliche Änderungen wirken sich dann auf das neue Projekt aus.


Schließen
---------

**Das Romanprojekt schließen**

Mit **Datei > Schließen**
können sie das Projekt schließen, ohne das Programm zu beenden.
Beim Schließen werden Sie gefragt, ob Sie das Projekt speichern wollen,
falls es ungesicherte Änderungen gibt.

.. note::
   Falls Sie ein anderes Projekt öffnen, wird das aktuell geladene Projekt
   automatisch geschlossen.


Beenden
-------

**Das Programm beenden**

-  Unter Windows können Sie das Programm mit **Datei > Beenden** 
   oder ``Alt``-``F4`` beenden.
-  Andernfalls können Sie das Programm mit **Datei > Beenden** 
   oder ``Strg``-``Q`` beenden.

.. note::
   Beim Beenden werden Sie gefragt, ob Sie das Projekt speichern wollen,
   falls es ungesicherte Änderungen gibt.

