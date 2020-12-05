import requests
import json 

username = 'your_name'
token = 'your_token'

gh_session = requests.Session()
gh_session.auth = (username, token)

val = input('Enter the number of the file: ')
 
f = open(val + '_pulls.json',encoding='utf-8',errors='ignore') 

data = json.load(f) 

payload = {}
headers = {}

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

utw1 = 0  # 2019-01 - 2020-05
utw2 = 0  # 2019-01 - 2019-06 
utw3 = 0  # 2019-07 - 2019-12
utw4 = 0  # 2020-01 - 2020-03
utw5 = 0  # 2020-04 - 2020-05
utw6 = 0  # 2020-01 - 2020-05
utw7 = 0  # 2020-01 - 2020-11
utw8 = 0  # 2019-01 - 2019-11
utw9 = 0  # 2020-01 - 2020-11

for i in data:
    url = i['comments_url']
    comments = json.loads(gh_session.get(url).text)
    for z in comments:
        c = z['created_at'].split('-')
        u = z['updated_at'].split('-')
        print(z['created_at'])
        print(z['updated_at'])
        print('')
        if c[0] == '2019':
            tw1 += 1
            if c[1] != '12':
                tw8 += 1
            if c[1] <= '06':
                tw2 += 1
            else:
                tw3 += 1
        else:
            if c[0] == '2020' and c[1] <'12':
                tw9 += 1
                if c[1] <= '05':
                    tw1 += 1
                    if c[1] < '04':
                        tw4 += 1
                    tw6 += 1
                    if c[1] >= '04':
                        tw5 += 1
                else:
                    tw7 += 1
        if u[0] == '2019':
            utw1 += 1
            if u[1] != '12':
                utw8 += 1
            if u[1] <= '06':
                utw2 += 1
            else:
                utw3 += 1
        else:
            if u[0] == '2020' and u[1] <'12':
                utw9 += 1
                if u[1] <= '05':
                    utw1 += 1
                    if u[1] < '04':
                        utw4 += 1
                    utw6 += 1
                    if u[1] >= '04':
                        utw5 += 1
                else:
                    utw7 += 1


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

print(str(utw1) + '\n')
print(str(utw2) + '\n')
print(str(utw3) + '\n')
print(str(utw4) + '\n')
print(str(utw5) + '\n')
print(str(utw6) + '\n')
print(str(utw7) + '\n')
print(str(utw8) + '\n')
print(str(utw9) + '\n')


f.close() 
