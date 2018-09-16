import os

# file_paths = []  # List which will store all of the full filepaths.
#
# for root, directories, files in os.walk(os.curdir):
#     for filename in files:
#         # Join the two strings in order to form the full filepath.
#         filepath = os.path.join(root, filename)
#         file_paths.append(filepath)  # Add it to the list.
#
# print(file_paths)

sourceFilePath = os.path.join(os.getcwd(), 'SourceFile.txt')

print(sourceFilePath)

sourceFile = open(sourceFilePath)

print(sourceFile)

lineCounter = 0
for line in sourceFile:
    # print(line)
    lineCounter += 1

print(lineCounter)
sourceFile.close()

catalogueName = 'Output'

newCataloguePath = os.path.join(os.getcwd(), catalogueName)

os.makedirs(newCataloguePath, exist_ok=True)

sourceFile = open(sourceFilePath)

numberOfLines = 100

tempList = []

fileNumberCounter = 0
loopCounter = numberOfLines
for line in sourceFile:
    loopCounter += 1
    if (loopCounter >= numberOfLines):
        loopCounter = 0
        fileNumberCounter += 1

        outputFile = open(os.path.join(newCataloguePath, 'File_Lines' + str(fileNumberCounter) + '.txt'), 'w')

        for l in tempList:
            outputFile.write(l)

        outputFile.close()
        tempList = []

        print("Next file: " + str(fileNumberCounter))

    tempList.append(line)
    print(line)

sourceFile.close()

print("-------------------------")

tempList = []

sourceFile = open(sourceFilePath)

numberOfFiles = 19
loopCounter = 0
fileNumberCounter = 0
for line in sourceFile:
    loopCounter += 1

    middle = loopCounter - 0.5

    if (middle > (fileNumberCounter * lineCounter) / numberOfFiles):
        fileNumberCounter += 1

        outputFile = open(os.path.join(newCataloguePath, 'File_Files' + str(fileNumberCounter) + '.txt'), 'w')

        for l in tempList:
            outputFile.write(l)

        outputFile.close()

        tempList = []

        print("Next file: " + str(fileNumberCounter))

    tempList.append(line)
    print(line)

sourceFile.close()
