import shutil

def moveTextFromFile(filename, filename2):
    f = open(filename, "r")
    contents=f.read()
    dest = shutil.move(filename2, filename)
    tmp = open("test.txt","w+")
    tmp.write(contents)
    tmp.close()
    
def askForInputsAndMove():
    filename = input("Enter the file name: ")
    filename2 = input("Enter the second file name: ")
    moveTextFromFile(filename, filename2)

askForInputsAndMove()

answer = input('do you want to move another file?')
if (answer == 'y'):
    askForInputsAndMove()


