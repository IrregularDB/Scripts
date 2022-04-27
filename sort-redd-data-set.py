import re
import sys
import string
import os

from os import listdir
from os.path import isfile, join

def getFilesInOrder(path):
    fileCounter = 0
    dictionary = {}
    for directory in getAllFirstLevelDirectories(path):
        for file in getAllFilesInFolder(directory):
            if file != "labels.dat":
                dictionary[fileCounter] = directory + "/" + file
                fileCounter += 1
    return dictionary
    

def getAllFirstLevelDirectories(folderPath):
    return [f.path for f in os.scandir(folderPath) if f.is_dir()]


def getAllFilesInFolder(folderPath):
    return [f for f in os.listdir(folderPath) if isfile(join(folderPath, f))]


def sortTheShitFiles(fullFilePath):
    with open(fullFilePath) as original_csv_file:
        data = original_csv_file.readlines()
        data.sort(key=lambda row: int(row.split(" ")[0].strip()))

        fullFilePath = fullFilePath.replace("low_freq", "Sorted")
        
        
        filenNameLen = len(fullFilePath)
        

        slashIndices = [i.start() for i in re.finditer('/', fullFilePath)]

        houseNumber = fullFilePath[int(slashIndices[len(slashIndices) - 2] + 1):int(slashIndices[len(slashIndices) - 1])]

        channelNumber = fullFilePath[int(slashIndices[len(slashIndices) - 1] + 1):len(fullFilePath) - 4]

        with open(fullFilePath[0:filenNameLen - 4] + "_sorted.csv", 'w') as new_file:
            for row in data:
                split = row.split(" ")
                new_file.write(houseNumber + "-" + channelNumber + " " + str(int(split[0])*1000) + " " + split[1])
            new_file.flush()


dictionary = getFilesInOrder("/home/simon/Development/REDD/low_freq")

for entry in dictionary.values():
    sortTheShitFiles(entry)

