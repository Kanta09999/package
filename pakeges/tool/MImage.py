from tool.imports import *
"""-------------------------------------------------------------------image----------------------------------------------------------------------------------"""
class MImage:
    global image, detector, predictor, lines, faces
    predictor_path = os.getcwd() + "/tool/dat/shape_predictor_68_face_landmarks.dat"
    face_cascade = cv2.CascadeClassifier(os.getcwd() + 'tool/case/haarcascade_frontalface_alt.xml')
    scaler = preprocessing.MaxAbsScaler()
    def __init__(self, image=None):
        self.image = io.imread(image)
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(self.predictor_path)
        try:
            self.faces = self.detector(self.image, 1)
        except Exception as e:
            print(type(e))
            
    def trim(self):
        for face in  self.faces:
            top = face.top()
            bottom = face.bottom()
            left = face.left()
            right = face.right()
        try:
            img = self.image[top:bottom, left:right]
        except Exception as e:
            pass
        return img, self.faces

    def setDatas(self, size=300):
        try:
            img, f = self.trim()
            if len(f) < 1:
                return False
            self.image = cv2.resize(img, (size, size))
            return True
        except Exception as e:
            raise e

    def getLandmark(self):
        try:
            img = self.image
            self.lines = ""
            dets = self.detector(img, 1)
            for d in dets:
                parts = self.predictor(img, d).parts()
            if len(parts) > 0:
                landmarks = np.array([[p.x, p.y] for p in self.predictor(img, dets[0]).parts()])
                #landmarks = max_abs_scaler.fit_transform(landmarks)
                landmarks = preprocessing.scale(landmarks)
                for i in range(len(landmarks)):
                    #landmarks[i] = landmarks[i] - landmarks[30]
                    self.lines += str(landmarks[i][0]) + "," +  str(landmarks[i][1]) + "\n"
            li = self.lines.split("\n")
            return li

        except Exception as e:
            return []
        

    def BGRtoRGB(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.image = image

    def getPoints(self):
        img = self.image
        self.lines = ""
        dets = self.detector(img, 1)
        for d in dets:
            parts = self.predictor(img, d).parts()
        return parts

    def  show(self):
        io.imshow(self.image)