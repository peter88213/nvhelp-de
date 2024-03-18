nv_templates
============

**Benutzerhandbuch**

Diese Seite gilt für die neueste Ausgabe von `nv_templates
<https://github.com/peter88213/nv_templates/>`__ release.
You can open it with **Hilfe > Vorlagen-Plugin Online-Hilfe**.


Das Plugin installieren
-----------------------

- Unzip the downloaded zipfile into a new folder.
- Move into this new folder and launch **setup.pyw**. This installs the plugin.

The plugin adds a **Erzählstruktur-Vorlagen** entry to the *novelibre* **Extras**-Menü,
einen **Aus Vorlage erzeugen**-Eintrag ins **Datei > Neu**-Untermenü,
and a **Vorlagen-Plugin Online-Hilfe** entry to the **Hilfe**-Menü.


Befehlsreferenz
---------------

Datei > Neu
~~~~~~~~~~~

Aus der Vorlage erzeugen
^^^^^^^^^^^^^^^^^^^^^^^^

This erzeugens a neu project with the narrative structure from a Markdown
template file.

-  First, a file select dialog asks for the neu project’s file name
   (novelibre v1.4+). If you cancel the dialog, you can select the file
   name later when saving the project.
-  Then a second file select dialog asks for the template file to apply.


Extras > Erzählstruktur-Vorlagen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Laden
^^^^^

This loads the narrative structure from a Markdown template file.

-  A file select dialog asks for the template file to apply.


Speichern
^^^^^^^^^

This saves the narrative structure to a Markdown template file.

-  A file select dialog asks for the neu template’s file name.


Ordner öffnen
^^^^^^^^^^^^^

This opens the templates fälter with the OS file manager, so you can
manage and edit the templates.


Konventionen
------------

In *novelibre*, you can define a narrative structure with stages. See
`Plotlinien <https://github.com/peter88213/novelibre/help/plotting>`__.
*nv_templates* faciliates the reuse of narrative structures.


Markdown-Dateistruktur
~~~~~~~~~~~~~~~~~~~~~~

The *Erzählstruktur-Vorlage* Markdown file defines such a structure with
headings and ordinary text.


Überschrift erster Ordnung für die Hauptstadien, z.B. Akte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first level heading begins with ``#``, followed by a space and a
stage title.


Überschrift zweiter Ordnung für untergeordnete Stadien oder Plotpunkte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The second level heading begins with ``##``, followed by a space and a
stage title.


^Gewöhnlicher Text
^^^^^^^^^^^^^^^^^^

Any text under a heading is used as a description for the element
generated from the heading.


Beispiel
^^^^^^^^
.. highlight:: markdown

:: 

    # Teil 1: Exposition

    Die Exposition dient der Einführung in die Welt der Geschichte. Ziel ist es, der Leserschaft genügend Information zu geben, um sich in der Welt der Geschichte zurechtzufinden.

    ## 1. Erzählabschnitt: Exposition der zentralen Figuren und ihrer Welt

    Die normale Welt: Wie sieht die Routine des Protagonisten aus? Wie lautet die zentrale Frage?

    ## Auslösendes Ereignis

    Etwas geschieht, das die normale Welt aus dem Gleichgewicht bringt: Was zerstört die bisherige Routine des Protagonisten?

    ## 2. Erzählabschnitt: Erste Handlung, ggf. retardierendes Moment

    Die Reaktion des Protagonisten auf das auslösende Ereignis: Wie reagiert der Protagonist auf das auslösende Ereignis?

    ## Erster Wendepunkt

    Der Protagonist nimmt den Kampf um sein Ziel auf. Er verlässt die alte Welt und begibt sich in eine unbekannte Welt: Was ist das Ziel des Protagonisten? Warum muss er es unbedingt erreichen? Wie lautet die dramatische Frage?

    # Teil 2: Entwicklung/Zuspitzung/Konfrontation

    Im ersten Wendepunkt tritt der Protagonist aus seiner gewohnten, aber gestörten Welt in eine neue, unbekannte Welt. Er muss in dieser neuen Welt bestehen, wenn er sein Ziel erreichen will. Im zweiten Akt geht es um die Versuche, mit denen er dieses Ziel realisieren will. Er wird scheitern und er wird kleine Erfolge haben, wird sich seinem Ziel annähern und wieder von ihm weggeschleudert. Es gelingt ihm jedoch nicht, sein Ziel endgültig zu erreichen, weil die antagonistische Kraft es immer wieder aufs Neue vermag, ihn daran zu hindern. Entscheidend ist, dass es -- trotz kleiner Zwischenerfolge -- tendenziell immer schwerer für ihn wird, sein Ziel zu erreichen, dass er immer mehr Risiken eingehen muss, weil die antagonistische Kraft ihm immer größere Steine in den Weg legt. Der Konflikt spitzt sich immer mehr zu.

    ## 3. Erzählabschnitt

    a) Alles läuft bestens: Welche Erfolge erzielt der Protagonist? Wie schafft er es, die Hindernisse der antagonistischen Kraft zu überwinden?

    b) Es geht immer weiter bergab: Welche Niederlagen muss der Protagonist einstecken? Wie hindert die antagonistische Kraft ihn daran, sein Ziel zu erreichen?

    ## Zentraler Punkt

    a) Im Moment größter Hoffnung muss der Protagonist einen Rückschlag einstecken, der ihn dazu führen kann, ein neues Ziel zu verfolgen.

    b) Der Protagonist kommt an seinem Tiefpunkt an, erlebt Tod und Wiedergeburt, schöpft jedoch neue Hoffnung und rappelt sich wieder auf.

    ## 4. Erzählabschnitt

    a) Der Protagonist erholt sich nicht von dem Rückschlag: Es geht weiter bergab.

    b) Mit neuem Mut und noch größerer Entschlossenheit verfolgt der Protagonist sein altes oder neues Ziel. alles läuft bestens.

    ## Zweiter Wendepunkt

    a) Der Protagonist ist kurz davor, alles zu verlieren, durchlebt Tod und Wiedergeburt und schöpft neuen Mut.

    b) Der Protagonist ist kurz davor, sein Ziel zu erreichen, wird dann jedoch zurückgeworfen.

    # Teil 3: Auflösung

    Im dritten Akt nimmt das Tempo zu. Der Protagonist und die antagonistische Kraft stehen sich zum großen Finale gegenüber, die antagonistische Kraft rüstet zum letzten und größten Gegenschlag. Der Protagonist gerät in eine Krisenentscheidung, und im Höhepunkt wird der Konflikt endgültig und unwiderruflich gelöst. Die antagonistische Kraft wird vernichtend geschlagen, und der Protagonist erreicht sein Ziel -- oder er verliert es für immer.

    ## 5. Erzählabschnitt

    Vorbereitung auf die alles entscheidende "letzte Schlacht".

    ## Krise

    Der Protagonist befindet sich in einem Dilemma und muss sich endgültig entscheiden, was er will.

    ## Höhepunkt

    Die "letzte Schlacht". Der Konflikt wird entschieden. Der Protagonist erreicht sein Ziel, oder verliert es für immer.

    ## 6. Erzählabschnitt

    Der Konflikt ist gelöst, der Protagonist ein neuer Mensch geworden: Was hat sich durch den Konflikt verändert? Wie geht es mit dem Protagonisten weiter?
    
This file generates the following structure in an empty project:

.. figure:: _images/structure01.png
   :alt: Screenshot


