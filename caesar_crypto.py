plain = input()

for shift in range(1,26):
    decrypted = ""
    for char in plain:
        decrypted+= chr((ord(char)-ord('a')+shift)%26 + ord('a'))
    print(decrypted)
    
    
