import sys
from machine import Pin # importe dans le code la lib qui permet de gerer les Pin de sortie et d'entré
from ledSegments import Segments
from imu import MPU6050
from vector3d import Vector3d
import time
from machine import Pin, I2C
import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
import json

pin_button = Pin(18, mode=Pin.IN, pull=Pin.PULL_UP) # declaration d'une variable de type pin ici la 14 
                                                    #et on prescise que c'est une pine d'entré de courant (IN)

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'mon tel'
password = 'Bonjour1'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://192.168.207.73:3000"

pins = [6,7,8,9,10,11,12,13,14,16]
seg = Segments(pins)
seg.show([0,0,0,0,0,0,0,0,0,0])

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)
maxgx = 0
player_id = 0
scores =[]

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while True:
    if pin_button.value() == 0:
        print('aaaa')
        # Following rows round values get for a more pretty print:
        """ax=round(imu.accel.x,2)
        ay=round(imu.accel.y,2)
        az=round(imu.accel.z,2)"""
        gx=round(imu.gyro.x)
        """gy=round(imu.gyro.y)
        gz=round(imu.gyro.z)
        tem=round(imu.temperature,2)
        print(ax,"\t",ay,"\t",az,"\t",gx,"\t",gy,"\t",gz,"\t",tem,"        ",end="\r")
        """
        
        player_id = player_id + 1
        gx=round(imu.gyro.x)
        print(gx)
        if gx < 25:
            seg.show([0,0,0,0,0,0,0,0,0,1])
        elif 25 < gx < 50:
            seg.show([0,0,0,0,0,0,0,0,1,1])
        elif 50 < gx < 75:
            seg.show([0,0,0,0,0,0,0,1,1,1])
        elif 75 < gx < 100:
            seg.show([0,0,0,0,0,0,1,1,1,1])
        elif 100 < gx < 125:
            seg.show([0,0,0,0,0,0,1,1,1,1])
        elif 125 < gx < 150:
            seg.show([0,0,0,0,0,1,1,1,1,1])
        elif 150 < gx < 175:
            seg.show([0,0,0,0,1,1,1,1,1,1])
        elif 175 < gx < 200:
            seg.show([0,0,0,1,1,1,1,1,1,1])
        elif 200 < gx < 225:
            seg.show([0,0,1,1,1,1,1,1,1,1])
        elif 225 < gx < 240:
            seg.show([0,1,1,1,1,1,1,1,1,1])
        else:
            seg.show([1,1,1,1,1,1,1,1,1,1])
        if gx> maxgx: maxgx = gx
        time.sleep(1)
        print(maxgx)
        try:     
            payload = {'id': player_id, 'value': gx}
            scores.append(payload)
            
            headers = {'Content-Type':'application/json'}
            data = (json.dumps(scores)).encode()
            r = urequests.post(url, data=data, headers=headers)
            print(data)
        
            # print(r.status_code)
            # print(r.content)
            # text = r.text
            # print(text) 
            
      
            r.close() # ferme la demande
            utime.sleep(1)  
        except Exception as e:
            print(e)
    
    
               
        # Following sleep statement makes values enought stable to be seen and
        # read by a human from shell
        

