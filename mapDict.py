
def mapDict(inputDict: dict, mapDict: dict) -> dict:

    outputDict = {}

    for inputKey in inputDict.keys():
        if inputKey in mapDict.keys():
            for iKey in range(len(mapDict[inputKey])-1, -1, -1):
                print(iKey)
                if iKey == len(mapDict[inputKey])-1:
                    subDict = {mapDict[inputKey][iKey].pop(): inputDict[inputKey]}

                elif iKey == 0:
                    outputDict[mapDict[inputKey][iKey].pop()] = subDict

                else:
                    subDict = {mapDict[inputKey][iKey].pop(): subDict}

    return outputDict


def main():
    inputDict = {'warmpress.fl': 1.56}
    dictMap = {'warmpress.fl': [['tyreFL'],['pTyreFL']]}

    outputDict = mapDict(inputDict, dictMap)
    print(outputDict)

if __name__ == '__main__':
    main()
