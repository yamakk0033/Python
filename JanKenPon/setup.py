import os
os.environ['TCL_LIBRARY'] = "C:\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Anaconda3\\tcl\\tk8.6"

from cx_Freeze import setup, Executable


setup(
    name = "test",
    version = "0.1",
    descriptiom = "test",
    executables = [Executable("test.py")]
    )