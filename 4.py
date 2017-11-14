from collections import defaultdict
import csv
def IsNumeric(x):
    try:
        x=int(x)
        return x
    except:
        return 0
f = open("D:/Recent.csv")
filereader = csv.DictReader(f)
mainDict=defaultdict(lambda: defaultdict(int))
for row in filereader:  # Create a dictionary as a value to each state in the stateChurchList dictionary
    if mainDict.get(row["STABBR"]) != None:
        continue
    else:
        mainDict[row["STABBR"]] = {"students in 4-year colleges": 0,"students in 2-year colleges": 0}
f.seek(0)
for row in filereader:     
    fourYear = IsNumeric(row["FIRSTGEN_YR4_N"])         
    twoYear = IsNumeric(row["FIRSTGEN_YR2_N"]) 
    state = row["STABBR"]
    mainDict[state]["students in 4-year colleges"]+=IsNumeric(fourYear) 
    mainDict[state]["students in 2-year colleges"]+=IsNumeric(twoYear)
for k,v in mainDict.items():    
    for innerkey, val in v.items():
        if mainDict[k]["students in 4-year colleges"]>mainDict[k]["students in 2-year colleges"]:
            print "In", k, "there are more students in 4-year colleges. Total is", mainDict[k]["students in 4-year colleges"]
        else:
            print "In", k, "there are more students in 2-year colleges. Total is", mainDict[k]["students in 2-year colleges"]

