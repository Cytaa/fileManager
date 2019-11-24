import os


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

    def setDir(self, path):
        os.chdir(path)
        self.dir = path

    def goToParDir(self):
        self.setDir(self.prepPathToPar())


    def showMeDir(self):
        root = self.dir

        for item in os.listdir(root):
            if os.path.isfile(os.path.join(root,item)):
                print(item + "\n")
            elif os.path.isdir(os.path.join(root,item)):
                print(item + "\n")





folder = Folder()
print(folder.getDir())
folder.goToParDir()
print(folder.getDir())
folder.showMeDir()
