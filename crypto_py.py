num = -200640142664324295933714 * 4

for i in range(1, 100):
    div = i**4-95**4
    if(i==95):
        continue
    if num%div == 0:
        ans = num//div
        print(str(ans))        
        break