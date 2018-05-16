import RPi.GPIO as GPIO
import time

RED = 23
GREEN = 12
YELLOW = 16

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RED,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(GREEN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(YELLOW,GPIO.OUT,initial=GPIO.LOW)

def main():
    while True:
       GPIO.output(RED,GPIO.HIGH)
       print('RED ON\n')
       time.sleep(0.5)
       GPIO.output(RED,GPIO.LOW)
       print('RED OFF...\n')
       time.sleep(0.5)
      
       GPIO.output(GREEN,GPIO.HIGH)
       print('GREEN ON\n')
       time.sleep(0.5)
       GPIO.output(GREEN,GPIO.LOW)
       print('GREEN OFF...\n')
       time.sleep(0.5)
      
       GPIO.output(YELLOW,GPIO.HIGH)
       print('YELLOW ON\n')
       time.sleep(0.5)
       GPIO.output(YELLOW,GPIO.LOW)
       print('YELLOW OFF...\n')
       time.sleep(0.5)

       pass
    pass

def destroy():
    GPIO.output(LEDPIN,GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
            main()
    except KeyboardInterrupt:
        destroy()
