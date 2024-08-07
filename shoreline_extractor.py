# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AutomaticShorelineExtraction
                                 A QGIS plugin
 This plugin enables the user to automatically extract shorelines and compute shoreline change rates.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-09-07
        git sha              : $Format:%H$
        copyright            : (C) 2023 by LocateIT
        email                : cogeos@locateit.co.ke
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os
import sys
ext_libs_path = os.path.join(os.path.dirname(__file__), 'ext-libs')
if ext_libs_path not in sys.path:
    sys.path.append(ext_libs_path)
else:
    count = sys.path.count(ext_libs_path)
    for i in range(count):
        sys.path.remove(ext_libs_path)
    sys.path.append(ext_libs_path)
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, QDate
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QFileDialog,QMessageBox

from qgis.core import QgsProject, Qgis, QgsVectorLayer, QgsRasterLayer, QgsMapLayerType, QgsApplication
from qgis.analysis import QgsNativeAlgorithms

# Initialize Qt resources from file resources.py
from .package_installer import install_packages
from .resources import *
# Import the code for the dialog
from .shoreline_extractor_dialog import AutomaticShorelineExtractionDialog
import os.path
# from .shoreline_extraction import auto_extract_shorelines

try:
    from .shoreline_change import shoreline_analysis
    from .SAR_Shoreline_Extractor import extract_SAR_Shoreline
    # from .imagedownloader import download_image
except ImportError:
    install_packages()

import subprocess

