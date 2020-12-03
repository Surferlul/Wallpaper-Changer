from cx_Freeze import setup, Executable

base = None    

executables = [Executable("backend.py", base=base), Executable("wrapper.py", base=base), Executable("Changer.py", base=base)]

packages = ["idna", "os", "ctypes", "praw", "glob", "time", "urllib", "progressbar", "imgur_downloader", "wx", "subprocess", "_thread"]
options = {
    'build_exe': {
        'build_exe': '.\\build',
        'packages':packages,
    },    
}

setup(
    name = "Changer",
    options = options,
    version = "1.1",
    description = 'Wallpaper changer by u/Surferlul',
    executables = executables
)