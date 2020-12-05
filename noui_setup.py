from cx_Freeze import setup, Executable

base = None
executables = [Executable("backend.py", base=base), Executable("wrapper.py", base=base, targetName="Changer.exe")]

packages = ["idna", "os", "ctypes", "praw", "glob", "time", "urllib", "progressbar", "imgur_downloader", "subprocess"]
options = {
    'build_exe': {
        'build_exe': '.\\noui_build',
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