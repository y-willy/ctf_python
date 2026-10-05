
byte = [82, 223, 179, 96, 241, 139, 28, 181, 87, 209, 159, 56,                                     
75, 41, 217, 38, 127, 201, 163, 233, 83, 24, 79, 184,
106, 203, 135, 88, 91, 57, 30, 0]

xor = []
answer = []

def ROR(x, r):
    r &= 7

    if r == 0:
        return x

    return ((x >> r) | (x << (8 - r))) & 0xFF


for i in range(len(byte)):
    xor.append(byte[i] ^ i)
    
for i in range(len(xor)):
    answer.append(ROR(xor[i], i%8))
    
for i in range(len(answer)):
    print(chr(answer[i]), end="")
    
  
