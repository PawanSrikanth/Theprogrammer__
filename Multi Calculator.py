import tkinter  as tk
from tkinter  import ttk
from idlelib.tooltip import Hovertip
import math

x = tk.Tk()
x.title('theprogrammer')
x.config(bg = 'lavender')
x.config(highlightcolor = 'white',highlightthickness = 2)

x.geometry('500x500')
x.geometry('+400+200')
x.resizable(0,0)

g = 'georgia'
v = 'verdana'
t = ('times new roman',10)

wel = tk.Label(x,text = "Welcome to   \n theprogrammer__")
wel.config(bg = 'lavender',fg = 'black',font = ('Times New Roman',30))
w = Hovertip(wel,'Click on Calculator Button',hover_delay = 1000)
wel.place(x = 110,y = 100)

def calc():
    z = tk.Toplevel()
    z.config(bg = 'lavender')
    z.resizable(0,0)
    z.config(highlightcolor = 'white',highlightthickness = 2)

    z.geometry('500x500')
    z.geometry('+400+200')
    
    l = tk.Label(z,width = 500,height= 500,bg = 'lavender')
    l.pack()
    
    
    def arithmetic():
        a = tk.Toplevel()
        a.geometry('300x300')
        a.geometry('+590+250')
        a.resizable(0,0)
        a.config(background = 'white')
        a.config(highlightcolor = 'white',highlightthickness = 2)
        
        
        def adding():
            num_1 = e1.get()
            num_2 = e2.get()
            
            num_1 = eval(num_1)
            num_2 = eval(num_2)
            
            final = num_1 + num_2
            
            res.delete(0,tk.END)
            res.insert(0,final)
            
        def subtract():
            num_1 = e1.get()
            num_2 = e2.get()
            
            num_1 = eval(num_1)
            num_2 = eval(num_2)
            
            
            final = num_1 - num_2
            
            res.delete(0,tk.END)
            res.insert(0,final)
            
        def multi():
            num_1 = e1.get()
            num_2 = e2.get()
            
            num_1 = eval(num_1)
            num_2 = eval(num_2)
            
            
            final = num_1 * num_2
            
            res.delete(0,tk.END)
            res.insert(0,final)
        
        def quo():
            num_1 = e1.get()
            num_2 = e2.get()
            
            num_1 = eval(num_1)
            num_2 = eval(num_2)
            
            
            final = num_1 / num_2
            
            res.delete(0,tk.END)
            res.insert(0,round(final,4))
        
        def remind():
            num_1 = e1.get()
            num_2 = e2.get()
            
            num_1 = eval(num_1)
            num_2 = eval(num_2)
            
            
            final = num_1 % num_2
            
            res.delete(0,tk.END)
            res.insert(0,final)
        
        ent1 = tk.Label(a,text = 'Enter Number 1',bg = 'white',fg = 'black',font = t,width = 12)
        ent1.place(x = 10,y = 22)
        
        e1 = tk.Entry(a,bg = 'white',fg = 'black',bd = 2,highlightcolor = 'black',highlightthickness = 2,font = (v,10))
        e1.place(x = 120,y = 20)
        
        ent2 = tk.Label(a,text = 'Enter Number 2',bg = 'white',fg = 'black',font = t,width = 12)
        ent2.place(x = 10,y = 72)
        
        e2 = tk.Entry(a,bg = 'white',fg = 'black',bd = 2,highlightcolor = 'black',highlightthickness = 2,font = (v,10))
        e2.place(x = 120,y = 70)
        
        res_1 = tk.Label(a,text = 'Result',bg = 'white',fg = 'black',font = t,width = 12)
        res_1.place(x = 10,y = 132)
        
        res = tk.Entry(a,bg = 'white',fg = 'black',bd = 2,highlightcolor = 'black',highlightthickness = 2,font = (v,10))
        res.place(x = 120,y = 130)
        
        
        def clearing():
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            res.delete(0,tk.END)

        add= tk.Button(a,text = '+',font = (g,10),bg = 'blue',fg = 'white',width = 3,command = adding,bd = 3)
        add.place(x = 20,y = 200)
        add = Hovertip(add,'Addition',hover_delay = 0) 
        
        sub = tk.Button(a,text = '-',font = g,bg = 'blue',fg = 'white',width = 3,command = subtract,bd = 3)
        sub.place(x = 70,y = 200)
        sub = Hovertip(sub,'Subtraction',hover_delay = 0)
        
        mul = tk.Button(a,text = '*',font = g,bg = 'blue',fg = 'white',width = 3,command = multi,bd = 3)
        mul.place(x = 120,y = 200)
        mul = Hovertip(mul,'Multiplication',hover_delay = 0)
        
        div = tk.Button(a,text = '/',font = g,bg = 'blue',fg = 'white',width = 3,command = quo,bd = 3)
        div.place(x = 170,y = 200)
        div = Hovertip(div,'Division',hover_delay = 0)
        
        rem = tk.Button(a,text = '%',font = g,bg = 'blue',fg = 'white',width = 3,command = remind,bd = 3)
        rem.place(x = 220,y = 200)
        rem = Hovertip(rem,'Reminder',hover_delay = 0)
        
        clear = tk.Button(a,text = 'Clear',font = g,bg = 'red',fg = 'white',width = 5,command = clearing,bd = 3)
        clear.place(x = 110,y = 250)
        clear = Hovertip(clear,'It will clear all the numbers \nin the entrybox',hover_delay = 0)
        
        a.mainloop()

    # Arithmetic
    ari = tk.Button(l,text = 'Arithmetic',bg = 'black',fg = 'green3',font = (g,12),width = 17,command = arithmetic)
    tool = Hovertip(ari,'+ - * / %',hover_delay = 0)
    ari.place(x = 10,y = 50)
    
    
    def singleinput():
        si = tk.Toplevel()
        si.geometry('300x330')
        si.geometry('+590+250')
        si.resizable(0,0)
        si.config(background = 'white')
        si.config(highlightcolor = 'white',highlightthickness = 2)
        
        
        ent1 = tk.Label(si,text = 'Enter Number 1',bg = 'white',fg = 'black',font = t,width = 12)
        ent1.place(x = 10,y = 22)
        
        e1 = tk.Entry(si,bg = 'white',fg = 'black',bd = 2,highlightcolor = 'black',highlightthickness = 2,font = (v,10))
        e1.place(x = 120,y = 20)
        
        ent2 = tk.Label(si,text = 'Result',bg = 'white',fg = 'black',font = t,width = 12)
        ent2.place(x = 10,y = 72)
        final = tk.Entry(si,bg = 'white',fg = 'black',bd = 2,highlightcolor = 'green3',highlightthickness = 2,font = (v,10))
        final.place(x = 120,y = 70)
        
        def ceilx():
            x = e1.get()
            x = eval(x)
            
            fin =  math.ceil(x)
            final.delete(0,tk.END)
            final.insert(0,fin)
            
        ceil = tk.Button(si,text = 'Ceil',font = g,bg = 'green3',fg = 'black',width = 3,command = ceilx)
        ceil.place(x = 30,y = 130)
        ceil = Hovertip(ceil,'Rounds a number upto\n the nearest integer',hover_delay = 0) 
        
        def degreesx():
            x = e1.get()
            x = eval(x)
            fin =  math.degrees(x)
            final.delete(0,tk.END)
            final.insert(0,fin)
        
        degrees = tk.Button(si,text = 'Deg',font = g,bg = 'green3',fg = 'black',width = 3,command = degreesx)
        degrees.place(x = 80,y = 130)
        degrees = Hovertip(degrees,'Converts an angle from \n from radians to degrees',hover_delay = 0)
        
        def expx():
            x = e1.get()
            x = eval(x)
            fin =  math.exp(x)
            final.delete(0,tk.END)
            final.insert(0,fin)
        
        exp = tk.Button(si,text = 'Exp',font = g,bg = 'green3',fg = 'black',width = 3,command = expx)
        exp.place(x = 130,y = 130)
        exp = Hovertip(exp,'Returns E raised to the power of x',hover_delay = 0)
        
        def fabsx():
            x = e1.get()
            x = eval(x)
            
            fin =  math.fabs(x)
            final.delete(0,tk.END)
            final.insert(0,fin)
        
        fabs = tk.Button(si,text = 'Fabs',font = g,bg = 'green3',fg = 'black',width = 3,command = fabsx)
        fabs.place(x = 180,y = 130)
        fabs = Hovertip(fabs,'Returns the absolute value \n of a number',hover_delay = 0)
    
        def factorialx():
            x = e1.get()
            x = eval(x)
            
            if(x < 0):
                final.insert(0,'Enter only positive value')
        
            else:
                fin =  math.factorial(x)
                final.delete(0,tk.END)
                final.insert(0,fin)
            
        factorial = tk.Button(si,text = 'Fact',font = g,bg = 'green3',fg = 'black',width = 3,command = factorialx)
        factorial.place(x = 230,y = 130)
        factorial = Hovertip(factorial,'Returns the factorial of a number',hover_delay = 0)
        
        
        def isqrtx():
            x = e1.get()
            x = eval(x)
            
            if(x < 0):
                final.insert(0,'Enter only positive value')

            else:
                fin =  math.isqrt(x)
                final.delete(0,tk.END)
                final.insert(0,fin)
        
        isqrt = tk.Button(si,text = 'Qrt',font = g,bg = 'yellow',fg = 'black',width = 3,command = isqrtx)
        isqrt.place(x = 30,y = 180)
        isqrt = Hovertip(isqrt,'Rounds a square root number \ndownwards to the nearest integer',hover_delay = 0) 
    
        def floorx():
            x = e1.get()
            x = eval(x)
            
            fin =  math.floor(x)
            final.delete(0,tk.END)
            final.insert(0,fin)
            
        floor = tk.Button(si,text = 'Flr',font = g,bg = 'yellow',fg = 'black',width = 3,command = floorx)
        floor.place(x = 80,y = 180)
        floor = Hovertip(floor,'Floor() - Rounds a number down \nto the nearest integer',hover_delay = 0) 
        
        def logx():
            x = e1.get()
            x = eval(x)
            
            if(x < 0):
                final.insert(0,'Enter only positive value')
            else:
                fin =  math.log(x)
                final.delete(0,tk.END)
                final.insert(0,fin)
            
        log = tk.Button(si,text = 'Log',font = g,bg = 'yellow',fg = 'black',width = 3,command = logx)
        log.place(x = 130,y = 180)
        log = Hovertip(log,'Returns the natural logarithm\nof a number,or the logarithm \nof a number to base',hover_delay = 0) 
        
        def log2x():
            x = e1.get()
            x = eval(x)
            
            if(x < 0):
                final.insert(0,'Enter only positive value')
            else:
                fin =  math.log2(x)
                final.delete(0,tk.END)
                final.insert(0,fin)
            
        log2 = tk.Button(si,text = 'Log2',font = g,bg = 'yellow',fg = 'black',width = 3,command = log2x)
        log2.place(x = 180,y = 180)
        log2 = Hovertip(log2,'Returns the base -2 logarithm of x',hover_delay = 0) 
        
        def log10x():
            x = e1.get()
            x = eval(x)
            
            if(x < 0):
                final.insert(0,'Enter only positive value')
            
            
            else:
                fin =  math.log10(x)
                final.delete(0,tk.END)
                final.insert(0,fin)
            
            
        
        log10 = tk.Button(si,text = 'Lg10',font = g,bg = 'yellow',fg = 'black',width = 3,command = log10x)
        log10.place(x = 230,y = 180)
        log10 = Hovertip(log10,'Log10 - Returns the base -10 logarithm of x',hover_delay = 0) 
        
        
        def radx():
            x = e1.get()
            x = eval(x)
            
            fin =  math.radians(x)
            final.delete(0,tk.END)
            final.insert(0,fin)
            
        
        radians = tk.Button(si,text = 'Rad',font = g,bg = 'blue',fg = 'white',width = 3,command = radx)
        radians.place(x = 30,y = 230)
        radians = Hovertip(radians,'converts a degree value into radians',hover_delay = 0) 
        
        def truncx():
            x = e1.get()
            x = eval(x)
            
            fin =  math.trunc(x)
            final.delete(0,tk.END)
            final.insert(0,fin)
            
        
        trunc = tk.Button(si,text = 'Trun',font = g,bg = 'blue',fg = 'white',width = 3,command = truncx)
        trunc.place(x = 80,y = 230)
        trunc = Hovertip(trunc,'Returns the truncated integer \n parts of a number',hover_delay = 0) 
        
        
        def sinx():
            x = e1.get()
            x = eval(x)
            
            fin =  math.sin(x)
            final.delete(0,tk.END)
            final.insert(0,fin)
            
        
        sin = tk.Button(si,text = 'Sin',font = g,bg = 'blue',fg = 'white',width = 3,command = sinx)
        sin.place(x = 130,y = 230)
        sin = Hovertip(sin,'Returns the sine of a number',hover_delay = 0) 
        
        def cosx():
            x = e1.get()
            x = eval(x)
            
            fin =  math.cos(x)
            final.delete(0,tk.END)
            final.insert(0,fin)
            
        cos = tk.Button(si,text = 'Cos',font = g,bg = 'blue',fg = 'white',width = 3,command = cosx)
        cos.place(x = 180,y = 230)
        cos = Hovertip(cos,'Returns the cosine of a number',hover_delay = 0) 
        
        def tanx():
            x = e1.get()
            x = eval(x)
            
            fin =  math.tan(x)
            final.delete(0,tk.END)
            final.insert(0,fin)
        
        tan = tk.Button(si,text = 'Tan',font = g,bg = 'blue',fg = 'white',width = 3,command = tanx)
        tan.place(x = 230,y = 230)
        tan = Hovertip(tan,'Returns the tangent of a number',hover_delay = 0) 
        
        def clearing():
            e1.delete(0,tk.END)
            final.delete(0,tk.END)
            
        clear = tk.Button(si,text = 'Clear',font = g,bg = 'red',fg = 'white',width = 5,command = clearing,bd = 3)
        clear.place(x = 110,y = 280)
        clear = Hovertip(clear,'It will clear all the numbers \nin the entrybox',hover_delay = 0)
  
    single = tk.Button(l,text = 'Single Input functions',bg = 'black',fg = 'green3',font = (g,12),width = 17,command = singleinput)
    tool2 = Hovertip(single,'fx(x)',hover_delay = 0)
    single.place(x = 10,y = 100)
    
    def unitconvert():
        u = tk.Toplevel()
        u.geometry('300x220')
        u.geometry('+590+250')
        u.resizable(0,0)
        u.config(background = 'white')
        u.config(highlightcolor = 'white',highlightthickness = 2) 
        
        def converter():
            first = str(first_unit.get())
            second = str(second_unit.get())
            
            units = ['Millimetre','Centimetre','Metre','kilometre']
            
            # 0 - 0
            if(first == units[0] and second == units[0]):
                e1.delete(0,tk.END)
                e2.delete(0,tk.END)
                e1.insert(0,0)
                e2.insert(0,0)
            
            if(first == units[1] and second == units[1]):
                e1.delete(0,tk.END)
                e2.delete(0,tk.END)
                e1.insert(0,0)
                e2.insert(0,0)
            
            if(first == units[2] and second == units[2]):
                e1.delete(0,tk.END)
                e2.delete(0,tk.END)
                e1.insert(0,0)
                e2.insert(0,0)
            
            if(first == units[3] and second == units[3]):
                e1.delete(0,tk.END)
                e2.delete(0,tk.END)
                e1.insert(0,0)
                e2.insert(0,0)
            
            if(first == units[0] and second == units[1]): #milli to centi
                entry1 = eval(e1.get())
                
                fin = entry1 * 0.1 
                
                e2.delete(0,tk.END)
                e2.insert(0,round(fin,2))
                        
            if(first == units[1] and second == units[0]): #centi to milli
                entry1 = eval(e1.get())
                
                fin = entry1 / 0.1 
                
                e2.delete(0,tk.END)
                e2.insert(0,round(fin,2))
            
            if(first == units[0]) and (second == units[2]): # millimetre to metre
                entry1 = eval(e1.get())
                
                
                Result = entry1 * 0.001
                
                e2.delete(0,tk.END)
                e2.insert(0,round(Result,5))
            
            if(first == units[2]) and (second == units[0]): # metre to millimetre
                entry1 = eval(e1.get())
            
                Result = entry1 / 0.001
                
                e2.delete(0,tk.END)
                e2.insert(0,round(Result,5))
            
                        
            if(first == units[0]) and (second == units[3]): # millimetre to Kilometre
                entry1 = eval(e1.get())

                
                Result = entry1 * 0.000001
                
                e2.delete(0,tk.END)
                e2.insert(0,round(Result,10))
            
            if(first == units[3]) and (second == units[0]):  #  kilometre to millimetre
                entry1 = eval(e1.get())

                
                Result = entry1 / 0.000001
                
                e2.delete(0,tk.END)
                e2.insert(0,round(Result,5))
            
               
            # units = ['Millimetre','Centimetre','Metre','kilometre']    
            if(first == units[1]) and (second == units[2]):  #  centi to metre
                entry1 = eval(e1.get())

                
                Result = entry1 * 0.01
                
                e2.delete(0,tk.END)
                e2.insert(0,round(Result,5))
            
            if(first == units[2]) and (second == units[1]):  #  metre to centi
                entry1 = eval(e1.get())

                
                Result = entry1 / 0.01
                
                e2.delete(0,tk.END)
                e2.insert(0,round(Result,5))
            
            if(first == units[1]) and (second == units[3]):  #  centi to kilo
                entry1 = eval(e1.get())

                
                Result = entry1 * 0.00001
                
                e2.delete(0,tk.END)
                e2.insert(0,round(Result,5))
            
            if(first == units[3]) and (second == units[1]):  #  kilo to centi
                entry1 = eval(e1.get())

                
                Result = entry1 * 100000
                
                e2.delete(0,tk.END)
                e2.insert(0,round(Result,5))
            
            if(first == units[2]) and (second == units[3]):  #  metre to kilo
                entry1 = eval(e1.get())

                
                Result = entry1 * 0.001
                
                e2.delete(0,tk.END)
                e2.insert(0,round(Result,5))
            
            if(first == units[3]) and (second == units[2]):  #  kilo to metre
                entry1 = eval(e1.get())

                
                Result = entry1 / 0.001
                
                e2.delete(0,tk.END)
                e2.insert(0,round(Result,5))
                
        
        first_unit = ttk.Combobox(u,foreground = 'red')
        
        first_unit['values'] = [ 'Millimetre','Centimetre','Metre','kilometre']
        first_unit.config(width = 10)
        first_unit.place(x = 20,y = 30)
        
        
        e1 = tk.Entry(u,bg = 'white',fg = 'red',bd = 2,highlightcolor = 'black',highlightthickness = 2,)
        e1.place(x = 150,y = 30)
        enter = Hovertip(e1,'Enter number here only',hover_delay = 1000)
        e1.insert(0,0)
        
        
        second_unit = ttk.Combobox(u,foreground = 'green3')
        second_unit['values'] = [ 'Millimetre','Centimetre','Metre','kilometre']
        second_unit.config(width = 10)
        second_unit.place(x = 20,y = 80)
        
        
        e2 = tk.Entry(u,bg = 'white',fg = 'green3',bd = 2,highlightcolor = 'black',highlightthickness = 2)
        e2.place(x = 150,y = 80)
        res = Hovertip(e2,'Result Box',hover_delay = 1000)
        e2.insert(0,0)
        
        
        cal = tk.Button(u,text = 'Convert',bg = 'cyan',fg = 'black',font = g,bd = 2,highlightcolor='black',highlightthickness = 2)
        cal.config(command = converter)
        cal.place(x = 100,y = 150)
        
        
        u.mainloop()
    
    unit = tk.Button(l,text = 'Metric Units',bg = 'black',fg = 'green3',font = (g,12),width = 17,command = unitconvert)
    tool3 = Hovertip(unit,'Mm Cm M Km',hover_delay = 0)
    unit.place(x = 10,y = 150)
    
    def double():
        d = tk.Toplevel()
        d.geometry('300x300')
        d.geometry('+590+250')
        d.resizable(0,0)
        d.config(background = 'white')
        d.config(highlightcolor = 'white',highlightthickness = 2)
        
        
        
        
        ent1 = tk.Label(d,text = 'Enter x value',bg = 'white',fg = 'black',font = t,width = 12)
        ent1.place(x = 10,y = 22)
        
        e1 = tk.Entry(d,bg = 'white',fg = 'black',bd = 2,highlightcolor = 'black',highlightthickness = 2,font = (v,10))
        e1.place(x = 120,y = 20)
        
        ent2 = tk.Label(d,text = 'Enter y value',bg = 'white',fg = 'black',font = t,width = 12)
        ent2.place(x = 10,y = 72)
        
        e2 = tk.Entry(d,bg = 'white',fg = 'black',bd = 2,highlightcolor = 'black',highlightthickness = 2,font = (v,10))
        e2.place(x = 120,y = 70)
        
        f = tk.Label(d,text = 'Result',bg = 'white',fg = 'black',font = t,width = 12)
        f.place(x = 10,y = 122)
        
                
        def power():
            x = eval(e1.get())
            y = eval(e2.get())
            
            z = math.pow(x,y)
            
            fin.delete(0,tk.END)
            fin.insert(0,z)
        
        def cps():
            x = eval(e1.get())
            y = eval(e2.get())
            
            z = math.copysign(x,y)
            fin.delete(0,tk.END)
            fin.insert(0,z)
        
        def gcd_():
            x = eval(e1.get())
            y = eval(e2.get())
            
            z = math.gcd(x,y)
            fin.delete(0,tk.END)
            fin.insert(0,z)
        
        def reminder():
            x = eval(e1.get())
            y = eval(e2.get())
            
            z = math.remainder(x,y)
            fin.delete(0,tk.END)
            fin.insert(0,z)
        
        def product():
            x = eval(e1.get())
            y = eval(e2.get())
            
            z = math.prod([x,y])
            fin.delete(0,tk.END)
            fin.insert(0,z)
        
        def clearing():
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            fin.delete(0,tk.END)

        
        
        
        fin = tk.Entry(d,bg = 'white',fg = 'black',bd = 2,highlightcolor = 'green3',highlightthickness = 2,font = (v,10))
        fin.place(x = 120,y = 120)

        pow_ = tk.Button(d,text = 'Pow',bg = 'lightgreen',fg = 'black',font = g,command = power,width = 8)
        p = Hovertip(pow_,'Returns the Value of x to the power of y',hover_delay = 0)
        pow_.place(x = 10,y = 180)
                
        copy = tk.Button(d,text = 'Copysign',bg = 'lightgreen',fg = 'black',font = g,command = cps,width = 8)
        cp = Hovertip(copy,'Returns a float consisting of the value \n of the first parameter and \n the sign of the second parameter',hover_delay = 0)
        copy.place(x = 105,y = 180)
        
        gcd = tk.Button(d,text = 'GCD',bg = 'lightgreen',fg = 'black',font = g,command = gcd_,width = 8)
        gc = Hovertip(gcd,'Returns the greatest common divisor of two integers',hover_delay = 0)
        gcd.place(x = 200,y = 180)
        
        rem = tk.Button(d,text = 'Rem',bg = 'lightgreen',fg = 'black',font = g,command = reminder,width = 8)
        rr = Hovertip(rem,'Returns the closest value that can \nmake numerator completely divisible by the denominator',hover_delay = 0)
        rem.place(x = 10,y = 230)
        
        pro = tk.Button(d,text = 'Prod',bg = 'lightgreen',fg = 'black',font = g,command = product,width = 8)
        pr = Hovertip(pro,'Returns the product of all \nthe elements in an iterable',hover_delay = 0)
        pro.place(x = 105,y = 230)
        
        clear = tk.Button(d,text = 'Clear',font = g,bg = 'red',fg = 'white',width = 8,command = clearing)
        clear.place(x = 200,y = 230)
        clear = Hovertip(clear,'It will clear all the numbers \nin the entrybox',hover_delay = 0)
        
        d.mainloop()
        
    di = tk.Button(l,text = 'Double unit functions',bg = 'black',fg = 'green3',font = (g,12),width = 17,command = double)
    da = Hovertip(di,'fx(x,y)',hover_delay = 0)
    di.place(x = 10,y = 200)
    
    def cyy():
        y = tk.Toplevel()
        y.geometry('300x300')
        y.geometry('+590+250')
        y.resizable(0,0)
        y.config(background = 'white')
        y.config(highlightcolor = 'white',highlightthickness = 2)
        
        money__ = tk.Label(y,text = "Enter Your Amount",font = (g,10),bg = 'white',fg = 'black',width = 18)
        money__.place(x = 5,y = 50)
        
        money = tk.Entry(y,bg = 'white',fg = 'black',font = (g,10),bd = 3,width = 13)
        money.place(x = 170,y = 50)
        
        c_money__ = tk.Label(y,text = "Choose Your Currency",font = (g,10),bg = 'white',fg = 'black',width = 18)
        c_money__.place(x = 5,y = 100)
        
        
        
        c_combo = ttk.Combobox(y,font = (g,10),width = 12)
        cur = 'INDIAN RUPEE','US DOLLAR','KUWAITI DINAR','JAPANESE YEN','EURO'
        c_combo['values'] = cur
        c_combo.place(x  = 165,y = 100)
        
        
        ex_money__ = tk.Label(y,text = "Currency you need",font = (g,10),bg = 'white',fg = 'black',width = 18)
        ex_money__.place(x = 5,y = 150)
        
        
        ex_combo = ttk.Combobox(y,font = (g,10),width = 12)
        ex_cur = 'INDIAN RUPEE','US DOLLAR','KUWAITI DINAR','JAPANESE YEN','EURO'
        ex_combo['values'] = ex_cur
        ex_combo.place(x  = 165,y = 150)
        
        
        
        def car():
            moneyx = eval(money.get())
            act = c_combo.get()
            needy = ex_combo.get()
        
            # us to ind
            if(act == 'US DOLLAR') and (needy == 'INDIAN RUPEE'):
                result = (moneyx * 82.85)
                # print(result)
                # final = (moneyx,act,'is equals',result,needy)
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            # ind to us
            if(act == 'INDIAN RUPEE') and (needy == 'US DOLLAR'):
                result = (moneyx / 82.85)
            
            
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
                
            # ind to ind
            if(act == 'INDIAN RUPEE') and (needy == 'INDIAN RUPEE'):
                result = moneyx
            
            
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            # us to us
            if(act == 'US DOLLAR') and (needy == 'US DOLLAR'):
                result = moneyx
            
            
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            # IND TO KUWAITI
            if(act == 'INDIAN RUPEE') and (needy == 'KUWAITI DINAR'):
                result = (moneyx / 270.34)
            
            
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            # KUWAITI TO IND
            if(act == 'KUWAITI DINAR') and (needy == 'INDIAN RUPEE'):
                result = (moneyx * 270.34)
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            # us to kuwaiti
            if(act == 'US DOLLAR') and (needy == 'KUWAITI DINAR'):
                result = (moneyx * 0.31)
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            # KUWAITI TO US
            if(act == 'KUWAITI DINAR') and (needy == 'US DOLLAR'):
                result = (moneyx / 0.31)
             
             
                ca = tk.Label(x,text = 'Converted Amount',font = g,bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
                
            # KUWAITI TO KUWAITI
            if(act == 'KUWAITI DINAR') and (needy == 'KUWAITI DINAR'):
                result = moneyx
            
            
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            # IND TO J_YEN
            if(act == 'INDIAN RUPEE') and (needy == 'JAPANESE YEN'):
                result = (moneyx * 1.80)
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            # J_YEN TO IND
            if(act == 'JAPANESE YEN') and (needy == 'INDIAN RUPEE'):
                result = (moneyx / 1.80)
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
              
            # US TO j_YEN 
            if(act == 'US DOLLAR') and (needy == 'JAPANESE YEN'):
                result = (moneyx * 149.40)
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
                
            # J_YEN TO  US
            if(act == 'JAPANESE YEN') and (needy == 'US DOLLAR'):
                result = (moneyx / 149.40)
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
        
            
            # KUWAIT TO J_YEN
            if(act == 'KUWAITI DINAR') and (needy == 'JAPANESE YEN'):
                result = (moneyx * 485.76)
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            # J_YEN TO KUWAITI DINAR
            if(act == 'JAPANESE YEN') and (needy == 'KUWAITI DINAR'):
                result = (moneyx / 485.76)
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            
            # J_YEN TO J_YEN
            if(act == 'JAPANESE YEN') and (needy == 'JAPANESE YEN'):
                result = moneyx 
                
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            
            # IND TO EURO
            if(act == 'INDIAN RUPEE') and (needy == 'EURO'):
                result = (moneyx * 0.011)
                
                
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            
            # IND TO EURO
            if(act == 'EURO') and (needy == 'INDIAN RUPEE'):
                result = (moneyx / 0.011)
                
                
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
                
            # US TO EURO
            if(act == 'US DOLLAR') and (needy == 'EURO'):
                result = (moneyx * 0.92)
                
                
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
                
                
            # EURO TO US
            if(act == 'EURO') and (needy == 'US DOLLAR'):
                result = (moneyx / 0.92)
                
                
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            
            # KUWAITI TO EURO
            if(act == 'KUWAITI DINAR') and (needy == 'EURO'):
                result = (moneyx * 2.99)
                
                
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
                
            # EURO TO KUWAITI
            if(act == 'EURO') and (needy == 'KUWAITI DINAR'):
                result = (moneyx / 2.99)
                
                
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            
            # J_YEN TO EURO
            if(act == 'JAPANESE YEN') and (needy == 'EURO'):
                result = (moneyx * 0.0061)
                
                
             
             
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
                
            # EURO TO J_YEN
            if(act == 'EURO') and (needy == 'JAPANESE YEN'):
                result = (moneyx / 0.0061)
                
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
            # EURO TO EURO
            if(act == 'EURO') and (needy == 'EURO'):
                result = moneyx
                
                ca = tk.Label(y,text = 'Converted Amount',font = (g,10),bg = 'white',fg = 'black',width = 18)
                ca.place(x = 5,y = 250)
                IND_US = tk.Entry(y,font = (g,10),bg = 'white',fg = 'black',width = 13)
                IND_US.insert(0,round(result,5))
                IND_US.place(x = 170,y = 250)
            
        #============================================================================================================================ 
        calculate = tk.Button(y,text = 'Compute',bg = 'BLACK',fg = 'GREEN',font = g,bd = 3,command = car)
        calculate.place(x = 100,y = 200)

        y.mainloop()
    
    
    cu = tk.Button(l,text = 'Currency converter',bg = 'black',fg = 'green3',font = (g,12),width = 17,command = cyy)
    curr = Hovertip(cu,'$$$$$',hover_delay = 0)
    cu.place(x = 10,y = 250)
    
    
    
    done = tk.Label(l,text = 'PROGRAMMED BY PAWAN SRI KANTH',bg = 'lavender')
    done.config(fg = 'black',font = ('Times New Roman',13))
    done.place(x = 180,y = 460)

    
    
    
    
    
    
    z.mainloop()
    
cal = tk.Button(x,text = 'Calculator',bg = 'black',fg = 'Lavender',bd = 3,borderwidth= 4,cursor = 'watch')
cal.config(font = ('Times New Roman',30))
cal.config(command = calc)


cal.place(x = 150,y = 230)

w = Hovertip(cal,'Click this',hover_delay = 0)

done = tk.Label(x,text = 'PROGRAMMED BY PAWAN SRI KANTH',bg = 'lavender')
done.config(fg = 'black',font = ('Times New Roman',13))
done.place(x = 180,y = 460)

x.mainloop()
