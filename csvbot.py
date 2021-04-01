import csv
s=""
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:   
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            s += row[0] "." + row[1] + " starts from " + row[2] "onwards and ends in"+ row[3] "website link" + row[4] 
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
   # print(f'Processed {line_count} lines.')
    print(s)
