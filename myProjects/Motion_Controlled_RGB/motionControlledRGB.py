from utime import sleep
import machine
import time
from machine import Pin, PWM

# Pin Definitions for individual colors of the RGB LED
green_LedPWM = PWM(Pin(14))
#green_Led = machine.Pin(14, machine.Pin.OUT)
red_LedPWM = PWM(Pin(12))
#red_Led = machine.Pin(12, machine.Pin.OUT)
blue_LedPWM = PWM(Pin(13))
#blue_Led = machine.Pin(13, machine.Pin.OUT)

#Declarations for Motion Sensor pins
power_Motion = Pin(0, Pin.OUT, Pin.PULL_UP)
signal_Motion = Pin(4, Pin.IN)

#GLOBAL CONSTANTS
REST = 0.0001  #Defines sleep duration
FREQ = 1000
STEP = 10

# Frequency setting for PWM
green_LedPWM.freq(FREQ)
red_LedPWM.freq(FREQ)
blue_LedPWM.freq(FREQ)

""" Basic RGB LED Modules Definitions
def showRed():
    green_Led.value(0)
    blue_Led.value(0)
    red_Led.value(1)
    #dimRed()
    return

def showBlue():
    green_Led.value(0)
    blue_Led.value(1)
    red_Led.value(0)
    #dimBlue()
    return

def showGreen():
    green_Led.value(1)
    blue_Led.value(0)
    red_Led.value(0)
    #dimGreen()
    return

def showPurple():
    green_Led.value(0)
    blue_Led.value(1)
    red_Led.value(1)
    #dimPurple()
    return

def showYellow():
    green_Led.value(1)
    blue_Led.value(1)
    red_Led.value(0)
    #dimYellow()
    return

def showOrange():
    green_Led.value(1)
    blue_Led.value(0)
    red_Led.value(1)
    #dimOrange()
    return

def showDark():
    green_Led.value(0)
    blue_Led.value(0)
    red_Led.value(0)
    return

def showWhite():
    green_Led.value(1)
    blue_Led.value(1)
    red_Led.value(1)
    return
"""

def dimOrange(duty):
    red_LedPWM.duty_u16(duty)
    green_LedPWM.duty_u16(duty)
    sleep(REST)
    return

def dimPurple(duty):
    red_LedPWM.duty_u16(duty)
    blue_LedPWM.duty_u16(duty)
    sleep(REST)
    return

def dimYellow(duty):
    green_LedPWM.duty_u16(duty)
    blue_LedPWM.duty_u16(duty)
    sleep(REST)
    return

def dimGreen(duty):
    green_LedPWM.duty_u16(duty)
    sleep(REST)
    return

def dimBlue(duty):
    blue_LedPWM.duty_u16(duty)
    sleep(REST)
    return

def dimRed(duty):
    red_LedPWM.duty_u16(duty)
    sleep(REST)
    return

def updateLocalTime(seconds):
    localTime = time.localtime(seconds)
    return localTime

def getSeconds():
    seconds = time.time()
    return seconds


# BEGIN LOOP OF PWM TESTING
while True:
    power_Motion.value(1)
    #print("value of pin 0 is %s " % str(power_Motion.value()))
    if (signal_Motion.value() == 1):
        print("motion is working")
        '''
        seconds = getSeconds()
        localTime = updateLocalTime(seconds)
        print("Start Dimming RED: %s" % str(localTime))
        for duty in range(0, 65025, STEP):
            dimRed(duty)
        for duty in range(65025, 0, -STEP):
            dimRed(duty)

        seconds = getSeconds()
        localTime = updateLocalTime(seconds)
        print("Start dimming GREEN: %s" % str(localTime))
        for duty in range(0, 65025, STEP):
            dimGreen(duty)
        for duty in range(65025, 0, -STEP):
            dimGreen(duty)

        seconds = getSeconds()
        localTime = updateLocalTime(seconds)
        print("Start dimming BLUE: %s" % str(localTime))
        for duty in range(0, 65025, STEP):
            dimBlue(duty)
        for duty in range(65025, 0, -STEP):
            dimBlue(duty)

        seconds = getSeconds()
        localTime = updateLocalTime(seconds)
        print("Start dimming ORANGE: %s" % str(localTime))
        for duty in range(0, 65025, STEP):
            dimOrange(duty)
        for duty in range(65025, 0, -STEP):
            dimOrange(duty)

        seconds = getSeconds()
        localTime = updateLocalTime(seconds)
        print("Start dimming PURPLE: %s" % str(localTime))
        for duty in range(0, 65025, STEP):
            dimPurple(duty)
        for duty in range(65025, 0, -STEP):
            dimPurple(duty)

        seconds = getSeconds()
        localTime = updateLocalTime(seconds)
        print("Start dimming YELLOW: %s" % str(localTime))
        for duty in range(0, 65025, STEP):
            dimYellow(duty)
        for duty in range(65025, 0, -STEP):
            dimYellow(duty)

        STEP += 1
        if(STEP == 100):
            STEP = 10
    else:
        break
    '''
#END OF PWM TESTING LOOP

"""BEGINNING OF TOGGLE COLORS
while(1):
    for count in range(100):
        #Reset Count Value
        if(count >= 100):
            count = 1

        if(count < 100):
            # Start with DARK mode
            showDark()
            # Showing RED for 5 seconds? ms?, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing RED: %s" % str(localTime))
            showRed()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing RED: %s" % str(localTime))

            #showing ORANGE for 1 second, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing ORANGE: %s" % str(localTime))
            showOrange()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing ORANGE: %s" % str(localTime))

            # showing YELLOW for (1) seconds, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing YELLOW: %s" % str(localTime))
            showYellow()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing YELLOW: %s" % str(localTime))

            # showing GREEN for (1) seconds, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing GREEN: %s" % str(localTime))
            showGreen()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing GREEN: %s" % str(localTime))

            # showing BLUE for (1) seconds, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing BLUE: %s" % str(localTime))
            showBlue()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing BLUE: %s" % str(localTime))

            # showing PURPLE for (1) seconds, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing PURPLE: %s" % str(localTime))
            showPurple()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing PURPLE: %s" % str(localTime))
            
            # showing YELLOW for (1) seconds, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing YELLOW: %s" % str(localTime))
            showYellow()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing YELLOW: %s" % str(localTime))
            
            # showing BLUE for (1) seconds, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing BLUE: %s" % str(localTime))
            showBlue()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing BLUE: %s" % str(localTime))
            
            # showing GREEN for (1) seconds, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing GREEN: %s" % str(localTime))
            showGreen()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing GREEN: %s" % str(localTime))

            # showing YELLOW for (1) seconds, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing YELLOW: %s" % str(localTime))
            showYellow()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing YELLOW: %s" % str(localTime))
            
            #showing ORANGE for 1 second, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing ORANGE: %s" % str(localTime))
            showOrange()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing ORANGE: %s" % str(localTime))
            
            # showing YELLOW for (1) seconds, then showing DARK
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("Start showing YELLOW: %s" % str(localTime))
            showYellow()
            time.sleep_ms(REST)
            showDark()
            seconds = getSeconds()
            localTime = updateLocalTime(seconds)
            print("End showing YELLOW: %s" % str(localTime))
            # End with WHITE mode
            showWhite()
        print("")
        print("Count is: " + str(count) + " out of 100.")
        print("")
"""

