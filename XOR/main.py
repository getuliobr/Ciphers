def xor(inStr: str, key: str) -> str:
  outStr = ""
  for i in range(len(inStr)):
    outStr += chr(ord(inStr[i]) ^ ord(key[i % len(key)]))
  return outStr

inStr = input("Enter a string: ")
key = input("Enter a key: ")
encrypted = xor(inStr, key)
decrypted = xor(encrypted, key)
print(f'{encrypted = }')
print(f'{decrypted = }')