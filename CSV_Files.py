'''
CSV

Comma separated values
'''


path = './schedule.csv'
lines = [line for line in open(path)]
print(lines)
lines = [line.strip().split(',') for line in open(path)]
print(lines)


import csv

path = './schedule.csv'
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)  # omit 1st line
data = [row for row in reader]

print(header)
print(data[0])