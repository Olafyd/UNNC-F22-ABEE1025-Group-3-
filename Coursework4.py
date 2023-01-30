# Part_4 of the Coursework
# Creator Name: Yu-Chieh CHUEH Yude Fu
# Date: 17.01.2023

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math
pai = math.pi

global R
global I
global L
global P
global ratio_equal
global E
###Set global variables

def ratio_func(ratio):
    global ratio_equal

    '''This is in order to get the effective ratio 
    which is varied for different end conditions 
    of the flexural points'''

    ratio_equal = ratio

def selected(event):
    global E

    if menu_p.get() == "Wood":
        E = 1.43
    
    if menu_p.get() == "Brick":
        E = 14
'''this is to get the E(Young's modulus) value of chosen material'''       


def calculate():
    global E
    global ratio_equal
    '''this is to calculate and show the answer
    ased on the formula P= pi^2*E*I/(L^2)'''

    R = float(e_R.get())
    '''this is to get the entered radius value'''

    I = float((pai*(R**4))/4)
    '''this is to get the I(Second Moment of Area) value
    ased on the equation I = pai*(R**4))/4'''

    L = float(float(e_L.get())*ratio_equal)

    try:
        R = float(e_R.get())
        1/float(e_L.get())
        L = float(float(e_L.get())*ratio_equal)
        float(E)
        res_P = (pai**2)*float(E)*I/(L**2)
    except NameError:
        messagebox.showerror(title = "Lack of data", 
                    message = "Please select a connection type")
    except ValueError:
        messagebox.showerror(title = "Lack of data", 
                    message = "Please select a property")
    except ZeroDivisionError:
        messagebox.showerror(title = "Lack of data", 
                    message = "Please check the r or L")
    # To check if the data entered properly 

    res_P = (pai**2)*float(E)*I/(L**2)
    '''this is to get the P(bucling load) based on the equation
    P = (pai**2)*E*I/(L**2)'''

    result = format(res_P,'.3f')
    P.set(result) 
    Label_P_e.update()
    return result    
    '''this is to return the result'''

''' -------Foundation------- '''

root = Tk()

root.title("Buckling Load Calculator")
# set the title of the software bar

root.geometry("845x502")
# set the size of the window

root.resizable(0, 0)
# prevent others change the size of the wiindow

icon = PhotoImage(file = "Load1.png")
# locate to the icon file

root.iconphoto(True, icon)
# set the icon of the software

Frame_info = LabelFrame(root, padx = 20, pady = 20)
Frame_enter = LabelFrame(root, padx = 20, pady = 10, relief = FLAT)
Frame_button = LabelFrame(root, padx = 20, relief = FLAT)
Frame_menu = LabelFrame(root, padx = 20, pady = 10, relief = FLAT)
Frame_calculate = LabelFrame(root, padx = 20, relief = FLAT)
Frame_result = LabelFrame(root, padx = 20, pady = 10)
# set the frame 
# relief = FLAT makes the border of each frame disappear
# padx and pady: add space horizontally and vertically

Frame_info.grid(row = 0, column = 0, sticky = W+E)
Frame_enter.grid(row = 1, column = 0, sticky = W+E)
Frame_button.grid(row = 2, column = 0, sticky = W+E)
Frame_menu.grid(row = 3, column = 0, sticky = W+E)
Frame_calculate.grid(row = 4, column = 0, sticky = W+E)
Frame_result.grid(row = 5, column = 0, pady = 10, sticky = W+E)
# layout each frame 
# sticky: make sure all the frames have the same width
# pady: create space vertically

''' -------Content------- '''

Label_title = Label(Frame_info, text = "Buckling Load Calculator")
Label_info = Label(Frame_info, text = 
			"This is only for the object with cross-section area as circle.")

Label_r = Label(Frame_enter, text = 
			"The radius of the cross-section area (r)  ")
Label_r_unit = Label(Frame_enter, text = " m")

Label_L = Label(Frame_enter, text = "The length of the object (L)  ")
Label_L_unit = Label(Frame_enter, text = " m")

