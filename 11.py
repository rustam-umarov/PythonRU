import csv
with open('D:/Recent.csv','r') as f,open('D:/11.csv','wb') as f_out:
     reader = csv.DictReader(f)
     writer = csv.writer(f_out)
     fieldnames=["INSTNM", "STABBR", "OVERALL_YR4_N", "UGDS", "VETERAN",
            "CONTROL", "POVERTY_RATE", "HIGHDEG", "FIRSTGEN_YR2_N", "FIRSTGEN_YR4_N",
            "ICLEVEL", "SCH_DEG", "FIRST_GEN", "PREDDEG", "C100_4", "RET_FT4"]
     writer.writerow(fieldnames)
     for row in reader:
            writer.writerow([row["INSTNM"],row["STABBR"],row["OVERALL_YR4_N"],row["UGDS"],row["VETERAN"],row["CONTROL"],row["POVERTY_RATE"],row["HIGHDEG"],row["FIRSTGEN_YR2_N"],row["FIRSTGEN_YR4_N"],row["ICLEVEL"],row["SCH_DEG"],row["FIRST_GEN"],row["PREDDEG"],row["C100_4"],row["RET_FT4"]])