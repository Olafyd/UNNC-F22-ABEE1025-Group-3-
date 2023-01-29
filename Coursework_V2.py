#Creator Name: Yu-Chieh CHUEH
#Date: 17.01.2023

from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Buckling Load Calculator")
# set the title of the software

Frame_info = LabelFrame(root, padx = 20, pady = 20)
Frame_info.grid(row = 0, column = 0, sticky = W+E)

Frame_enter = LabelFrame(root, padx = 20, pady = 20)
Frame_enter.grid(row = 1, column = 0, sticky = W+E)

Frame_button = LabelFrame(root, padx = 20, pady = 20)
Frame_button.grid(row = 2, column = 0, sticky = W+E)

Frame_menu = LabelFrame(root, padx = 20, pady = 20)
Frame_menu.grid(row = 3, column = 0, sticky = W+E)

Frame_calculate = LabelFrame(root, padx = 20, pady = 20)
Frame_calculate.grid(row = 4, column = 0, sticky = W+E)

Frame_result = LabelFrame(root, padx = 20, pady = 20)
Frame_result.grid(row = 5, column = 0, sticky = W+E)
# set the frame 

Label_title = Label(Frame_info, text = "Buckling Load Calculator")
Label_info = Label(Frame_info, text = 
			"This is only for the object with cross-section area as circle.")
Label_r = Label(Frame_enter, text = "The radius of the cross-section area (r)  ")
Label_r_unit = Label(Frame_enter, text = " m")
Label_L = Label(Frame_enter, text = "The length of the object (L)  ")
Label_L_unit = Label(Frame_enter, text = " m")
Label_c = Label(Frame_button, text = "Type of connection:", pady = 10)
Label_p = Label(Frame_menu, text = "Property")
Label_P = Label(Frame_result, text = "P =  ")
Label_P_unit = Label(Frame_result, text = " N")
# create the text widgets

e_r = Entry(Frame_enter, width = 10)
e_L = Entry(Frame_enter, width = 10)
e_P = Entry(Frame_result, width = 10)
# create the enter box widgets 


Button_P = Button(Frame_button, text = "Pinned ends", padx = 35)
Button_F = Button(Frame_button, text = "Fixed ends", padx = 35)
Button_PF = Button(Frame_button, text = "Pinned and fixed ends")
Button_Ff = Button(Frame_button, text = "Fixed and free ends")
Button_F_ = Button(Frame_button, text = "Fixed and ", padx = 35)
Button_C = Button(Frame_calculate, text = "Calculate")
# create the button widgets

options_p = [
			"Wood",
			"Brick"
			]
# create the options list

clicked = StringVar()
clicked.set(options_p[0])
# set the clicked

menu_p = OptionMenu(Frame_menu, clicked, *options_p)
# create the dropdown menu

Label_title.grid(row = 0, column = 0, sticky = W)
Label_info.grid(row = 1, column = 0, sticky = W)
# Frame_info

Label_r.grid(row = 0, column = 0, sticky = W)
e_r.grid(row = 0, column = 1, pady = 20)
Label_r_unit.grid(row = 0, column = 2)

Label_L.grid(row = 1, column = 0, sticky = W)
e_L.grid(row = 1, column = 1, pady = 20)
Label_L_unit.grid(row = 1, column = 2)
# Frame_enter

Label_c.grid(row = 0, column = 0, sticky = W)

Button_P.grid(row = 1, column = 0)
Button_F.grid(row = 1, column = 1)
Button_PF.grid(row = 1, column = 2)
Button_Ff.grid(row = 1, column = 3)
Button_F_.grid(row = 1, column = 4)
# Frame_button\

Label_p.grid(row = 0, column = 0)
menu_p.grid(row = 0, column = 1, padx = 10)
# Frame_menu

Button_C.grid(row = 0, column = 0, pady = 10)
# Frame_calculate

Label_P.grid(row = 0, column = 0, pady = 10)
e_P.grid(row = 0, column = 1)
Label_P_unit.grid(row = 0, column = 2)
# Frame_result

root.mainloop()