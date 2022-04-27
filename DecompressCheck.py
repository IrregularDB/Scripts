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


def compare_timestamps(generated_timestamp, original_timestamp, threshold):
    
    difference = original_timestamp - generated_timestamp

    if threshold < abs(difference):
        exit(-2)


def compare_values(generatedValueStr, originalValueStr, error_bound):
    originalValue = float(originalValueStr.strip())
    generatedValue = float(generatedValueStr.strip())

    if originalValue == generatedValue:
        return

    difference = originalValue - generatedValue

    percentageDifference = (1 - (originalValue - abs(difference)) / originalValue) * 100

    if error_bound < round(percentageDifference, 5):
        exit(-3)


def compare_files(originalDataFullPath, generatedDataFullPath, error_bound, threshold):
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

            compare_timestamps(generatedData[1], originalData[1], threshold)

            compare_values(generatedData[2], originalData[2], error_bound)


def do_check():
    error_bound = 10 # Set to error_bound ingested with 
    threshold = 100 # Set to threshold ingested with

    originalFiles = getFilesInOrder("/home/simon/Development/REDD/sorted") # Set to original files that was ingested
    generatedFiles = getFilesInOrder("/home/simon/Development/REDD/decompressed") # Set to decompressed / recreted data file path

    for i in originalFiles:
        compare_files(originalFiles[i], generatedFiles[i], error_bound, threshold)


do_check()
