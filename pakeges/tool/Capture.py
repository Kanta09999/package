from tool.imports import *
"""--------------------------------------------------------------capture----------------------------------------------------------------------------------"""
class Capture:
    global face_cascade, cap, image, detector, predictor, lines
    dir = os.getcwd()
    predictor_path = dir + "/tool/dat/shape_predictor_68_face_landmarks.dat"
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('tool/case/haarcascade_frontalface_alt.xml')
        self.cap = cv2.VideoCapture(0)
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(self.predictor_path)

    def done(self):
        self.cap.release()
        cv2.destroyAllWindows()
        
    def trim(self, img):
        faces = self.face_cascade.detectMultiScale(img, 1.3, 5)
        for rect in faces:
            num = 150
            rect[1] = max(rect[1] - num, 1);
            rect[0] = max(rect[0] - num, 1);
            rect[3] = max(rect[3] + num * 2.25, 1);
            rect[2] = max(rect[2] + num * 1.5, 1);
            img = img[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
        return img, faces

    def start(self):
        while (True):
            ret, dst_image = self.cap.read()
            size = 300
            img, faces = self.trim(dst_image)#cv2.cvtColor(dst_image, cv2.COLOR_BGR2GRAY)
            re_image = img
            if len(faces) > 0:
                try: 
                    self.lines = ""
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = cv2.resize(img, (size, size))
                    dets = self.detector(img, 1)
                    for d in dets:
                        parts = self.predictor(img, d).parts()
                    if len(parts) > 0:
                        for part in parts:
                            self.lines += str(part.x) + "," + str(part.y) + "\n"    
                        break
                except Exception as e:
                    pass
                
            #cv2.imshow("frame", dst_image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.done()
        return re_image

    def startPic(self):
        ret, image = self.cap.read()
        return image

    def getLandmark(self):
        return self.lines

    def getLandmarkStrs(self):
        return self.lines.split("\n")

    def getLandmarkVal(self):
        li = self.getLandmarkStrs()
        returnVal = []
        for i in li :
            if(i is ''):
                break
            temp = i.split(",")
            returnVal.append([int(temp[0]), int(temp[1])])
        return returnVal