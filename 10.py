import csv
with open('D:/Recent.csv', 'rb') as f,open('D:/New.csv', 'wb') as f_out:
     reader = csv.DictReader(f)
     writer = csv.writer(f_out)
     writer.writerow(reader.fieldnames)
     for row in reader:
        if row["ICLEVEL"] == "1":
            values = [row[field] for field in reader.fieldnames]
            writer.writerow(values)