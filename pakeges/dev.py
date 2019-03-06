from set import  *

model = loadH5("Pose.h5")
boolean = False
img = None


def subProcess(q, arr, v, switch):
	while v.value == 0:
		try:
			img = q.get()
			value = judge(img)
			print(value)
			if len(value) > 0:
				arr[0] = value[0][0]
				arr[1] = value[0][1]
			else :
				arr[0] = 9999
				arr[1] = 9999
			switch.value = 0
		except Exception as e:
			print(type(e))

def mainProcess(q, arr, v, switch):
	global img
	cap = cv2.VideoCapture(0)
	while True:
		try:
			_, image = cap.read()
			dst_image = image
			img = image
			height =img.shape[0]
			width = img.shape[1]
			dst_image =  cv2.resize(dst_image, (int(width*1.35), int(height*1.35)))
			if switch.value == 0:
				q.put(dst_image)
				switch.value = -1
			val = model.predict(np.array([arr[:]]))
			#cv2.putText(画像, 文字, 左下座標, フォント, 文字の大きさ, 色, 文字の太さ, 線の種類)
			if val > 0.5:
				cv2.putText(dst_image, 'OK', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2, cv2.LINE_AA)
			cv2.imshow("", dst_image)
			if cv2.waitKey(1) & 0xFF == ord(' '):
				v.value = 1
				break
		except Exception as e:
			print(type(e))
	cap.release()
	cv2.destroyAllWindows()
	cv2.imwrite('UI/image/temp.jpg', img)

def takePic():
	q = Queue()
	v = Value('i', 0)
	switch = Value('i', 0)
	array = Array('i', 2)

	init_p = Process(target=initProcess, args=(array, ))
	init_p.start()
	init_p.join()

	sub_p = Process(target=subProcess, args=(q, array, v, switch))
	sub_p.start()

	mainProcess(q, array, v, switch)



def main():
	takePic()
	#test()
	#MainApp().run()

	

	

if __name__ == '__main__':
	main()
	