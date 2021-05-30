from hanover_flipdot import display
from hanover_flipdot import fonts
import time

display = display.Display("COM10", 1, 96, 16, fonts.unscii, False, False)

textPattern = [chr(0x00)] * 12 # Pattern of 12 characters (ASCII 0)

display.erase_all()
display.send()
time.sleep(4)
display.write_text(textPattern, line = 0, column = 0)
display.write_text(textPattern, line = 8, column = 0)
display.send()


