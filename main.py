import csv
import operator
import sys
import string
import os
import pandas as pd

from os import listdir
from os.path import isfile, join


def getFilesInOrder(path):
    fileCounter = 0
    dictionary = {}
    for directory in getAllFirstLevelDirectories(path):
        for file in getAllFilesInFolder(directory):
            if file != "labels.dat":
                dictionary[fileCounter] = directory + "\\" + file
                fileCounter += 1
    return dictionary


def getAllFirstLevelDirectories(folderPath):
    return [f.path for f in os.scandir(folderPath) if f.is_dir()]


def getAllFilesInFolder(folderPath):
    return [f for f in listdir(folderPath) if isfile(join(folderPath, f))]


def compareFiles(originalDataFullPath, generatedDataFullPath, maxPercentageAllowableError):
    with open(originalDataFullPath, mode='rt') as original_csv_file, open(generatedDataFullPath, mode='rt', encoding='utf-16') as generated_csv_file:
        original_csv_lines = original_csv_file.readlines()
        generated_csv_lines = generated_csv_file.readlines()
        bla = original_csv_lines[1].strip()
        mappedData = [x.strip() for x in original_csv_lines]
        original_csv_lines = list(filter(lambda item: len(item) != 1, mappedData))

        numberOfLinesInOriginalData = len(original_csv_lines)
        numberOfLinesInGeneratedData = len(generated_csv_lines)

        if numberOfLinesInOriginalData != numberOfLinesInGeneratedData:
            exit(-7)

        for i in range(numberOfLinesInOriginalData):
            originalData = original_csv_lines[i].split(" ")
            generatedData = generated_csv_lines[i].split(" ")

            compareTimestamps(generatedData[0], originalData[0])

            compareValues(generatedData[1], originalData[1], maxPercentageAllowableError)


def compareTimestamps(generated_timestamp, original_timestamp):
    if original_timestamp.strip() != generated_timestamp.strip():
        exit(-2)


def compareValues(generatedValueStr, originalValueStr, maxAllowablePercentageDiff):
    originalValue = float(originalValueStr.strip())
    generatedValue = float(generatedValueStr.strip())

    if originalValue == generatedValue:
        return

    difference = originalValue - generatedValue

    percentageDifference = (1 - (originalValue - abs(difference)) / originalValue) * 100

    if maxAllowablePercentageDiff < round(percentageDifference, 5):
        exit(-3)


def sortTheShitFiles(fullFilePath):
    with open(fullFilePath) as original_csv_file:
        data = original_csv_file.readlines()
        data.sort(key=lambda row: int(row.split(" ")[0].strip()))

        filenNameLen = len(fullFilePath)
        with open(fullFilePath[0:filenNameLen - 4] + "_sorted.csv", 'w') as new_file:
            for row in data:
                new_file.write(row)
            new_file.flush()

def copyOfSortTheShitFiles(fullFilePath):
    counter = None
    with open(fullFilePath) as original_csv_file:
        data = original_csv_file.readlines()
        data.sort(key=lambda row: int(row.split(" ")[0].strip()))

        outputPath = fullFilePath.replace("low_freq", "output")
        filenNameLen = len(outputPath)
        with open(outputPath [0:filenNameLen - 4] + "_sorted.csv", 'w') as new_file:
            for row in data:
                if counter is None:
                    counter = int(row.split(" ")[0].strip())
                new_file.write(str(counter) + " " + row.split(" ")[1].strip() + "\n")
                counter += 1
            new_file.flush()

def writeFileXTimes(fullInputPath, numberOfRepeats,  outputDirectory):
    counter = None
    with open(fullInputPath) as original_csv_file:
        data = original_csv_file.readlines()
        data.sort(key=lambda row: int(row.split(" ")[0].strip()))

        splits = fullInputPath.split("\\")
        filename = splits[len(splits) - 1]

        with open(outputDirectory + "\\" + filename, 'w') as new_file:
            for x in range(numberOfRepeats):
                for row in data:
                    if counter is None:
                        counter = int(row.split(" ")[0].strip())
                    new_file.write(str(counter) + " " + row.split(" ")[1].strip() + "\n")
                    counter += 1
            new_file.flush()

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
                    print(fullFilePath + ";" + str(currentValue) + "has timestamps that decrease")
                    break
        # if not failedOnCurrentFile:
            # print("file: " + fullFilePath + " is fine")

def identidyIfFileHasFixedSamplingInterval(fullFilePath):
    SAMPING_ITERVAL = 1;
    prevValue = None
    failedOnCurrentFile = None
    with open(fullFilePath) as original_csv_file:
        for line in original_csv_file.readlines():
            currentValue = int(line.split(" ")[0].strip())
            if prevValue is None:
                prevValue = currentValue
            else:
                if prevValue + SAMPING_ITERVAL == currentValue:
                    prevValue = currentValue
                else:
                    failedOnCurrentFile = True
                    # print(fullFilePath + ";" + str(currentValue) + " contains gaps or does not have " + str(SAMPING_ITERVAL) + "as samplingInterval")
                    break
        if not failedOnCurrentFile:
            print("file: " + fullFilePath + " is fine")


def lowFrequencyPerformanceTestDataGeneration(fullFilePath, outputPath, percentOfDataAsHigh, howManyDataPointsToSkip):
    with open(fullFilePath) as original_csv_file:
        #assumes original data is sorted
        data = original_csv_file.readlines()
        # data.sort(key=lambda row: int(row.split(" ")[0].strip()))

        fullOutputPath = outputPath + "percentDataAsHighFreq_" + str(percentOfDataAsHigh) + "\\howManyDataPointsSkippedPerDataPoint_" + str(howManyDataPointsToSkip) + "\\"

        if not os.path.exists(fullOutputPath):
            os.makedirs(fullOutputPath)

        splits = fullFilePath.split("\\")
        filename = splits[len(splits) - 1]

        amountOfRows = len(data)
        amountOfRowsToProcess = int(amountOfRows * ((100 - percentOfDataAsHigh) / 100))

        with open(fullOutputPath + filename, 'w') as new_file:
            new_file.write("SI " + str((howManyDataPointsToSkip + 1) * 1000) + "\n")
            counter = 0
            for i in range(amountOfRowsToProcess):
                if counter == 0:
                    new_file.write(data[i])

                if counter == howManyDataPointsToSkip:
                    counter = 0
                else:
                    counter += 1

            new_file.write("SI 1000\n")
            for i in range(amountOfRowsToProcess, amountOfRows, 1):
                new_file.write(data[i])
            new_file.flush()


if __name__ == "__main__":
    args = sys.argv[1:]

    originalDataPath = args[0]
    generatedDataPath = args[1]
    # percentageAllowableError = float(args[2])

    originalFiles = getFilesInOrder(originalDataPath)
    # generatedFiles = getFilesInOrder(generatedDataPath)

    # if len(originalFiles) != len(generatedFiles):
    #     exit(-4)

    # highFrequentPercentageValues = [5,10,20,30,50,70,90]
    # howManyToSkip = [1,4,9,59]

    numberOfRepeats = 15
    for i in originalFiles:
        writeFileXTimes(originalFiles[i], numberOfRepeats, generatedDataPath)

    # for highFreq in highFrequentPercentageValues:
    #     for xToSkip in howManyToSkip:
    #         for i in originalFiles:

                # lowFrequencyPerformanceTestDataGeneration(originalFiles[i], generatedDataPath, highFreq, xToSkip)
                # compareFiles(originalFiles[i], generatedFiles[i], percentageAllowableError)
                # print(i)
                # copyOfSortTheShitFiles(originalFiles[i])

