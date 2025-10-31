import base64
import math
from pwn import *
from Crypto.Util.number import *
# chr() : 아스키 코드 -> 문자열
# ord() : 문자열 -> 아스키 코드

# bytes.fromhex() : 16진수 -> 문자열
# bytes.hex() : 16진수로 변환
# base64.b64encod() 바이트 문자열 -> Base64 문자열
# long_to_bytes() 정수형태 바이트로 변환

# ^ xor function, xor()


cry = "54586b6458754f7b215c7c75424f21634f744275517d6d"  
cry = bytes.fromhex(cry)  
for i in range(256):
    dec = "".join(chr(i^b) for b in cry)
    if "DH" in dec:
        print(dec)

#16진수로 이루어져있는 암호문을 바이트로 변환 후 1바이트의 key값을 range로 돌려가면서 DH가 들어있는 구문을 찾아냄.
#xor로 암호화
