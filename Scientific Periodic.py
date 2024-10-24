import tkinter
from idlelib.tooltip import Hovertip
x = tkinter.Tk()
x.configure(bg = "black")
x.resizable(0,0)

frame = tkinter.Frame(x,highlightbackground = 'white',highlightthickness = 10)

x.geometry("890x500")
x.geometry('+50+50')

x.maxsize(890,500)

x.title("theprogrammer__")

g = "georgia"
font = g

c = "calibiri(body)"
font = c

v = 'verdana'

title = tkinter.Label(x,text = "PERIODIC TABLE OF ELEMENTS",font = (g,20),fg = "white",bg = "black",highlightcolor = 'white',highlightbackground = 'white',highlightthickness= 2 )
title.place(x = 230,y = 30)

def h1():       # Hydrogen
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.config(bg = 'violet')
    h.title("theprogrammer__")
        
    h.geometry('+40+59')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Hydrogen',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'H',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '1',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '1.00784',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# hydrogen 1
hy = tkinter.Button(x,text = "H",fg = "black",bg = "violet",width = 4,font = g,command = h1)
hy.place(x = 40,y = 59)
hy = Hovertip(hy,text = "1 Hydrogen",hover_delay = 0)


def l3():       # Lithium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.config(bg = 'red')
    h.title("theprogrammer__")
    
    
    h.geometry('+40+90')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    
    n = tkinter.Label(h,text = 'Lithium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Li',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '3',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '6.941',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    
    h.mainloop()


# Lithium 3
li = tkinter.Button(x,text = "Li",fg = "black",bg = "red",width = 4,font = g,command = l3)
li.place(x = 40,y = 90)
li = Hovertip(li,text = "3 Lithium",hover_delay = 0)


def na11():       # Sodium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.config(bg = 'red')
    h.title("theprogrammer__")
    
    
    h.geometry('+40+121')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    
    n = tkinter.Label(h,text = 'Sodium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Na',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '11',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '22.989769',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# Sodium 11
na = tkinter.Button(x,text = "Na",fg = "black",bg = "red",width = 4,font = g,command = na11)
na.place(x = 40,y = 121)
na = Hovertip(na,text = "11 Sodium",hover_delay = 0)


def k19():       # Potassium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.config(bg = 'red')
    h.title("theprogrammer__")
        
    h.geometry('+40+152')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
        
    n = tkinter.Label(h,text = 'Potassium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'K',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '19',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '39.0983',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# Potassium 19
k = tkinter.Button(x,text = "K",fg = "black",bg = "red",width = 4,font = g,command = k19)
k.place(x = 40,y = 152)
k = Hovertip(k,text = "19 Potassium",hover_delay = 0)

def rb37():       # Rubiduim
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'red')
    h.geometry('+40+183')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Rubiduim',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Rb',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '37',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '85.4678',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# Rubidium
rb = tkinter.Button(x,text = "Rb",fg = "black",bg = "red",width = 4,font = g,command = rb37)
rb.place(x = 40,y = 183)
rb = Hovertip(rb,text = "37 Rubidium",hover_delay = 0)


def cs55():       # Caesium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'red')
    h.geometry('+40+214')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Caesium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Cs',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '55',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '132.90547',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# Caesium 55
rb = tkinter.Button(x,text = "Cs",fg = "black",bg = "red",width = 4,font = g,command = cs55)
rb.place(x = 40,y = 214)
rb = Hovertip(rb,text = "55 Caesium",hover_delay = 0)


def fr87():       # Francium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'red')
    h.geometry('+40+245')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Francium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Fr',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '87',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '223',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# Francium 87
rb = tkinter.Button(x,text = "Fr",fg = "black",bg = "red",width = 4,font = g,command = fr87)
rb.place(x = 40,y = 245)
rb = Hovertip(rb,text = "87 Francium",hover_delay = 0)


def be4():       # Beryllium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'Orange')
    h.geometry('+85+90')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Beryllium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Be',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '4',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '9.012182',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# Beryllium
rb = tkinter.Button(x,text = "Be",fg = "black",bg = "Orange",width = 4,font = g,command = be4)
rb.place(x = 85,y = 90)
rb = Hovertip(rb,text = "4 Beryllium",hover_delay = 0)


def mg12():       # Beryllium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'Orange')
    h.geometry('+85+121')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Magnesium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Mg',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '12',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '24.989769',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# Magnesium 12
rb = tkinter.Button(x,text = "Mg",fg = "black",bg = "Orange",width = 4,font = g,command = mg12)
rb.place(x = 85,y = 121)
rb = Hovertip(rb,text = "12 Magnesuim",hover_delay = 0)



def ca20():       # Calcium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'Orange')
    h.geometry('+85+152')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Calcium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ca',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '20',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '40.078',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# calcuim 20
rb = tkinter.Button(x,text = "Ca",fg = "black",bg = "Orange",width = 4,font = g,command = ca20)
rb.place(x = 85,y = 152)
rb = Hovertip(rb,text = "20 Calcuim",hover_delay = 0)

def sr38():       # Strontium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'Orange')
    h.geometry('+85+183')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Strontium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Sr',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '38',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '87.62',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# strontium 38
rb = tkinter.Button(x,text = "Sr",fg = "black",bg = "Orange",width = 4,font = g,command = ca20)
rb.place(x = 85,y = 183)
rb = Hovertip(rb,text = "38 Strontium",hover_delay = 0)


def ba56():       # barium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'Orange')
    h.geometry('+85+214')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Barium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ba',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '56',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '137.327',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# barium 56
rb = tkinter.Button(x,text = "Ba",fg = "black",bg = "Orange",width = 4,font = g,command = ba56)
rb.place(x = 85,y = 214)
rb = Hovertip(rb,text = "56 Barium",hover_delay = 0)


def ra88():       # radium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'Orange')
    h.geometry('+85+245')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Radium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ra',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '88',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '226',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

#  Radium
rb = tkinter.Button(x,text = "Ra",fg = "black",bg = "Orange",width = 4,font = g,command = ra88)
rb.place(x = 85,y = 245)
rb = Hovertip(rb,text = "88 Radium",hover_delay = 0)

def sc21():       # scandium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    h.geometry('+130+152')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Scandium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Sc',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '21',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '44.955912',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

#  Scandium
rb = tkinter.Button(x,text = "Sc",fg = "black",bg = "yellow",width = 4,font = g,command = sc21)
rb.place(x = 130,y = 152)
rb = Hovertip(rb,text = "21 Scandium",hover_delay = 0)

def y39():       # yttrium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    h.geometry('+130+183')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Yttrium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Y',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '39',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '88.90585',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

#  yttrium 39
rb = tkinter.Button(x,text = "Y",fg = "black",bg = "yellow",width = 4,font = g,command = y39)
rb.place(x = 130,y = 183)
rb = Hovertip(rb,text = "39 Yttrium",hover_delay = 0)


def ti22():       # Titanium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    h.geometry('+175+152')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Titanium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ti',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '22',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '47.867',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

#  titanium
rb = tkinter.Button(x,text = "Ti",fg = "black",bg = "yellow",width = 4,font = g,command = ti22)
rb.place(x = 175,y = 152)
rb = Hovertip(rb,text = "22 Titanium",hover_delay = 0)

def v23():       # Vanadium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    h.geometry('+220+152')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Vanadium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'V',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '23',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '50.9415',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

#  vanadium
rb = tkinter.Button(x,text = "V",fg = "black",bg = "yellow",width = 4,font = g,command = v23)
rb.place(x = 220,y = 152)
rb = Hovertip(rb,text = "23 Vanadium",hover_delay = 0)


def cr24():       # Chromium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    h.geometry('+265+152')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Chromium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Cr',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '24',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '51.9961',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

#  chromium
rb = tkinter.Button(x,text = "Cr",fg = "black",bg = "yellow",width = 4,font = g,command = cr24)
rb.place(x = 265,y = 152)
rb = Hovertip(rb,text = "24 Chromium",hover_delay = 0)


def mn25():       # Manganese
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    h.geometry('+310+152')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Manganese',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Mn',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '25',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '54.938044',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

#  Manganese 25
rb = tkinter.Button(x,text = "Mn",fg = "black",bg = "yellow",width = 4,font = g,command = mn25)
rb.place(x = 310,y = 152)
rb = Hovertip(rb,text = "25 Manganese",hover_delay = 0)

def fe26():       # Iron
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    h.geometry('+350+152')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Iron',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Fe',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '26',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '55.845',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

#  iron 26
rb = tkinter.Button(x,text = "Fe",fg = "black",bg = "yellow",width = 4,font = g,command = fe26)
rb.place(x = 355,y = 152)
rb = Hovertip(rb,text = "26 Iron",hover_delay = 0)

def co27():       # cobalt
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    h.geometry('+400+152')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Cobalt',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Co',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '27',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '58.933195',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

#  cobalt 27
rb = tkinter.Button(x,text = "Co",fg = "black",bg = "yellow",width = 4,font = g,command = co27)
rb.place(x = 400,y = 152)
rb = Hovertip(rb,text = "27 Cobalt",hover_delay = 0)


def ni28():       # Nickel
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    h.geometry('+445+152')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Nickel',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ni',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '28',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '58.6934',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

#  nickel 28
rb = tkinter.Button(x,text = "Ni",fg = "black",bg = "yellow",width = 4,font = g,command = ni28)
rb.place(x = 445,y = 152)
rb = Hovertip(rb,text = "28 Nickel",hover_delay = 0)

def cu29():       # copper
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Copper',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Cu',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '29',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '63.546',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+490+152')
    
    h.mainloop()

# copper
rb = tkinter.Button(x,text = "Cu",fg = "black",bg = "yellow",width = 4,font = g,command = cu29)
rb.place(x = 490,y = 152)
rb = Hovertip(rb,text = "29 Copper",hover_delay = 0)

def zn30():       # zinc
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Zinc',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Zn',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '30',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '65.38',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+535+152')
    
    h.mainloop()

# copper
rb = tkinter.Button(x,text = "Zn",fg = "black",bg = "yellow",width = 4,font = g,command = zn30)
rb.place(x = 535,y = 152)
rb = Hovertip(rb,text = "30 Zinc",hover_delay = 0)


def zr40():       # Zirconium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    h.geometry('+175+183')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Zirconium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Zr',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '40',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '91.224',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.mainloop()

# Zirconium
rb = tkinter.Button(x,text = "Zr",fg = "black",bg = "yellow",width = 4,font = g,command = zr40)
rb.place(x = 175,y = 183)
rb = Hovertip(rb,text = "40 Zirconium",hover_delay = 0)

def nb41():       # Niobium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Niobium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Nb',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '41',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '92.90638',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+220+183')
    
    h.mainloop()

# Niobium
rb = tkinter.Button(x,text = "Nb",fg = "black",bg = "yellow",width = 4,font = g,command = nb41)
rb.place(x = 220,y = 183)
rb = Hovertip(rb,text = "41 Niobium",hover_delay = 0)


def mo42():       # Molybdenum
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Molybdenum',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Mo',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '42',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '95.95',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+265+183')
    
    h.mainloop()

# Niobium
rb = tkinter.Button(x,text = "Mo",fg = "black",bg = "yellow",width = 4,font = g,command = mo42)
rb.place(x = 265,y = 183)
rb = Hovertip(rb,text = "42 Molybdenum",hover_delay = 0)

def tc43():       # Technetium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Technetium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Tc',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '43',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '98',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+310+183')
    
    h.mainloop()

# technetium
rb = tkinter.Button(x,text = "Tc",fg = "black",bg = "yellow",width = 4,font = g,command = tc43)
rb.place(x = 310,y = 183)
rb = Hovertip(rb,text = "43 Technetium",hover_delay = 0)

def ru44():       # ruthenium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Ruthenium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ru',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '44',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '101.07',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+355+183')
    
    h.mainloop()

# ruthenium 44
rb = tkinter.Button(x,text = "Ru",fg = "black",bg = "yellow",width = 4,font = g,command = ru44)
rb.place(x = 355,y = 183)
rb = Hovertip(rb,text = "44 Ruthenium",hover_delay = 0)

def rh45():       # rhodium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Rhodium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Rh',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '45',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '102.9055',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+400+183')
    
    h.mainloop()

# rhodium 45
rb = tkinter.Button(x,text = "Rh",fg = "black",bg = "yellow",width = 4,font = g,command = rh45)
rb.place(x = 400,y = 183)
rb = Hovertip(rb,text = "45 Rhodium",hover_delay = 0)

def pd46():       # palladium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Palladium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Pd',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '46',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '106.42',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+445+183')
    
    h.mainloop()

# pd46
rb = tkinter.Button(x,text = "Pd",fg = "black",bg = "yellow",width = 4,font = g,command = pd46)
rb.place(x = 445,y = 183)
rb = Hovertip(rb,text = "46 Palladium",hover_delay = 0)


def ag47():       # silver
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Silver',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ag',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '47',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '107.8682',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+490+183')
    
    h.mainloop()

# Silver
rb = tkinter.Button(x,text = "Ag",fg = "black",bg = "yellow",width = 4,font = g,command = ag47)
rb.place(x = 490,y = 183)
rb = Hovertip(rb,text = "47 Silver",hover_delay = 0)

def cd48():       # cadmium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Cadmium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Cd',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '48',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '112.414',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+535+183')
    
    h.mainloop()

# cadmium 
rb = tkinter.Button(x,text = "Cd",fg = "black",bg = "yellow",width = 4,font = g,command = cd48)
rb.place(x = 535,y = 183)
rb = Hovertip(rb,text = "48 Cadmium",hover_delay = 0)



    
#  57 - 71
rb = tkinter.Button(x,text = "57-71",fg = "black",bg = "cyan",width = 4,font = g)
rb.place(x = 130,y = 214)
rb = Hovertip(rb,text = "Lanthanide",hover_delay = 0)


def hf72():       # Hafnium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Hafnium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Hf',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '72',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '178.49',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+175+214')
    
    h.mainloop()

# Hafnium
rb = tkinter.Button(x,text = "Hf",fg = "black",bg = "yellow",width = 4,font = g,command = hf72)
rb.place(x = 175,y = 214)
rb = Hovertip(rb,text = "72 Hafnium",hover_delay = 0)

def ta73():       # Tantalum
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Tantalum',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ta',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '73',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '180.94788',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+220+214')
    
    h.mainloop()

# Tantalum 73
rb = tkinter.Button(x,text = "Ta",fg = "black",bg = "yellow",width = 4,font = g,command = ta73)
rb.place(x = 220,y = 214)
rb = Hovertip(rb,text = "73 Tantalum",hover_delay = 0)

def w74():       # Tungsten
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Tungsten',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'W',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '74',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '183.84',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+265+214')
    
    h.mainloop()

# Tungsten
rb = tkinter.Button(x,text = "W",fg = "black",bg = "yellow",width = 4,font = g,command = w74)
rb.place(x = 265,y = 214)
rb = Hovertip(rb,text = "74 Tungsten",hover_delay = 0)


def re75():       # rhenium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Rhenium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Re',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '75',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '186.207',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+310+214')
    
    h.mainloop()

# Rhenium 75
rb = tkinter.Button(x,text = "Re",fg = "black",bg = "yellow",width = 4,font = g,command = re75)
rb.place(x = 310,y = 214)
rb = Hovertip(rb,text = "75 Rhenium",hover_delay = 0)


def os76():       # osmium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Osmium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Os',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '76',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '190.23',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+355+214')
    
    h.mainloop()

# osmium 76
rb = tkinter.Button(x,text = "Os",fg = "black",bg = "yellow",width = 4,font = g,command = os76)
rb.place(x = 355,y = 214)
rb = Hovertip(rb,text = "76 Osmium",hover_delay = 0)


def ir77():       # iridium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
        
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Iridium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ir',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '77',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '192.217',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+400+214')
    
    h.mainloop()

