import sys
import string
import os

from os import listdir
from os.path import isfile, join

def getAllFirstLevelDirectories(folderPath):
    return [f.path for f in os.scandir(folderPath) if f.is_dir()]


def getAllFilesInFolder(folderPath):
    return [f for f in os.listdir(folderPath) if isfile(join(folderPath, f))]

def getFilesInOrder(path):
    fileCounter = 0
    dictionary = {}
    for directory in getAllFirstLevelDirectories(path):
        for file in getAllFilesInFolder(directory):
            if file != "labels.dat":
                dictionary[fileCounter] = directory + "/" + file
                fileCounter += 1
    return dictionary

def identidyIfFileHasDescendingTimestamps(fullFilePath):
    prevValue = None
    failedOnCurrentFile = None
    with open(fullFilePath) as original_csv_file:
        for line in original_csv_file.readlines():
            currentValue = int(line.split(" ")[0].strip())
            if prevValue is None:
                prevValue = currentValue
            else:
                if prevValue < currentValue:
                    prevValue = currentValue
                else:
                    failedOnCurrentFile = True
                    print(fullFilePath + ";" + str(currentValue) + " has timestamps out of order")
                    break
        # if not failedOnCurrentFile:
            # print("file: " + fullFilePath + " is fine")

dictionary = getFilesInOrder("/home/simon/Development/REDD/low_freq")

for entry in dictionary.values():
    identidyIfFileHasDescendingTimestamps(entry)