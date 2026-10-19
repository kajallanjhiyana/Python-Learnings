# with open("Concepts/filesystem/data/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Concepts/filesystem/data/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("Concepts/filesystem/data/weather_data.csv")
print(type(data)) #<class 'pandas.DataFrame'> -> A DataFrame is a table with rows and columns, just like an Excel sheet.
print(type(data["temp"])) #<class 'pandas.Series'> -> A Series is a single column of data from a DataFrame.

temp_list = data["temp"].to_list()
print(temp_list)

#Get data in columns
print(data["condition"])
print(data.condition)

#Get data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

#Create a dataframe from scratch
data_dict = {
    "students": ["emily", "pani", "da", "khatti", "mitthi"],
    "scores": [20, 0, 100, 50, 25]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Concepts/filesystem/data/students_data.csv")