import board    
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c_bus = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c_bus)


chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

print(chan0.voltage,chan1.voltage,chan2.voltage,chan3.voltage,)