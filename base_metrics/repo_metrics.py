import csv
import dateparser # can probably find a faster method to do this
import datetime

def metrics(year_start, month_start, year_end, month_end, commit_history):
    start = datetime.datetime(year_start, month_start, 1, tzinfo=datetime.timezone.utc)
    end = datetime.datetime(year_end + (month_end == 12), 
              (month_end + 1 if month_end < 12 else 1), 1,  tzinfo=datetime.timezone.utc) - datetime.timedelta(days=1) # making end date include all dates in end month
    timeframe = []
    previous_history = []
    # print("start= ", start)
    # print("end= ", end)
    for row in commit_history:
        # if date in timefram
        if row[-1] >= start and row[-1] <= end:
            timeframe.append(row)
            # print("in timeframe date= ", row[-1])
        elif row[-1]<start:
            previous_history.append(row)
            # print("in prev_hist date= ", row[-1])
    in_timeframe_devs = [x[2] for x in timeframe]
    in_timeframe_devs_unique = set(in_timeframe_devs)
    previous_history_devs = [x[2] for x in previous_history]
    previous_history_devs_unique = set(previous_history_devs)
    new_devs = in_timeframe_devs_unique.difference(previous_history_devs_unique)
    return [len(in_timeframe_devs_unique), len(new_devs), len(timeframe)]

N_of_active_devs = -1
N_of_new_devs = -1
N_of_commits = -1

commit_history_file = open("committed_all_time.csv",encoding='utf-8',errors='ignore')
commit_history = list(csv.reader(commit_history_file))
# commit_history = commit_history[0:10] # test on smaller range
# convert the timestamp string into a datetime and append it to the end of the list
for row in commit_history:
    # 'Thu Nov 26 13:29:19 2020 +0100' , date_formats=['%a %b %d %H:%M:%S %Y']
    row = row.append(dateparser.parse(row[-1]))
# print(commit_history[0][-1])

print("done preprocessing")

#time-windows are inclusive of all days in end month
tw1 = 0  # 2019-01 - 2020-05
tw2 = 0  # 2019-01 - 2019-06 
tw3 = 0  # 2019-07 - 2019-12
tw4 = 0  # 2020-01 - 2020-03
tw5 = 0  # 2020-04 - 2020-05
tw6 = 0  # 2020-01 - 2020-05
tw7 = 0  # 2020-01 - 2020-11
tw8 = 0  # 2019-01 - 2019-11
tw9 = 0  # 2020-01 - 2020-11

print(metrics(2019, 1, 2020, 5, commit_history))
print(metrics(2019, 1, 2019, 6, commit_history))
print(metrics(2019, 7, 2019, 12, commit_history))
print(metrics(2020, 1, 2020, 3, commit_history))
print(metrics(2020, 4, 2020, 5, commit_history))
print(metrics(2020, 1, 2020, 5, commit_history))
print(metrics(2020, 6, 2020, 11, commit_history))
print(metrics(2019, 1, 2019, 11, commit_history))
print(metrics(2020, 1, 2020, 11, commit_history))

