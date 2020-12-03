
import json 

val = input('Enter the number of the file: ')
 
f = open(val + '_pulls.json',encoding='utf-8',errors='ignore') 

data = json.load(f) 

#time-windows
tw1 = 0  # 2019-01 - 2020-05
tw2 = 0  # 2019-01 - 2019-06 
tw3 = 0  # 2019-07 - 2019-12
tw4 = 0  # 2020-01 - 2020-03
tw5 = 0  # 2020-04 - 2020-05
tw6 = 0  # 2020-01 - 2020-05
tw7 = 0  # 2020-01 - 2020-11
tw8 = 0  # 2019-01 - 2019-11
tw9 = 0  # 2020-01 - 2020-11

for i in data:
    if i['closed_at'] != None:
        x = i['closed_at'].split('-')
        if x[0] == '2019':
            tw1 += 1
            if x[1] != '12':
                tw8 += 1
            if x[1] <= '06':
                tw2 += 1
            else:
                tw3 += 1
        else:
            if x[0] == '2020' and x[1] <'12':
                tw9 += 1
                if x[1] <= '05':
                    tw1 += 1
                    if x[1] < '04':
                        tw4 += 1
                    tw6 += 1
                    if x[1] >= '04':
                        tw5 += 1
                else:
                    tw7 += 1
                    

print('TW1: ' + str(tw1) + '\n')
print('TW2: ' + str(tw2) + '\n')
print('TW3: ' + str(tw3) + '\n')
print('TW4: ' + str(tw4) + '\n')
print('TW5: ' + str(tw5) + '\n')
print('TW6: ' + str(tw6) + '\n')
print('TW7: ' + str(tw7) + '\n')
print('TW8: ' + str(tw8) + '\n')
print('TW9: ' + str(tw9) + '\n')

#printing results again for copying purposes
print(str(tw1) + '\n')
print(str(tw2) + '\n')
print(str(tw3) + '\n')
print(str(tw4) + '\n')
print(str(tw5) + '\n')
print(str(tw6) + '\n')
print(str(tw7) + '\n')
print(str(tw8) + '\n')
print(str(tw9) + '\n')


f.close() 
