class States(object):
    def __init__(self, statesArr):
        self.statesArr = statesArr;

    def getByName(self, name):
        for i in self.statesArr:
            if i[0] == name:
                return i[1]
