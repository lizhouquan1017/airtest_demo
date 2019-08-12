# coding:utf-8
__author__ = "lzq"
import os
import time


# 获取文件
def get_pylist(file_path):
    dirlist = os.listdir(file_path)
    pylist = []
    for i in range(len(dirlist)):
        file_name = dirlist[i].split(".")
        if dirlist[i] != "__init__.py" and dirlist[i] != "__pycache__":
            if file_name[1].lower() == "py":
                pylist.append(file_name[0])
    return pylist


# 获取截图
def get_screen(self, starttime, devices, action):
    reportpath = os.path.join(os.getcwd(), "report")
    screenpath = os.path.join(reportpath, "screen")
    print("screenpath=", screenpath)
    png = screenpath + "\\" + time.strftime('%Y%m%d_%H%M%S', time.localtime(starttime)) + "_" + "_" + action + ".png"
    print("png=", png)
    os.system("adb -s " + devices + " shell screencap -p /sdcard/screencap.png")
    fp = open(png, "a+", encoding="utf-8")
    fp.close()
    os.system("adb -s " + devices + " pull /sdcard/screencap.png " + png)
    print("<img src='" + png + "' width=600 />")
    return png
