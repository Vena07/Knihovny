# demo 1

from machine import Pin


# CONSTANTS
KEY_UP   = const(0)
KEY_DOWN = const(1)

keys = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]

# Pin names for Pico
def ROWS(pin1,pin2,pin3,pin4):
    global rows
    rows = [pin1,pin2,pin3,pin4]

def COLS(pin1,pin2,pin3,pin4):
    global cols
    cols = [pin1,pin2,pin3,pin4]    

# set pins for rows as outputs
row_pins = [Pin(pin_name, mode=Pin.OUT) for pin_name in rows]

# set pins for cols as inputs
col_pins = [Pin(pin_name, mode=Pin.IN, pull=Pin.PULL_DOWN) for pin_name in cols]

def init():
    for row in range(0,4):
        for col in range(0,4):
            row_pins[row].low()

def scan(row, col):
    """ scan the keypad """

    # set the current column to high
    row_pins[row].high()
    key = None

    # check for keypressed events
    if col_pins[col].value() == KEY_DOWN:
        key = KEY_DOWN
    if col_pins[col].value() == KEY_UP:
        key = KEY_UP
    row_pins[row].low()

    # return the key state
    return key


# set all the columns to low
init()

for row in range(4):
    for col in range(4):
        key = scan(row, col)
        if key == KEY_DOWN:
            last_key_press = keys[row][col]
         