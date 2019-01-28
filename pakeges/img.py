from set import *
import matplotlib.pyplot as plt

positions = [[12, 27], [12, 39], [14, 59], [15, 59], [16, 59], [16, 67]]
model = loadH5("Pose.h5")
dir = os.listdir('./img/')
def_image = cv2.imread('./def.jpg')

for path in dir:
	if '.jpg' in path:
		print(path)
	else:
		continue
	base = MImage('./img/' + path)
	j1 = judge(base.image)
	v1 = model.predict(j1)
	if v1 < 0.5:
		print('change//val:' + str(v1))
	else:
		print('base image ' + path )
		break
base_landmarks = base.getLandmark()
b_f = base.setDatas()
if b_f == False: 
	sys.exit()

for path in dir:
	try:
		t = def_image
		if '.jpg' in path or '.jpeg' in path:
			pass
		else:
			continue
		imobj = MImage('./img/' + path)
		j2 = judge(imobj.image)
		v2 = model.predict(j2)
		if v2 < 0.5:
			print('pass' + path)
			continue
		if imobj.setDatas():
			landmarks = imobj.getLandmark()
			for landmark in base_landmarks:
				try:
					t = landmark.split(",")
					x = float(t[0])
					y = float(t[1])
					plt.plot(x, y * -1, 'ro')

				except Exception as e:
					pass
			for landmark in landmarks:
				try:
					t = landmark.split(",")
					x = float(t[0])
					y = float(t[1])
					plt.plot(x, y * -1, 'bo')
				except Exception as e:
					print(type(e))
					pass
		print("o", path)
		plt.show()
		plt.pause(0.2)
		plt.cla()
	except Exception as e:
		pass
	