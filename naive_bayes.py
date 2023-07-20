# import pandas as pd

def separate_by_class(dataset):
  separated = dict()
  
  for i in range(len(dataset)):
    vector = dataset[i]
    class_value = vector[-1]
    if (class_value not in separated):
      separated[class_value] = list()
    separated[class_value].append(vector)
  
  return separated

def mean(numbers):
  return sum(numbers) / float(len(numbers));

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

separated = separate_by_class(dataset)

for label in separated:
  print(label)
  for row in separated[label]:
    print(row)

# df = pd.read_csv('employee_vehicle.csv')
sp_class = separate_by_class(df)

print(sp_class)