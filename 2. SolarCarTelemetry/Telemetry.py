import time      #time
import board    
import busio
import adafruit_mcp9808
import adafruit_gps
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import serial
import psycopg2

#setup I2C Bus
i2c_bus = busio.I2C(board.SCL, board.SDA)

#create the temperature sensor using I2C Buss
mcp = adafruit_mcp9808.MCP9808(i2c_bus)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c_bus)

# setup serial bus
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)
 
# Create a GPS module instance.
gps = adafruit_gps.GPS(uart, debug=False)

# Turn on the basic GGA and RMC info (what you typically want)
gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')

# Set GPS update rate 
gps.send_command(b'PMTK220,1000')

#sets value for ADC Gain
GAIN=1

#correction factors for voltage dividers
adc0correction=92.54378
adc1correction=28.45011379
adc2correction=1
adc3correction=1

#conversion factor for knots to mph
knotsconversion=1.15078

#initialize last time
last_print = time.monotonic()

#initialize amphour
amphour=100

#initialize shunt resistance
shuntresistance=.0075

#opens the connection to the DB
try:
    conn = psycopg2.connect(
         dbname='dd1bpvtvs1alq3',
         user='zfguszkndowgtn',
         password='e41a639c9f4a37a400efbc5940ae418fee0c16f37648522b5f0b1c28abfa7a88',
         host='ec2-54-227-246-152.compute-1.amazonaws.com',
         port='5432')
    print("connected")
    cur = conn.cursor()
except:
    print("I am unable to connect to the database.")

#open the file and retrieve the runnig amp our count
try:
    amphourstorage=open('amphour.txt','r')
    amphour=float(amphourstorage.read())
except:
    amphour=0


def calcamphour(oldtime,newtime,currentamps):
    return (newtime-oldtime)/3600*currentamps

while True:
    gps.update()
    # Every second print out current location details if there's a fix.
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print('Waiting for fix...')
            continue
        
    #read Temperature and voltage
    tempC = mcp.temperature
    chan0 = AnalogIn(ads, ADS.P0)
    chan1 = AnalogIn(ads, ADS.P1)
    chan2 = AnalogIn(ads, ADS.P2)
    chan3 = AnalogIn(ads, ADS.P3)
    
    #correct values
    tempF = tempC * 9 / 5 + 32
    volt0=chan0.voltage*adc0correction
    volt1=chan1.voltage*adc1correction
    volt2=chan2.voltage*adc2correction
    volt3=chan3.voltage*adc3correction
    
    if (gps.speed_knots != None):
        gpsspeedmph=gps.speed_knots*knotsconversion
        
    else:
        gpsspeedmph=0
    
    currentamps=volt3/shuntresistance
    
    try:
        amphoursused=calcamphour(lastamptime,current,currentamps)
        lastamptime=current
        
    except:
        amphoursused=0
        lastamptime=current
    
    amphour-=amphoursused
    
    if gps.has_fix:
        print("Fix")
        cur.execute("INSERT INTO public.solardata (datetime, latitude, longitude, speed, mainvoltage, auxvolt, current, motortemp,amphours) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)",
                    (gps.timestamp_utc,gps.latitude,gps.longitude, gpsspeedmph, volt0,volt1,currentamps,tempC,amphour))
        conn.commit()
        
        amphourstorage=open('amphour.txt','w')
        amphourstorage.write(str(amphour))
        amphourstorage.close()
        
        time.sleep(10)
        
    
         
    
