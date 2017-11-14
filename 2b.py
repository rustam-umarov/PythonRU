import operator
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
f = open("D:/Recent.csv")
filereader = csv.DictReader(f)
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
publicSchoolVeterans = {}
privateSchoolVeterans = {}
for k,v in mainDict.items():
   publicSchoolVeterans[k] = mainDict[k][0]
sorted_x = sorted(publicSchoolVeterans.items(), key=operator.itemgetter(1),reverse=True)
for k,v in mainDict.items():
   privateSchoolVeterans[k] = mainDict[k][1]
sorted_x_public = sorted(publicSchoolVeterans.items(), key=operator.itemgetter(1),reverse=True)
sorted_x_private = sorted(privateSchoolVeterans.items(), key=operator.itemgetter(1),reverse=True)
for k,v in sorted_x_public:
    print k, "has",int(v),"veterans in public schools"
print "********************************************************"
for k,v in sorted_x_private:
    print k, "has",int(v),"veterans in private schools"



            