# Iridium 77
rb = tkinter.Button(x,text = "Ir",fg = "black",bg = "yellow",width = 4,font = g,command = ir77)
rb.place(x = 400,y = 214)
rb = Hovertip(rb,text = "77 Iridium",hover_delay = 0)

def pt78():       # platinum
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Platinum',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Pt',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '78',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '195.084',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+445+214')
    
    h.mainloop()

# Platinum 78
rb = tkinter.Button(x,text = "Pt",fg = "black",bg = "yellow",width = 4,font = g,command = pt78)
rb.place(x = 445,y = 214)
rb = Hovertip(rb,text = "78 Platium",hover_delay = 0)


def au79():       # gold
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Gold',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Au',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '79',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '196.96657',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+490+214')
    
    h.mainloop()

# Gold
rb = tkinter.Button(x,text = "Au",fg = "black",bg = "yellow",width = 4,font = g,command = au79)
rb.place(x = 490,y = 214)
rb = Hovertip(rb,text = "79 Gold",hover_delay = 0)


def hg80():       # Mercury
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Mercury',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Hg',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '80',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '200.59',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+535+214')
    
    h.mainloop()

# mercury
rb = tkinter.Button(x,text = "Hg",fg = "black",bg = "yellow",width = 4,font = g,command = hg80)
rb.place(x = 535,y = 214)
rb = Hovertip(rb,text = "80 Mercury",hover_delay = 0)




