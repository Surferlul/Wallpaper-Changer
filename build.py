from subprocess import call, Popen, DETACHED_PROCESS
from shutil import rmtree
from os.path import isdir
if isdir(".\\build"):
    print("Removing .\\build")
    rmtree(".\\build")
if isdir(".\\noui_build"):
    print("Removing .\\noui_build")
    rmtree(".\\noui_build")
Popen(["powershell", """python3 noui_setup.py build; python3 -c "input('\\n\\n________________________________\\nBUILD FINISHED\\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\\n\\n')\""""], shell=True, creationflags=DETACHED_PROCESS)
call("python3 setup.py build", shell=True)
print(
"""

________________________________
BUILD FINISHED
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
"""
)
input()