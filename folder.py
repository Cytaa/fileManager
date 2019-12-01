import os
import shutil


class Folder:

    def __init__(self):
        self.dir = os.getcwd()

    def getDir(self):
        return self.dir

    def findLastBack(self):

        for i in range(len(self.dir) - 1, -1, -1):
            if self.dir[i] == "\\":
                return i

    def prepPathToPar(self):

        nDir = []

        for i in range(self.findLastBack()):
            nDir.append(self.dir[i])

        nDir = "".join(nDir)

        return nDir

    def prepPathToChild(self, path):

        nDir = []

        for i in range(len(self.dir)):
            nDir.append(self.dir[i])

        nDir.append("\\")

        for i in range(len(path)):
            nDir.append(path[i])

        nDir = "".join(nDir)

        return nDir

    def setDir(self, path):
        os.chdir(path)
        self.dir = path

    def goToParDir(self):
        self.setDir(self.prepPathToPar())

    def goToChilDir(self, dirPath):
        self.setDir(self.prepPathToChild(dirPath))

    def showMeDir(self):
        root = self.dir

        for item in os.listdir(root):
            if os.path.isfile(os.path.join(root, item)):
                print(item + "\n")
            elif os.path.isdir(os.path.join(root, item)):
                print(item + "\n")

    def createADir(self, name):
        if not os.path.exists(name):
            os.mkdir(name)

    def copyAFile(self, file, dest):
        shutil.copy2(file, dest)

    def deleteDownloads(self):
        path = "C:\\Users\\" + os.getlogin() + "\\downloads"
        shutil.rmtree(path,True)

