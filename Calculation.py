import csv
import statistics

with open('SOCR-HeightWeight.csv', newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

weight_list = []

for i in file_data[2]:
    weight_list.append(float(i))

mean = statistics.mean(weight_list)
median = statistics.median(weight_list)
mode = statistics.mode(weight_list)

print(f"Mean is :- {mean}")
print(f"Median is :- {median}")
print(f"Mode is :- {mode}")
