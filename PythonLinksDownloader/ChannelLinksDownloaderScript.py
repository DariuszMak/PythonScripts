import os
import urllib.request, re
from bs4 import BeautifulSoup
# file_paths = []  # List which will store all of the full filepaths.
#
# for root, directories, files in os.walk(os.curdir):
#     for filename in files:
#         # Join the two strings in order to form the full filepath.
#         filepath = os.path.join(root, filename)
#         file_paths.append(filepath)  # Add it to the list.
#
# print(file_paths)

# file = open(os.path.join(os.getcwd(), 'SourceFile.txt')).read()
# soup = BeautifulSoup(file, "html.parser")

sourceFilePath = os.path.join(os.getcwd(), 'SourceFile.txt')

print(sourceFilePath)

sourceFile = open(sourceFilePath, mode="r", encoding="utf-8")

print(sourceFile)

regularExpression = r"https://www.youtube.com/watch\?v=(.*?)\""

setoflinks = []

result = None


for line in sourceFile:
    result = re.findall(regularExpression, line)

    for r in result:

        if r:
            #print(r)
            setoflinks.append(r)

sourceFile.close()


outputFile = open(os.path.join(os.getcwd(), 'OutputFile.txt'), 'w')

for x in setoflinks:
    completeString = "https://www.youtube.com/watch?v=" + x

    print(completeString)
    outputFile.write(completeString + '\n')

outputFile.close()