from hanover_flipdot import display
from hanover_flipdot import fonts
import time

#display = display.Display("COM10", 1, 96, 16, fonts.unscii_16, True, False)
display = display.Display("COM10", 1, 96, 16, fonts.unscii, False, True)

while True:
    display.write_text(time.strftime("%H:%M:%S"), line = 0, column = 20)
    display.write_text(time.strftime("%a %B %d"), line = 8, column = 0)
    display.send()
    time.sleep(3)

