import I2C_LCD_driver
from time import *
from machine import Pin
import time 

hz_1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
hz_2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
hz_3 = Pin(14, Pin.IN, Pin.PULL_DOWN)
hz_4 = Pin(11, Pin.IN, Pin.PULL_DOWN)

vi_1 = Pin(17, Pin.IN, Pin.PULL_DOWN)
vi_2 = Pin(16, Pin.IN, Pin.PULL_DOWN)
vi_3 = Pin(27, Pin.IN, Pin.PULL_DOWN)

sub = Pin(3, Pin.IN, Pin.PULL_DOWN)
add = Pin(4, Pin.IN, Pin.PULL_DOWN)
equel = Pin(5, Pin.IN, Pin.PULL_DOWN)
clr = Pin(2, Pin.IN, Pin.PULL_DOWN)

DSP = I2C_LCD_driver.lcd()
equation = ''

def clear():
    global equation
    del equation
    equation = ''
    DSP.lcd_clear()
    
def solve(eq):
    
    global equation
  
    try:
        result = eval(eq)
    except:
        DSP.lcd_display_string("error", 2)
    else:
        
        result_str = str(result)
        number_of_characters = len(result_str)

        if number_of_characters > 16:
            DSP.lcd_display_string("ERROR", 2)
        else:
            DSP.lcd_display_string(result_str, 2)
    
    
def Main():
    global equation
    if hz_1() == 1:
        if vi_1() == 1:
            # one
            equation+= "1"
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
            
        elif vi_2() == 1:
            # two
            equation+= '2'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
            
        elif vi_3() == 1:
            # three
            equation+= '3'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
    
    if hz_2() == 1:
        if vi_1() == 1:
            # four
            equation+= '4'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
            
        elif vi_2() == 1:
            # five
            equation+= '5'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
            
        elif vi_3() == 1:
            # six
            equation+= '6'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
            
    if hz_3() == 1:
        if vi_1() == 1:
            # seven
            equation+= '7'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
            
        elif vi_2() == 1:
            # eight
            equation+= '8'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
            
        elif vi_3() == 1:
            # nine
            equation+= '9'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
    
    if hz_4() == 1:
        
        if vi_1() == 1:
            # multiply
            equation+= '*'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
        
        elif vi_2() == 1:
            # null
            equation+= '0'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
            
        
        elif vi_3() == 1:
            # divide
            equation+= '/'
            DSP.lcd_display_string(equation, 1)
            sleep(0.5)
    
    if sub() == 1:
        # subtract
        equation+= '-'
        DSP.lcd_display_string(equation, 1)
        sleep(0.5)
    
    if add() == 1:
        # add
        equation+= '+'
        DSP.lcd_display_string(equation, 1)
        sleep(0.5)
    
    if clr() == 1:
        # clear
        clear()
        sleep(0.5)
    
    if equel() == 1:
        # equel
        solve(equation)
        sleep(0.5)
        
            
while True:
    Main()
 
