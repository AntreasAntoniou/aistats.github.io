import sys
import os

data_dir = "/home/antreas/antreasantoniou.github.io/committee.csv"
target_dir = "/home/antreas/antreasantoniou.github.io/committee.txt"
with open(data_dir, mode="r") as open_csv:
    data = open_csv.readlines()

data = data[1:]
output_file = []

for entry in data:
    name, surname, institution, email = entry.split(",")
    entry_line = "<li><p>{name} {surname}    ({institution}) </li></p>\n".format(name=name, surname=surname,
                                                                          institution=institution)
    output_file.append(entry_line)

with open(target_dir, mode="wb+") as write_file:
    write_file.writelines(output_file)