# 89 - 103
rb = tkinter.Button(x,text = "89-103",fg = "black",bg = "hotpink3",width = 4,font = g)
rb.place(x = 130,y = 245)
rb = Hovertip(rb,text = "Actinide",hover_delay = 0)



def rf104():       # 104 Rutherfordium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Rutherfordium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Rf',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '104',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '267',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+175+245')
    
    h.mainloop()

# 104 Rutherfordium
rb = tkinter.Button(x,text = "Rf",fg = "black",bg = "yellow",width = 4,font = g,command = rf104)
rb.place(x = 175,y = 245)
rb = Hovertip(rb,text = "104 Rutherfordium",hover_delay = 0)

def db105():       # 105 Dubnium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Dubnium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Db',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '105',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '268.126',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+220+245')
    
    h.mainloop()

# 105 Dubnium
rb = tkinter.Button(x,text = "Db",fg = "black",bg = "yellow",width = 4,font = g,command = db105)
rb.place(x = 220,y = 245)
rb = Hovertip(rb,text = "105 Dubnium",hover_delay = 0)

def sg106():       # Seaborgium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Seaborgium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Sg',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '106',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '269',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+265+245')
    
    h.mainloop()

# 106 seaborgium
rb = tkinter.Button(x,text = "Sg",fg = "black",bg = "yellow",width = 4,font = g,command = sg106)
rb.place(x = 265,y = 245)
rb = Hovertip(rb,text = "106 Seaborgium",hover_delay = 0)


def bh107():       # Bohrium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Bohrium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Bh',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '107',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '264',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+310+245')
    
    h.mainloop()

# 107 Bohrium
rb = tkinter.Button(x,text = "Bh",fg = "black",bg = "yellow",width = 4,font = g,command = bh107)
rb.place(x = 310,y = 245)
rb = Hovertip(rb,text = "107 Bohrium",hover_delay = 0)



def hs108():       # 108 Hassium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Hassium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Hs',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '108',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '269',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+355+245')
    
    h.mainloop()

