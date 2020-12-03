from subprocess import call
from shutil import rmtree
from os.path import isdir
if isdir(".\\build"):  
    rmtree(".\\build")
call("python3 setup.py build", shell=True)
print(
"""

________________________________
BUILD FINISHED
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
"""
)
input()