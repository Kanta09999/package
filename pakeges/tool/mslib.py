from tool.Capture import *
from tool.PyMySQL import *
from tool.MImage import *
from tool.DatabaseCSV import *
from tool.ObjectData import *
from tool.imports import *

from tool.MyKeras import * #nerul network
from tool.lib_c import * #Mac for



""" 
v  script

"""
def sendInf():
    pass

def createPairPoints(points):
    returnValue = [ ]
    positions = [[12, 27], [12, 39], [14, 59], [15, 59], [16, 59], [16, 67]]
    for pos in positions:
        v1, v2 = points[pos[0]].split(",")
        v3, v4 = points[pos[1]].split(",")
        print(str(round(float(v1), 2)) + str(",") + str(round(float(v2), 2)))
        points[pos[0]] = str(round(float(v1), 2)) + str(",") + str(round(float(v2), 2))
        points[pos[1]] = str(round(float(v3), 2)) + str(",") + str(round(float(v4), 2))
        returnValue.append(points[pos[0]] + str(",") +  points[pos[1]])
    return returnValue

def saveImage(path, img):
    cv2.imwrite(path, img)

def saveFile(lines, path):
    file = open(path, 'w')
    val = ""
    for line in lines:
        val += line + "/"
    file.write(val)
    file.close()

def readFile(name):
    file = open(name)
    data = file.read()
    lis = data.split("/")
    lis.pop()
    file.close()
    return lis

def loadH5(name='model.h5'):
    model = load_model(name)
    return model

def createImg_data(path, size=(64, 64)):
    img = load_img(path, target_size=size)
    img_array = img_to_array(img)
    return np.reshape(img_array, (1, size[0], size[1], img_array.shape[2]))

def run(cmd):
    subprocess.run(cmd.split())