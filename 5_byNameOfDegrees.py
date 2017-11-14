from collections import OrderedDict
from collections import defaultdict
import csv
import xlrd
def IsNumeric(x):
    try:
        x=float(x)
        return x
    except:
        return 0
def IsNumericInt(x):
    try:
        x=int(x)
        return x
    except:
        return 0
f=open("D:/Recent.csv")
xlBook = xlrd.open_workbook("D:/CollegeScorecardDataDictionary-08-18-2016.xlsx")
xlSheet = xlBook.sheet_by_name('data_dictionary')
myValueDict={}
for i in range(296,334):
    myValueDict[xlSheet.cell(i,4).value]=xlSheet.cell(i,0)
filereader = csv.DictReader(f)
Columns=["PCIP"+str(x) for x in range(0,54)]
schoolNumber=defaultdict(lambda: defaultdict(int))
for row in filereader:
    for key in myValueDict.keys():
        if row[key] != None:
            value = IsNumeric(row[key])*IsNumeric(row["UGDS"])
            schoolNumber[row["STABBR"]][key]+=IsNumericInt(value)
for key,value in schoolNumber.items():
        ordered = OrderedDict(sorted(value.items(), key=lambda x: x[1], reverse=True))
        orderedKeys = ordered.keys()
        orderedValues = ordered.values()
        a = 0
        if len(ordered) > 3:
            a = 3
        else:
            a = len(ordered)

        print "State: {}".format(key)
        for i in range(0, a):
            print "{} - {}".format(myValueDict[orderedKeys[i]], int(orderedValues[i]))