import tkinter as tk
import tkinter.simpledialog as simpledialog
import sys

name = ""
def dialog():
	global name
	root = tk.Tk()
	root.withdraw()
	str_data=simpledialog.askstring("Input Box", "名前を入力してください（半角英数字）", initialvalue='文字列を入力（半角英数字）')
	name = str_data

dialog()
print("tool/pnt/" + name + ".pnt")
from set import *
from dev import *
try:
	takePic()
	imobj = MImage("UI/image/temp.jpg")
	line = imobj.getLandmark()
	point = createPairPoints(line)
	saveFile(point, "tool/pnt/" + name + ".pnt")
except Exception as e:
	print("ERROR")