# 108 Hassium
rb = tkinter.Button(x,text = "Hs",fg = "black",bg = "yellow",width = 4,font = g,command = hs108)
rb.place(x = 355,y = 245)
rb = Hovertip(rb,text = "108 Hassium",hover_delay = 0)


def mt109():       # 109 Meitnerium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Meitnerium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Mt',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '109',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '276',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+400+245')
    
    h.mainloop()

# 109 Meitnerium
rb = tkinter.Button(x,text = "Mt",fg = "black",bg = "yellow",width = 4,font = g,command = mt109)
rb.place(x = 400,y = 245)
rb = Hovertip(rb,text = "109 Meitnerium",hover_delay = 0)

def ds110():       # 110 Darmstadtium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Darmstadtium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ds',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '110',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '281',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+445+245')
    
    h.mainloop()

# 110 Darmstadtium
rb = tkinter.Button(x,text = "Ds",fg = "black",bg = "yellow",width = 4,font = g,command = ds110)
rb.place(x = 445,y = 245)
rb = Hovertip(rb,text = "110 Darmstadtium",hover_delay = 0)

def rg111():       # Roentgenium  111
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Roentgenium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Rg',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '111',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '282',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+490+245')
    
    h.mainloop()

# Roentgenium  282
rb = tkinter.Button(x,text = "Rg",fg = "black",bg = "yellow",width = 4,font = g,command = rg111)
rb.place(x = 490,y = 245)
rb = Hovertip(rb,text = "111 Roentgenium",hover_delay = 0)


def cn112():       # copernicium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'yellow')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Copernicium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Cn',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '112',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '285',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+535+250')
    
    h.mainloop()

# copernicium 112
rb = tkinter.Button(x,text = "Cn",fg = "black",bg = "yellow",width = 4,font = g,command = cn112)
rb.place(x = 535,y = 245)
rb = Hovertip(rb,text = "112 Copernicium",hover_delay = 0)


def b5():       # 5 Boron
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'skyblue')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Boron',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'B',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '5',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '10.811',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+580+90')
    
    h.mainloop()

# 5 Boron
rb = tkinter.Button(x,text = "B",fg = "black",bg = "skyblue",width = 4,font = g,command = b5)
rb.place(x = 580,y = 90)
rb = Hovertip(rb,text = "5 Boron",hover_delay = 0)

def al13():       # 13 Aluminium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = '13 Aluminium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Al',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '13',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '26.9815',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+580+130')
    
    h.mainloop()

# aluminium
rb = tkinter.Button(x,text = "Al",fg = "black",bg = "green2",width = 4,font = g,command = al13)
rb.place(x = 580,y = 121)
rb = Hovertip(rb,text = "13 Aluminium",hover_delay = 0)


def ga31():       # 31 Gallium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = '31 Gallium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ga',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '31',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '69.723',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+580+152')
    
    h.mainloop()

# 31 Gallium
rb = tkinter.Button(x,text = "Ga",fg = "black",bg = "green2",width = 4,font = g,command = ga31)
rb.place(x = 580,y = 152)
rb = Hovertip(rb,text = "31 Gallium",hover_delay = 0)


def in49():       # 49 Indium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = '49 Indium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'In',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '49',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '114.818',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+580+183')
    
    h.mainloop()

# 49 Indium
rb = tkinter.Button(x,text = "In",fg = "black",bg = "green2",width = 4,font = g,command = in49)
rb.place(x = 580,y = 183)
rb = Hovertip(rb,text = "49 Indium",hover_delay = 0)



def tl81():       # 81 Thallium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = '81 Thallium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Tl',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '81',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '204.3833',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+580+183')
    
    h.mainloop()

# 81 Thallium
rb = tkinter.Button(x,text = "Tl",fg = "black",bg = "green2",width = 4,font = g,command = tl81)
rb.place(x = 580,y = 214)
rb = Hovertip(rb,text = "81 Thallium",hover_delay = 0)


def nh113():       # 113 Nihonium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = '113 Nihonium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Nh',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '113',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '286',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+580+145')
    
    h.mainloop()

# 113 Nihonium
rb = tkinter.Button(x,text = "Nh",fg = "black",bg = "green2",width = 4,font = g,command = nh113)
rb.place(x = 580,y = 245)
rb = Hovertip(rb,text = "113 Nihonium",hover_delay = 0)



def c6():       # 6 Carbon
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'violet')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Carbon',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'C',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '6',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '12.011',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+625+90')
    
    h.mainloop()

# 6 Carbon
rb = tkinter.Button(x,text = "C",fg = "black",bg = "violet",width = 4,font = g,command = c6)
rb.place(x = 625,y = 90)
rb = Hovertip(rb,text = "6 Carbon",hover_delay = 0)


def n7():       # 7 Nitrogen
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'violet')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Nitrogen',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'N',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '7',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '14.0067',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+670+90')
    
    h.mainloop()

# 7 Nitrogen
rb = tkinter.Button(x,text = "N",fg = "black",bg = "violet",width = 4,font = g,command = n7)
rb.place(x = 670,y = 90)
rb = Hovertip(rb,text = "7 Nitrogen",hover_delay = 0)

def o8():       # 8 Oxygen
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'violet')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Oxygen',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'O',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '8',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '15.999',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+715+90')
    
    h.mainloop()

# 8 Oxygen
rb = tkinter.Button(x,text = "O",fg = "black",bg = "violet",width = 4,font = g,command = o8)
rb.place(x = 715,y = 90)
rb = Hovertip(rb,text = "8 Oxygen",hover_delay = 0)

def f9():       # 9 Fluorine
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'deeppink2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Fluorine',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'F',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '9',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '18.998403',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+760+90')
    
    h.mainloop()

# 9 Fluorine
rb = tkinter.Button(x,text = "F",fg = "black",bg = "deeppink2",width = 4,font = g,command = f9)
rb.place(x = 760,y = 90)
rb = Hovertip(rb,text = "9 Fluorine",hover_delay = 0)


def he2():       # 2 Helium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'lightgoldenrod3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Helium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'He',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '2',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '4.002602',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+805+59')
    
    h.mainloop()

# 2 Helium
rb = tkinter.Button(x,text = "He",fg = "black",bg = "lightgoldenrod3",width = 4,font = g,command = he2)
rb.place(x = 805,y = 59)
rb = Hovertip(rb,text = "2 Helium",hover_delay = 0)


def ne10():       # 10 Neon
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'lightgoldenrod3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Neon',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ne',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '10',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '20.1797',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+805+90')
    
    h.mainloop()

