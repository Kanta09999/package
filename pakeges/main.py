import tkinter as tk
from tkinter import StringVar
import os

name = ""
def button_selected():
	global root, name
	if len(listbox.curselection()) == 0:
		return
	index = listbox.curselection()[0]
	name = listbox.get(index)
	root.quit()
li_t = os.listdir('tool/pnt/')
print(li_t)
if li_t[0] in '.DS_Store':
	li_t.remove('.DS_Store')
li = []
for i in li_t:
	li.append(i.replace(".pnt", ""))
root = tk.Tk()
var = StringVar(value=li)
listbox = tk.Listbox(root,listvariable=var,height=len(li))
listbox.pack()
button = tk.Button(root, text="select", command=button_selected)
button.pack(pady=10)
root.mainloop()


from set import  *
import eel
from time import sleep

python_path = "/Users/kazuseida/anaconda3/envs/dev/bin/python"
cal = Calculator()

@eel.expose
def calculate():
	imobj = MImage("UI/image/temp.jpg")
	if imobj.setDatas():
		eel.second_background(10); line = imobj.getLandmark()
		eel.second_background(30); point = createPairPoints(line)
		eel.second_background(60); b_point = readFile("tool/pnt/" + name + ".pnt")
		eel.second_background(90); result = cal.getResult(b_point, point)
		sleep(0.1)
		eel.second_background(100)
		eel.result(int(result))
		print("tool/pnt/" + name + ".pnt")
	else :
		sys.exit()

def main():
	eel.init("./UI/")
	web_app_options = {
		'mode': "chrome-app", #or "chrome"
		'port': 8080,
		'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
	}
	eel.start("index.html", size=(2000, 1300))
	
if __name__ == '__main__':
	main()

