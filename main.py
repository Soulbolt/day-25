import pandas

# Read csv file that can then be printed and displayed as a table
# data = pandas.read_csv("weather_data.csv")  # Can print individual columns: data["temp]"
# print(data["temp"])

# Convert csv to  dictionary
# data_dict = data.to_dict()
# print(data_dict)
# Convert column to a list
# temp_list = data["temp"].tolist()
# print(temp_list)
# Find average temp
# average = sum(temp_list) / len(temp_list)
# print(f"Average temp: {average}")
# Pandas way to find average
# print(f"Pandas way: {data["temp"].mean()}")
# Pandas way to find Max value
# print(f"Max value: {data["temp"].max()}")
# Can print columns with this convention. Panda converts headings to objects for accessibility
# print(data.condition)
# Get Data in row
# print(data[data.day == "Monday"])
# Get data in row with the highest Temp: data[condition]
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# Convert Mondays temp from Celsius to Fahrenheit
# print((data.temp[0]*9/5) + 32)

# Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# Save into a csv file
# data.to_csv("new_data.csv")
# Use csv data to retrieve count of squirrels fur color and count then create a new DataFrame
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_color_count)
print(cinnamon_color_count)
print(black_color_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color_count, cinnamon_color_count, black_color_count]
}

squirrel_data = pandas.DataFrame(data_dict)
print(squirrel_data)
squirrel_data.to_csv("Squirrel_count.csv")
