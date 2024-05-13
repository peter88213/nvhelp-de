Extras-Menü
===========

**Vermischte Funktionen**

.. figure:: _images/tools_menu02.png
   :alt: novelibre Screenshot

.. note:: 
   The *Extras*-Menü can be extended by plugins to add more
   features.

Plugin manager
--------------

**Die installierten Plugins anzeigen und verwalten**

Mit **Extras > Plugin manager**
kann man den *Installierte Plugins*-Dialog öffnen.

.. figure:: _images/tools_menu01.png
   :alt: novelibre Screenshot

-  Successfully installed plugins are displayed black on white by
   default.
-  Outdated plugins are grayed out.
-  Plugins that cannot run are displayed in red, with an error message.

How to update a plugin
   1. Select the plugin you want to update. If the **Homepage** Schaltfläche is
      activated kann man click on it, and your system browser opens the plugin
      Homepage. Otherwise, you have to know the source of the plugin yourself.
   2. Gehe zu the plugin Homepage and download the latest release. Install it
      according to the instructions.

How to uninstall a plugin
   Select the plugin, and click on the **Löschen** Schaltfläche.

.. admonition:: About version compatibility
    
   On the window frame, you see the *novelibre* version, consisting of
   three numbers that are separated by points.
   
   ``<major version number>.<minor version number>.<patch level>``
   
   In the **novelibre API** column, you see the plugin’s compatibility
   information, consisting of two numbers that are separated by points.
   
   ``<major version number>.<minor version number>``
   
   The rule for compatibility
      -  The plugin’s *novelibre API* major version number must be the same as
         *novelibre’s* major version number.
      -  The plugin’s *novelibre API* minor version number must be less than
         or equal to *novelibre’s* minor version number.
   
   Fix incompatibilities
      -  If the plugin’s *novelibre API* major version number is greater than
         *novelibre’s* major version number, *novelibre* needs to be updated.
      -  If the plugin’s *novelibre API* major version number is less than
         *novelibre’s* major version number, the plugin needs to be updated.
      -  If the plugin’s *novelibre API* minor version number is greater than
         *novelibre’s* minor version number, *novelibre* needs to be updated.


Installationsordner öffnen
--------------------------

**Die Dateiverwaltung aufrufen**

Mit **Extras > Installationsordner öffnen**
kann man den *novelibre*-Installationsordner im Dateimanager öffnen.
This might come in handy if you wish to edit configuration files,
or install your own plugins.

