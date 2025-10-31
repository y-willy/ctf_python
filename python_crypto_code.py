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


cipher_b64 = "IREHWYJZMEcGCODGMMbTENDDGcbGEMJZGEbGEZTFGYaGKNRTMIcGIMBSGRQTSNDDGAaWGYZRHEbGCNRQMUaDOMbEMRTGEYJYGUaWGOJQMYZHa==="
cipher_bytes = base64.b64decode(cipher_b64)

print(cipher_bytes)  # 바이트 형태 출력
