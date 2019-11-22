import os


class Folder:

    def __init__(self):
        self.getDir()

    def getDir(self):

        self.dir = os.getcwd()

        return dir

    def findPar(self, path):

        for i in range(len(path) - 1, -1, -1):
            if path[i] == "\\":
                return i


    def getParDir(self, path, lastBack):

        nDir = []

        for i in range(lastBack):
            nDir.append(path[i])

        nDir = "".join(nDir)
        
        return nDir 

    def setDir(self, path):
        os.chdir(path)

    def goToParDir(self):
        pass
        


folder = Folder()
folder.getParDir(folder.dir, folder.findPar(folder.dir))