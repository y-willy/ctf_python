from pwn import *
import re
from typing import List

Host = "host8.dreamhack.games"
Port = 12740

r = remote(Host,Port, timeout=5)
cry = r.recvline(timeout=5)
seed = [int(n) for n in re.findall(rb'\d+',cry)]
print("recv:", cry)

for a in range(256):
    try:
        k_list_str = [str(a ^ b) for b in seed]
        dec = " ".join(k_list_str)
        r.sendline(dec.encode())
    
        resp = r.recvline(timeout=5)
        if b"Corr" in resp:
            resp = r.recvline(timeout=5)
            print(resp)
        
    except EOFError:
        break

r.close()    

