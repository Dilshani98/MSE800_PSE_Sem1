class FileRead:

    def __init__(self, filePath, mode):
        self.filePath = filePath
        self.mode = mode

    def readFile(self):
        data = open(self.filePath,self.mode, encoding='utf-8')

        with data as file:
            lines = file.readlines()
            for line in lines:
                print(line[0:-1])

        data.close()
        return lines

    def getCount(self,lines):
        count =0 
        for line in lines:
            for char in line:
                if char == '*':
                    count +=1
        return count
        

if __name__ == "__main__":

    filePath = "C:/YooBee/PSE/Docs/3280709.txt"
    mode = "r"

    obj = FileRead(filePath, mode) 

    lines = obj.readFile()

    count = obj.getCount(lines)

    print (f"Total '*' count in the file: {count}")