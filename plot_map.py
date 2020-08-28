# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:42:55 2020

@author: priya
"""

from qgis.core import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import osgeo
import glob
from datetime import datetime
from qgis.gui import *
import subprocess
from math import ceil
from qgis.utils import iface

def exportMap(in_file, dist_file, state_name, epsg_code = 3857):
    
    # remove the vector and raster layers already added
    p = QgsProject.instance()
    p.removeAllMapLayers()
    
    # Set the installation directory of qgis as prefix path
    QgsApplication.setPrefixPath("/usr", True)
    
    # Intialize the map canvas
    canvas = QgsMapCanvas()
    
    # Set the projection information to one variable
    qgis_crsid = QgsCoordinateReferenceSystem.EpsgCrsId
    crs = QgsCoordinateReferenceSystem(epsg_code, qgis_crsid)

    # Read vector layer and set crs
    dist = QgsVectorLayer(dist_file, 'DISTRICT', 'ogr')
    dist.setCrs(crs)

    # Read raster layer and set the layername as baseName
    in_data = QgsRasterLayer(in_file, baseName)
    in_data.setCrs(crs)
    vec_data = QgsVectorLayer(dist_file,baseName)
    vec_data.setCrs(crs)
    # Add layers to the Qgis map registry
    p.addMapLayer(in_data)
    p.addMapLayer(vec_data)
   
    #p.addMapLayer(dist) 
    
    # Load the layer styles
    in_data.loadNamedStyle(ras_uri)
    dist.loadNamedStyle(dist_uri)
    
    
    #vector_canvas_layer = QgsMapCanvas(vector_layer)
    
    # Add layers to the map canvas
    layers = [in_data]
    canvas.setLayers(layers)
        
    veclayers = [vec_data]
    canvas.setLayers(veclayers)
    veclayers.insert(0, canvas)
    
    # Zoom the canvas to extent of all layers
    
    canvas.zoomToFullExtent()
    paperSize = [270,200]

   # Set margins and paper size right
    lm = 12         # left margin
    tm = 20         # upper margin
    bm = 20         # lower margin
    
    # add map
    x, y = lm, tm
    w, h = paperSize[0] - 2 * lm, paperSize[1] - bm

    # Create a maprender and by default it take layers from canvas
    mapSettings = canvas.mapSettings()
    #get a reference to the layout manager
    manager = p.layoutManager()
    #add layout to manager
    # Create the new Qgis Layout
    c = QgsPrintLayout(p)
    c.initializeDefaults()
    
#    cosmetic
    page = c.pageCollection().pages()[0]
    page.setPageSize(QgsLayoutSize(paperSize[0],paperSize[1]))
    manager.addLayout(c) 
    out_map = QgsLayoutItemMap(c)
    out_map.setCrs(crs)
   
    
   # adding grid
    out_map.setExtent(canvas.extent())
    qgs_layout_item_map_grid = QgsLayoutItemMapGrid("New grid",out_map)
    out_map.attemptSetSceneRect(QRectF(x, y, w, h))
    out_map.setFrameEnabled(True)
    
    # Extent
    #ext = canvas.extent()
    rectangle = QgsRectangle(canvas.extent())
    #rectangle = QgsRectangle(71.918, 10.978, 81.422, 19.059) #canvas.extent()  
    out_map.setExtent(rectangle)
    c.addLayoutItem(out_map)
    out_map.attemptMove(QgsLayoutPoint(1.502,0.944, QgsUnitTypes.LayoutCentimeters))
    out_map.attemptResize(QgsLayoutSize(19.917,18.764, QgsUnitTypes.LayoutCentimeters))
    c.addLayoutItem(out_map)
    
    #map layout property
    qgs_layout_item_map_grid.setAnnotationPrecision(0)
    qgs_layout_item_map_grid.setAnnotationFrameDistance(1)
    qgs_layout_item_map_grid.setAnnotationEnabled(True)
    qgs_layout_item_map_grid.setAnnotationFormat(QgsLayoutItemMapGrid.DegreeMinutePadded)
    qgs_layout_item_map_grid.setCrs(QgsCoordinateReferenceSystem(4326))
    qgs_layout_item_map_grid.setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Right)
    qgs_layout_item_map_grid.setAnnotationDirection( QgsLayoutItemMapGrid.Vertical,QgsLayoutItemMapGrid.Left)
    qgs_layout_item_map_grid.setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Top)
    grid_interval = 0.0005
    qgs_layout_item_map_grid.setIntervalX(grid_interval)  
    qgs_layout_item_map_grid.setIntervalY(grid_interval) 
    out_map.setEnabled(True)
    qgs_layout_item_map_grid.setStyle(QgsLayoutItemMapGrid.FrameAnnotationsOnly)
    qgs_layout_item_map_grid.setFrameStyle(QgsLayoutItemMapGrid.ExteriorTicks)
    qgs_layout_item_map_grid.setFrameSideFlag(QgsLayoutItemMapGrid.FrameRight, False)
    qgs_layout_item_map_grid.setFrameSideFlag(QgsLayoutItemMapGrid.FrameTop, False)
    out_map.grids().addGrid(qgs_layout_item_map_grid)
    c.addLayoutItem(out_map) 

    #Putting Scale
    item = QgsLayoutItemScaleBar(c)
    item.setLinkedMap(out_map)
    item.setStyle('Double Box') # optionally modify the style
    item.applyDefaultSize()
    item.setNumberOfSegmentsLeft(0)
    item.setNumberOfSegments (3)
    item.attemptMove(QgsLayoutPoint(23, 18.5, QgsUnitTypes.LayoutCentimeters))
    item.setMapUnitsPerScaleBarUnit(1)
    item.setUnitLabel('m')
    item.update()
    c.addItem(item)
    
    #set label
    
    in_file_bs = os.path.basename(in_file)
    date_label =  in_file_bs[4:6]+ '-'+ in_file_bs[4:6] + '-' + in_file_bs[:4] 
    label = QgsLayoutItemLabel(c)
    label.setText(date_label)
    label.setFont(QFont("Arial",18))
    label.adjustSizeToText() 
    label.attemptMove(QgsLayoutPoint(24, 4.5, QgsUnitTypes.LayoutCentimeters))
    c.addItem(label)
   
    #adding north arrow
    picture= QgsLayoutItemPicture(c)
    picture.setPicturePath(nArrow_png)
    picture.attemptMove(QgsLayoutPoint(24.5,0.524, QgsUnitTypes.LayoutCentimeters))
    picture.attemptResize(QgsLayoutSize(2.201,3.005, QgsUnitTypes.LayoutCentimeters))
    c.addLayoutItem(picture)
    
    #add date
    dateLabel = QgsLayoutItemLabel(c)
    d = time.localtime()
    dString = "%d-%d-%d" % (d[2],  d[1],  d[0])
    dateLabel.setText(dString)
    textFont = QFont("Arial", 25)  
    dateLabel.attemptMove(QgsLayoutPoint(17.5,0.63, QgsUnitTypes.LayoutCentimeters))
    dateLabel.setFont(textFont)
    dateLabel.adjustSizeToText()
    dateStringWidth = dateLabel.sizeForText().width()
    c.addItem(dateLabel)
                                                     
    #adding legend
    legend= QgsLayoutItemPicture(c)
    legend.setPicturePath(legend_png) 
    legend.attemptMove(QgsLayoutPoint(24, 6.325, QgsUnitTypes.LayoutCentimeters))
    legend.attemptResize(QgsLayoutSize(4.612, 11.111, QgsUnitTypes.LayoutCentimeters))
    c.addLayoutItem(legend)

    canvas.show()
    # Save image in png format
    exporter = QgsLayoutExporter(c)
    exporter.exportToImage( out_dir+date_label+".png",QgsLayoutExporter.ImageExportSettings())  
    
    
    ''' Function to publish maps into wordpress '''
if __name__ == '__main__':
    in_file = "path of input raster"
    # Load vector and raster layer using qml style
    dist_uri = 'style file'
    ras_uri = 'style file'
    out_dir = "output fig location "
    nArrow_png = "north arrow image"
    baseName = 'Name'
    composer_label = 'name'

    # Function to export the map as image    
    
    dist_file = 'vector file'
    state_name = 'Name'
    qgs = QgsApplication([], False)
    qgs.initQgis()
    
    imgFile = exportMap(in_file, dist_file, state_name)

    # Exit the qgis application
    qgs.exitQgis()