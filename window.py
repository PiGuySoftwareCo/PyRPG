from tkinter import *
import enemiespawn
import mainmap
import pythonrpg
##### ##### ##### ##### #####
game_view_1="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
game_view_2="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
game_view_3="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
game_view_4="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
game_view_5="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
game_view_6="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
game_view_7="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
game_view_8="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
game_view_9="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
game_view_10="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
game_view_11="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

root=Tk()
root.title("The Stolen Crown")
root.minsize(width=1000, height=500)
root.maxsize(width=1000, height=500)
##### ##### ##### ##### #####
###i am going to group the items by row###
a1=Button(root, text="                  items                    ")
b1=Button(root, text="                 skills                    ")
c1=Button(root, text="                   map                     ")
d1=Button(root, text="                  menu                     ")

a1.grid(row=1,column=1,columnspan=5)
b1.grid(row=1,column=6,columnspan=5)
c1.grid(row=1,column=11,columnspan=5)
d1.grid(row=1,column=16,columnspan=5)
##### ##### ##### ##### #####
e1_e5=Label(root, text=game_view_1)
f1_f5=Label(root, text=game_view_2)
g1_g5=Label(root, text=game_view_3)
h1_h5=Label(root, text=game_view_4)
i1_i5=Label(root, text=game_view_5)
j1_j5=Label(root, text=game_view_6)
k1_k5=Label(root, text=game_view_7)
l1_l5=Label(root, text=game_view_8)
m1_m5=Label(root, text=game_view_9)
n1_n5=Label(root, text=game_view_10)
o1_o5=Label(root, text=game_view_11)
##### ##### ##### ##### #####
e1_e5.grid(row=2, column=5, columnspan=5)
f1_f5.grid(row=3, column=5, columnspan=5)
g1_g5.grid(row=4, column=5, columnspan=5)
h1_h5.grid(row=5, column=5, columnspan=5)
i1_i5.grid(row=6, column=5, columnspan=5)
j1_j5.grid(row=7, column=5, columnspan=5)
k1_k5.grid(row=8, column=5, columnspan=5)
l1_l5.grid(row=9, column=5, columnspan=5)
m1_m5.grid(row=10, column=5, columnspan=5)
n1_n5.grid(row=11, column=5, columnspan=5)
o1_o5.grid(row=12, column=5, columnspan=5)
