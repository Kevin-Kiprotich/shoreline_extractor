from .package_installer import install_packages
try:
    import os
    import glob
    import natsort
    import rasterio
    from rasterio.plot import show
    import numpy as np
    import geopandas as gpd
    import matplotlib.pyplot as plt
    from matplotlib_scalebar.scalebar import ScaleBar
    from matplotlib.patches import Patch
    from shapely.ops import unary_union
    from .codes.shoreline import Create_points, ExtrapolateOut, ExtrapolateIn
    from .codes.shoreline import create_union_polygon, create_shoreline_change_points
    from .codes.shoreline import merge_shoreline_change, linearring_to_polygon
    from shapely.geometry import MultiPolygon, Polygon
    from qgis.PyQt.QtWidgets import QMessageBox
    
except ImportError:
    install_packages()
    
import warnings
warnings.filterwarnings("ignore")
from qgis.core import QgsProject,QgsVectorLayer
def addMapLayer(path):
    project = QgsProject.instance()
    filename=path.split('/')[-1][0:-5]
    layer=QgsVectorLayer(path,filename,'ogr')
    if layer.isValid():
        project.instance().addMapLayer(layer)
    else:
        print("Failed to load layer")
def check_file_structure(path, file_name):
    file_path = os.path.join(path, file_name)
    return os.path.exists(file_path) and os.path.isfile(file_path)
def show_error_message(message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()


def shoreline_analysis(dlg):
    try:
        #read combobox text
        shoreline_fp_1 = dlg.baselineShorelineComboBox.currentText()
        shoreline_fp_2=dlg.comparisonShorelineComboBox.currentText()
        # changeType=dlg.changeTypeComboBox.currentText()

        year1=int(dlg.baselineYearLineEdit.text())
        year2=int(dlg.comparisonYearLineEdit.text()) 
        total_years=year2-year1
        outputpath=dlg.outputSClineEdit.text()
        print(outputpath)
        #search for layernames marching the combobox text
        baseShoreline=QgsProject.instance().mapLayersByName(shoreline_fp_1)[0]
        comparisonShoreline=QgsProject.instance().mapLayersByName(shoreline_fp_2)[0]

        #obtain the directory and read each geojson with geopandas
        baseShoreline=baseShoreline.source().split('|')[0]
        comparisonShoreline=comparisonShoreline.source().split('|')[0]
        shl_past = gpd.read_file(baseShoreline).dropna().reset_index(drop=True)
        shl_present = gpd.read_file(comparisonShoreline).dropna().reset_index(drop=True)
        
        # Convert LinearRing to Polygon
        shl_past = linearring_to_polygon(shl_past)
        shl_present = linearring_to_polygon(shl_present)
        dlg.progressBar.setValue(20)
        
    
        erosion = gpd.overlay(shl_past, shl_present, how='difference', keep_geom_type=False)


        if check_file_structure(outputpath,"erosion.json"):
            raise PermissionError("erosion.json already exists")
        

        erosion.to_file(outputpath+'/erosion.json', driver='GeoJSON')
        addMapLayer(outputpath+'/erosion.json')
        

        if check_file_structure(outputpath,"accretion.json"):
            raise PermissionError("accretion.json already exists")
        

        accretion = gpd.overlay(shl_present, shl_past, how='difference', keep_geom_type=False)
        accretion.to_file(outputpath+'/accretion.json', driver='GeoJSON')
        addMapLayer(outputpath+'/accretion.json')
        # Export growth and retreat geometry to GeoJSON
        
        

        # # Create union polygon from geodata of growth area 
        accretion_poly = create_union_polygon(accretion)

        # # Create union polygon from geodata of retreat area 
        erosion_poly = create_union_polygon(erosion)

        # Create shoreline change as points along shoreline
        accretion_shoreline_change = create_shoreline_change_points(shl_present, accretion_poly)
        erosion_shoreline_change = create_shoreline_change_points(shl_present, erosion_poly)
        dlg.progressBar.setValue(40)


        # Export shoreline growth and retreat to GeoJSON
        if check_file_structure(outputpath,"accretion_points.json"):
            raise PermissionError("eccretion_points.json already exists")
        
        if check_file_structure(outputpath,"erosion_points.json"):
            raise PermissionError("erosion_points.json already exists")
        

        accretion_shoreline_change.to_file(outputpath+'/accretion_points.json', driver='GeoJSON')
        erosion_shoreline_change.to_file(outputpath+'/erosion_points.json', driver='GeoJSON')
        addMapLayer(outputpath+'/accretion_points.json')
        addMapLayer(outputpath+'/erosion_points.json')
        # Calculate total year
        # total_year = int(shoreline_fp[-1][-21:-17]) - int(shoreline_fp[0][-21:-17]) + 1

        # Create shoreline change
        change_distance = merge_shoreline_change(accretion_shoreline_change, erosion_shoreline_change)
        dlg.progressBar.setValue(80)
        shoreline_change = erosion_shoreline_change.drop(columns=['change_m'])
        shoreline_change['total change_m'] = change_distance
        shoreline_change['rate per year_m'] = (shoreline_change['total change_m']/total_years).round(2)
        # print(outputpath)


        # # Export shoreline change to GeoJSON
        if check_file_structure(outputpath,"shorelineChange.json"):
            raise PermissionError("shorelineChange.json already exists")
        

        shoreline_change.to_file(outputpath+'/shorelineChange.json', driver='GeoJSON')
        addMapLayer(outputpath+'/shorelineChange.json')
        dlg.progressBar.setValue(90)
        dlg.progressBar.setValue(100)
    
    except ValueError as error:
        if "Length of values" in str(error):
            show_error_message("There are no changes in the shoreline.")
        else:
            show_error_message("Unknown Error!! Please report this via the provided bug tracker in the plugins Manager")

    except PermissionError as error:
        show_error_message(str(error)+ "!! Delete the file or choose a different folder.")

