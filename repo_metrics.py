import csv
import dateparser # can probably find a faster method to do this

N_of_active_devs = -1
N_of_new_devs = -1
N_of_commits = -1

in_study_file = open("committed_in_study_period.csv")
in_study = list(csv.reader(in_study_file))
# conver the timestamp string into a datetime and append it to the end of the list
for row in in_study:
    row = row.append(dateparser.parse(row[-1]))

pre_study_file = open("committed_pre_study_period.csv")
pre_study = list(csv.reader(pre_study_file))
for row in pre_study:
    row = row.append(dateparser.parse(row[-1]))

in_study_devs = [x[2] for x in in_study]
in_study_devs_unique = set(in_study_devs)
# print(in_study_devs_unique)
N_of_active_devs = len(in_study_devs_unique)

pre_study_devs = [x[2] for x in pre_study]
pre_study_devs_unique = set(pre_study_devs)
# print(pre_study_devs_unique)
new_devs = in_study_devs_unique.difference(pre_study_devs_unique)
N_of_new_devs = len(new_devs)

print(N_of_active_devs)
print(N_of_new_devs)


test = in_study[0:10]


print(test)