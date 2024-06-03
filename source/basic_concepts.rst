Grundlegende Konzepte
=====================


Die Buch-Hierarchie
-------------------

Teile
~~~~~

Wir gehen davon aus, dass ein Roman aus Kapiteln
und Abschnitten besteht.
Teile sind optional; technisch sind sie Kapitel auf der
ersten Ebene.
Dennoch befinden sie sich im Projektbaum von *novelibre*
auf der selben Ebene wie die Kapitel, doch sie erhalten
ihre Überschriften eine Ebene höher.
Damit dienen Teile hauptsächlich dazu, zwischen den Kapiteln
Überschriften erster Ordung einzufügen, wenn erforderlich.


.. hint::
   Sie können Kapitel in Teile umwandeln und umgekehrt, indem
   Sie einfach ihre `Ebene ändern
   <tree_context_menu.html#ebene-andern>`__.

.. note::
   Ein Vorgänger von *novelibre* war `novelyst 
   <https://peter88213.github.io/novelyst/>`__. 
   Dort sind die Teile auf einer höheren Hierarchieebene als 
   die Kapitel im Projektbaum, so wie es der logischen 
   Vorstellung entspricht.
   Damit war es möglich, Teile mitsamt ihren untergeordneten
   Kapiteln zu verschieben, oder gesamte Teile als "unbenutzt"
   zu kennzeichnen.
   In der Praxis erwies sich das jedoch als umständlich. 
   Ich finde es einfacher, nur die Teile-Grenzen zu verschieben
   und die Kapitelreihenfolge unverändert zu lassen, wenn
   Teile definiert werden.  


Kapitel
~~~~~~~

Ein *novelibre*-Projekt muss mindestens ein Kapitel haben.
In exportierten Dokumenten haben reguläre Kapitel Überschriften
zweiter Ordnung.
Für *novelibre* dienen Kapitel nur als Behälter für Abschnitte,
welchen die eigentliche dramaturgische Funktion zugeschrieben wird.
Deshalb gibt es nur einige wenige
`Kapiteleigenschaften <chapter_view.html>`__
einzustellen.


Abschnitte
~~~~~~~~~~

Bei *novelibre* gehört der gesamte Textinhalt zu Abschnitten.
Abschnitte können Szenen, Erklärungen, Beschreibungen oder
erzählerische Zusammenfassungen sein -- Sie sind vollkommen
frei, wenn es darum geht, den Romantext in Abschnitte zu
unterteilen.
Es gibt eine Auswahl von `Abschnitts-Metadaten
<section_view.html>`__ zur freien Verwendung.

Im Textkörper der eportieren Dokumente werden Abschnittswechsel
per Voreinstellung durch Abschnittstrenner gekennzeichnet,
etwa so:

``* * *``

Wenn Sie allerdings beim Plotten und Organisieren kleinteligere
Abschnitte brauchen, als es die Leser später sehen sollen,
könne Sie Abschnitte auch ohne Abschnittstrenner als einfache Absätze
`an den vorherigen Abschnitt anhängen
<section_view.html#an-den-vorherigen-abschnitt-anhangen>`__.


Teil/Kapitel/Abschnittstypen
----------------------------

Jeder Teil, jedes Kapitel und jeder Abschnitt hat einen Typ, den
Sie über das Kontextmenü oder das Teil/Kapitel/Abschnitt-Menü
ändern können.
Der Typ kann *Normal* oder *Unbenutzt* sein.

Normal
   -  "Normale" Teile, Kapitel und Abschnitte werden gezählt.
      Ihre Anzahl ist in der Statusleiste zu sehen.
   -  "Normale" Abschnitte werden ins manuskript exportiert
      und tragen zur Wortzählung bei.
   -  "Normale" Teile und Kapitel können untergeordnete Elemente
      von jedem Typ haben.
   -  "Normale" Abschnitte werden im Projektbaum entsprechend dem
      eingestellten `Farbgebungsmodus
      <view_menu.html#farbgebungsmodus>`__ eingefärbt.

Unbenutzt
   Sie können Teile, Kapitel und Abschnitte als unbenutzt kennzeichnen,
   um sie von der Wortzählung und vom Export auszuschließen.

   -  Die Projektbaum-Unterelemente unbenutzter Teile und Kapitel
      sind ebenfalls unbenutzt.
   -  Kennzeichnen Sie einen Abschnitt als "Unbenutzt",
      bleiben seine sonstigen Eigenschaften erhalten.
   -  Unbenutzte Projektbaumelemente werden in grauer Farbe dargestellt.


Abschnitts-Status
-----------------

Über das Kontextmenü oder das Abschnitt-Menü können Sie jedem
"normalen" Abschnitt einen Fertigstellungsstatus zuordnen.

-  Sie können einen `Farbgebungsmodus <view_menu.html#farbgebungsmodus>`__
   einstellen, in dem Abschnitte je nach Status in unterschiedlichen
   Farben dargestellt werden.
-  Wahlweise können Sie einen Status zur aktuellen
   `Arbeitsphase <book_view.html#schreibfortschritt>`__,
   erklären und einen `Farbgebungsmodus
   <view_menu.html#farbgebungsmodus>`__
   wählen, der Abschnitte hervorhebt, die nicht im Plan liegen.
