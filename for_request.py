import requests

url = 'https://webhacking.kr/challenge/code-5/?hit=YOUR NICKNAME'
cookie = {'PHPSESSID' : 'YOUR COOKIE VALUE'}
for i in range (1,100):
    res = requests.get(url, cookies=cookie)

    
