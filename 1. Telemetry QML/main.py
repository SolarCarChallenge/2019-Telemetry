import sys
import serial
from io import StringIO
import csv
from openpyxl import Workbook, load_workbook
import datetime
from dateutil.parser import parse
import time
import psycopg2

from PyQt5.QtCore import QCoreApplication, Qt, QUrl
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from PyQt5.Qt import QStringListModel





ampHourvalue=0
batteryCapacity=100


# Create an instance of the application
app = QGuiApplication(sys.argv)
# Create QML engine
engine = QQmlApplicationEngine()



class Dash(QObject):

    #create the signals that change the GUI     
    auxVoltage = pyqtSignal(float, arguments=['auxvolt'])
    mainVoltage = pyqtSignal(float, arguments=['mainvolt'])
    mainCurrent = pyqtSignal(float, arguments=['maincur'])
    carSpeed = pyqtSignal(float, arguments=['speedmph'])
    ampHour = pyqtSignal(float, arguments=['amphr'])
    motorTemp = pyqtSignal(float, arguments=['tempval'])
    
    @pyqtSlot()
    def reset(self):
        global ampHourvalue
        global batteryCapacity  
        ampHourvalue=batteryCapacity #put amp hour capacity here
        self.ampHour.emit(ampHourvalue)
   
    
    @pyqtSlot(str)
    def set(self,value):   #allows the user to update the amphour counter
        global ampHourvalue  #pulls in global variable
        ampHourvalue=float(value)  #converts value from string to number
        self.ampHour.emit(ampHourvalue)  #sends the signal to update display.

# create a dashboard object
dashboard = Dash()



        
class ThreadClass(QThread):
    # Create the signal
    auxVoltage = pyqtSignal(float, arguments=['auxvolt'])
    mainVoltage = pyqtSignal(float, arguments=['mainvolt'])
    mainCurrent = pyqtSignal(float, arguments=['maincur'])
    carSpeed = pyqtSignal(float, arguments=['speedmph'])
    ampHour = pyqtSignal(float, arguments=['amphr'])
    motorTemp = pyqtSignal(float, arguments=['tempval'])


    def opendb(self):
        try:
            self.conn = psycopg2.connect(
                        dbname='dd1bpvtvs1alq3',
                        user='zfguszkndowgtn',
                        password='e41a639c9f4a37a400efbc5940ae418fee0c16f37648522b5f0b1c28abfa7a88',
                        host='ec2-54-227-246-152.compute-1.amazonaws.com',
                        port='5432')
            print("connected")
            self.cur = self.conn.cursor()
        except:
            print("I am unable to connect to the database.")
        

    
    
    
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)     
        
        #connects the signals from the thread to the object
        self.auxVoltage.connect(dashboard.auxVoltage)
        self.mainVoltage.connect(dashboard.mainVoltage)
        self.mainCurrent.connect(dashboard.mainCurrent)
        self.carSpeed.connect(dashboard.carSpeed)
        self.ampHour.connect(dashboard.ampHour)
        self.motorTemp.connect(dashboard.motorTemp)

        


    def run(self):
        #This implementation of amp hours needs work
        global ampHourvalue  
        global batteryCapacity
        
        
        self.opendb()
        
        
        
        while True:

            comm="SELECT * from public.solardata"    
            self.cur.execute(comm)
            lastrow=self.cur.rowcount

            
            comm=("SELECT * from public.solardata WHERE id = %s" %(lastrow))
            print(comm)
            
            self.cur.execute(comm)
            dataset=self.cur.fetchone()

            
            #extract individual data points
            timestamp=(dataset[1])
            auxvalue=float(dataset[6])
            mainvalue=float(dataset[7])
            currentvalue=float(dataset[8])
            speedvalue=float(dataset[5])
            ampHourvalue=float(dataset[10])
            motortempvalue=float(dataset[9])
            
            #round to two desimal places
            auxvalue=round(auxvalue,2)
            mainvalue=round(mainvalue,2)
            currentvalue=round(currentvalue,2)
            speedvalue=round(speedvalue,2)
            ampHourvalue=round(ampHourvalue,3)
            motortempvalue=round(motortempvalue,2)
            
 
            # Emit the signals
            self.auxVoltage.emit(auxvalue)
            self.mainVoltage.emit(mainvalue)
            self.mainCurrent.emit(currentvalue)
            self.carSpeed.emit(speedvalue)
            self.ampHour.emit(ampHourvalue)
            self.motorTemp.emit(motortempvalue)

            
            time.sleep(2)

            
        pass       








    # register it in the context of QML
    engine.rootContext().setContextProperty("dashboard", dashboard)
    #load qml file into engine
    engine.load(QUrl('main4.qml'))


    
threadclass=ThreadClass()
threadclass.start()

engine.quit.connect(app.quit)
sys.exit(app.exec_())
app.exec_()
