letters = "abcdefghijklmnopqrstuvwxyz"

def dec_enc(text, key, mode): 
    result = ""
    if mode == "d":
        key = -key
    
    for letter in text:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= 26:
                    new_index -= 26
                elif new_index < 0:
                    new_index += 26
                result += letters[new_index]
    print(result)
    return result

text = input()
key = int(input())
mode = input()
a = dec_enc(text, key, mode)
print(a)