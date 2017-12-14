#/*****************************************
#* Author: Kyle De Laurell
#* Date: 10/11/2017
#* Description: This is the source file
#* that reads an amount.txt file of numbers and
#* uses dynamic programming to find the min
#* number of coins and utputs an array of optimal coins
#*******************************************/

V = []
lineCoins = True
testFile = open ("change.txt", "w")

with open ("amount.txt", "r") as myfile:
    for line in myfile:
        if lineCoins:
            lineCoins = False
            numbers = line.split()
            V = []
            for num in numbers:
                V.append(int(num))
            #print("V = " + str(V))
            testFile.write("V = " + str(V) + "\n")
            ###print(V)
        else:
            lineCoins = True
            AValue = line.split()
            for a in AValue:
                A = int(a)
            #print("A = " + str(A))
            testFile.write("A = " + str(A) + "\n")
            ###print(A)
            r = [[0 for x in range(A + 1)] for y in range(len(V) + 1)]
            s = [[0 for x in range(len(V))] for y in range(A + 1)]
            for i in range(1, A + 1):
                r[0][i] = i
                #s[0][i] = 0
            C = []
            for j in range(1, len(V) + 1):
                #s[j] = 0
                ##print
                for i in range(1, A + 1):
                    if V[j - 1] == i:
                        r[j][i] = 1
                        for x in range(0, len(V)):
                            s[i][x] = 0
                        s[i][j-1] = 1
                        ##print("i = " + str(i))
                        ##print(s[i])
                    elif V[j - 1] > i:
                        r[j][i] = r[j-1][i]
                        for x in range(0, len(V)):
                            s[i][x] = s[i][x]
                        ##print("i = " + str(i))
                        ##print(s[i])
                    else:
                        r[j][i] = min(r[j-1][i], 1 + r[j][i-V[j-1]])
                        if r[j][i] == r[j-1][i]:
                            ###print("i = " + str(i))
                            for x in range(0, len(V)):
                                s[i][x] = s[i-1][x]
                            s[i][0] = s[i][0] + 1
                            ###print(s[i])
                        else:
                            ###print("i = " + str(i))
                            ###print("PATH 2")
                            for x in range(0, len(V)):
                                s[i][x] = s[i-V[j-1]][x]
                            #s[i] = s[i-V[j-1]]
                            s[i][j-1] = s[i][j-1] + 1
                            ###print(s[i])
            ##print s

            for j in range(1, len(V) + 1):
                for i in range(1, A + 1):
                    ##print
                    ##print s[i],
                    ##print r[j][i],
                    if(j == len(V) and i == A):
                        ##print
                        #print("ANSWER = " + str(r[j][i]))
                        ##print(r[j][i])
                        #print s[i]
                        testFile.write("C[] = " + str(s[i]) + "\n")
