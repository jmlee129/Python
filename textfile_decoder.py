__author__ = 'juniormints'

import random
import sys
import os
import matplotlib.pyplot as plt

class TextFileDecoder:
    __fileName = ''
    __recipe = ''
    __chamber = ''
    __time = []
    __batch = ''
    __parsedText = []
    __processes = 0

    def __init__(self, fileName):
        self.__fileName = fileName

    def parseText(self):
        text_file = open(self.__fileName)
        tempParsedText = text_file.read().split('\n')
        counter = 0
        for index in range(len(tempParsedText)):
            tempList = tempParsedText[index].split(',')
            if tempList[0] == 'Process Step':
                counter += 1
            if tempList[len(tempList) - 1] == '':
                tempList = tempList[:-1]
            self.__parsedText.extend(tempList)
        self.__processes = counter

    def sortInfo(self):
        self.__recipe = self.__parsedText[1]
        self.__chamber = self.__parsedText[3]
        self.__time = self.__parsedText[4:7]
        self.__batch = self.__parsedText[8]
        self.__parsedText = self.__parsedText[9:]

    def graphData(self):
        for index in range(self.__processes):
            self.sortProcess(index)

    def sortProcess(self, num):
        counter = 2
        numParameters = 0
        processStep = []
        number = ''
        while self.__parsedText[counter] != str(num):
            processStep.append(self.__parsedText[counter])
            counter += 1
        number = self.__parsedText[counter]
        counter += 2
        parameters = []
        while self.__parsedText[counter] != 'Demands':
            numParameters += 1
            parameters.append(self.__parsedText[counter])
            counter += 1
        demands = []
        counter += 1
        while self.__parsedText[counter] != 'Readbacks':
            parameters.append(self.__parsedText[counter])
            counter += 1
        readbacks = {}
        readbackCount = 0
        while self.__parsedText[counter] == 'Readbacks':
            counter += 1
            readbackCount += 1
            readbacks['lst_%s' % readbackCount] = []
            for index in range(numParameters):
                readbacks['lst_%s' % readbackCount].append(self.__parsedText[counter])
                counter += 1
            if counter == len(self.__parsedText):
                break





test = TextFileDecoder('TKFGaPPhC13_Etch.txt')
test.parseText()
test.sortInfo()
test.sortProcess(1)