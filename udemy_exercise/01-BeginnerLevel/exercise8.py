'''
@name calculate_love_score() 
@desc Calculates the love score between two names 
@input name1 - the name of person 1 
@input name2 - the name of person 2 
@return The love score of the user 
'''
def calculate_love_score(name1, name2):
    tCount = 0
    rCount = 0
    uCount = 0
    eCount = 0
    lCount = 0
    oCount = 0
    vCount = 0
    veCount = 0 
    nameLists = []
    name1char = list(name1.lower())
    for i in name1char:
        nameLists.append(i)

    for j in list(name2.lower()):
        nameLists.append(j)

    for k in nameLists:
        match k:
            case "t":
                tCount = tCount + 1
            case "r":
                rCount = rCount + 1
            case "u":
                uCount = uCount + 1
            case "e":
                eCount = eCount + 1
    trueScore = tCount + rCount + uCount + eCount
    for k in nameLists:
        match k:
            case "l":
                lCount = lCount + 1
            case "o":
                oCount = oCount + 1
            case "v":
                vCount = vCount + 1
            case "e":
                veCount = veCount + 1
    loveCount = lCount + oCount + vCount + veCount
    print("Love Score = " + str(trueScore) + str(loveCount))       
calculate_love_score("Kanye West", "Kim Kardashian")