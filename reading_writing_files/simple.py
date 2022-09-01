import csv
output = open('myCSV.CSV',mode='w')
mywriter=csv.writer(output)
header=['name','age']
mywriter.writerow(header)
data=['Bob Smith',40]
mywriter.writerow(data)
output.close()
