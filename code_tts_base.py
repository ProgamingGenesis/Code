
def class_get (x, usr_input):
    try:
        x(usr_input)
        return True
    except:
        return False

def ls_indexor (string):
    try:
        i = ls_text.index(string)
    except:
        i = -1
    return i
name = str
agrument_list = []
def write_to_file(file_name, argument_list):
    file = open(file_name, "w")
    for cmd in argument_list:
        cmd = cmd + "\n"
        file.write(cmd)
end = True

while end == True:
    text = input(">>> ")
    ls_text = text.split(" ")

    if ls_indexor("file") != -1 and ls_indexor("make") != -1:
        if ls_indexor("name") != -1:
            file_name = ls_text[ls_indexor("name") + 1] + '.py'
            fp = open(file_name, 'x')
            fp.close()
    if ls_indexor("set") != -1:
        if ls_text[ls_indexor("set") + 1] == "variable":
            name = ls_text[ls_indexor("variable") + 1] + " = "
            value = ls_text[ls_indexor("to") + 1]
            if class_get(int, value) == True:
                cmd = name + value
                agrument_list.append(cmd)
                print("Done!")
                break
            if class_get(str, value) == True:
                cmd = name + " '" + value + "' "
                agrument_list.append(cmd)
                print("Done!")
    if ls_indexor("print") != -1 and ls_indexor("write") != -1:
                if ls_indexor("print") + 1 != "variable":
                    spiter = text.split("print ")
                    out_line = '''print("''' + spiter[1] + '''")'''
                    agrument_list.append(out_line)
    if "close file" in text:
        end = False

write_to_file(file_name, agrument_list)
