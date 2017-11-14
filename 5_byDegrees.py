########SORT!!!!!
from collections import OrderedDict
from collections import defaultdict
import csv
def IsNumeric(x):
    try:
        float(x)
        return x
    except:
        return 0
f = open("D:/Recent.csv")
filereader = csv.DictReader(f)
mainDict=defaultdict(lambda: defaultdict(int))
statesDict=defaultdict(lambda: defaultdict(int))
for row in filereader:  # Create a dictionary as a value to each state in the stateChurchList dictionary
    if mainDict.get(row["STABBR"]) != None:
        continue
    else:
        mainDict[row["STABBR"]] = {"Non-degree":0, "Certificate":0,"Associate":0,"Bachelors":0,"Graduate":0}
f.seek(0)
for row in filereader:                 
    pnf = IsNumeric(row["HIGHDEG"])
    state = row["STABBR"]
    if pnf == "0":
        mainDict[state]["Non-degree"]+=1
    elif pnf == "1":
        mainDict[state]["Certificate"]+=1
    elif pnf == "2":
        mainDict[state]["Associate"]+=1
    elif pnf == "3":
        mainDict[state]["Bachelors"]+=1
    elif pnf == "4":
        mainDict[state]["Graduate"]+=1
for k, value in mainDict.items():
        print k, "has the following", (sorted(value.items(), key=lambda x: x[1], reverse = True))
        
