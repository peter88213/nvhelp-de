Extras-Menü
===========

**Vermischte Funktionen**

.. note:: 
   Das *Extras*-Menü kann durch Plugins um zusätzliche Funktionen erweitert werden.

Pluginmanager
-------------

**Die installierten Plugins anzeigen und verwalten**

Mit **Extras > Plugin manager**
können Sie den *Installierte Plugins*-Dialog öffnen.

.. figure:: _images/tools_menu01.png
   :alt: novelibre Screenshot

- Erfolgreich installierte Plugins werden standardmäßig schwarz auf weiß dargestellt.
- Veraltete Plugins werden ausgegraut.
- Plugins, die nicht funktionieren, werden zusammen mit einer Fehlermeldung in roter
  Schrift dargestellt.

Wie Sie ein Plugin aktualisieren
   1. Wählen Sie das Plugin aus, das Sie aktualisieren wollen.
      Falls die **Homepage**-Schaltfläche aktiviert ist,
      können Sie darauf klicken, und Ihr System-Webbrowser öffnet die Homepage.
      Andernfalls müssen Sie die Quelle des Plugins selbst kennen.
   2. Gehen Sie zur Plugin-Homepage und laden Sie die neueste Version herunter.
      Installieren Sie das Plugin gemäß Anleitung.

Wie Sie ein Plugin deinstallieren
   Wählen Sie das Plugin aus und klicken Sie auf die **Löschen**-Schaltfläche.

.. admonition:: Über die Kompatibilität von Versionen
    
   Auf dem Fensterrahmen sehen Sie die Version von *novelibre*, 
   die aus drei Zahlen besteht, die durch Punkte getrennt sind.
   
   ``<Hauptversionsnummer>.<Nebenversionsnummer>.<Patchlevel>``
   
   In der Spalte **novelibre API** sehen Sie die Kompatibilitätsinformation
   des Plugins, die aus zwei zurch einen Punkt getrennte Zahlen besteht.
   
   ``<Hauptversionsnummer>.<Nebenversionsnummer>``
   
   Die Regel für die Kompatibilität
      - Die *novelibre API*-Hauptversionsnummer des Plugins muss mit der
        Hauptversionsnummer von *novelibre* übereinstimmen.
      - Die *novelibre API* Nebenversionsnummer des Plugins muss kleiner
        oder gleich wie die Nebenversionsnummer von *novelibre* sein.
   
   Inkompatibilität beheben
      - Wenn die *novelibre API*-Hauptversionsnummer des Plugins größer
        als die Hauptversionsnummer von *novelibre* ist,
        muss *novelibre* aktualisiert werden.
      - Wenn die *novelibre API*-Hauptversionsnummer des Plugins kleiner
        als die Hauptversionsnummer von *novelibre* ist,
        muss das Plugin aktualisiert werden.
      - Wenn die *novelibre API* Nebenversionsnummer des Plugins größer
        als die Nebenversionsnummer von *novelibre* ist,
        muss *novelibre* aktualisiert werden.


Installationsordner öffnen
--------------------------

**Die Dateiverwaltung aufrufen**

Mit **Extras > Installationsordner öffnen**
können Sie den *novelibre*-Installationsordner im Dateimanager öffnen.
Das kann praktisch sein, wenn Sie Konfigurationsdateien bearbeiten
oder eigene Plugins installieren wollen.

