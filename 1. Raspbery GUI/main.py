from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import time
import os

import time      #time
import board    
import busio
import adafruit_mcp9808
import adafruit_gps
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import serial
import psycopg2
from tkinter.constants import CENTER

global RunTelem
RunTelem=None


#this class sets up the unser interface for the PI
class User_Interface(tk.Frame):
    
    #called when the class is created
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        
        #define some variables
        self.fontize=30
        self.entrywidth=10
        self.leftframecolor='grey82'
        self.fontstyle="Helvetica"
        self.operator=""
        
        #opens the file contianing the cumulative amphours
        try:
            self.amphourstorage=open('amphour.txt','r')
            self.amphour=float(self.amphourstorage.read())
            self.amphourstorage.close()
        except:
            self.amphour=0
        
        
        #calls the function to lay out the windows for the GUI
        self.configure_gui()
        
        #lays out the cunctions of the gui
        self.layout_gui()

        
    def configure_gui(self):
        #recongigure master window to fit screen
        self.master.title("Solar Car Challenge")
        self.master.geometry("800x460+0+0")
        self.master.resizable(width=False, height=False)
        
    
    
    #function executes a safe shutdown of the Pi
    def shutdown(self):
        print("Goodbye")
        os.system("shutdown now -h")
    
    #creates the pop up window to confirm shutdown to prevent accidental shutdown
    def shutdownconfirm(self):
        self.confirmwin= tk.Toplevel()
        self.confirmwin.wm_title("Shutdown")
        self.confirmwin.geometry("800x400+0+0")
        self.confirmwin.config(bg='red')
        
        a=Label(self.confirmwin, text = 'Confirm Shutdown', font=(self.fontstyle, 40), bg=self.leftframecolor, justify=CENTER)
        a.grid(sticky='we')
        a.grid(row=0, column=0, columnspan=2, sticky=W+E+N+S, padx=1, pady =1)
        
        
        self.confirmwin.grid_columnconfigure(0, weight=1)
        self.confirmwin.grid_columnconfigure(1, weight=1)
        self.confirmwin.grid_rowconfigure(0, weight=1)
        self.confirmwin.grid_rowconfigure(0, weight=3)
        
        
        but1=Button(self.confirmwin,padx=15,pady=30,bd=4,bg='white',command=self.shutdown,text="Yes",font=(self.fontstyle, 40))
        but1.grid(row=1, column=0,sticky=W+E+N+S, padx=1, pady =1)

        
        but2=Button(self.confirmwin,padx=15,pady=30,bd=4,bg='white',command=self.confirmwin.destroy,text="No",font=(self.fontstyle, 40))
        but2.grid(row=1, column=1,sticky=W+E+N+S, padx=1, pady =1)
        
        
    
    
    #starts running the program to aquire data and sets the run variable to true
    def SetTrue(self):
        global RunTelem
        RunTelem=True
        print("Starting Telemetry")
        print("Run Telem=",RunTelem)
        self.startbutton.config(bg='green', text="Running")
        
        Cardata.aquire()
        
    #stops the data acquistion program by setting run variable to false    
    def SetFalse(self):
        global RunTelem
        RunTelem=False
        print("Stopping Telemetry")
        print("Run Telem=",RunTelem)
        self.startbutton.config(bg=self.leftframecolor, text="Start")

    #part of the amp our update that takes the input number and adds to the the total
    def clickbut(self,number):   #lambda:clickbut(1)
        self.operator=self.operator+str(number)
        self.textin.set(self.operator)
        
    #function the rights amphours to file
    def setamphour(self):
        self.amphourstorage=open('amphour.txt','w')
        self.amphourstorage.write(self.operator)
        self.amphourstorage.close()
        self.amphourdatadatavariable.set(self.operator)
        self.win.destroy()

        
    #pop up window to enter amphours    
    def popupwindow(self):
        self.win= tk.Toplevel()
        self.win.wm_title("enter Amp Hours")
        self.win.geometry("800x460+0+0")
        self.win.config(background='Dark gray')
        
        self.textin=StringVar()
        
        self.fontize1=39
        
        metext=Entry(self.win,textvar=self.textin, font=(self.fontstyle, self.fontize1))
        metext.grid(row=0, columnspan=3,sticky=W+E+N+S, padx=2, pady =2)

        self.pdx=4
        self.pdy=4
        
        self.operator=""
        
        but1=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut(1),text="1",font=(self.fontstyle, self.fontize1))
        but1.grid(row=1, column=0,sticky=W+E+N+S, padx=1, pady =1)
        
        but2=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut(2),text="2",font=(self.fontstyle, self.fontize1))
        but2.grid(row=1, column=1,sticky=W+E+N+S, padx=1, pady =1)
        
        but3=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut(3),text="3",font=(self.fontstyle, self.fontize1))
        but3.grid(row=1, column=2,sticky=W+E+N+S, padx=1, pady =1)
        
        but4=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut(4),text="4",font=(self.fontstyle, self.fontize1))
        but4.grid(row=2, column=0,sticky=W+E+N+S, padx=1, pady =1)
        
        but5=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut(1),text="1",font=(self.fontstyle, self.fontize1))
        but5.grid(row=2, column=1,sticky=W+E+N+S, padx=1, pady =1)
        
        but6=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut(6),text="6",font=(self.fontstyle, self.fontize1))
        but6.grid(row=2, column=2,sticky=W+E+N+S, padx=1, pady =1)
        
        but7=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut(7),text="7",font=(self.fontstyle, self.fontize1))
        but7.grid(row=3, column=0,sticky=W+E+N+S, padx=1, pady =1)
        
        but8=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut(8),text="8",font=(self.fontstyle, self.fontize1))
        but8.grid(row=3, column=1,sticky=W+E+N+S, padx=1, pady =1)
        
        but9=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut(9),text="9",font=(self.fontstyle, self.fontize1))
        but9.grid(row=3, column=2,sticky=W+E+N+S, padx=1, pady =1)
        
        but0=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut(0),text="0",font=(self.fontstyle, self.fontize1))
        but0.grid(row=4, column=1,sticky=W+E+N+S, padx=1, pady =1)
        
        butdot=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.clickbut("."),text=".",font=(self.fontstyle, self.fontize1))
        butdot.grid(row=4, column=2,sticky=W+E+N+S, padx=1, pady =1)
        
        butenter=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.setamphour(),text="Enter",font=(self.fontstyle, self.fontize1))
        butenter.grid(row=1, column=4, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=10, pady =5)
        
        butcancel=Button(self.win,padx=self.pdx,pady=self.pdy,bd=4,bg='white',command=lambda:self.win.destroy(),text="Cancel",font=(self.fontstyle, self.fontize1))
        butcancel.grid(row=3, column= 4, columnspan=2,rowspan=2, sticky=W+E+N+S, padx=10, pady =5)
        
    
    #defines the lay out of the main GUI
    def layout_gui(self):
        frameleft=tk.Frame(self.master, bg=self.leftframecolor, width=600, height=400)
        frameleft.columnconfigure(1, weight=1)
        frameleft.grid(row=0,column=0, sticky=W+E+N+S)


        frameright=tk.Frame(self.master, bg='red', width=200, height=400)
        frameright.columnconfigure(2, weight=1)
        frameright.grid(row=0,column=1,sticky=W+E+N+S)
        
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=2)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        
        #labels or names for the data
        a=Label(frameleft, text = 'Speed', font=(self.fontstyle, self.fontize), bg=self.leftframecolor)
        b=Label(frameleft, text = 'Current', font=(self.fontstyle, self.fontize), bg=self.leftframecolor)
        c=Label(frameleft, text = 'Main Voltage', font=(self.fontstyle, self.fontize), bg=self.leftframecolor)
        d=Label(frameleft, text = 'Aux Voltage',font=(self.fontstyle, self.fontize), bg=self.leftframecolor)
        e=Label(frameleft, text = 'Amp Hours',font=(self.fontstyle, self.fontize) , bg=self.leftframecolor)
        
        #data strings where we will put our data later
        self.speeddatavariable = StringVar(frameleft, value='Hello')
        self.currentdatavariable = StringVar(frameleft, value='Hello')
        self.maindatavariable = StringVar(frameleft, value='Hello')
        self.auxdatadatavariable = StringVar(frameleft, value='Hello')
        self.amphourdatadatavariable = StringVar(frameleft, value='Hello')
        
        
        #place on the gui we will enter the data
        self.speeddata=Entry(frameleft, textvariable=self.speeddatavariable, font=(self.fontstyle, self.fontize), justify=CENTER, width=self.entrywidth)
        self.currentdata=Entry(frameleft, textvariable=self.currentdatavariable,font=(self.fontstyle, self.fontize), justify=CENTER, width=self.entrywidth)
        self.maindata=Entry(frameleft, textvariable=self.maindatavariable, font=(self.fontstyle, self.fontize), justify=CENTER, width=self.entrywidth)
        self.auxdata=Entry(frameleft, textvariable=self.auxdatadatavariable, font=(self.fontstyle, self.fontize), justify=CENTER, width=self.entrywidth)
        self.amphourdata=Entry(frameleft, textvariable=self.amphourdatadatavariable, font=(self.fontstyle, self.fontize), justify=CENTER, width=self.entrywidth)
        
        #enters data on grid
        a.grid(row=0, column=0,sticky=W+E+N+S, padx=15, pady =15)
        b.grid(row=1, column=0,sticky=W+E+N+S, padx=15, pady =15)
        c.grid(row=2, column=0,sticky=W+E+N+S, padx=15, pady =15)
        d.grid(row=3, column=0,sticky=W+E+N+S, padx=15, pady =15)
        e.grid(row=4, column=0,sticky=W+E+N+S, padx=15, pady =15)
        self.speeddata.grid(row=0, column=1, padx=15, pady =15)
        self.currentdata.grid(row=1, column=1, padx=15, pady =15)
        self.maindata.grid(row=2, column=1, padx=15, pady =15)
        self.auxdata.grid(row=3, column=1, padx=15, pady =15)
        self.amphourdata.grid(row=4, column=1, padx=15, pady =15)
        
        
        #creates the buttons for the right frame and enters them on a grid
        self.startbutton=Button(frameright, text= "Start", font=(self.fontstyle, self.fontize),justify=CENTER, padx=10, pady=20, command=self.SetTrue)
        self.startbutton.grid(row=0,column=0,sticky=W+E+N+S,padx=5, pady =5)
        
        self.endbutton=Button(frameright, text= "End", font=(self.fontstyle, self.fontize),justify=CENTER, padx=10, pady=20,command=self.SetFalse)
        self.endbutton.grid(row=1,column=0,sticky=W+E+N+S,padx=5, pady =5)
        
        self.shutdownbutton=Button(frameright, text= "Shutdown", font=(self.fontstyle, 15),justify=CENTER, padx=10, pady=20, command=self.shutdownconfirm)
        self.shutdownbutton.grid(row=0,column=1,sticky=W+E+N+S,padx=5, pady =5)
        
        self.setamphourbutton=Button(frameright, text= "Set AmpHr", font=(self.fontstyle, 18),justify=CENTER, padx=10, pady=20,wraplength=50, command=self.popupwindow)
        self.setamphourbutton.grid(row=1,column=1,sticky=W+E+N+S,padx=5, pady =5)
        
        frameright.grid_columnconfigure(0, weight=1)
        frameright.grid_columnconfigure(1, weight=1)
        frameright.grid_rowconfigure(0, weight=1)
        frameright.grid_rowconfigure(1, weight=1)
        



