from ctypes import windll
from praw import Reddit
from glob import glob
from time import sleep
from time import time
from urllib.request import urlretrieve
from os import getcwd, remove, system
import progressbar
import urllib.request
from imgur_downloader import ImgurDownloader
import _thread
from subprocess import Popen, CREATE_NEW_CONSOLE

CONFIG = ".config"
CLIENT = ".client"
intrvl = float(open(CONFIG, "r").read().split()[0])
imgpath = ""
start = time()
client = open(CLIENT, "r").read().split()

class NoImage(Exception):
    pass

reddit = Reddit(client_id=client[0],
                client_secret=client[1],
                user_agent='Wallpaper changer by u/Surferlul')

class MyProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()

def del_file(path, Seconds=10):
    Popen("powershell.exe Sleep(" + str(Seconds) + "); Remove-Item .\\Images\\" + path, shell=True, creationflags=CREATE_NEW_CONSOLE)

posts = open(".history", "r").read()
for i in reddit.subreddit("wallpaper").hot(limit = 1000):
    if i.url not in posts:
        submission = i
        break

open(".history", "a").write(submission.url + "\n")
try:
    if "imgur" in submission.url:
        if submission.url.split("/")[-1].split(".")[-1] not in ["jpg", "jpeg", "png"]:
            print("Downoading", submission.url)
        else:
            print("Downoading", submission.url, "as", submission.url.split("\\")[-1])
        ImgurDownloader(
        submission.url,
        "./Images/",
        file_name=submission.url.split("/")[-1]
            if submission.url.split("/")[-1].split(".")[-1] not in ["jpg", "jpeg", "png"] 
            else submission.url.split("/")[-1].split(".")[0]
        ).save_images()
        if submission.url.split("/")[-1].split(".")[-1] not in ["jpg", "jpeg", "png"]:
            windll.user32.SystemParametersInfoW(20, 0, getcwd() + "\\" + glob("./Images/" + submission.url.split("/")[-1] + ".*")[0], 0)
            if not int(open(CONFIG, "r").read().split()[1]):
                del_file(glob(submission.url.split("/")[-1] + ".*")[0])
        else:
            windll.user32.SystemParametersInfoW(20, 0, getcwd() + "\\Images\\" + submission.url.split("/")[-1] , 0)
            if not int(open(CONFIG, "r").read().split()[1]):
                del_file(submission.url.split("/")[-1])
    else:
        if submission.url.split("/")[-1].split(".")[-1] not in ["jpg", "jpeg", "png"]:
            raise NoImage
        imgpath = "Images\\" + submission.url.split("/")[-1]
        print("Downoading", submission.url, "as", submission.url.split("\\")[-1])
        urlretrieve(submission.url, imgpath, MyProgressBar())
        windll.user32.SystemParametersInfoW(20, 0, getcwd() + "\\" + imgpath, 0)
        if not int(open(CONFIG, "r").read().split()[1]):
            del_file(submission.url.split("/")[-1])

    end = time()

    intrvl += start - end
    if intrvl >= 0:
        pbar = progressbar.ProgressBar(maxval=intrvl)
        pbar.start()
        if intrvl < 10:
            for i in range(1, int(intrvl * 10) + 1):
                sleep(intrvl / int(intrvl * 10))
                try:
                    pbar.update(intrvl / int(intrvl * 10) * i)
                except:
                    pbar.update(int(intrvl))
                    print("test")
        else:
            for i in range(1, 101):
                sleep(intrvl / 100)
                pbar.update(intrvl / 100 * i)
        pbar.finish()
    elif int(open(CONFIG, "r").read().split()[3]):
        intrvl -= 2 * (start - end)
        print("Interval was rounded up to " + str(round(intrvl * 100) / 100) + "s because the download needed longer than the interval.")
except NoImage:
    print("Error: Url doesn't point to an Image")
except Exception as E:
    print("Error: " + type(E).__name__)
