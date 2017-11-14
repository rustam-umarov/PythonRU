import codecs
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def IsNumeric(x):
    try:
        x=int(x)
        return x
    except:
        return 0
f = codecs.open("D:/Recent.csv","r",encoding="utf-8-sig")
s = codecs.open("D:/sal2014_is.csv","r",encoding="utf-8-sig")
mainReader = csv.DictReader(f)
schoolId = csv.DictReader(s)
schoolNumber={}
schoolList={}
salaryByState={}
meanDict={}
for k in schoolId:
    if k["ARANK"]=="7":
        schoolList[k["UNITID"]]=k["SAOUTLT"] 
for i in mainReader:
        if schoolNumber.get(i["STABBR"])<>None:
               schoolNumber.update({i["STABBR"]:(schoolNumber.get(i["STABBR"]) + 1)})      
        else:
            schoolNumber[i["STABBR"]] = 1
f.seek(0)
for row in mainReader:
    if schoolList.get(row["UNITID"])!=None:
        if salaryByState.get(row["STABBR"])<>None:
                salaryByState.update({row["STABBR"]:(salaryByState.get(row["STABBR"]) + IsNumeric(schoolList.get(row["UNITID"])))})      
        else:
                salaryByState[row["STABBR"]] = IsNumeric(schoolList.get(row["UNITID"]))  
for key in schoolNumber.keys():
   meanDict[key]=salaryByState[key] / schoolNumber[key]
print meanDict

