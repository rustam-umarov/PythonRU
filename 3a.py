import csv
def IsNumeric(x):
    try:
        float(x)
        return x
    except:
        return 0
f = open("D:/MERGED2014_15_PP.csv")
filereader = csv.DictReader(f)
mainDict={}
for row in filereader:  # Create a dictionary as a value to each state in the stateChurchList dictionary
    if mainDict.get(row["STABBR"]) != None:
        continue
    else:
        mainDict[row["STABBR"]] = [0] * 3        
f = open("D:/Recent.csv")
filereader = csv.DictReader(f)
for row in filereader:
    numOfStudents = IsNumeric(row["UGDS"])                   
    pnf = IsNumeric(row["CONTROL"])
    povertyRate = IsNumeric(row["POVERTY_RATE"]) 
    state = row["STABBR"]
    s = float(numOfStudents) * float(povertyRate)
    if pnf == "1":
        mainDict[state][0]+=s
    elif pnf == "2":
        mainDict[state][1]+=s
    elif pnf == "3":
        mainDict[state][2]+=s
for k,v in mainDict.items():
    print "State", k, "has", int(mainDict[k][0]/100),"Public", int(mainDict[k][1]/100),"Profit and", int(mainDict[k][2]/100),"For-profit students at schools"



            