## Required Modules

For this application, you will need to add some additional modules not included.  You can load them using apt-get from the command line.  To download the modules, open the command line and type:

```
sudo apt-get update
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
sudo apt-get install python3-pyqt5
sudo apt-get install qtdeclarative5-*
sudo apt-get install qml-module-qtquick*
sudo apt-get install qtquickcontrols5-*
sudo apt-get install qml-module-qtquick2
sudo apt-get install python3-openpyxl
sudo pip3 install python-dateutil
sudo apt-get install python3-pyqt5.qtquick
```

## Required Modules

To start the program, open terminal, change director to the folder where the program is store using the CD command, and start the program with the following command.

```
sudo python3 main.py
```

## Customization

The Graphical User Interface(GUI) is written in a QT5 and is implemented using python and the PyQT5 library.  Don't worry if that doesn't mean anything to you.  QT has a free [community edition](https://www.qt.io/download) that makes it easy to change the layout or look of the GUI. You make changes by opening and editing the QML file in QT creator.  For some reason, QT creator designer tab does not like the Connections section of the QML file.  A simple solution is to cut the Connections section out, open the designer tab, and then past the connections back into the code.  

You will probably want to customize the application to your car and voltage.  The easily modified vector images are stored in the /svg images folder.  You can modify them directly.  However, it is easier to modify the vector images that were used to produce the .png files.  These files can be found in the /vector images folder.  I used the GNU program [Inkskape](https://inkscape.org/en/) to create the gauges.  Using a vector program you can easily change the text on the gauge faces, the color, or the rings.

If you need change the range of a gauge, you will need to recalibrate the gauge to your new values by modifying the QML file..  This is done in the function section of the code.  Below is an example of the sweep of the Auxiliary voltage gauge.

```
    function auxangle(value)
    {
        if (value <= 7){
            return -48
        }

        if (value >= 17){
            return 229
        }
        return ((value*27.7)-241.9)
```

The first value, in this example 7, is the lowest value on the face.  It correlates to a needle rotation of -48 degrees.  The second value, 17 in this example is the highest value on the face.  On this gauge that correlates to 229 degrees.  The last statement is the most important.  It is how the rotation is calculated for any value between the high and low numbers on the gauge face.  The divisions on the gauge face are all equal.  As a result we can draw a line between the two points.  You might recognize the formula y=mx+b from math class.  Solving for the equation of the line allows us to calculate the function that returns an angle for a given value.
