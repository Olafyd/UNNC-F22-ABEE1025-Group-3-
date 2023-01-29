# Part_4 of the Coursework
# Creator Name: Yu-Chieh CHUEH
# Date: 17.01.2023

from tkinter import *
from PIL import ImageTk, Image
from logic import *
# the second is for the icon

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
e_R = Entry(Frame_enter, width = 15, textvariable = r)

l = StringVar()
l.set("0")
e_L = Entry(Frame_enter, width = 15, textvariable = l)
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

clicked.set(options_p[0])
# set the default as "Wood"

menu_p = OptionMenu(Frame_menu, clicked, *options_p)
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