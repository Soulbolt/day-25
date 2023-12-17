import pandas
# Read csv file that can then be printed and displayed as a table
data = pandas.read_csv("weather_data.csv")  # Can print individual columns: data["temp]"
print(data["temp"])
