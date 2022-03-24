green = '\033[92m' #GREEN
RESET = '\033[0m' #RESET COLOR
red = '\033[31m'

def ymxb (slope, y_int, start=0, increment=1, loops=5, write=True):
    print('x | y\n-----') if write==True else print
    out_in = {}
    for i in range(loops):
        y = slope*start + y_int
        
        print(start,'|', y) if write==True else print
        out_in[start] = y

        start += increment
    
    return out_in

# for y=mx+b formated equations only rn
def PONS (x_var1, y_int1, x_var2, y_int2):
    # for this example we're using the equations: 3x+2 and 5x-8
    # 3x + 2 | x_var1:3x   y_int1:2
    # 5x-8 | x_var2:5x  y_int2: -8
    
    #preserves and equation to be used for later
    m = x_var1 
    b = y_int1

    # 3x+2 = 5x-8
    y_int1 += -y_int2 # add the opposite of the non variable +8
    # 3x+10 = 5x

    x_var2 += -x_var1 # add the opposite of the variable side -3x
    
    # 10 = 2x
    y_int1 = y_int1/x_var2
    x_var2 = x_var2/x_var2

    x = y_int1
    y = m*x + b

    return f'The Point Of Intersection is: ( {green}{x}{RESET} , {red}{y}{RESET} )'

print(PONS(3, 2,5,-8))

def ToYMXB(string):
    # for this example I'm using 
