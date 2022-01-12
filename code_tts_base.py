import subprocess

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
            cmd = name + value
            with open(file_name, 'w') as f:
                f.write(cmd)
 

        
