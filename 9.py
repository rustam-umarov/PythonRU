from collections import defaultdict
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def IsNumeric(x):
    try:
        x=float(x)
        return x
    except:
        return 0
def IsZero(x):
    if x==0:
        return 1
    return x
f=codecs.open("D:/Recent.csv","r",encoding="utf-8-sig")
filereader = csv.DictReader(f)
mainDict=defaultdict(lambda: defaultdict(float))
for row in filereader:  # Create a dictionary as a value to each state in the stateChurchList dictionary
        mainDict[row["STABBR"]] = ["Public",0,0,"Private",0,0,"For-profit",0,0]
f.seek(0)

for row in filereader:
    completionRate = row["C100_4"]
    state = row["STABBR"] 
    schoolType = row["CONTROL"]
    if schoolType=="1":
        mainDict[state][1]+=IsNumeric(completionRate)
        mainDict[state][2]+=1
    elif schoolType=="2":
        mainDict[state][4]+=IsNumeric(completionRate)
        mainDict[state][5]+=1        
    elif schoolType=="3":
        mainDict[state][7]+=IsNumeric(completionRate)
        mainDict[state][8]+=1
for k,v in mainDict.items():
    print k, "has following average: ","\n", v[0],":",v[1]/IsZero(v[2]),"\n", v[3],":",v[4]/IsZero(v[5]), "\n", v[6],":",v[7]/IsZero(v[8]),"\n","/////////////////////////////////"  