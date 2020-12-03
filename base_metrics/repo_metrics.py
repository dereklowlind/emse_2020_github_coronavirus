import csv
import dateparser # can probably find a faster method to do this
import datetime

def metrics(year, month, commit_history):
    timeframe = []
    previous_history = []
    for row in commit_history:
        if row[-1].year == year and row[-1].month == month:
            timeframe.append(row)
        elif row[-1].year == year and month < month:
            previous_history.append(row)
        elif row[-1].year < year:
            previous_history.append(row)


    in_timeframe_devs = [x[2] for x in timeframe]
    in_timeframe_devs_unique = set(in_timeframe_devs)
    previous_history_devs = [x[2] for x in previous_history]
    previous_history_devs_unique = set(previous_history_devs)
    new_devs = in_timeframe_devs_unique.difference(previous_history_devs_unique)
    return [len(in_timeframe_devs_unique), len(new_devs), len(timeframe)]

N_of_active_devs = -1
N_of_new_devs = -1
N_of_commits = -1

commit_history_file = open("committed_all_time.csv")
commit_history = list(csv.reader(commit_history_file))
# convert the timestamp string into a datetime and append it to the end of the list
for row in commit_history:
    # 'Thu Nov 26 13:29:19 2020 +0100' , date_formats=['%a %b %d %H:%M:%S %Y']
    row = row.append(dateparser.parse(row[-1]))


print("done preprocessing")


print(metrics(2019, 1, commit_history))
