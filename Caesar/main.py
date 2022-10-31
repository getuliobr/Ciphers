def shiftChar(ch: str, shift: int) -> str:
    outCh = ''
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift
      if stayInAlphabet > ord('z'):
          stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      outCh = finalLetter
    return outCh

def caesar(inStr: str, shift: int) -> str:
    outStr = ''
    for ch in inStr:
      c = ord(ch)
      if c >= ord('a') and c <= ord('z'):
        c = (c - ord('a') + shift) % 26 + ord('a')
      elif c >= ord('A') and c <= ord('Z'):
        c = (c - ord('A') + shift) % 26 + ord('A')
      outStr += chr(c)
    return outStr

inStr = input('Enter the message to encrypt/decrypt: ')
shift = int(input('Enter the shift amount (1-25): '))
print('Encrypted string: ', caesar(inStr, shift))