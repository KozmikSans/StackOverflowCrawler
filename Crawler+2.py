import sys
import traceback
from tkinter import mainloop
from UI import *
try:
    print("Hello world i dont know how to write pretty code" + 1)
    

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info() # gets exception data
    exc_string = traceback.format_exc() # saving exception text for tkinter use
    ui = UI(exc_type,exc_obj,exc_string)
    mainloop()