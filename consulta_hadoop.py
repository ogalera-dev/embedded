#!/bin/python
import urllib2
import json

# importem la llibreria GPIO

import RPi.GPIO as GPIO, feedparser, time


# configuracio per els ports GPIO
# utilitzarem la identificacio BCM per els ports GPIO
GPIO.setmode(GPIO.BCM)

SEG_A = 21
SEG_B = 20
SEG_C = 16
SEG_D = 12
SEG_E = 25
SEG_F = 24
SEG_G = 23

D2_SEG_A = 06
D2_SEG_B = 05
D2_SEG_C = 22
D2_SEG_D = 27
D2_SEG_E = 17
D2_SEG_F=4
D2_SEG_G = 18

#LED_GROC = 6
LED_VERD = 13
LED_VERMELL = 19
LED_BLAU = 26


# indiquem els ports de sortida GPIO
#GPIO.setup(LED_GROC, GPIO.OUT) ## GPIO 6 com a sortida. Led GROC
GPIO.setup(LED_VERD, GPIO.OUT) ## GPIO 13 com a sortida. Led VERD
GPIO.setup(LED_VERMELL, GPIO.OUT) ## GPIO 19 com a sortida. Led VERMELL
GPIO.setup(LED_BLAU, GPIO.OUT) ## GPIO 26 com a sortida. Led BLAU

#Configuracio del primer digit
GPIO.setup(SEG_A, GPIO.OUT) ## GPIO 21 com a sortida. SEGMNENT A
GPIO.setup(SEG_B, GPIO.OUT) ## GPIO 20 com a sortida. SEGMNENT B
GPIO.setup(SEG_C, GPIO.OUT) ## GPIO 16 com a sortida. SEGMNENT C
GPIO.setup(SEG_D, GPIO.OUT) ## GPIO 12 com a sortida. SEGMNENT D
GPIO.setup(SEG_E, GPIO.OUT) ## GPIO 25 com a sortida. SEGMNENT E
GPIO.setup(SEG_F, GPIO.OUT) ## GPIO 24 com a sortida. SEGMNENT F
GPIO.setup(SEG_G, GPIO.OUT) ## GPIO 23 com a sortida. SEGMNENT G

#Configuracio del segon digit
GPIO.setup(D2_SEG_A, GPIO.OUT) ## GPIO 21 com a sortida. SEGMNENT A
GPIO.setup(D2_SEG_B, GPIO.OUT) ## GPIO 20 com a sortida. SEGMNENT B
GPIO.setup(D2_SEG_C, GPIO.OUT) ## GPIO 16 com a sortida. SEGMNENT C
GPIO.setup(D2_SEG_D, GPIO.OUT) ## GPIO 12 com a sortida. SEGMNENT D
GPIO.setup(D2_SEG_E, GPIO.OUT) ## GPIO 25 com a sortida. SEGMNENT E
GPIO.setup(D2_SEG_F, GPIO.OUT) ## GPIO 24 com a sortida. SEGMNENT F
GPIO.setup(D2_SEG_G, GPIO.OUT) ## GPIO 23 com a sortida. SEGMNENT G


def PRINT_DISPLAY(display, digito):
    # activem els segments segons el numero
    if digito== 0: # numero 0
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_E if display == 1 else D2_SEG_E, True) # segment e
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
    elif digito== 1: # numero 1
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
    elif digito== 2: # numero 2
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_E if display == 1 else D2_SEG_E, True) # segment e
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 3: # numero 3
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 4: # numero 4
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 5: # numero 5
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 6: # numero 6
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_E if display == 1 else D2_SEG_E, True) # segment e
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 7: # numero 7
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
    elif digito== 8: # numero 8
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_E if display == 1 else D2_SEG_E, True) # segment e
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 9: # numero 9
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    GPIO.output(D2_SEG_F, True)

#inicialitzem a 0
def INICIALIZAR_DISPLAY():
    GPIO.output(SEG_A, False) # segment a
    GPIO.output(SEG_B, False) # segment b
    GPIO.output(SEG_C, False) # segment c
    GPIO.output(SEG_D, False) # segment d
    GPIO.output(SEG_E, False) # segment e
    GPIO.output(SEG_F, False) # segment f
    GPIO.output(SEG_G, False) # segment g
    GPIO.output(D2_SEG_A, False) # segment a
    GPIO.output(D2_SEG_B, False) # segment b
    GPIO.output(D2_SEG_C, False) # segment c
    GPIO.output(D2_SEG_D, False) # segment d
    GPIO.output(D2_SEG_E, False) # segment e
    GPIO.output(D2_SEG_F, False) # segment f
    GPIO.output(D2_SEG_G, False) # segment g

def INICIALITZAR_LEDS():
#    GPIO. output(LED_GROC, False)
    GPIO. output(LED_VERD, False)
    GPIO. output(LED_VERMELL, False)
    GPIO. output(LED_BLAU, False)


def mappers():
    contents = json.load(urllib2.urlopen("http://192.168.1.220:23233/mappers"))
    return contents['mappers']

def reducers():
    contents = json.load(urllib2.urlopen("http://192.168.1.220:23233/reducers"))
    return contents['reducers']


fiMappers = False


#Inici map

INICIALIZAR_DISPLAY()
INICIALITZAR_LEDS()

anterior = -1
while not fiMappers:
    m = mappers()
    if m != 100 and anterior == -1:
        GPIO.output(LED_VERMELL,1)
    if m == 100:
        fiMappers = True
    if anterior < m:
        INICIALIZAR_DISPLAY()
        PRINT_DISPLAY(1, m%10)
        m = m / 10
        PRINT_DISPLAY(2, m if m < 10 else 9)
        anterior = m


INICIALIZAR_DISPLAY()
INICIALITZAR_LEDS()
fiReducers = False
anterior = -1
while not fiReducers:
    r = reducers()
    if m != 100 and anterior == -1:
        GPIO.output(LED_BLAU, 1)
    if r == 100:
        fiReducers = True
    if anterior < r:
        INICIALIZAR_DISPLAY()
        PRINT_DISPLAY(1, r%10)
        r = r / 10
        PRINT_DISPLAY(2, r if r < 10 else 9)
        anterior = r

INICIALITZAR_LEDS()
GPIO.output(LED_VERD, 1)
INICIALIZAR_DISPLAY()
