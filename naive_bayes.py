# import pandas as pd
from math import sqrt

def separate_by_class(dataset):
  separated = dict()
  
  for i in range(len(dataset)):
    vector = dataset[i]
    class_value = vector[-1]
    if (class_value not in separated):
      separated[class_value] = list()
    separated[class_value].append(vector)
  
  return separated

# Calculate the mean of a list of numbers
def mean(numbers):
  return sum(numbers) / float(len(numbers))

# Calculate the standard deviation of a list of numbers
def stdev(numbers):
  avg = mean(numbers)
  variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers) - 1)
  return sqrt(variance)

# Calculate the mean, stdev and count for each column in a dataset
def summarize_dataset(dataset):
  summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
  del(summaries[-1])
  return summaries

# Test separating data by class
dataset = [
  ["Laki-laki", 20, 8000000, "Single", "Kendaraan pribadi"],
  ["Laki-laki", 35, 14000000, "Single", "Kendaraan umum"],
  ["Perempuan", 26, 10000000, "Single", "Kendaraan umum"],
  ["Perempuan", 27, 12000000, "Menikah", "Kendaraan pribadi"],
  ["Laki-laki", 21, 9000000, "Single", "Kendaraan pribadi"],
  ["Laki-laki", 22, 11000000, "Single", "Kendaraan pribadi"],
  ["Perempuan", 32, 15000000, "Menikah", "Kendaraan umum"],
  ["Perempuan", 26, 8000000, "Menikah", "Kendaraan umum"],
  ["Laki-laki", 25, 9000000, "Single", "Kendaraan umum"],
  ["Perempuan", 20, 10000000, "Single", "Kendaraan pribadi"]
]

# separated = separate_by_class(dataset)

# for label in separated:
#   print(label)
#   for row in separated[label]:
#     print(row)

summary = summarize_dataset(dataset)
print(summary)

# print(separate_by_class(separated))

# df = pd.read_csv('employee_vehicle.csv')
# sp_class = separate_by_class(df)

# print(sp_class)