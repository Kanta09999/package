from tool.imports import *
"""-------------------------------------------------------------------csv----------------------------------------------------------------------------------"""
class DatabaseCSV:
    global file, li, column_datas
    def __init__(self, file):
        self.column_datas = []
        self.file = pd.read_csv(file)
        self.li = self.file.values.tolist()
        self.column_datas = self.file.T.values.tolist()
    def save(self, name='datas.csv'):
        self.file.to_csv(name)