-  Neu erstellte Abschnitte erhalten den Status "Gliederung".
-  Wortzahlen nach Status erscheinen in den `Bucheigenschaften
   <book_view.html#schreibfortschritt>`__.


-----------------


Figuren und Erzählwelt
----------------------

Sie können Figuren, Schauplätze und Gegenstände definieren
und sie mit Abschnitten in Beziehung setzen, um ihr
Vorkommen in der Geschichte zu verfolgen.
*novelibre* speichert auch einige Metadaten dazu,
hauptsächlich als praktische Merkhilfe beim Schreiben
oder Überarbeiten.

.. note::
   *novelibre* ist nicht dazu gedacht, umfangreichen 
   Weltenbau zu dokumentieren. 
   Für so etwas gibt es eine Vielzahl spezialisierter Anwendungsprogramme, 
   Online- und Offline-Wikis, und Notizverwaltungssoftware.  
   *novelibre* bietet jedoch die Möglichkeit, Bilddateien und 
   Dokumente mit den Figuren, Schauplätzen und Gegenständen zu 
   verlinken, um den Zugriff darauf zu erleichern. 
   

.. important::
   Um den Abschnitten **Perspektiv-Figuren** zuweisen zu können, 
   müssen Sie diese zuerst `erzeugen <characters_menu.html#hinzufugen>`__. 


-----------------

Text formatieren
----------------

Wir setzen voraus, dass ein Romantext nur einige wenige
Arten von Textauszeichnung braucht.
Beim Import von ODT unterstützt *novelibre* die folgenden Formate:

-  *Betont*-Zeichenstil oder Kursivschrift.
-  *Stark betont*-Zeichenstil oder Fettschrift.
-  *Zitat* (Vom Textkörper visuell abgesetzter Absatz).
-  *Ungeordnetes Listenelement* (Eingerückter Absatz mit einem Aufzählungszeichen).


Kommentare, Fuß- und Endnoten
-----------------------------

*novelibre* unterstützt ODT-Kommentare, Fußnoten und Endnoten.

.. tip::
   *novelibre* bietet keine Unterstützung für Bilder.
   Sie können dafür Kommentare als Platzhalter benutzen, um sie
   ganz am Schluss durch die Bilder (oder andere Sonderformatierungen, 
   die nicht durch *novelibre* abgedeckt sind) zu ersetzen, 
   wenn es darum geht, den `fertiggestellten Roman 
   <export_menu.html#manuskript-zum-drucken-nur-exportieren>`__ 
   für die Veröffentlichung vorzubereiten. 


Über den Umgang mit der Dokumentensprache
-----------------------------------------

ODF-Dokumenten ist üblicherweise eine Sprache zugeordnet, die
über die Rechtschreibprüfung und länderspezifische Zeichenersetzung
bestimmt.
Darüberhinaus erlaubt *Writer*, Textpassagen andere Sprachen als die
Dokumentensprache zuzuweisen, um fremdsprachlichen Text zu kennzeichnen,
oder die Rechtschreibprüfung außer Kraft zu setzen.

Dokument gesamt
   Die Projektsprache (Sprachencode gemäß ISO 639-1 und Ländercode
   entsprechend ISO 3166-2) kann in den **Buch**-Einstellungen
   (rechtes Fenster) unter `Sprache des Dokuments
   <book_view.html#sprache-des-dokuments>`__ vorgegeben werden.

Textpassagen in Abschnitten
   *novelibre* unterstützt die zeichenweise und absatzweise Zuordnung
   anderer Sprachen.

-----------------

Projekt-Sperre
--------------

Wenn man ein Dokument exportiert, das außerhalb von *novelibre* bearbeitet
werden kann, kann das Projekt automatisch gesperrt werden, um nicht
durcheinander zu kommen.
Das Verhalten hängt von den `Exportieren-Optionen <export_menu.html#optionen>`__
ab.

.. important::
   Das Projekt kann nur gesperrt werden, wenn alle Änderungen gespeichert sind. 

Im gesperrten Zustand kann das Projekt nicht über die Benutzerschnittstelle
bearbeitet werden.
Die Fußleiste wird dann invertiert dargestellt, die Menüeinträge
für Dateneingabe und Export sind ausgegraut, und die Eingabeelemente
im  *Eigenschaften*-Fenster sind deaktiviert.

Die Projektsperre bleibt auch nach Programmbeendigung erhalten.
Dazu wird automatisch eine Sperrdatei namens ``.LOCK.<project name>.novx#``
angelegt.
Löscht man diese Datei, während *novelibre* nicht läuft, ist das
Projekt beim nächsten Programmstart entsperrt.

Gewöhnlich wird das Projekt automatisch entsperrt, nachdem ein extern
bearbeitetes Dokument zurück importiert wurde.

.. hint::
   Die Projektsperre ist nichts weiter als eine starke Merkhilfe.
   Sie können das Projekt jederzeit auf eigene Gefahr 
   `von Hand entsperren <file_menu.html#entsperren>`__ . 
   Sie können es auch `von Hand sperren <file_menu.html#sperren>`__,
   fals erforderlich. 
   Die Schaltfläche |Sperren/Entsperren| in der Werkzeugleiste
   schaltet zwischen gesperrt und entsperrt hin und her.


.. |Sperren/Entsperren| image:: _images/lock.png


