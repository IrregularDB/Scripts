import os

from os import listdir
from os.path import isfile, join
from pickletools import long1


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


def compare_timestamps(generated_timestamp, original_timestamp, threshold):
    
    difference = int(original_timestamp) - int(generated_timestamp)

    if threshold < abs(difference):
        print("failed: code 2 fail on timestamp check: " + "difference " + str(difference) + ", org " + str(original_timestamp) + ", generated " + str(generated_timestamp))
        raise Exception("timestamp compare failed")


def compare_values(generatedValueStr, originalValueStr, error_bound):
    originalValue = float(originalValueStr.strip())
    generatedValue = float(generatedValueStr.strip())

    if originalValue == generatedValue:
        return

    difference = originalValue - generatedValue

    if originalValue == 0:
        print("Original value is 0, generated value: " + str(generatedValue))
        raise Exception("original value 0")

    percentageDifference = (1 - (originalValue - abs(difference)) / originalValue) * 100

    #smallBoundBuffer = 0.005
    if (error_bound) < round(percentageDifference, 10):
        print("Error bound:" + error_bound)
        print("percentageDifference: " + percentageDifference)
        print("failed: code 3")
        exit(-3)


def compare_files(originalDataFullPath, generatedDataFullPath, error_bound, threshold):
    with open(originalDataFullPath, mode='rt') as original_csv_file, open(generatedDataFullPath, mode='rt') as generated_csv_file:
        original_csv_lines = original_csv_file.readlines()
        generated_csv_lines = generated_csv_file.readlines()

        mappedData = [x.strip() for x in original_csv_lines]
        original_csv_lines = list(filter(lambda item: len(item) != 1, mappedData))

        numberOfLinesInOriginalData = len(original_csv_lines)
        numberOfLinesInGeneratedData = len(generated_csv_lines)

        if numberOfLinesInOriginalData != numberOfLinesInGeneratedData:
            print("failed: code 7")
            print("Failed for files: " + originalDataFullPath + " AND: " + generatedDataFullPath)
            exit(-7)

        previouseTime = -1
        for i in range(numberOfLinesInOriginalData):
            originalData = original_csv_lines[i].split(" ")
            generatedData = generated_csv_lines[i].split(" ")
            currentTime = int(generatedData[1])

            if currentTime <= previouseTime:
                print("EXCEPTION: timestamp is lower than previous timestamp")
                print(currentTime)
                exit(1)

            previouseTime = currentTime

            try:
                compare_timestamps(generatedData[1], originalData[1], threshold)
                compare_values(generatedData[2], originalData[2], error_bound)
            except:
                print("EXCEPTION: Originalpath: " + originalDataFullPath + " Generated path: " + generatedDataFullPath + " timestampO: " + originalData[1] + " timestampG: " + generatedData[1])
                exit(-100)

def do_check():
    print("hejsa")
    error_bound = 10 # Set to error_bound ingested with
    threshold = 1000 # Set to threshold ingested with

    originalFiles = getFilesInOrder("/home/simon/Development/REDD/IntegrationTestVerification") # Set to original files that was ingested
    generatedFiles = getFilesInOrder("/home/simon/Development/REDD/decompressed") # Set to decompressed / recreted data file path

    originalFilesList = sorted(originalFiles.values())
    generatedFilesList = sorted(generatedFiles.values())

    for i in range(len(originalFilesList)):
        print("Comparing: " + originalFilesList[i] + ", with: " + generatedFilesList[i])
        compare_files(originalFilesList[i], generatedFilesList[i], error_bound, threshold)

    print("Success")

do_check()
