import csv
import sys

from tabulate import tabulate
if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments ')
if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments ')
if not sys.argv[1].endswith('.csv'):
    sys.exit('Not a csv file')
try:
     with open(sys.argv[1]) as file:
        reader= csv.reader(file)
        first_line= next(reader)
        rows=[]
        for row in reader:
            rows.append(row)
        print(tabulate(rows, headers=first_line, tablefmt="grid"))
except FileNotFoundError:
    sys.exit('File not found')