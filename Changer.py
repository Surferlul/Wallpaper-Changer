import wx
from glob import glob
from os import remove, getcwd, mkdir
from os.path import isfile, getsize, isdir
from subprocess import Popen, CREATE_NEW_CONSOLE, DETACHED_PROCESS

ids = {}
CONFIG = ".config"
HISTORY = ".history"
DESIGN = {
    "Interval Text":        (10, 13),
    "Interval":             (10, 30),
    "Save":                 (11, 63),
    "Hidden":               (10, 93),
    "Safe Mode":     (10, 123),
    "Clear Cache":          (10, 150),
    "Cache Information":    (120,153),
    "Clear History":        (10, 180),
    "History Information":  (120,183),
    "Refresh":              (10, 210),
    "Start":                (10, 240)
}

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

class ChangerUI(wx.Frame):

    def __init__(self, *args, **kw):
        super(ChangerUI, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        
        self.itxt = wx.StaticText(self, pos=DESIGN["Interval Text"], label="Interval:")

        self.Intl = wx.TextCtrl(self, pos=DESIGN["Interval"], style=wx.TE_PROCESS_ENTER, size=(100, 24))
        self.Intl.SetValue(open(CONFIG, "r").read().split()[0])
        ids[self.Intl.GetId()] = "Interval"

        self.Save = wx.CheckBox(self, pos=DESIGN["Save"], label="Save Wallpapers")
        ids[self.Save.GetId()] = "Save"
        self.Save.SetValue(int(open(CONFIG, "r").read().split()[1]))

        self.Hd = wx.CheckBox(self, pos=DESIGN["Hidden"], label="Start Hidden")
        ids[self.Hd.GetId()] = "Hidden"
        self.Hd.SetValue(int(open(CONFIG, "r").read().split()[2]))

        self.Ap = wx.CheckBox(self, pos=DESIGN["Safe Mode"], label="Safe Mode")
        ids[self.Ap.GetId()] = "Safe"
        self.Ap.SetValue(int(open(CONFIG, "r").read().split()[3]))

        self.cl = wx.Button(self, label="Clear Cache", pos=DESIGN["Clear Cache"], size=(100, 28))
        ids[self.cl.GetId()] = "Clear Cache"
        self.clh = wx.Button(self, label="Clear History", pos=DESIGN["Clear History"], size=(100, 28))
        ids[self.clh.GetId()] = "Clear History"
        self.st = wx.Button(self, label="Start", pos=DESIGN["Start"], size=(100, 28))
        ids[self.st.GetId()] = "Start"
        self.rf = wx.Button(self, label="Refresh", pos=DESIGN["Refresh"], size=(100, 28))
        ids[self.rf.GetId()] = "Refresh"

        self.cinf = wx.StaticText( self,
                                    label= str(int(sum([getsize(i) for i in glob("./Images/*.*")]) / 1024 / 10.24) / 100) + " MB, " + str(len(glob("./Images/*.*"))) + " Files", 
                                    pos=DESIGN["Cache Information"])
        ids[self.cinf.GetId()] = "Cache Information"
        self.hinf = wx.StaticText( self,
                                    label= str(len(open(HISTORY, "r").read().split())) + " Entries", 
                                    pos=DESIGN["History Information"])
        ids[self.hinf.GetId()] = "History Information"
        
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        self.Bind(wx.EVT_BUTTON, self.OnPress)
        self.Bind(wx.EVT_CHECKBOX, self.OnPress)
        self.Bind(wx.EVT_FSWATCHER, self.DirChanged)

        self.SetSize((self.cinf.GetSize().x + 140, DESIGN["Start"][1] + 70))
        self.SetTitle('Changer')
        self.Centre()

    def DirChanged(self, e):
        self.cinf.SetLabel(str(int(sum([getsize(i) for i in glob("./Images/*.*")]) / 1024 / 10.24) / 100) + " MB, " + str(len(glob("./Images/*.*"))) + " Files")

    def OnEnter(self, e):

        if ids[e.GetId()] == "Interval":
            try:
                float(self.Intl.GetValue())
                fr = open(CONFIG, "r")
                c = fr.read().split()
                fr.close()
                fw = open(CONFIG, "w")
                c[0] = self.Intl.GetValue()
                fw.write("\n".join(c))
                fw.close()
            except:
                print("Invalid Value!")
                self.Intl.SetValue(open(CONFIG, "r").read().split()[0])

    def OnPress(self, e):
        if ids[e.GetId()] == "Clear Cache":
            for i in [i for i in glob("./Images/*.*") if i.split(".")[-1] in ["jpg", "jpeg", "png"]]:
                remove(i)
            self.cinf.SetLabel(str(int(sum([getsize(i) for i in glob("./Images/*.*")]) / 1024 / 10.24) / 100) + " MB, " + str(len(glob("./Images/*.*"))) + " Files")
            self.SetSize((self.cinf.GetSize().x + 140, DESIGN["Start"][1] + 70))

        if ids[e.GetId()] == "Clear History":
            open(".history", "w").write("")
            self.hinf.SetLabel(str(len(open(HISTORY, "r").read().split())) + " Entries")

        if ids[e.GetId()] == "Save":
            fr = open(CONFIG, "r")
            c = fr.read().split()
            fr.close()
            fw = open(CONFIG, "w")
            c[1] = str(int(self.Save.GetValue()))
            fw.write("\n".join(c))
            fw.close()
        
        if ids[e.GetId()] == "Hidden":
            fr = open(CONFIG, "r")
            c = fr.read().split()
            fr.close()
            fw = open(CONFIG, "w")
            c[2] = str(int(self.Hd.GetValue()))
            fw.write("\n".join(c))
            fw.close()
        
        if ids[e.GetId()] == "Safe":
            fr = open(CONFIG, "r")
            c = fr.read().split()
            fr.close()
            fw = open(CONFIG, "w")
            c[3] = str(int(self.Ap.GetValue()))
            fw.write("\n".join(c))
            fw.close()
        
        if ids[e.GetId()] == "Start":
            if int(open(CONFIG, "r").read().split()[2]):
                Popen(["wrapper.exe"], shell=True, creationflags=CREATE_NEW_CONSOLE)
            else:
                Popen(["wrapper.exe"], shell=True, creationflags=DETACHED_PROCESS)

        if ids[e.GetId()] == "Refresh":
            integrity_check()
            self.hinf.SetLabel(str(len(open(HISTORY, "r").read().split())) + " Entries")
            self.cinf.SetLabel(str(int(sum([getsize(i) for i in glob("./Images/*.*")]) / 1024 / 10.24) / 100) + " MB, " + str(len(glob("./Images/*.*"))) + " Files")
            self.SetSize((self.cinf.GetSize().x + 140, DESIGN["Start"][1] + 70))
            self.Intl.SetValue(open(CONFIG, "r").read().split()[0])
            self.Save.SetValue(int(open(CONFIG, "r").read().split()[1]))
            self.Hd.SetValue(int(open(CONFIG, "r").read().split()[2]))
            self.Ap.SetValue(int(open(CONFIG, "r").read().split()[3]))



def main():

    integrity_check()
    app = wx.App()
    cu = ChangerUI(None)
    cu.Show()
    app.MainLoop()


if __name__ == '__main__':
    main() 