# function that does the nuts and bolts a data collection        
class Telem():
    
    #setup function of the main data collection program
    #here is where you would define any new sensors.
    def __init__(self,master):
        self.master=master
        #setup I2C Bus
        self.i2c_bus = busio.I2C(board.SCL, board.SDA)
        
        #create the temperature sensor using I2C Buss
        self.mcp = adafruit_mcp9808.MCP9808(self.i2c_bus)
        
        # Create the ADC object using the I2C bus
        self.ads = ADS.ADS1015(self.i2c_bus)
        
        # setup serial bus
        self.uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)
         
        # Create a GPS module instance.
        self.gps = adafruit_gps.GPS(self.uart, debug=False)
        
        # Turn on the basic GGA and RMC info (what you typically want)
        self.gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        
        # Set GPS update rate 
        self.gps.send_command(b'PMTK220,1000')
        
        #sets value for ADC Gain
        self.GAIN=1
        
        #correction factors for voltage dividers
        self.adc0correction=92.54378
        self.adc1correction=28.45011379
        self.adc2correction=1
        self.adc3correction=1
        
        #conversion factor for knots to mph
        self.knotsconversion=1.15078
        
        #initialize last time
        self.last_print = time.monotonic()
        
        #initialize amphour
        self.amphour=100
        
        #initialize shunt resistance
        self.shuntresistance=.0075
        
        #opens the connection to the DB
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
        
        #open the file and retrieve the runnig amp our count

        self.lastamptime=None
        
    #function calculated amp hours used.  THis is the simplest formula and should be updated to include Peukerts equation
    def calcamphour(self,oldtime,newtime,currentamps):
        return ((newtime-oldtime)/3600)*currentamps


    # main program that polls each of the sensors
    #if any additional sensors are added, they need to be called here
    def aquire(self):
        #print("Run Telem=",RunTelem)

        if RunTelem: 
            #check gor GPS fix update
            self.gps.update()
            
            
            #get the current amp hour reading form it storate
            try:
                self.amphourstorage=open('amphour.txt','r')
                self.amphour=float(self.amphourstorage.read())
                self.amphourstorage.close()
            except:
                self.amphour=0
            
            
            # Escape if it has not been longer then a second from last call
            self.current = time.monotonic()
            if self.current - self.last_print >= 1.0:
                self.last_print = self.current
                if not self.gps.has_fix:
                    # Try again if we don't have a fix yet.
                    print('Waiting for fix...')

                
            #read Temperature and voltage
            self.tempC = self.mcp.temperature
            self.chan0 = AnalogIn(self.ads, ADS.P0)
            self.chan1 = AnalogIn(self.ads, ADS.P1)
            self.chan2 = AnalogIn(self.ads, ADS.P2)
            self.chan3 = AnalogIn(self.ads, ADS.P3)
            
            #correct values
            self.tempF = self.tempC * 9 / 5 + 32
            self.volt0=self.chan0.voltage*self.adc0correction
            self.volt1=self.chan1.voltage*self.adc1correction
            self.volt2=self.chan2.voltage*self.adc2correction
            self.volt3=self.chan3.voltage*self.adc3correction
            

            #convert speed from knots to mph
            if (self.gps.speed_knots != None):
                self.gpsspeedmph=self.gps.speed_knots*self.knotsconversion
                
                
            else:
                self.gpsspeedmph=0
            
            self.currentamps=self.volt3/self.shuntresistance
            

            
            #check to see if there was a previous time stored
            if (self.lastamptime == None):
                self.lastamptime=self.current
            
            
            #calculate amphours used
            #should add Puekerts equations for best accuracy
            try:
                self.amphoursused=self.calcamphour(self.lastamptime,self.current,self.currentamps)
                self.lastamptime=self.current
                
            except:
                self.amphoursused=0
                self.lastamptime=self.current
            

            self.amphour-=self.amphoursused
            
            
            #update the data base
            if self.gps.has_fix:
                #print("Fix")
                self.cur.execute("INSERT INTO public.solardata (datetime, latitude, longitude, speed, mainvoltage, auxvolt, current, motortemp,amphours) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)",
                            (self.gps.timestamp_utc,self.gps.latitude,self.gps.longitude, self.gpsspeedmph, self.volt0,self.volt1,self.currentamps,self.tempC,self.amphour))
                self.conn.commit()
                
                amphourstorage=open('amphour.txt','w')
                amphourstorage.write(str(self.amphour))
                amphourstorage.close()
                

            #update the GUI with new values
            GUI.auxdatadatavariable.set(str(round(self.volt0,2)))
            GUI.maindatavariable.set(str(round(self.volt1,2)))
            GUI.speeddatavariable.set(str(round(self.gpsspeedmph,2)))
            GUI.currentdatavariable.set(str(round(self.currentamps,2)))
            GUI.amphourdatadatavariable.set(str(round(self.amphour,2)))                
            
            #sets the update rate
            self.master.after(5000, self.aquire)


        

    
    
            

        
    


#calls the functions necissary to sets up the gui and collection systems
window = tk.Tk()
GUI=User_Interface(window)
Cardata=Telem(window)



#starts the main loop that creates the gui
window.mainloop()
 
        