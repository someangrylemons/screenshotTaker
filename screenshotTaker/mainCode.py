import pyautogui as pag
import os
from time import sleep

def findCoordinatesOfBoxDrawnByTwoCursorPositions ():
    '''
    This program will find the coordinates at two separate mouse position and then calculate the coordinates of a box
    connecting them. The coordinates of the box will be returned in (x , y , width, height) where ( x , y ) indicate
    the top left corner of the box.

    :return:
    '''
    input('When ready input anything')
    countDown()
    topLeftCorner = pag.position()
    print("move to next location")
    countDown()
    bottomRightCorner = pag.position()
    print("Top left " + str(topLeftCorner) + ' --- Bottom right ' + str(bottomRightCorner))
    x1 = topLeftCorner[0]
    y1 = topLeftCorner[1]
    x2 = bottomRightCorner[0]
    y2 = bottomRightCorner[1]
    width = x2 - x1
    height = y2 - y1
    boxCoordinates = (x1 , y1 , width , height)
    print(boxCoordinates)
    return boxCoordinates

def collectScreenshotsOfBoxAtGivenCoordinates (coordinates:tuple, nameOfImage:str, relativePathForDirectory:str, numberOfScreenshotsToMake:int=50, needToMakeDirectory=False,  ):
    scriptDirectory = os.getcwd()
    if needToMakeDirectory == True:
        newDirectoryName = os.path.join(scriptDirectory, relativePathForDirectory)
        os.makedirs(newDirectoryName)
    absoluteName = os.path.join(scriptDirectory, relativePathForDirectory)
    for i in range (numberOfScreenshotsToMake):
        imageName = os.path.join(absoluteName, nameOfImage)
        imageNameWithExtension = imageName + str(i+1) + '.png'
        pag.screenshot(imageNameWithExtension, region=coordinates)
        print('Captured image, saved to ' + imageNameWithExtension)
        sleep(0.1)

def collectScreenshotsOfBoxAtCursorPositions (nameOfImage, relativePathForDirectory, numberOfScreenshotsToMake=50, needToMakeDirectory=False) :
    boxCorners = findCoordinatesOfBoxDrawnByTwoCursorPositions()
    print('coordinates found: ' + str(boxCorners))
    sleep(0.25)
    collectScreenshotsOfBoxAtGivenCoordinates(boxCorners, nameOfImage , relativePathForDirectory , numberOfScreenshotsToMake , needToMakeDirectory)

def countDown (countdownFromX=5):
    for i in range(countdownFromX):
        print(countdownFromX-i)
        sleep(1)


if __name__ == '__main__':
    collectScreenshotsOfBoxAtCursorPositions( 'testsRound2' , 'testing\\test3' , numberOfScreenshotsToMake=9 , needToMakeDirectory=False)