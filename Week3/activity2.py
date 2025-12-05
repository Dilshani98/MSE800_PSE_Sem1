# Append String in the text file
class FileRead:

    def __init__(self, filePath, appendContent): #initialize with self param
        self.filePath = filePath
        self.appendContent = appendContent

    def appendFile(self): # append required text
        with open(self.filePath, "a") as file:
            print(self.appendContent)
            file.write(self.appendContent + "\n")
            file.close()

    def printFile(self): #print file content
        data = open(self.filePath,"r", encoding='utf-8')

        with data as file:
            lines = file.readlines()
            for line in lines:
                print(line[0:-1])

        data.close()
        

if __name__ == "__main__":

    #define file path & content to append
    filePath = "C:/YooBee/PSE/Docs/3280709.txt"
    appendContent = "End of File"

    obj = FileRead(filePath, appendContent) #create object

    obj.appendFile() #call methods

    obj.printFile()
   