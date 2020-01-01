#####Created by codebreaker on 26-12-2019

import sys
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def encrypt(message):
    cipher=''
    for letter in message:
        if letter != ' ':
            cipher+=MORSE_CODE_DICT[letter] + ' '
        else:
            cipher+=' '
    return cipher
def decrypt(cipher):
    message=''
    character=''
    for letter in cipher:
      if letter != ' ':
            i = 0
            character += letter
      else:
            i += 1
            if i == 2 :
                message += ' '
            else:
                message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)] 
                citext = ''
    return message

def blink_led(morse):
        print("Blinking Morse Code......")
        for code in morse:
               if code=='-':
                   #print("Its dash",code)
                   GPIO.output(8, GPIO.HIGH)
                   sleep(1)
                   GPIO.output(8, GPIO.LOW)
                   sleep(0.75)
               elif code=='.':
		  # print("Its dot",code)
                   GPIO.output(8, GPIO.HIGH)
                   sleep(0.40)
                   GPIO.output(8, GPIO.LOW)
                   sleep(0.75)
               elif code==' ':
                   #print("Space",code)
                   sleep(1.5)
try:
    msg=str(sys.argv[1])
    print("Your message:",msg)
    morse=encrypt(msg)
    print("Your Morse Code:",morse)
    blink_led(morse)
    print("Done!")
    GPIO.cleanup()
except (KeyboardInterrupt):
   GPIO.cleanup()
