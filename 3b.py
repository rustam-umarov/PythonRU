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
statesDict={}
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
f.seek(0)
for c in filereader:
    if IsNumeric(c["UGDS"]):
        statesDict.update({c["STABBR"]:statesDict.get(c["STABBR"],0) + float(c["UGDS"])})
for k,v in mainDict.items():
    print "State", k, "has", int(mainDict[k][0])/statesDict[k],"% of Public", int(mainDict[k][1])/statesDict[k],"% of Profit and", int(mainDict[k][2])/statesDict[k],"% of For-profit students"


            