class FileRead:

    def readFile(file_path, mode):
        data = open(file_path,mode, encoding='utf-8')

        with data as file:
            lines = file.readlines()
            for line in lines:
                print(line[0:-1])

        data.close()
        return lines

    def getCount(lines):
        count =0 
        for line in lines:
            for char in line:
                if char == '*':
                    count +=1
        return count
        

if __name__ == "__main__":

    filePath = input("Enter file path to read: ")
    mode = input("Enter mode: ")

    lines = FileRead.readFile(filePath, mode)

    count = FileRead.getCount(lines)

    print (f"Total '*' count in the file: {count}")
    
    #C:/YooBee/PSE/Docs/3280709.txt