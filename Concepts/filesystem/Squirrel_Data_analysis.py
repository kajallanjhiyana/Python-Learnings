import pandas

data = pandas.read_csv("Concepts/filesystem/data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261019.csv")
# d = {
#     "Black" : 0,
#     "Gray" : 0,
#     "Cinnamon" : 0
# }

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
d =  {
          "Fur color" : ["Black", "Gray", "Cinnamon"],
          "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
    }

print(d)
df = pandas.DataFrame(d)
df.to_csv("Concepts/filesystem/data/squirrel_count.csv")

# k = (data["Primary Fur Color"])
# for i, j in k.items():
#     if j == "Black":
#         d["Black"] += 1
#     elif j == "Gray":
#         d["Gray"] += 1
#     elif j == "Cinnamon":
#         d["Cinnamon"] += 1
# df = pandas.DataFrame(d, index = [0]) # The dictionary contains individual values and doesn't contains any list or dict stuff so we will need pass an index otherwise it will throw error
# df.to_csv("Concepts/filesystem/data/Squirrel_color.csv")
