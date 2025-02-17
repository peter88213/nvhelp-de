Mit novelibre plotten
=====================


Ein Strukturmodell anwenden
---------------------------

Wenn Sie eine Geschichte entsprechend einem Strukturmodell
(z.B. dem *Drei-Akt-Modell*, der *Heldenreise* oder dem
*Save The Cat Beat Sheet*) in Stadien zerlegen wollen,
fügen Sie einfach die Stadien zwischen den Abschnitten
ein, um den Beginn zu kennzeichnen.
Das gibt Ihnen farblich abgesetzte Zwischenüberschriften
in der Baumansicht. Diese erscheinen nicht im Manuskript.

.. image:: _images/acts01.png
   :alt: Akte

Mit dem `nv_templates-Plugin
<https://github.com/peter88213/nv_templates/>`__ können Sie
vorgefertigte Strukturmodelle aus Markdown-Vorlagendateien laden,
oder das Strukturmodell Ihrer Geschichte zur Wiederverwendung
abspeichern.

-----------------

Plotlinien definieren
---------------------

*novelibre* bietet *Plotlinien* als ein mächtiges und flexibles Konzept
zum Plotten an.

.. image:: _images/plotlines01.png
   :alt: Plotlinien

"Plotlinie" kann eine Reihe von Bedeutungen haben:
Erzählstrang, Figurenbogen, Handlungsfaden, Nebenhandlung,
Abfolge von Vorbereitung und Durchführung, und so weiter.
Sie können sich eine Plotlinie als eine Strecke vorstellen,
entlang derer Plotpunkte angeordnet sind, welche den Fortgang
der Handlung charakterisieren.
Solchen Plotpunkten können Abschnitte zugeordnet werden, um deren
Bedeutung für den Plot anzuzeigen.


-  *novelibre* lässt Sie eine beliebige Zahl von Plotlinien definieren.
-  Jeder Plotlinie können Sie beliebig viele Abschnitte zuordnen.
-  Jedem Abschnitt können Sie beliebig viele Plotlinien zuordnen.
-  Eine Plotlinie kann beliebig viele Plotpunkte umfassen.
-  Ein Plotpunkt kann höchstens einem Abschnitt zugeordnet werden.
-  Jedem Abschnitt können Sie beliebig viele Plotpunkte zuordnen.

Die Verbindung von Abschnitten und Plotpunkten ist in der Baumansicht
in der Spalte "Plotpunkte" zu sehen.

Sie können Plotlinien auch verwenden, um benannte Verbindungen wie z.B.
*Vorbereitung → Durchführung* oder *Ursache → Wirkung*
zwischen Abschnitten herzustellen, so dass Sie solche Beziehungen verfolgen
können, auch wenn die Abschnitte weit auseinanderliegen.

.. image:: _images/causality01.png
   :alt: Example

.. tip::
   Das `scap_novx <https://github.com/peter88213/scap_novx>`__-Werkzeug 
   kann ein neues *novelibre*-Projekt aus einem Plotentwurf
   mit Plotlinien und Plotpunkten erzeugen, der mit Hilfe des
   `Scapple <https://www.literatureandlatte.com/scapple/overview>`__ 
   Mindmappers erstellt wurde. 

   .. image:: _images/scapple_plot_lines.png
      :alt: Example


Handlungsraster (Plot grid)
---------------------------

*novelibres* `Handlungsraster
<plot_menu.html#handlungsraster-plot-grid-zum-bearbeiten-exportieren>`__
ist eine Tabelle mit einer Reihe pro Abschnitt und und einer
Zusammenstellung plotrelevanter Metadaten in den Spalten.
Die erste sichtbare Spalte enthält Querverweise auf die Abschnitte im
`Manuskript <export_menu.html#manuskript-zum-bearbeiten>`__.
Jede Plotlinie hat ihre eigene Spalte im Handlungsraster,
wo die `Plotliniennotizen <section_view.html#plotlinien>`__ zu sehen sind.
Das Handlungsraster bietet Ihnen einen bequemen Weg,
die Notizen zu den Plotlinien einzutragen und das Große Ganze
Ihrer Plotkonstruktion zu überblicken.


.. image:: _images/plot_grid01.png
   :alt: Example



.. hint::
   Sie können einen Abschnitt einer Plotlinie zuordnen,
   indem Sie Text in die entsprechende Zelle für die
   Plotliniennotizen eingeben. 
 
