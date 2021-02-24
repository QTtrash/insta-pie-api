import csv
import os.path
data_folder = os.path.join("insta-pie-api", "src", "api", "User")

file_to_open = os.path.join(data_folder, "result.csv")


def group():
    users = []
    with open(file_to_open) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=";")
        for row in csvReader:
            users.append(row[0])

    users = users[1:]
    return users
