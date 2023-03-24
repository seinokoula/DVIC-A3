from machine import Pin
import utime

class Segments(object):
    def __init__(self, pins):
        self.led_list = [Pin(pin, Pin.OUT) for pin in pins]

    def show(self, array):
        for x in range(len(self.led_list)):
            self.led_list[x].value(not(array[x]))
     

    def cycle(self):
        array = [0,0,0,0,0,0,0,0,0,1]
        print("aaa")
        while True:
            array = array[1:]+array[:1]
            self.show(array)
            utime.sleep(0.05)

    def percent(self, n):
        thresholds=[100,90,80,70,60,50,40,30,20,10]
        array=list(map(lambda x: (1,0)[x>n],thresholds))
        self.show(array)

if __name__ == "__main__":
    pins = [6,7,8,9,10,11,12,13,14,16]
    seg = Segments(pins)
    seg.cycle()
