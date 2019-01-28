from tool.imports import *
"""-------------------------------------------------------------------keras----------------------------------------------------------------------------------"""
import keras
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import *
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.models import load_model
from keras.optimizers import *
from keras.preprocessing.image import *
from keras.applications.xception import Xception
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.applications.resnet50 import ResNet50
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.applications.mobilenet import MobileNet

class MyKeras:
    global X_train, X_test, y_train, y_test, model, loss, accuracy, history
    model_vgg16 = "./model_vgg16.h5"
    def __init__(self, X, Y, test=0.3, state=64):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, Y, test_size=test, random_state=state)
        self.model = Sequential()
        print("X_train shape", self.X_train.shape)
        print("X_test shape", self.X_test.shape)
        print("you should use 'resetModel(model)'")

    def resetModel(self, model):
        self.model = Sequential()
        self.model = model
        self.model.summary()

    def fit(self, epoch=50, batch=1, bose=1):
        self.history = self.model.fit(self.X_train, self.y_train, epochs=epoch, batch_size=batch, verbose=bose, validation_data=(self.X_test, self.y_test))
        return self.history

    def printTest(self, bose=0):
        self.loss, self.accuracy = self.model.evaluate(self.X_test, self.y_test, verbose=bose)
        print("loss : ", self.loss)
        print("accuracy : ", self.accuracy)

    def showResultOnPlot(self):
        plt.plot(self.history.history['acc'])
        plt.plot(self.history.history['val_acc'])
        plt.title('model accuracy')
        plt.xlabel('epoch')
        plt.ylabel('accuracy')
        plt.legend(['acc', 'val_acc'], loc='lower right')
        plt.show()
        plt.plot(self.history.history['loss'],)
        plt.plot(self.history.history['val_loss'])
        plt.title('model loss')
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend(loc='lower right')
        plt.show()

    def vgg16Set(self, num_cls):
        vgg16 = None
        if not os.path.exists(self.model_vgg16):
            input_shape = Input(self.X_train.shape[1:])
            vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_shape)
            self.save(name=self.model_vgg16)
        else :
             vgg16 = load_model(self.model_vgg16)
        model = Sequential()
        model.add(Flatten(input_shape=vgg16.output_shape[1:]))
        model.add(Dense(256, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(num_cls, activation='softmax'))
        model = Model(input=vgg16.input, output=model(vgg16.output))
        for layer in model.layers[:15]:
            layer.trainable=False  
        model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])
        self.model = model

    def save(self, name='model.h5'):
        self.model.save(name)