# 10 Neon
rb = tkinter.Button(x,text = "Ne",fg = "black",bg = "lightgoldenrod3",width = 4,font = g,command = ne10)
rb.place(x = 805,y = 90)
rb = Hovertip(rb,text = "10 Neon",hover_delay = 0)


def si14():       # 14 Silicon
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'skyblue')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Silicon',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Si',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '14',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '28.0855',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+625+121')
    
    h.mainloop()

# 14 Silicon
rb = tkinter.Button(x,text = "Si",fg = "black",bg = "skyblue",width = 4,font = g,command = si14)
rb.place(x = 625,y = 121)
rb = Hovertip(rb,text = "14 Silicon",hover_delay = 0)


def p15():       # 15 Phosphorus
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'violet')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Phosphorus',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'P',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '15',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '30.973762',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+670+121')
    
    h.mainloop()

# 15 Phosphorus
rb = tkinter.Button(x,text = "P",fg = "black",bg = "violet",width = 4,font = g,command = p15)
rb.place(x = 670,y = 121)
rb = Hovertip(rb,text = "15 Phosphorus",hover_delay = 0)


def s16():       # 16 Sulfur
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'violet')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Sulfur',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'S',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '16',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '32.065',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+715+121')
    
    h.mainloop()

# 16 Sulfur
rb = tkinter.Button(x,text = "S",fg = "black",bg = "violet",width = 4,font = g,command = s16)
rb.place(x = 715,y = 121)
rb = Hovertip(rb,text = "16 Sulfur",hover_delay = 0)

def cl17():       #17 Chlorine
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'deeppink2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Chlorine',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Cl',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '17',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '35.453',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+760+121')
    
    h.mainloop()

# 17 Chlorine
rb = tkinter.Button(x,text = "Cl",fg = "black",bg = "deeppink2",width = 4,font = g,command = cl17)
rb.place(x = 760,y = 121)
rb = Hovertip(rb,text = "17 Chlorine",hover_delay = 0)

def ar18():       #18 Argon
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'lightgoldenrod3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Argon',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ar',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '18',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '39.948',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+805+121')
    
    h.mainloop()

#  18 Argon
rb = tkinter.Button(x,text = "Ar",fg = "black",bg = "lightgoldenrod3",width = 4,font = g,command = ar18)
rb.place(x = 805,y = 121)
rb = Hovertip(rb,text = "18 Argon",hover_delay = 0)

def ge32():       # 32 Germanium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'skyblue')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Germanium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ge',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '32',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '72.64',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+805+152')
    
    h.mainloop()

# 32 Germanium
rb = tkinter.Button(x,text = "Ge",fg = "black",bg = "skyblue",width = 4,font = g,command = ge32)
rb.place(x = 625,y = 152)
rb = Hovertip(rb,text = "32 Germanium",hover_delay = 0)

def sn50():       # 50 Tin
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Tin',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Sn',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '50',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '118.71',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+625+183')
    
    h.mainloop()

# 50 Tin
rb = tkinter.Button(x,text = "Sn",fg = "black",bg = "green2",width = 4,font = g,command = sn50)
rb.place(x = 625,y = 183)
rb = Hovertip(rb,text = "50 Tin",hover_delay = 0)


def pb82():       # 82 lead
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Lead',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Pb',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '82',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '207.2',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+625+214')
    
    h.mainloop()

# 82 Lead
rb = tkinter.Button(x,text = "Pb",fg = "black",bg = "green2",width = 4,font = g,command = pb82)
rb.place(x = 625,y = 214)
rb = Hovertip(rb,text = "82 Lead",hover_delay = 0)

def fl114():       # 114 Flerovium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Flerovium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Fl',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '114',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '289',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+625+255')
    
    h.mainloop()

# 114 Flerovium
rb = tkinter.Button(x,text = "Fl",fg = "black",bg = "green2",width = 4,font = g,command = fl114)
rb.place(x = 625,y = 245)
rb = Hovertip(rb,text = "114 Flerovium",hover_delay = 0)


def as33():       # 33 Arsenic
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'skyblue')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Arsenic',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'As',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '33',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '74.9216',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+670+152')
    
    h.mainloop()

# 33 Arsenic
rb = tkinter.Button(x,text = "As",fg = "black",bg = "skyblue",width = 4,font = g,command = as33)
rb.place(x = 670,y = 152)
rb = Hovertip(rb,text = "33 Arsenic",hover_delay = 0)


def se34():       # 34 Selenium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'violet')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Selenium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Se',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '34',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '78.96',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+715+152')
    
    h.mainloop()

# 34 Selenium
rb = tkinter.Button(x,text = "Se",fg = "black",bg = "violet",width = 4,font = g,command = se34)
rb.place(x = 715,y = 152)
rb = Hovertip(rb,text = "34 Selenium",hover_delay = 0)


def br35():       # 35 Bromine
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'deeppink2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Bromine',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Br',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '35',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '79.904',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+760+152')
    
    h.mainloop()

# 35 Bromine
rb = tkinter.Button(x,text = "Br",fg = "black",bg = "deeppink2",width = 4,font = g,command = br35)
rb.place(x = 760,y = 152)
rb = Hovertip(rb,text = "35 Bromine",hover_delay = 0)

def kr36():       # 36 Kryton
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'lightgoldenrod3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Krypton',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Kr',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '36',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '83.798',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+805+152')
    
    h.mainloop()

# 36 Krypton
rb = tkinter.Button(x,text = "Kr",fg = "black",bg = "lightgoldenrod3",width = 4,font = g,command = kr36)
rb.place(x = 805,y = 152)
rb = Hovertip(rb,text = "36 Krypton",hover_delay = 0)

def sb51():       # 51 Antimony
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'skyblue')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Antimony',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Sb',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '51',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '121.76',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+670+183')
    
    h.mainloop()

# 51 Antimony
rb = tkinter.Button(x,text = "Sb",fg = "black",bg = "skyblue",width = 4,font = g,command = sb51)
rb.place(x = 670,y = 183)
rb = Hovertip(rb,text = "51 Antimony",hover_delay = 0)

def te52():       # 52 Tellurium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'skyblue')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Tellurium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Te',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '52',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '127.6',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+715+183')
    
    h.mainloop()

# 52 Tellurium
rb = tkinter.Button(x,text = "Te",fg = "black",bg = "skyblue",width = 4,font = g,command = te52)
rb.place(x = 715,y = 183)
rb = Hovertip(rb,text = "52 Tellurium",hover_delay = 0)

