import sys
from cx_Freeze import setup, Executable

setup(
    name = "FSLogParse",
    version = "3.1",
    description = "FSLogParse",
    executables = [Executable("PyLogParse.py", base = "Win32GUI")])