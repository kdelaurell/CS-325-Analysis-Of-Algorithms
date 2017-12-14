#/*****************************************
#* Author: Kyle De Laurell
#* Date: 10/22/2017
#* Description: This is the python file that
#* reads in start and stop times from act.txt
#* sorts them and then uses a greedy algorithm
#* to find the optimal solution
#*******************************************/

def mergeSort(startSet, left, right, endSet, timeSet):
    if left < right:

        middle = (left+(right-1))/2

        mergeSort(startSet, left, middle, endSet, timeSet)
        mergeSort(startSet, middle+1, right,endSet, timeSet)
        merge(startSet, left, middle, right, endSet, timeSet)

def merge(startArr, start, mid, end, endArr, timeArr):
    lenL = mid - start + 1
    lenR = end- mid


    L = [0] * (lenL)
    R = [0] * (lenR)
    L2 = [0] * (lenL)
    R2 = [0] * (lenR)
    L3 = [0] * (lenL)
    R3 = [0] * (lenR)


    for i in range(0 , lenL):
        L[i] = startArr[l + i]
        L2[i] = endArr[l + i]
        L3[i] = timeArr[l + i]

    for j in range(0 , lenR):
        R[j] = startArr[m + 1 + j]
        R2[j] = endArr[m + 1 + j]
        R3[j] = timeArr[m + 1 + j]


    i = 0
    j = 0
    k = l

    while i < lenL and j < lenR :
        if L[i] <= R[j]:
            startArr[k] = L[i]
            endArr[k] = L2[i]
            timeArr[k] = L3[i]
            i += 1
        else:
            startArr[k] = R[j]
            endArr[k] = R2[j]
            timeArr[k] = R3[j]
            j += 1
        k += 1

    while i < lenL:
        startArr[k] = L[i]
        endArr[k] = L2[i]
        timeArr[k] = L3[i]
        i += 1
        k += 1

    while j < lenR:
        startArr[k] = R[j]
        endArr[k] = R2[j]
        timeArr[k] = R3[j]
        j += 1
        k += 1


def greedyLtoS(startArr, endArr, timeArr, optimalArr):
    n = len(startArr)
    optimalArr.append(timeArr[n-1])
    lastIndex = n - 1
    for x in range(n - 2, 0, -1):
        testIndex = lastIndex

        if(endArr[x] <= startArr[testIndex]):
            optimalArr.append(timeArr[x])
            lastIndex = x


#opens act.txt file for reading
with open ("act.txt", "r") as myfile:
    #initializes variables
    counter = 0
    setCounter = 0

    #loops through each line of file to gather data
    for line in myfile:
        if counter == 0:
            counter = 1
            setCounter += 1
            lineCounter = 0
            print 'Set ', setCounter
            ANum = line.split()
            for a in ANum:
                numActivities = int(a)
            timeIndexSet = []
            startTimeSet = []
            endTimeSet = []
            optimalSet = []
        else:
            act = line.split()
            inlineCount = 0
            #loops throught the line checking getting start and finish times
            for sf in act:
                if inlineCount == 0:
                    actNum = int(sf)
                    inlineCount += 1
                    timeIndexSet.append(int(sf))
                elif inlineCount == 1:
                    startTimeSet.append(int(sf))
                    inlineCount += 1
                elif inlineCount == 2:
                    endTimeSet.append(int(sf))
            lineCounter += 1
            if lineCounter == numActivities:
                counter = 0
                mergeSort(startTimeSet, 0, numActivities - 1, endTimeSet, timeIndexSet)
                greedyLtoS(startTimeSet, endTimeSet, timeIndexSet, optimalSet)
                print 'Number of activities listed: ', len(optimalSet)
                print optimalSet
