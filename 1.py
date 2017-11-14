import csv
f = open("D:/Recent.csv")
filereader = csv.DictReader(f)
EngineerDict={}
def IsNumeric(x):
    try:
        x = float(x)
        return x
    except:
        return 0
for row in filereader:
    State = row["STABBR"]
    Total = IsNumeric(row["OVERALL_YR4_N"])
    Percentage = IsNumeric(row["PCIP14"])
    State = row["STABBR"]
    if Percentage>0 and Total>0:
        if EngineerDict.get(State)<>None:
            EngineerDict.update({State:(EngineerDict.get(State)+Percentage*Total)})
        else:
            EngineerDict[State] = Percentage*Total
key, value = max(EngineerDict.iteritems(), key=lambda x:x[1])
print key,"has maximum number of Engineers, which is", value 


