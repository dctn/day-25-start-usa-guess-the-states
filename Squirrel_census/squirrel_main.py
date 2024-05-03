# import csv
#
# with open(file="weather-data.csv") as file:
#
#     csv_data = csv.reader(file)
#     for i in csv_data:
#         print(i)
# °F = (°C × 1.8) + 32
import pandas

# Central-Park-Squirrel-Census-Squirrel-Data
# Primary Fur Color

animal_data = pandas.read_csv("Squirrel_census/Central-Park-Squirrel-Census-Squirrel-Data.csv")
animal_color_data = animal_data["Primary Fur Color"]

animal_color_data_list = animal_color_data.to_list()
gray = 0
cinnamon = 0
black = 0
for i in animal_color_data_list:
    if i == "Gray":
        gray += 1
    elif i == "Cinnamon":
        cinnamon += 1
    else:
        black += 1

color_data = {"color": ["gray", "red","black"],
              "count": [gray,cinnamon,black]}

data = pandas.DataFrame(color_data)
data.to_csv("goal.csv")