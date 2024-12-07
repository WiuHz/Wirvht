def Caesar_Code(text, shift, mode):
    res = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord("A")
            else:
                start = ord("a")

        encrypted = chr(ord(char) - start + shift) % 26 + start 
        decrypted = chr(ord(char) - start - shift) % 26 + start
        text += char
        res.append(text)
    return res

text = list(map(str, input().split()))
shift = 3
mode = str(input())
if __name__ == Caesar_Code:
    if mode == "encrypto":
        print(encrypted)
    elif mode == "decrypto":
        print(decrypted)

    