def i53():       # 53 Iodine
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'deeppink2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Iodine',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'I',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '53',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '126.90447',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+760+183')
    
    h.mainloop()

# 53 Iodine
rb = tkinter.Button(x,text = "I",fg = "black",bg = "deeppink2",width = 4,font = g,command = i53)
rb.place(x = 760,y = 183)
rb = Hovertip(rb,text = "53 Iodine",hover_delay = 0)



def xe54():       # 54 Xenon
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'lightgoldenrod3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Xenon',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'xe',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '54',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '131.90545',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+805+183')
    
    h.mainloop()

# 54 Xenon
rb = tkinter.Button(x,text = "Xe",fg = "black",bg = "lightgoldenrod3",width = 4,font = g,command = xe54)
rb.place(x = 805,y = 183)
rb = Hovertip(rb,text = "54 Xenon",hover_delay = 0)


def bi83():       # 83 Bismuth
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Bismuth',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Bi',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '83',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '208.9804',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+670+214')
    
    h.mainloop()

# 83 Bismuth
rb = tkinter.Button(x,text = "Bi",fg = "black",bg = "green2",width = 4,font = g,command = bi83)
rb.place(x = 670,y = 214)
rb = Hovertip(rb,text = "83 Bismuth",hover_delay = 0)


def po84():       # 84 Polonium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'skyblue')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Polonium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Po',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '84',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '209',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+715+214')
    
    h.mainloop()

# 84 Polonium
rb = tkinter.Button(x,text = "Po",fg = "black",bg = "skyblue",width = 4,font = g,command = po84)
rb.place(x = 715,y = 214)
rb = Hovertip(rb,text = "84 Polonium",hover_delay = 0)


def at85():       # 85 Astatine
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'deeppink2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Astatine',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'At',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '85',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '210',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+760+214')
    
    h.mainloop()

# 85 Astatine
rb = tkinter.Button(x,text = "At",fg = "black",bg = "deeppink2",width = 4,font = g,command = at85)
rb.place(x = 760,y = 214)
rb = Hovertip(rb,text = "85 Astatine",hover_delay = 0)

def rn86():       # 86 Radon
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'lightgoldenrod3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Radon',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Rn',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '86',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '222',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+805+214')
    
    h.mainloop()

# 86 Radon
rb = tkinter.Button(x,text = "Rn",fg = "black",bg = "lightgoldenrod3",width = 4,font = g,command = rn86)
rb.place(x = 805,y = 214)
rb = Hovertip(rb,text = "86 Radon",hover_delay = 0)

def mc115():       # 115 Moscovium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Moscovium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Mc',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '115',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '289',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+670+245')
    
    h.mainloop()



# 115 Moscovium
rb = tkinter.Button(x,text = "Mc",fg = "black",bg = "green2",width = 4,font = g,command = mc115)
rb.place(x = 670,y = 245)
rb = Hovertip(rb,text = "115 Moscovium",hover_delay = 0)


def lv116():       # 116 Livermorium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'green2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Livermorium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Lv',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '116',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '293',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+715+245')
    
    h.mainloop()



# 116 Livermorium
rb = tkinter.Button(x,text = "Lv",fg = "black",bg = "green2",width = 4,font = g,command = lv116)
rb.place(x = 715,y = 245)
rb = Hovertip(rb,text = "116 Livermorium",hover_delay = 0)


def ts117():       # 117 Tennessine
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'deeppink2')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Tennessine',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ts',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '117',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '294',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+760+245')
    
    h.mainloop()



# 117 Tennessine
rb = tkinter.Button(x,text = "Ts",fg = "black",bg = "deeppink2",width = 4,font = g,command = ts117)
rb.place(x = 760,y = 245)
rb = Hovertip(rb,text = "117 Tennessine",hover_delay = 0)


def og118():       # 118 Oganesson
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'lightgoldenrod3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Oganesson',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Og',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '118',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '294',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+805+245')
    
    h.mainloop()

# 118 Oganesson
rb = tkinter.Button(x,text = "Og",fg = "black",bg = "lightgoldenrod3",width = 4,font = g,command = og118)
rb.place(x = 805,y = 245)
rb = Hovertip(rb,text = "118 Oganesson",hover_delay = 0)

# Lamthanide

def la57():       # 57 Lanthanum
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Lanthanum',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'La',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '57',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '138.90547',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+130+275')
    
    h.mainloop()

# 57 Lanthanum
rb = tkinter.Button(x,text = "La",fg = "black",bg = "cyan",width = 4,font = g,command = la57)
rb.place(x = 130,y = 305)
rb = Hovertip(rb,text = "57 Lanthanum",hover_delay = 0)


def ce58():       # 58 Cerium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Cerium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ce',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '58',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '140.116',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+175+305')
    
    h.mainloop()

# 58 Cerium
rb = tkinter.Button(x,text = "Ce",fg = "black",bg = "cyan",width = 4,font = g,command =ce58)
rb.place(x = 175,y = 305)
rb = Hovertip(rb,text = "58 Cerium",hover_delay = 0)


def pr59():       # 59 Praseodymium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Praseodymium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Pr',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '59',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '140.90765',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+220+305')
    
    h.mainloop()

# 59 Praseodymium
rb = tkinter.Button(x,text = "Pr",fg = "black",bg = "cyan",width = 4,font = g,command = pr59)
rb.place(x = 220,y = 305)
rb = Hovertip(rb,text = "59 Praseodymium",hover_delay = 0)


def nd60():       # 60 Neodymium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Neodymium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Nd',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '60',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '144.242',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+265+305')
    
    h.mainloop()

# 60 Neodymium
rb = tkinter.Button(x,text = "Nd",fg = "black",bg = "cyan",width = 4,font = g,command = nd60)
rb.place(x = 265,y = 305)
rb = Hovertip(rb,text = "60 Neodymium",hover_delay = 0)


def pm61():       # 61 Promethium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Promethium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Pm',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '61',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '145',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+310+305')
    
    h.mainloop()

# 61 Promethium
rb = tkinter.Button(x,text = "Pm",fg = "black",bg = "cyan",width = 4,font = g,command = pm61)
rb.place(x = 310,y = 305)
rb = Hovertip(rb,text = "61 Promethium",hover_delay = 0)

def sm62():       # 62 Samarium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Samarium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Sm',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '62',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '150.36',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+355+305')
    
    h.mainloop()

# 62 Samarium
rb = tkinter.Button(x,text = "Sm",fg = "black",bg = "cyan",width = 4,font = g,command = sm62)
rb.place(x = 355,y = 305)
rb = Hovertip(rb,text = "62 Samarium",hover_delay = 0)

