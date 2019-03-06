from tool.imports import *
"""-------------------------------------------------------------------B-File----------------------------------------------------------------------------------"""
class ObjectData:
    global file, path
    def __init__(self, file=None, path=None):
        self.file = file
        self.path = path

    def load(self):
        self.file = open(self.path, 'r')
        re = pickle.load(self.file)
        self.close()
        return re

    def loadB(self):
        self.file = open(self.path, 'rb')
        re = pickle.load(self.file)
        self.close()
        return re

        
    def save(self, data):
        self.file = open(self.path, 'wb')
        pickle.dump(data, self.file)
        self.close()
        

    def close(self):
        self.file.close
