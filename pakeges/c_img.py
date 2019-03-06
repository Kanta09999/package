from set import *
import matplotlib.pyplot as plt


img = MImage('./img/def.jpg')
landmarks = img.getLandmark()
for mark in landmarks :
	t = mark.split(",")
	try:
		x = round(float(t[0]),2)
		y = round(float(t[1]),2)
		print(x, y)
		plt.plot(x, -1 * y, 'bo')
	except Exception as e:
		print(type(e))
	
plt.show()
plt.pause(0.2)
plt.cla()
	