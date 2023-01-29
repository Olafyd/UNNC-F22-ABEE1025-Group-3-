import math
pai = math.pi

global R
global I
global L
global P
global ratio_equal
global clicked
global options_p
global E
global ratio_equal
###Set global variables

def ratio_func(ratio): 

'''This is in order to get the effective ratio 
which is varied for different end conditions
of the flexural points'''

    ratio_equal = ratio

def calculate():
    
'''this is to calculate and show the answer
based on the formula P= pi^2*E*I/(L^2)'''

    R = float(e_R.get())
    '''this is to get the entered radius value'''

    I = float((pai*(R**4))/4)
    '''this is to get the I(Second Moment of Area) value
    ased on the equation I = pai*(R**4))/4'''

    if ratio_equal == None:
        print("Please choose the type of connection first")
        return
    '''this is to prevent forgetting choosing connection type'''

    else:
        L = float(float(e_L.get())*ratio_equal)
    '''this is in order to get the effective length based 
    on the equation L = length*ratio'''

    clicked=options_p[0]
    '''this is to set the default value of the material'''
    
    if clicked == "Wood":
        E = 1.43
    if clicked == "Brick":
        E =14
    '''this is to get the E(Young's modulus) value of chosen material'''

    res_P = (pai**2)*float(E)*I/(L**2)
    '''this is to get the P(bucling load) based on the equation
    P = (pai**2)*E*I/(L**2)'''

    result = format(res_P,'.3f')
    P.set(result) 
    Lable_P_e.update()
    return result
    '''this is to return the result'''