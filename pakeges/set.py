from tool.mslib import *
from multiprocessing import *


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("tool/dat/shape_predictor_68_face_landmarks.dat")


def getLandmark(img):
	rects  = detector(img, 1)
	if len(rects) <= 0:
		pass
	else :
		landmarks = np.array([[p.x, p.y] for p in predictor(img, rects[0]).parts()])
		return landmarks
	return []
def logic(landmark):
    landmark = np.array(landmark)
    chin = landmark[30]
    landmark[17] = abs(landmark[17] - chin)
    landmark[12] = abs(landmark[12] - chin)
    landmark[4] = abs(landmark[4] - chin)
    landmark[26] = abs(landmark[26] - chin)
        
    t1 = abs(landmark[17] - landmark[12]) + 1
    t2 = abs(landmark[4] - landmark[26]) + 1
    val = [(t2[0] * t1[0]), (t1[1] * t2[1])]
    return val

def judge(img):
    landmark = getLandmark(img)
    if len(landmark) > 0:
        val = logic(landmark)
        val = np.array([val])
        return val
    return np.array([[999, 999]])

def initProcess(arr):
    arr[0] = 9999
    arr[1] = 9999
