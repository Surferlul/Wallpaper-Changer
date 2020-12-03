from os import mkdir, getcwd
from os.path import isfile, isdir
from subprocess import Popen, call
from time import sleep

CONFIG = ".config"
HISTORY = ".history"

def integrity_check():
    for i in [1]:
        if not isfile(CONFIG):
            pass
        elif len(open(CONFIG, "r").read().split()) < 4:
            pass
        else:
            break
        open(CONFIG, "w").write("600\n1\n0\n1")
        print(CONFIG + " is missing")
        print("generating " + CONFIG + " with default value of\n   Interval = 600 seconds\n   Save Wallpapers = True\n   Start Hidden = False\n   Approximate Time = True")
    if not isfile(HISTORY):
        open(HISTORY, "w").write("")
        print(HISTORY + " is missing")
        print("generating " + HISTORY)
    if not isdir(".\\Images"):
        mkdir(".\\Images")
        print(getcwd() + "\\Images is missing")
        print("generating " + getcwd() + ".\\Images")

while True:
    try:
        integrity_check()
        if int(open(CONFIG, "r").read().split()[3]):
            call(["backend.exe"], shell=True)
        else:
            Popen(["backend.exe"], shell=True)
            sleep(float(open(CONFIG, "r").read().split()[0]))
    except Exception as E:
        print("Error: " + type(E).__name__)
        if type(E).__name__ == "KeyboardInterrupt":
            break
