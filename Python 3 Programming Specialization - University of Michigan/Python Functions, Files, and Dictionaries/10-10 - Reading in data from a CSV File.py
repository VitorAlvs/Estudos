import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#We are able to read in CSV files the same way we have with other text files. Because of the standardized structure of the data, there is a common pattern for processing it. To practice this, we will be using data about olympic events.
#Typically, CSV files will have a header as the first line, which contains column names. Then, each following row in the file will contain data that corresponds to the appropriate columns.
#All file methods that we have mentioned - `read`, `readline`, and `readlines`, and simply iterating over the file object itself - will work on CSV files. In our examples, we will iterate over the lines. Because the values on each line are separated with commas, we can use the `.split()` method to parse each line into a collection of separate value.
fileconnection = open("10-4Doc1.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {} - {}".format(
                vals[0],
                vals[4],
                vals[5]))