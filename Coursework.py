#Creator Name: Yu-Chieh CHUEH
#Date: 17.01.2023

from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Buckling Load Calculator")
# set the title of the software


Label_info = Label(root, text = 
			"This is only for the object with cross-section area as circle.")
Label_r = Label(root, text = "The radius of the cross-section area (r)")
Label_r_unit = Label(root, text = "m")
Label_L = Label(root, text = "The length of the object (L)")
Label_L_unit = Label(root, text = "m")
Label_c = Label(root, text = "Type of connection:")
Label_p = Label(root, text = "Property")
Label_P = Label(root, text = "P = ")
# create the text widgets

e_r = Entry(root, width = 50)
e_L = Entry(root, width = 50)
e_P = Entry(root, width = 20)
# create the enter box widgets 


Button_P = Button(root, text = "Pinned ends")
Button_F = Button(root, text = "Fixed ends")
Button_PF = Button(root, text = "Pinned and fixed ends")
Button_Ff = Button(root, text = "Fixed and free ends")
Button_F_ = Button(root, text = "Fixed and ")
Button_C = Button(root, text = "Calculate")
# create the button widgets

options_p = [
			"Wood",
			"Brick"
			]
# create the options list

clicked = StringVar()
clicked.set(options_p[0])
# set the clicked

menu_p = OptionMenu(root, clicked, *options_p)
# create the dropdown menu

Label_info.grid(row = 0, column = 0, pady = 10, columnspan = 5)
# the first row

Label_r.grid(row = 1, column = 0, columnspan = 2)
e_r.grid(row = 1, column = 2, pady = 10, columnspan = 3)
Label_r_unit.grid(row = 1, column = 5)
# the second row

Label_L.grid(row = 2, column = 0, columnspan = 2)
e_L.grid(row = 2, column = 2, pady = 10, columnspan = 3)
Label_L_unit.grid(row = 2, column = 5)
# the third row

Label_c.grid(row = 3, column = 0, pady = 10)
# the fourth row

Button_P.grid(row = 4, column = 0)
Button_F.grid(row = 4, column = 1)
Button_PF.grid(row = 4, column = 2)
Button_Ff.grid(row = 4, column = 3)
Button_F_.grid(row = 4, column = 4)
# the fifth row

Label_p.grid(row = 5, column = 0)
menu_p.grid(row = 5, column = 1)
# the sixth row

Button_C.grid(row = 6, column = 0, pady = 10)
# the seventh row

Label_P.grid(row = 7, column = 0, pady = 10)
e_P.grid(row = 7, column = 1, columnspan = 3)
# the eigth row

root.mainloop()