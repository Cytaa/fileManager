from folder import Folder
from os import system


class CmdMenu:

    def __init__(self):
        self.chooser = 0
        self.folder = Folder()
        self.createAMenu()

    def createAMenu(self):
        while self.chooser != 9:
            print(self.folder.getDir())
            print(""" 
1. Show whats in current directory
2. Go to parent directory
3. Go to child directory
4. Create new dir""")
            self.chooser = int(input("choose your option"))
            if self.chooser == 1:
                self.clear()
                self.folder.showMeDir()
            elif self.chooser == 2:
                self.folder.goToParDir()
                self.clear()
            elif self.chooser == 3:
                dir = input("insert dir name: ")
                self.folder.goToChilDir(dir)
                self.clear()
            elif self.chooser == 4:
                name = input("whats ur dirs name: ")
                self.folder.createADir(name)
                self.clear()

    def clear(self):

        if system == "nt":
            _ = self.clear()
        else:
            _ = system("clear")


menu = CmdMenu()