Label_c = Label(Frame_button, text = "Type of connection:")

Label_p = Label(Frame_menu, text = "Property:")

Label_P = Label(Frame_result, text = "P =  ")
P = StringVar()
P.set("0")
Label_P_e = Label(Frame_result, width = 15, textvariable = P)
Label_P_unit = Label(Frame_result, text = " N")
# create the label widgets to show text


r = StringVar()
r.set("0")
e_R = Entry(Frame_enter, width = 10, textvariable = r)
l = StringVar()
l.set("0")
e_L = Entry(Frame_enter, width = 10, textvariable = l)
# create the text box widgets 

Button_P = Button(Frame_button, text = "Pinned ends", 
		padx = 35, command=lambda: ratio_func(1))
Button_F = Button(Frame_button, text = "Fixed ends", 
		padx = 35, command=lambda: ratio_func(0.5))
Button_PF = Button(Frame_button, text = "Pinned and fixed ends", 
		command=lambda: ratio_func(0.699))
Button_Ff = Button(Frame_button, text = "Fixed and free ends", 
		command=lambda: ratio_func(2))
Button_FG_ = Button(Frame_button, text = "Fixed and guided ends", 
		command=lambda: ratio_func(1))

Button_C = Button(Frame_calculate, text = "Calculate", 
		command = calculate)
# create the button widgets
# padx: make each buttons have similar width

options_p = [
			"Wood",
			"Brick"
			]
# create the options list
#clicked = StringVar()
#clicked.set(options_p[0])
# set the default as "Wood"

menu_p = ttk.Combobox(Frame_menu, value = options_p, state = "readonly")
menu_p.current(0)
menu_p.bind("<<ComboboxSelected>>", selected)
# create the dropdown menu

''' -------Font------- '''

Font_title = ("Arial", 25, "bold")
# define the font type(family, size, effect)
Label_title.configure(font = Font_title)
# set the title's font

Font_content = ("Arial", 12)
# define the font type(family, size, effect)
Label_info.configure(font = Font_content)
Label_r.configure(font = Font_content)
Label_r_unit.configure(font = Font_content)
Label_L.configure(font = Font_content)
Label_L_unit.configure(font = Font_content)
Label_c.configure(font = Font_content)
Label_p.configure(font = Font_content)
Label_P.configure(font = Font_content)
Label_P_unit.configure(font = Font_content)
# set the content's font

Font_result = ("Arial", 15)
# define the font type(family, size, effect)
Label_P.configure(font = Font_result)
Label_P_unit.configure(font = Font_result)
# set the result's font

''' -------Layout-------'''

Label_title.grid(row = 0, column = 0, sticky = W)
Label_info.grid(row = 1, column = 0, sticky = W)
# sticky: make sure each frame text align to the left
'''-------------------Frame_info---------------------'''

Label_r.grid(row = 0, column = 0, sticky = W)
e_R.grid(row = 0, column = 1, pady = 20)
Label_r_unit.grid(row = 0, column = 2)
# pady: adjust the space between each lines

Label_L.grid(row = 1, column = 0, sticky = W)
e_L.grid(row = 1, column = 1)
Label_L_unit.grid(row = 1, column = 2)
'''------------------Frame_enter---------------------'''

Label_c.grid(row = 0, column = 0, sticky = W, pady = 10)

Button_P.grid(row = 1, column = 0)
Button_F.grid(row = 1, column = 1)
Button_PF.grid(row = 1, column = 2)
Button_Ff.grid(row = 1, column = 3)
Button_FG_.grid(row = 1, column = 4)
'''------------------Frame_button---------------------'''

Label_p.grid(row = 0, column = 0, pady = 20)
menu_p.grid(row = 0, column = 1, padx = 15)
'''------------------Frame_menu-----------------------'''

Button_C.pack()
# pack: set to the centre of the window
'''------------------Frame_calculate------------------'''

Label_P.grid(row = 0, column = 0, pady = 10)
Label_P_e.grid(row = 0, column = 1)
Label_P_unit.grid(row = 0, column = 2)
'''------------------Frame_result---------------------'''

root.mainloop()