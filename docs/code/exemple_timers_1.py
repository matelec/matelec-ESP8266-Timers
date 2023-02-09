from machine import Pin, Timer
import time

def blink_ledR(led):
    led.value(not led.value())

ledR = Pin(16, Pin.OUT)
compteur = 0
ledR.off()

blinkTimer= Timer(-1)
blinkTimer.init(period=500, mode=Timer.PERIODIC, callback=lambda t:blink_ledR(ledR))

while True:
    compteur=compteur+1
    print (compteur)
    time.sleep(2)
    

    