from folder import Folder





class CmdMenu:

    def __init__(self):
        self.chooser = 0
        folder = Folder()

        while self.chooser != 9:
            print(""" 
1. Show your current directory
2. Show whats in current directory
2. Go to parent directory
3. Go to child directory""")
            self.chooser = int(input("choose ur option"))
            if self.chooser == 1:
                print(folder.getDir())
            elif self.chooser == 2:
                folder.showMeDir()

        

    def nextOption(self):
        pass






menu = CmdMenu()