class AutomaticShorelineExtraction:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'AutomaticShorelineExtraction_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Call the function to install packages when the plugin is loaded
        # self.install_required_packages()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&CoGEOS ')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('AutomaticShorelineExtraction', message)
    
    def install_required_packages(self):
        # Check the Python version
        if sys.version_info < (3, 8):
            print("This plugin requires Python 3.8 or higher.")
            print("You are currently using Python", sys.version)
            print("Please upgrade your Python version to 3.8 or higher.")
        else:
            print("Python version is compatible.")
            try:
                # Get the path to the bundled requirements.txt file
                # requirements_file_path = os.path.join(self.plugin_dir, 'requirements.txt')
                
                #list of packages to install
                packages_to_install = ['folium', 'rasterio', 'rtree', 'pandas', 'geopandas', 'geemap', 'mapclassify', 'contextily', 'matplotlib_scalebar', 'opencv-python', 'natsort', 'scikit-learn']

                # Iterate through the list and install each package
                for package in packages_to_install:
                    try:
                        subprocess.check_call(['pip', 'install', package])
                        print(f"Successfully installed {package}")
                    except subprocess.CalledProcessError as e:
                        print(f"Error installing {package}: {str(e)}")
            except Exception as e:
                print(f"Error installing required packages: {str(e)}")


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str
        QgsProject.instance().layerWillBeRemoved.connect(self.getLayers())
            QgsProject.instance().layerLoaded.connect(self.getLayers())
        
        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/shoreline_extractor/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'CoGEOS Toolkit'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&CoGEOS '),
                action)
            self.iface.removeToolBarIcon(action)

    """
        Get the active tabs
        for selection of processes to run
    """
    def get_active_tab(self):
        major_tab_name=self.dlg.shorelineExtractionWidget.tabText(self.dlg.shorelineExtractionWidget.currentIndex())
        if major_tab_name == "Image Downloader":
            return major_tab_name
        elif major_tab_name == "Extract Shoreline":
            current_tab_name=self.dlg.shorelineChange.tabText(self.dlg.shorelineChange.currentIndex())
            return current_tab_name
    def show_error_message(self,message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()
    ## function to run the processes
    def process(self):
        #check the current tab

        major_tab_name=self.dlg.shorelineExtractionWidget.tabText(self.dlg.shorelineExtractionWidget.currentIndex())

        if major_tab_name == "Image Downloader":
            print(major_tab_name)
            if self.dlg.DownloadOutputLineEdit.text() =="":
                self.show_error_message("Provide Output Path")
            else:
                pass
                # download_image(self.dlg)

        elif major_tab_name == "Extract Shoreline":
            current_tab_name = self.dlg.shorelineChange.tabText(self.dlg.shorelineChange.currentIndex())
            if current_tab_name == "Automatic Shoreline Extraction":
                print('tab 1')
                if self.dlg.outputASElineEdit.text()=="":
                    self.show_error_message("Provide Output Path")
                else:
                    pass
                    # auto_extract_shorelines(self.dlg,self.getLayers())
            elif current_tab_name == "Shoreline Change":
                if self.dlg.outputSClineEdit.text()=="":
                    self.show_error_message("Provide Output Path")
                else:
                    shoreline_analysis(self.dlg)
            elif current_tab_name == "Shoreline Extraction (SAR Sentinel-1)":
                extract_SAR_Shoreline(self.dlg)

    def getBandCount(self):
        rasterlayerName=self.dlg.inputRasterASECombobox.currentText()
        layers=QgsProject.instance().mapLayersByName(rasterlayerName)
        if layers:
            selectedRasterLayer=layers[0]
            num_bands=selectedRasterLayer.bandCount()

            self.dlg.rasterBandASEComboBox.clear()
            self.dlg.rasterBandASEComboBox.addItems([str(num) for num in range(1,num_bands+1)])

            return num_bands
    def refresh(self):
        self.dlg.baselineShorelineComboBox.clear()
        self.dlg.comparisonShorelineComboBox.clear()
        self.dlg.BoundComboBoxSAR.clear()
        self.dlg.DownloadOutputLineEditSAR.clear()
        self.dlg.DownloadStartDateEditSAR.setDate(QDate.currentDate())
        self.dlg.DownloadEndDateEditSAR.setDate(QDate.currentDate())
        self.dlg.progressBar.setValue(0)
        self.dlg.baselineYearLineEdit.clear()
        self.dlg.comparisonYearLineEdit.clear()
    def getLayers(self):
        # Fetch the currently loaded layers
        layers = QgsProject.instance().mapLayers().values()
        # Get only raster layers
        major_tab_name=self.dlg.shorelineExtractionWidget.tabText(self.dlg.shorelineExtractionWidget.currentIndex())
        current_tab_name = self.dlg.shorelineChange.tabText(self.dlg.shorelineChange.currentIndex())

        layer_list=""
        if major_tab_name == "Image Downloader":
            # print(major_tab_name)
            vector_layers=[layer for layer in layers if layer.type() == QgsMapLayerType.VectorLayer and layer.dataProvider().name()=='ogr']
            layer_list=vector_layers
            self.dlg.BoundComboBox.addItems([layer.name() for layer in vector_layers])
            self.dlg.baselineShorelineComboBox.addItems([layer.name() for layer in vector_layers])
            self.dlg.comparisonShorelineComboBox.addItems([layer.name() for layer in vector_layers])
            self.dlg.BoundComboBoxSAR.addItems([layer.name() for layer in vector_layers])
        elif major_tab_name == "Extract Shoreline":

            if current_tab_name == "Automatic Shoreline Extraction":
                raster_layers = [layer for layer in layers if layer.type() == QgsMapLayerType.RasterLayer and layer.dataProvider().name()=='gdal']
                layer_list=raster_layers
                self.dlg.inputRasterASECombobox.addItems([layer.name() for layer in raster_layers])

            elif current_tab_name == "Shoreline Change":
                # Filter the layers to only include GeoJSON vector layers
                geojson_layers = [layer for layer in layers if layer.type() == QgsMapLayerType.VectorLayer and layer.dataProvider().name()=='ogr']
                self.dlg.baselineShorelineComboBox.addItems([layer.name() for layer in geojson_layers])
                self.dlg.comparisonShorelineComboBox.addItems([layer.name() for layer in geojson_layers])
                self.dlg.BoundComboBoxSAR.addItems([layer.name() for layer in geojson_layers])
                layer_list=geojson_layers
            elif current_tab_name == "Shoreline Extraction (SAR Sentinel-1)":
                geojson_layers = [layer for layer in layers if layer.type() == QgsMapLayerType.VectorLayer and layer.dataProvider().name()=='ogr']
                self.dlg.baselineShorelineComboBox.addItems([layer.name() for layer in geojson_layers])
                self.dlg.comparisonShorelineComboBox.addItems([layer.name() for layer in geojson_layers])
                self.dlg.BoundComboBoxSAR.addItems([layer.name() for layer in geojson_layers])
            return layer_list
    
    def select_output_folder(self):
        active_tab_name=self.get_active_tab()
        output_dir_name = QFileDialog.getExistingDirectory(None, "Select a directory", "")
        if active_tab_name == "Image Downloader" and output_dir_name.strip() != "":
            self.dlg.DownloadOutputLineEdit.setText(output_dir_name)
        elif active_tab_name == "Automatic Shoreline Extraction" and output_dir_name.strip() != "":
            self.dlg.outputASElineEdit.setText(output_dir_name)
        elif active_tab_name == "Shoreline Change" and output_dir_name.strip() != "":
            self.dlg.outputSClineEdit.setText(output_dir_name)
        elif active_tab_name == "Shoreline Extraction (SAR Sentinel-1)":
            self.dlg.DownloadOutputLineEditSAR.setText(output_dir_name)

    # def browseOutputClicked(self):
    #     output_dir_name = QFileDialog.getExistingDirectory(None, "Select a directory", "")
    #     self.dlg.outputSClineEdit.setText(output_dir_name)
        # options = QFileDialog.Options()
        # file_path, _ = QFileDialog.getSaveFileName(self.dlg, "Shoreline Change Output", "", "geojson (*.json);;All Files (*)", options=options)

        # if file_path:
        #     self.dlg.outputSClineEdit.setText(file_path)
    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = AutomaticShorelineExtractionDialog()
            self.dlg.button_box.accepted.disconnect()
            self.dlg.button_box.accepted.connect(self.process)
            # self.dlg.browseOutputFolder.clicked.connect(self.select_output_folder)
            # self.dlg.inputRasterASECombobox.currentIndexChanged.connect(lambda: self.getBandCount())
            self.dlg.shorelineChange.currentChanged.connect(self.getLayers)
            self.dlg.openFolder_2.clicked.connect(self.select_output_folder)
            # self.dlg.browseOutputDownload.clicked.connect(self.select_output_folder)
            self.dlg.browseOutputSAR.clicked.connect(self.select_output_folder)
            # QgsProject.instance().layerWillBeRemoved.connect(self.getLayers)
            QgsProject.instance().layerLoaded.connect(self.getLayers)
        
        shorelineChangeType=['accresion','erosion']
        # # Clear the contents of the comboBox from previous runs
        # self.dlg.inputRasterASECombobox.clear()
        # self.dlg.rasterBandASEComboBox.clear()
        # self.dlg.changeTypeComboBox.clear()
        # self.dlg.changeTypeComboBox.addItems([item for item in shorelineChangeType])
        self.refresh()
        self.getLayers()
        
        # self.dlg.inputBaselineRastercomboBox.clear()
        # self.dlg.inputComparisonRastercomboBox.clear()


        # show the dialog
        self.dlg.show()
        