def eu63():       # 63 Europium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Europium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Eu',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '63',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '151.964',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+400+305')
    
    h.mainloop()

# 63 Europium
rb = tkinter.Button(x,text = "Eu",fg = "black",bg = "cyan",width = 4,font = g,command = eu63)
rb.place(x = 400,y = 305)
rb = Hovertip(rb,text = "63 Europium",hover_delay = 0)

def gd64():       # 64 Gadolinium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Gadolinium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Gd',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '64',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '157.25',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+445+305')
    
    h.mainloop()

# 64 Gadolinium
rb = tkinter.Button(x,text = "Gd",fg = "black",bg = "cyan",width = 4,font = g,command = gd64)
rb.place(x = 445,y = 305)
rb = Hovertip(rb,text = "64 Gadolinium",hover_delay = 0)

def tb65():       #65 Terbium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Terbium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Tb',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '65',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '158.92535',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+490+305')
    
    h.mainloop()

# 65 Terbium
rb = tkinter.Button(x,text = "Tb",fg = "black",bg = "cyan",width = 4,font = g,command = tb65)
rb.place(x = 490,y = 305)
rb = Hovertip(rb,text = "65 Terbium",hover_delay = 0)


def dy66():       #66 Dysprosium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Dysprosium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Dy',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '66',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '162.5',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+535+305')
    
    h.mainloop()

# 66 Dysprosium
rb = tkinter.Button(x,text = "Dy",fg = "black",bg = "cyan",width = 4,font = g,command = dy66)
rb.place(x = 535,y = 305)
rb = Hovertip(rb,text = "66 Dysprosium",hover_delay = 0)

def ho67():       #67 Holmium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Holmium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ho',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '67',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '164.93032',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+580+305')
    
    h.mainloop()

# 67 Holmium
rb = tkinter.Button(x,text = "Ho",fg = "black",bg = "cyan",width = 4,font = g,command = ho67)
rb.place(x = 580,y = 305)
rb = Hovertip(rb,text = "67 Holmium",hover_delay = 0)


def er68():       #68 Erbium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Erbium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Er',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '68',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '167.259',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+625+305')
    
    h.mainloop()

# 68 Erbium
rb = tkinter.Button(x,text = "Er",fg = "black",bg = "cyan",width = 4,font = g,command = er68)
rb.place(x = 625,y = 305)
rb = Hovertip(rb,text = "68 Erbium",hover_delay = 0)




def tm69():       #69 Thulium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Thulium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Tm',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '69',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '168.93421',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+670+305')
    
    h.mainloop()

# 69 Thulium
rb = tkinter.Button(x,text = "Tm",fg = "black",bg = "cyan",width = 4,font = g,command = tm69)
rb.place(x = 670,y = 305)
rb = Hovertip(rb,text = "69 Thulium",hover_delay = 0)




def yb70():       #70 Ytterbium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Ytterbium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Yb',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '70',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '173.04',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+715+305')
    
    h.mainloop()

# 70 Ytterbium
rb = tkinter.Button(x,text = "Yb",fg = "black",bg = "cyan",width = 4,font = g,command = yb70)
rb.place(x = 715,y = 305)
rb = Hovertip(rb,text = "70 Ytterbium",hover_delay = 0)


def lu71():       #71 Lutetium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'cyan')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Lutetium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Lu',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '71',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '173.04',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+760+305')
    
    h.mainloop()

# 71 Lutetium
rb = tkinter.Button(x,text = "Lu",fg = "black",bg = "cyan",width = 4,font = g,command = lu71)
rb.place(x = 760,y = 305)
rb = Hovertip(rb,text = "71 Lutetium",hover_delay = 0)



def ac89():       #89 Actinium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Actinium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Ac',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '89',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '277',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+130+336')
    
    h.mainloop()

# 89 Actinium
rb = tkinter.Button(x,text = "Ac",fg = "black",bg = "Hotpink3",width = 4,font = g,command = ac89)
rb.place(x = 130,y = 336)
rb = Hovertip(rb,text = "89 Actinium",hover_delay = 0)

def th90():       # 90 Thorium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Thorium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Th',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '90',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '232.03806',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+175+336')
    
    h.mainloop()

# 90 Thorium
rb = tkinter.Button(x,text = "Th",fg = "black",bg = "Hotpink3",width = 4,font = g,command = th90)
rb.place(x = 175,y = 336)
rb = Hovertip(rb,text = "90 Thorium",hover_delay = 0)

def pa91():       # 91 Protactinium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Protactinium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Pa',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '91',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '231.03588',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+220+336')
    
    h.mainloop()

# 91 Protactinium
rb = tkinter.Button(x,text = "Pa",fg = "black",bg = "Hotpink3",width = 4,font = g,command = pa91)
rb.place(x = 220,y = 336)
rb = Hovertip(rb,text = "91 Protactinium",hover_delay = 0)

def u92():       # 92 Uranium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Uranium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'U',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '92',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '238.02891',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+265+336')
    
    h.mainloop()

# 92 Uranium
rb = tkinter.Button(x,text = "U",fg = "black",bg = "Hotpink3",width = 4,font = g,command = u92)
rb.place(x = 265,y = 336)
rb = Hovertip(rb,text = "92 Uranium",hover_delay = 0)

def np93():       # 93 Neptunium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Neptunium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Np',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    an = tkinter.Label(h,text = '93',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '237.0482',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+310+336')
    
    h.mainloop()

# 93 Neptunium
rb = tkinter.Button(x,text = "Np",fg = "black",bg = "Hotpink3",width = 4,font = g,command = np93)
rb.place(x = 310,y = 336)
rb = Hovertip(rb,text = "93 Neptunium",hover_delay = 0)


def pu94():       # 94 Plutonium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Plutonium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Pu',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '94',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '244',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+355+336')
    
    h.mainloop()

# 94 Plutonium
rb = tkinter.Button(x,text = "Pu",fg = "black",bg = "Hotpink3",width = 4,font = g,command = pu94)
rb.place(x = 355,y = 336)
rb = Hovertip(rb,text = "94 Plutonium",hover_delay = 0)

def am95():       # 95 Americium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Americium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Am',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '95',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '243',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+400+336')
    
    h.mainloop()

# 95 Americium
rb = tkinter.Button(x,text = "Am",fg = "black",bg = "Hotpink3",width = 4,font = g,command = am95)
rb.place(x = 400,y = 336)
rb = Hovertip(rb,text = "95 Americium",hover_delay = 0)

