from screenshotTaker import mainCode

def cursorInput(nameOfImage, relativePathForDirectory, numberOfScreenshotsToMake=50, needToMakeDirectory=False):
    mainCode.collectScreenshotsOfBoxAtCursorPositions(nameOfImage, relativePathForDirectory, numberOfScreenshotsToMake, needToMakeDirectory)

def coordinateInput (coordinates:tuple, nameOfImage:str, relativePathForDirectory:str, numberOfScreenshotsToMake:int=50, needToMakeDirectory=False,):
    mainCode.collectScreenshotsOfBoxAtGivenCoordinates(coordinates, nameOfImage, relativePathForDirectory, numberOfScreenshotsToMake, needToMakeDirectory,)