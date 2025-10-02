import requests

url = 'https://webhacking.kr/challenge/code-5/?hit=romantic'
cookie = {'PHPSESSID' : 'p13m2hu8jvqq95rmf532doanei'}
for i in range (1,100):
    res = requests.get(url, cookies=cookie)
    