novelibre aufgeben
==================

Sie haben eine Menge Zeit und Arbeit in ein Romanprojekt mit *novelibre*
gesteckt, sind aber zur Ansicht gekommen, dass *novelibre* doch nicht das
Richtige für Sie ist? Keine Sorge, die Mühe war nicht umsonst.
Sie können so gut wie alles in Form von *Writer*-Textdokumenten und
*Calc*-Tabellen exportieren.


So verwenden Sie Ihre Projekte ohne novelibre weiter
----------------------------------------------------

Wenn Sie also doch lieber nach der klassischen Methode mit OpenOffice oder
LibreOffice weiterarbeiten, erzeugen Sie einfach ein
`endgültiges Manuskriptdokument <export_menu.html#endgultiges-manuskriptdokument-nur-export>`__
und eine `Abschnittsliste <section_menu.html#abschnittsliste-nur-export>`__
oder ein
`Handlungsraster <plot_menu.html#handlungsraster-plot-grid-zum-bearbeiten-exportieren>`__.
Außerdem je nach Bedarf Beschreibungen Ihrer Figuren, Schauplätze usw.
als Textdokumente, Tabellen, oder
`Desktop-Wiki <https://github.com/peter88213/nv_zim/>`__.
Das alles können Sie dann von Hand weiterführen.

- Für den Umstieg auf `yWriter <https://spacejock.com/yWriter7.html>`__
  benutzen Sie am besten das `nv_yw7 Plugin <https://github.com/peter88213/nv_yw7/>`__.
- Für den Umstieg auf `novelWriter <https://novelwriter.io/>`__ können Sie Ihr Projekt
  zunächst in ein yWriter-Projekt umwandeln (siehe oben), und dann mit dem
  `yw2nw-Konvertierungswerkzeug <https://peter88213.github.io/yw2nw/>`__
  ein *novelWriter*-Projekt daraus machen.

Falls *novelibre* aus irgend einem Grund nicht mehr verfügbar ist,
kann man die *.novx*-Dateien auch mit Hilfe des
`css-Stylesheets <file_menu.html#style-sheet-kopieren>`__ im Webbrowser anzeigen
und alles Notwendige über die Zwischenablage kopieren.

Für Kenner besteht schileßlich noch die Möglichkeit, per *XSLT*-Transformation
ganz andere Dateiformate aus den *.novx*-Dateien zu erzeugen.
Beispiele dafür finden sich
`im novelibre repository <https://github.com/peter88213/novelibre/tree/main/xslt>`__.


So deinstallieren Sie novelibre
-------------------------------

1. Öffnen Sie den Installationsordner (das Unterverzeichnis ``.novx`` in Ihrem
   Benutzerverzeichnis).

   .. tip::
      Besonders einfach geht das aus *novelibre* heraus mit
      **Extras > Installationsordner öffnen**.
 
2. Falls Sie *novelibre* unter Windows als Standardanwendung für *.novx*-Dateien
   eingerichtet haben, machen Sie das rückgängig, indem Sie
   ``remove_novelibre.reg`` ausführen (Doppelklick und bestätigen).

3. Wechseln Sie eine Ebene höher in Ihr Benutzerverzeichnis und löschen Sie den
   Installationsordner. Damit verschwindet *novelibre* mitsamt den Plugins
   und Hilfsprogrammen von Ihrem Computer.

4. Entfernen Sie die *novelibre*-Verknüpfung vom Desktop.


.. note::
   Als Entwickler interessiere ich mich natürlich für Ihre Erfahrungen mit *novelibre*. 
   Zögern Sie nicht, einen entsprechenden Beitrag im 
   `Diskussionsforum <https://github.com/peter88213/novelibre/discussions>`__ zu hinterlassen. 

