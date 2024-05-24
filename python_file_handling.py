# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all 
# files and subdirectories in a given directory. Your script 
# should prompt the user for the directory filePath and then 
# display the contents.

# Expected Outcome: The script should correctly list all files
# and subdirectories in the specified directory. Handle exceptions 
# for invalid paths or inaccessible directories.

import os

def displayDirectory(filePath):
    try:
        if os.filePath.exists(filePath):
            print("DIRECTORY:", filePath)
            # List all files and subdirectories in the given filePath
            for item in os.listdir(filePath):
                print(item)
        else:
            print("DIRECTORY DOESN'T EXIST!")
    except Exception as e:
        print("ERROR:", e)

directoryPath = input("ENTER PATH OF FILE: ")

displayDirectory(directoryPath)

# Task 2: File Size Reporter:

# Problem Statement: Write a Python program that reports 
# the sizes of all files in a specific directory. The program 
# should ask the user for a directory directoryPath and then print each 
# file's name and size within that directory.

# Expected Outcome: Your program should display the name and size 
# (in bytes) of each file in the given directory. Ensure that the 
# program only reports on files, not directories, and handles any 
# errors gracefully.

import os

try:
    directoryPath = input("PATH OF DIRECTORY: ")

    if os.directoryPath.exists(directoryPath):
        print("SIZE OF DIRECTORY:", directoryPath)
        for file in os.listdir(directoryPath):
            pathOfFile = os.directoryPath.join(directoryPath, file)
            if os.directoryPath.isfile(pathOfFile):
                file_size = os.directoryPath.getsize(pathOfFile)
                print(f"{file}- {file_size}")
    else:
        print("DIRECTORY DOES NOT EXIST!")
except Exception as e:
    print("ERROR:", e)

# Task 3: File Extension Counter:

# Problem Statement: Develop a Python script that counts the 
# number of files of each extension type in a directory. For 
# instance, in a directory with five '.txt' files and three '.py' 
# files, the script should report "TXT: 5" and "PY: 3".

# Expected Outcome: The script should accurately num and display 
# the number of files for each extension type in the specified directory. 
# Handle different cases of file extensions (e.g., '.TXT' and '.txt' should 
# be considered the same).

import os

try:
    directoryPath = input("DIRECTORY PATH: ")

    if os.directoryPath.exists(directoryPath):
        print("NUMBER OF FILE EXT. IN DIRECTORY:", directoryPath)
        numExtensions = {}

        for file in os.listdir(directoryPath):
            pathOfFile = os.directoryPath.join(directoryPath, file)
            if os.directoryPath.isfile(pathOfFile):
                extOfFile = os.directoryPath.splitext(file)[1].lower()
                numExtensions[extOfFile] = numExtensions.get(extOfFile, 0) + 1
        
        for extension, num in numExtensions.items():
            print(f"{extension.upper()}: {num}")
    else:
        print("ERROR: DIRECTORY DOES NOT EXIST!")
except Exception as e:
    print("ERROR:", e)

# Task 1: Email Extractor:

# Problem Statement: Write a Python script to extract all 
# email addresses from a given text file (contacts.txt). 
# The file contains a mix of text and email addresses.

# Expected Outcome: The script should output a list of 
# all unique email addresses found in the file. Utilize 
# regex to accurately identify email addresses amidst other text.

import re
import os

def extractEmail(filename):
    try:
        with open(filename, 'r') as file:
            fileData = file.read()
            emailFormat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
            uniqueEmails = set(re.findall(emailFormat, fileData))
            return uniqueEmails
    except Exception as e:
        print("ERROR:", e)
        return []

fileData = """
Contact List:
John Doe - john.doe@example.com
Jane Smith - jane.smith@gmail.com

For inquiries, please contact info@example.com
"""
filename = "contacts.txt"
with open(filename, 'w') as file:
    file.write(fileData)

emails = extractEmail(filename)

print("UNIQUE EMAILS:")
for email in emails:
    print(email)

os.remove(filename)

# Task 2: Historical Weather Data Compiler

# Problem Statement: Compile and analyze historical weather data from 
# multiple files (weather_2020.txt, weather_2021.txt, etc.). Each file 
# contains daily temperature data. Calculate the average temperature for 
# each year and identify the year with the highest average.

# Expected Outcome: An aggregated view of average temperatures
# for each year and identification of the year with the highest
# average temperature, showcasing data aggregation and analysis skills.

import os

def avgTemp(year, temperatures):
    yearlyTemp = [int(temp.split(",")[1].rstrip("°C")) for temp in temperatures if temp.startswith(year)]
    return sum(yearlyTemp) / len(yearlyTemp) if yearlyTemp else 0

def displayTemps(filePath):
    with open(filePath) as file:
        return file.read().split()

def processTempData(directory):
    avgTemps = {}
    for filename in os.listdir(directory):
        if filename.startswith("weather_data") and filename.endswith(".txt"):
            year = filename.split("_")[1].split(".")[0]
            temperatures = displayTemps(os.path.join(directory, filename))
            avgTemps[year] = avgTemp(year, temperatures)
    maxAvgYr = max(avgTemps, key=avgTemps.get)
    maxAvgTemp = avgTemps[maxAvgYr]
    return avgTemps, maxAvgYr, maxAvgTemp

directory = "weather_data"
avgTemps, maxAvgYr, maxAvgTemp = processTempData(directory)

print("AVG TEMPS:")
for year, avgTemp in avgTemps.items():
    print(f"{year}: {avgTemp}°C")
print(f"\nYEAR OF HIGHEST AVG TEMP: {maxAvgYr} ({maxAvgTemp}°C)")
