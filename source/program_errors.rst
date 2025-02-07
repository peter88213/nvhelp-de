Programmfehler
==============

*novelibre* hat sich bei der täglichen Arbeit als sehr stabil erwiesen.
Es gibt keine geheimnisvollen Abstürze, und es werden auch keine Programmpakete
von Drittanbietern verwendet, wie sie bei anderen Anwendungsprogrammen hin und
wieder Probleme bereiten.

Dennoch gibt es keine Garantie für die Fehlerfreiheit.
*novelibre* hat eine offene Programmarchitektur, um umfangreiche Funktionserweiterungen
durch Plugins zu ermöglichen.
Das bringt leider auch mit sich, dass ein Programmierfehler in einem Plugin
das ganze Programm beeinträchtigen kann.


Was tun bei einem Fehler?
-------------------------

1. Daten sichern

   Wenn ein Programmfehler auftritt, der nicht zu einem harten Abbruch führt,
   sollte sich ein Warnfenster öffnen, das die Beendigung der Programmsitzung empfiehlt.
   In diesem Fall können Sie noch versuchen, Änderungen zu speichern.

2. Das Programm und alle Plugins aktualisieren

   Stellen Sie bitte sicher, dass Sie die neueste Version von *novelibre* und
   all seinen Plugins haben.
   Haben Sie einen veralteten Programmstand, könnte der Fehler, der bei Ihnen auftritt,
   bereits behoben sein.

3. Den Fehler melden

   Wenn das Problem damit nicht gelöst ist, könnte es sich um einen noch unbekannten
   Programmierfehler handeln.

   Im Installationsverzeichnis von *novelibre* sollte sich eine Textdatei namens
   `error.log` befinden, in der die Codezeilen aufgelistet sind, die zum Fehler geführt haben.
   Der Inhalt dieser Datei kann dem Entwickler helfen, das Problem zu beseitigen.

   Wenn Sie also zur Verbesserung von *novelibre* beitragen wollen,
   Sie können die Homepage von *novelibre* oder eines Plugins, das Ihnen verdächtig vorkommt,
   besuchen und im Abschnitt *Issues* einen Fehlerbericht einreichen.
   Dazu benötigen Sie jedoch ein Benutzerkonto, das kostenlos ist.

   .. hint:: 
      Schauen Sie sich auch bei den *issues* um, ob Ihr Fehler bereits gemeldet ist. 
      In diesem Fall können sie dieses *issue* um einen Kommentar ergänzen. 
      
      Wenn sie sich ein wenig auskennen, können Sie auch einen Blick auf die geschlossenen 
      Vorgänge werfen, und gegebenenfalls einen wieder öffnen.
      
      Wenn Sie einen neuen Fehler melden, füllen Sie bitte das *Bug report*-Formular aus.
      Geben Sie bitte an, welche Plugins Sie installiert haben. 
       

4. Plugins deinstallieren

   Wenn sich *novelibre* starten lässt, öffnen Sie den
   `Plugin-Manager <tools_menu.html#pluginmanager>`__,
   löschen Sie nacheinander alle Plugins, und starten Sie *novelibre* neu.
   Wenn sich der Fehler nicht mehr reproduzieren lässt, können Sie vorläufig
   ohne Plugins weiterarbeiten.

5. Zu einer alten Version zurückkehren

   Wenn das nichts nützt, Sie aber schon längere Zeit ohne Probleme mit
   *novelibre* gearbeitet haben, könnte das Problem mit einem fehlerbehafteten
   Update eingeschleppt worden sein.
   Falls Sie noch die vorherige Programmversion in Ihrem *Download*-Ordner haben,
   installieren Sie diese (und bei Bedarf auch die alten Plugins) erneut.



