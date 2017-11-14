import csv
def IsNumeric(x):
    try:
        float(x)
        return x
    except:
        return 0
f = open("D:/Recent.csv")
filereader = csv.DictReader(f)
mainDict={}
for row in filereader:  # Create a dictionary as a value to each state in the stateChurchList dictionary
    if mainDict.get(row["STABBR"]) != None:
        continue
    else:
        mainDict[row["STABBR"]] = [0] * 3        
f.seek(0)
for row in filereader:
    numOfStudents = IsNumeric(row["UGDS"])          
    veteran = IsNumeric(row["VETERAN"])         
    pnf = IsNumeric(row["CONTROL"]) 
    state = row["STABBR"]
    s = float(numOfStudents) * float(veteran)
    if pnf == "1":
        mainDict[state][0]+=s
    elif pnf == "2":
        mainDict[state][1]+=s
    elif pnf == "3":
        mainDict[state][2]+=s
for k,v in mainDict.items():
    if mainDict[k][0]+mainDict[k][1]<mainDict[k][2]:
        print "State", k, "has more veterans in for-profit in comparison with public and private schools!","Total:", int(v[2])