def cm96():       # 96 Curium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Curium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Cm',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '96',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '247',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+445+336')
    
    h.mainloop()

# 96 Curium
rb = tkinter.Button(x,text = "Cm",fg = "black",bg = "Hotpink3",width = 4,font = g,command = cm96)
rb.place(x = 445,y = 336)
rb = Hovertip(rb,text = "96 Curium",hover_delay = 0)


def bk97():       # 97 Berkelium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Berkelium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Bk',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '97',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '247',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+490+336')
    
    h.mainloop()

# 97 Berkelium
rb = tkinter.Button(x,text = "Bk",fg = "black",bg = "Hotpink3",width = 4,font = g,command = bk97)
rb.place(x = 490,y = 336)
rb = Hovertip(rb,text = "97 Berkelium",hover_delay = 0)

def cf98():       # 98 Californium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Californium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Cf',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '98',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '251',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+535+336')
    
    h.mainloop()

# 98 Californium
rb = tkinter.Button(x,text = "Cf",fg = "black",bg = "Hotpink3",width = 4,font = g,command = cf98)
rb.place(x = 535,y = 336)
rb = Hovertip(rb,text = "98 Californium",hover_delay = 0)


def es99():       # 99 Einsteinium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Einsteinium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Es',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '99',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '252',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+580+336')
    
    h.mainloop()

# 99 Einsteinium
rb = tkinter.Button(x,text = "Es",fg = "black",bg = "Hotpink3",width = 4,font = g,command = es99)
rb.place(x = 580,y = 336)
rb = Hovertip(rb,text = "99 Einsteinium",hover_delay = 0)

def fm100():       # 100 Fermium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Fermium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Fm',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '100',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '257',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+625+336')
    
    h.mainloop()

# 100 Fermium
rb = tkinter.Button(x,text = "Fm",fg = "black",bg = "Hotpink3",width = 4,font = g,command = fm100)
rb.place(x = 625,y = 336)
rb = Hovertip(rb,text = "100 Fermium",hover_delay = 0)

def md101():       # 101 Mendelevium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Mendelevium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Md',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '101',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '258',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+670+336')
    
    h.mainloop()

# 101 Mendelevium
rb = tkinter.Button(x,text = "Md",fg = "black",bg = "Hotpink3",width = 4,font = g,command = md101)
rb.place(x = 670,y = 336)
rb = Hovertip(rb,text = "101 Mendelevium",hover_delay = 0)

def no102():       # 102 Nobelium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Nobelium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'No',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '102',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '259',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+615+336')
    
    h.mainloop()

# 102 Nobelium
rb = tkinter.Button(x,text = "No",fg = "black",bg = "Hotpink3",width = 4,font = g,command = no102)
rb.place(x = 715,y = 336)
rb = Hovertip(rb,text = "102 Nobelium",hover_delay = 0)

def lr103():       # 103 Lawrencium
    h = tkinter.Toplevel()
    h.geometry("350x200")
    h.resizable(0,0)
    h.title("theprogrammer__")
    
    h.config(bg = 'hotpink3')
    
    name = tkinter.Label(h,text = "Name :",font = g,bg = "black",fg = "white",width = 14)
    name.place(x = 20,y = 30)
    
    symbol = tkinter.Label(h,text = "Symbol :",font = g,bg = "black",fg = "white",width = 14)
    symbol.place(x = 20,y = 70)
    
    atomic_n = tkinter.Label(h,text = "Atomic Number :",font = g,bg = "black",fg = "white",width = 14)
    atomic_n.place(x = 20,y = 110)
    
    atomic_m = tkinter.Label(h,text = "Atomic Mass :",font = g,bg = "black",fg = "white",width = 14)
    atomic_m.place(x = 20,y = 150)
    
    n = tkinter.Label(h,text = 'Lawrencium',font = g,bg = "black",fg = "white",width = 14)
    n.place(x = 170,y = 30)
    
    s = tkinter.Label(h,text = 'Lr',font = g,bg = "black",fg = "white",width = 14)
    s.place(x = 170,y = 70)
    
    
    an = tkinter.Label(h,text = '103',font = v,bg = "black",fg = "white",width = 13)
    an.place(x = 170,y = 110)
    
    am = tkinter.Label(h,text = '262',font = v,bg = "black",fg = "white",width = 13)
    am.place(x = 170,y = 150)
    
    h.geometry('+760+336')
    
    h.mainloop()

# 103 Lawrencium
rb = tkinter.Button(x,text = "Lr",fg = "black",bg = "Hotpink3",width = 4,font = g,command = lr103)
rb.place(x = 760,y = 336)
rb = Hovertip(rb,text = "103 Lawrencium",hover_delay = 0)

code = tkinter.Label(x,text = "PROGRAMMED BY PAWAN SRI KANTH",font = g,fg = 'white',bg = 'black')
code.place(x = 550,y = 470)

akkali = tkinter.Label(x,text = "Alkali Metal",font = g,fg = 'black',bg = 'red',width = 13)
akkali.place(x = 20,y = 400)

akkali = tkinter.Label(x,text = "Alkaline Earth",font = g,fg = 'black',bg = 'Orange',width = 13)
akkali.place(x = 20,y = 430)

akkali = tkinter.Label(x,text = "Transition Metal",font = g,fg = 'black',bg = 'yellow',width = 13)
akkali.place(x = 20,y = 460)

akkali = tkinter.Label(x,text = "Nonmetal",font = g,fg = 'black',bg = 'violet',width = 13)
akkali.place(x = 170,y = 400)

akkali = tkinter.Label(x,text = "Halogen",font = g,fg = 'black',bg = 'deeppink2',width = 13)
akkali.place(x = 170,y = 430)

akkali = tkinter.Label(x,text = "Noble Gas",font = g,fg = 'black',bg = 'lightgoldenrod3',width = 13)
akkali.place(x = 170,y = 460)

akkali = tkinter.Label(x,text = "Basic Metal",font = g,fg = 'black',bg = 'green2',width = 13)
akkali.place(x = 320,y = 400)

akkali = tkinter.Label(x,text = "Semimetal",font = g,fg = 'black',bg = 'skyblue',width = 13)
akkali.place(x = 320,y = 430)

akkali = tkinter.Label(x,text = "Lanthanide",font = g,fg = 'black',bg = 'cyan',width = 13)
akkali.place(x = 320,y = 460)

akkali = tkinter.Label(x,text = "Actinide",font = g,fg = 'black',bg = 'hotpink3',width = 13)
akkali.place(x = 470,y = 400)

x.mainloop()
