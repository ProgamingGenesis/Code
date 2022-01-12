from os import posix_spawn

def class_get (x, usr_input):
    try:
        x(usr_input)
        return True
    except:
        return False

def ls_indexor (string):
    try:
        i = ls_txt.index(string)
    except:
        i = -1
    return i


while True:
    text = input(">>> ")
    ls_txt = text.split(" ")
    
    if ls_indexor("file") != -1 and ls_indexor("make") != -1:
        if ls_indexor("name") != -1:
            file_name = ls_txt[ls_indexor("name") + 1] + '.py'
            fp = open(file_name, 'x')
            fp.close()
    
    if ls_indexor("set") != -1:
        if ls_txt[ls_indexor("set") + 1] == "variable":
            name = ls_txt[ls_indexor("variable") + 1] + " = "
            value = ls_txt[ls_indexor("to") + 1]
            if class_get(int, value) == True:
                cmd = name + value
                with open(file_name, 'w') as f:
                    f.write(cmd)   
            if class_get(str, value) == True:
                cmd = name + " '" + value + "' "
                with open(file_name, 'w') as f:
                    f.write(cmd)   
    