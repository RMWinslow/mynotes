---
title: Importing Inkscape land shapes into QGIS
categories: online
tags:
  - computers
  - mapping
  - hobby
  - art
---

There are lots of guides online for taking a QGIS map, exporting it to a vector format, and then using Inkscape to clean it up and make it pretty. 
But I want to do the opposite. I want to take a vector map outline which I designed in Inkscape and import it into QGIS so that I can annotate it with city labels and other information.


## In Inkscape

1. Clean up your file 
    - Simplest if you just have the shapes you want to import on a single layer with nothing else in the svg file.
2. Save the file as a .dxf file.
    - Inkscape calls this file format `Desktop Cutting Plotter`
    - .dxf files are AutoCAD's `Drawing Exchange Format`, and designed for interoperability between software.
        - This is the only vector file format that I've gotten QGIS to reliably read.




## In QGIS

1. Create a new project
    - If you are making a discworld and want to use the built-in coordinate systems, then in project properties, set the CRS to North_Pole_Azimuthal_Equidistant.
    - If you're not going to use the geodata, and just want a handy labelling database, just use Cartesian or whatever. It doesn't matter.
3. Import your .dxf file as a new vector layer.
    - `Layer > Add Layer > Add Vector Layer` or press `Ctrl+Shift+V` 
    - Source Type `file`, encoding `automatic`, browse for the file in the Vector Dataset dialogue.
    - Then click Add. Sometimes it will import extra stuff, but what you want is the layer made of LINES
    - Right-click the layer after importing and set the layer CRS
4. Now we need to convert the imported line layer into a nice clean polygon layer
   1. Open the Processing Toolbox sidebar
        - `Processing > Toolbox` or press `Ctrl+Alt+T` 
        - This is where we will search for the processing steps we need later.
   2. Fix the geometry
        - Make sure you have the imported lines selected in the Layers pane.
        - Search for `Fix geometries` in the Processing Toolbox and double-click on that option, then click `Run`
        - This will make a new temporary layer called `Fixed geometries`
   3. Polygonize the Lines
        - Make sure you have the `Fixed geometries` layer selected in the Layers pane.
        - Search for `Polygonize` in the Processing Toolbox.
        - Choose the option under the `Vector Geometry` header, *not* the one under `Raster Conversion`.
        - Double-click and run. It might take a while.
        - This will make a new temporary layer called `Polygons`
   4. Finalize the imported Polygon layer
        - In the layers dialogue, right-click on the `Polygons` layer and click `Make Permanent`. Give it a name and click OK. 
            - If you don't do this, the layer will be disacarded when you exit QGIS
        - Rename the layer to something descriptive.
        - If you double-click on the layer, it will open a dialogue where you can do things like edit the styles.


If you've lost your map, right-click on the layer and choose `Zoom to Layer`

