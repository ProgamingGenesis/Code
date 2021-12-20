def en_ceaser(text , shift):
    #turns a string into a list of charaters
    word = list(text)
    i = 0
    #prints orignal text
    print("".join(word))
    #for loop for each letter or char in list
    for char in word:
        #ords char so it turns into a number
        char = ord(char)

        #Applies cipther to a (this one was tricky)
        if char == 97:
            #if the letter shift is to the right it's added to the ord of a
            if shift > 0:
                char = char + shift
                #then it's turned back into a character
                word[i] = chr(char)
            #if the letter shift is to the left (negitve) ord(a) is set to ord(z)
            #and then shift is added
            if shift < 0:
                char = 123 + shift
                #then it's turned back into a character
                word[i] = chr(char)
        
        if char == 123:
            if shift > 0:
                char = 97
                char = char + shift 
                word[i] = chr(char)
            if shift < 0:
                char = 1 - shift
                word[i] = chr(char)
        #every other letter
        else: 
            word[i] = chr(char + shift)
        
        i = i + 1
    return print("".join(word))

def de_ceaser(text, shift):
    word = list(text)
    i = 0
    print("".join(word))
    for char in word:
        char = ord(char)

        if char == 97:
            if shift > 0:
                char = char - shift
                word[i] = chr(char)
            if shift < 0:
                char = 123 - shift
                word[i] = chr(char)
        else: 
            word[i] = chr(char - shift)
        
        i = i + 1
    return print("".join(word))

en_ceaser("z", 3)
de_ceaser("huln", 3)
