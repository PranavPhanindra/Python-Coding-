import csv

def CsvToDict(filename) :
    with open(filename,'r') as thecsvfile :
        reader = csv.DictReader(thecsvfile)
        for row in reader:
            print(row) 



filename = input("Enter the csv filename : " )
CsvToDict(filename)
