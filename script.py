#Function to display the best score.

def display(best):
    print "\n\n"
    print "Best score is :- " + str(best[0])
    print "  "
    
    for i in range(1,((len(best) - 1)/2) + 1):
        print "--------------------------------------------------"
        print best[i]
        print best[i + 1]
        print "--------------------------------------------------"
    

#Function for finding best score from the two lists having all permutations.

def bestscore(seqlst1,seqlst2):
    finalscore = [0,'First sequence','Second sequence']
    for i in seqlst1:
        for j in seqlst2:
            if len(i) < len(j):
                for k in range(0,(len(j) - len(i)) + 1):
                    if k != 0:
                        i.insert(k - 1,"*")
                        #print i
                    tempscore = scoreit(i,j)    
                    if tempscore > finalscore[0]:
                        finalscore = [0,'First sequence','Second sequence']
                        finalscore[0] = tempscore
                        finalscore[1] = i
                        finalscore[2] = j
                    if tempscore == finalscore[0]:
                        finalscore.append(i)
                        finalscore.append(j)
                    """if k != 0:
                        i.remove('*')"""
            elif len(j) <= len(i):
                for k in range(0,(len(i) - len(j)) + 1):
                    if k != 0:
                        j.insert(k - 1,"*")
                        #print j
                    tempscore = scoreit(i,j)    
                    if tempscore > finalscore[0]:
                        finalscore = [0,'First sequence','Second sequence']
                        finalscore[0] = tempscore
                        finalscore[1] = i
                        finalscore[2] = j
                    if tempscore == finalscore[0]:
                        finalscore.append(i)
                        finalscore.append(j)
                    """if k != 0:
                        i.remove('*')"""
    #print seqlst1
    #print seqlst2
    display(finalscore)
    
                        

#Function for scoring.

def scoreit(ss1,ss2):
    score = 0
    if len(ss1) < len(ss2):
        for i in range(0,len(ss1)):
            if ss1[i] != '-' and ss1[i] != '*' and ss1[i] == ss2[i]:
                score = score + 1
    else:
        for i in range(0,len(ss2)):
            if ss2[i] != '-' and ss1[i] == ss2[i]:
                score = score + 1
    return score

#Adding single indel and doing permutation.

def addpermute(se):
    lst = []
    for i in range(0,len(se) + 1):
        se.insert(i,"-")
        tempse = []
        for j in range(0,len(se)):
            tempse.append(se[j])
        lst.append(tempse)
        se.pop(i)
    #print lst
    return lst
    
#Number of times

def permute(listSequence1,listSequence2,numberOfIndels1,numberOfIndels2):
    lst1 = [listSequence1]
    start1 = 1
    lst2 = [listSequence2]
    start2 = 1

    #First string permutations.
    
    for j in range(0,numberOfIndels1):
        firstlength1 = len(lst1)
        for i in range(firstlength1 - start1,firstlength1):
            templstt1 = addpermute(lst1[i])
            for k in range(len(templstt1)):
                 lst1.append(templstt1[k])
        secondlength1 = len(lst1)
        start1 = secondlength1 - firstlength1

    #Second string permutations.
        
    for j in range(0,numberOfIndels2):
        firstlength2 = len(lst2)
        for i in range(firstlength2 - start2,firstlength2):
            templstt2 = addpermute(lst2[i])
            for k in range(len(templstt2)):
                 lst2.append(templstt2[k])
        secondlength2 = len(lst2)
        start2 = secondlength2 - firstlength2

    """

    for i in range(0,len(lst1)):
        #print lst1[i]

    print str("  ")
    print "--------------------------------------------------"
    print str("  ")
    
    for i in range(0,len(lst2)):
        print lst2[i]

    """

    bestscore(lst1,lst2)
            
        
#Input the DNA sequence in string and maximum number of indels.

DNASequences1 = raw_input("Enter the first string :- ")
DNASequences2 = raw_input("Enter the second string :- ")
numberOfIndels1 = int(raw_input("Maximum number of indels in first sequence :- "))
numberOfIndels2 = int(raw_input("Maximum number of indels in second sequence :- "))

#Finding the length of both strings.

lengthOfSequence1 = len(DNASequences1)
lengthOfSequence2 = len(DNASequences2)

#Converting DNA strings dnas1 and dnas2 into list namely s1 and s2.

listSequence1 = []

for i in range(0,lengthOfSequence1):
    listSequence1.append(DNASequences1[i])
    
listSequence2 = []

for i in range(0,lengthOfSequence2):
    listSequence2.append(DNASequences2[i])

#Calling  Permutations

permute(listSequence1,listSequence2,numberOfIndels1,numberOfIndels2)





