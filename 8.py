import csv
import xlrd
from heapq import nlargest
import codecs
import operator
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def IsNumeric(x):
    try:
        x=float(x)
        return x
    except:
        return 0
f=codecs.open("D:/Recent.csv","r",encoding="utf-8-sig")
xlBook = xlrd.open_workbook("D:/CollegeScorecardDataDictionary-08-18-2016.xlsx")
xlSheet = xlBook.sheet_by_name('data_dictionary')
filereader = csv.DictReader(f)
rate={}
myValue={}
degreeRate={}
Columns=["PCIP"+str(x) for x in range(1,54)]
for i in range(296,334):
    myValue[xlSheet.cell(i,4).value]=xlSheet.cell(i,0)
for row in filereader:
    if row["ICLEVEL"]=="1" and IsNumeric(row["FIRST_GEN"])!=0:
        rate[row["INSTNM"]] = row["FIRST_GEN"]
ratePure = dict((k, v) for k, v in rate.iteritems() if v != "NULL")
schools = nlargest(4, ratePure.items(), key=lambda k: k[1])
schoolsDict = dict(schools)
top = [x[0] for x in schools]
f.seek(0)
for r in filereader:
    for i in range(0,len(top)):
        if r["INSTNM"] == top[i]:
            for key in myValue.keys():
                if r[key] !=None:
                    degreeRate[myValue[key]] = IsNumeric(r[key])
                    sorted_x = sorted(degreeRate.items(), key=operator.itemgetter(1), reverse=True)
            print "Rate in",top[i],"is",ratePure[top[i]]
            for d in range(0,3):
                print sorted_x[d]