import requests

f = open('gitusers.txt', 'r')
for line in f:
    fp = line.strip()
    r = requests.get('https://github.com/'+fp)
    print(str(r.status_code) + "    " + str(fp))