import tkinter
x = tkinter.Tk()
x.title("theprogrammer__")
x.geometry('500x500')
x.maxsize(500,500)
x.config(bg = 'black')

g = 'georgia'
v = 'verdana'

def tenth():
    t = tkinter.Toplevel()
    t.geometry('500x500')
    t.maxsize(500,500)
    t.config(bg = 'black')
    
    def checking():
        ta = (tam_entry.get())
        e  = (eng_entry.get())
        m  = (mat_entry.get())
        s  = (sci_entry.get())
        ss = (soc_entry.get())
        
        
        ta = eval(ta)
        e = eval(e)
        m = eval(m)
        s = eval(s)
        ss = eval(ss)
        
        total = ta + e + m + s + ss
        per = (total / 500)  * 100
        # print(total)
        # print(per)
        per_round = round(per,2)
        
        if(ta >= 35):
            passed = tkinter.Label(t,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
            passed.place(x = 350,y = 100)
        
        else:
            failed = tkinter.Label(t,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
            failed.place(x = 350,y = 100)
        
        if(e >= 35):
            passed = tkinter.Label(t,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
            passed.place(x = 350,y = 150)
        
        else:
            failed = tkinter.Label(t,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
            failed.place(x = 350,y = 150)
        
        if(m >= 35):
            passed = tkinter.Label(t,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
            passed.place(x = 350,y = 200)
        
        else:
            failed = tkinter.Label(t,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
            failed.place(x = 350,y = 200)
            
        if(s >= 35):
             passed = tkinter.Label(t,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
             passed.place(x = 350,y = 250)
         
        else:
             failed = tkinter.Label(t,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
             failed.place(x = 350,y = 250)
             
        if(ss >= 35):
             passed = tkinter.Label(t,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
             passed.place(x = 350,y = 300)
         
        else:
             failed = tkinter.Label(t,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
             failed.place(x = 350,y = 300)    
        
        
        if( ta >= 35 and e >= 35 and m >= 35 and s  >= 35 and ss >= 35):
            
            examp = tkinter.Label(t,text = "Examination Passed",fg = 'lightgreen',bg = 'black',font = v,width = 17)
            examp.place(x = 100,y = 420 )
        
        else:
            examf = tkinter.Label(t,text = "Examination Failed",fg = 'red',bg = 'black',font = v,width = 17)
            examf.place(x = 100,y = 420 )
        
        
        
        tot = tkinter.Label(t,text = 'Total',bg = 'white',fg = 'black',font = v)
        tot.place(x = 170,y = 350)
        
        tot_ = tkinter.Entry(t,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
        tot_.place(x = 230,y = 350)
        tot_.insert(0,total)
        
        
        per_label = tkinter.Label(t,text = " % ",font = g,fg = 'white',bg = 'black')
        per_label.place(x = 320,y = 350)
        
        per_ = tkinter.Entry(t,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
        per_.place(x = 350,y = 350)
        per_.insert(0,per_round)
    
    
    
    ten = tkinter.Label(t,text = "10 TH",bg = 'white',fg = 'black',font = 'verdana')
    ten.pack()

    tam = tkinter.Label(t,text = "Tamil",bg = 'white',fg = 'black',font = (g,20),width = 10)
    tam.place(x = 30,y = 100)
    
    tam_entry = tkinter.Entry(t,font = (v,20),width = 5,justify = 'center')
    tam_entry.place(x = 220,y = 100)  
    
    
    eng = tkinter.Label(t,text = "English",bg = 'white',fg = 'black',font = (g,20),width = 10)
    eng.place(x = 30,y = 150)
    
    eng_entry = tkinter.Entry(t,font = (v,20),width = 5,justify = 'center')
    eng_entry.place(x = 220,y = 150)  
    
    
    mat = tkinter.Label(t,text = "Mathematics",bg = 'white',fg = 'black',font = (g,20),width = 10)
    mat.place(x = 30,y = 200)
    
    mat_entry = tkinter.Entry(t,font = (v,20),width = 5,justify = 'center')
    mat_entry.place(x = 220,y = 200)
    
    sci = tkinter.Label(t,text = "Science",bg = 'white',fg = 'black',font = (g,20),width = 10)
    sci.place(x = 30,y = 250)
    
    sci_entry = tkinter.Entry(t,font = (v,20),width = 5,justify = 'center')
    sci_entry.place(x = 220,y = 250)
    
    soc = tkinter.Label(t,text = "Social Science",bg = 'white',fg = 'black',font = (g,20),width = 10)
    soc.place(x = 30,y = 300)
    
    soc_entry = tkinter.Entry(t,font = (v,20),width = 5,justify = 'center')
    soc_entry.place(x = 220,y = 300)
    
    check = tkinter.Button(t,text = "Check",bg = 'green',fg = 'white',command = checking,font = (g,15))
    check.place(x = 60,y = 350)
    
    done = tkinter.Label(t,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
    done.place(x = 180,y = 470 )
    
    t.mainloop()


def eleven():
    e = tkinter.Toplevel()
    e.geometry('500x500')
    e.maxsize(500,500)
    e.config(bg = 'black')
    
    ele = tkinter.Label(e,text = "11 TH",bg = 'white',fg = 'black',font = 'verdana')
    ele.pack()
    
        
    def computer_app():
        c = tkinter.Toplevel()
        c.geometry('500x500')
        c.maxsize(500,500)
        c.config(bg = 'black')
        
        
        def checking_com_app():
            t = tam_entry.get()
            e = eng_entry.get()
            ca = com_a_entry.get() 
            ac = acc_entry.get()
            com_ = com_entry.get()
            eco_ = eco_entry.get()
            
            t = eval(t)
            e = eval(e)
            ca = eval(ca)
            ac = eval(ac)
            com_ = eval(com_)
            eco_ = eval(eco_)
            
            total = t + e + ca + ac + com_ + eco_
            per = (total / 600)  * 100
            # print(total)
            # print(per)
            per_round = round(per,2)
            
            
            if(t >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 70)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 70)
            
            if(e >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 120)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 120)
           
            if(ca >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 170)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 170)
            
            if(ac >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 220)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 220)
            
            if(com_ >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 270)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 270)
            
            if(eco_ >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 320)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 320)
            
            if( t >= 35 and e >= 35 and ca >= 35 and ac  >= 35 and com_ >= 35 and eco_ >= 35):
                
                examp = tkinter.Label(c,text = "Examination Passed",fg = 'lightgreen',bg = 'black',font = v,width = 17)
                examp.place(x = 100,y = 420 )
            
            else:
                examf = tkinter.Label(c,text = "Examination Failed",fg = 'red',bg = 'black',font = v,width = 17)
                examf.place(x = 100,y = 420 )
            
            
            tot = tkinter.Label(c,text = 'Total',bg = 'white',fg = 'black',font = v)
            tot.place(x = 170,y = 380)
            
            tot_ = tkinter.Entry(c,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            tot_.place(x = 230,y = 380)
            tot_.insert(0,total)
            
            
            per_label = tkinter.Label(c,text = " % ",font = g,fg = 'white',bg = 'black')
            per_label.place(x = 320,y = 380)
            
            per_ = tkinter.Entry(c,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            per_.place(x = 350,y = 380)
            per_.insert(0,per_round)
                
            
        ele = tkinter.Label(c,text = "11 TH",bg = 'white',fg = 'black',font = 'verdana')
        ele.pack()
        
        tam = tkinter.Label(c,text = "Tamil",bg = 'white',fg = 'black',font = (g,20),width = 10)
        tam.place(x = 30,y = 70)
        
        tam_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        tam_entry.place(x = 220,y = 70)
        
        eng = tkinter.Label(c,text = "English",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eng.place(x = 30,y = 120)
        
        eng_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        eng_entry.place(x = 220,y = 120)
        
        com_a = tkinter.Label(c,text = "Computer App",bg = 'white',fg = 'black',font = (g,20),width = 10)
        com_a.place(x = 30,y = 170)
        
        com_a_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        com_a_entry.place(x = 220,y = 170)
        
        acc = tkinter.Label(c,text = "Accountancy",bg = 'white',fg = 'black',font = (g,20),width = 10)
        acc.place(x = 30,y = 220)
        
        acc_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        acc_entry.place(x = 220,y = 220)
        
        com = tkinter.Label(c,text = "Commerce",bg = 'white',fg = 'black',font = (g,20),width = 10)
        com.place(x = 30,y = 270)
        
        com_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        com_entry.place(x = 220,y = 270)
        
        eco = tkinter.Label(c,text = "Economics",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eco.place(x = 30,y = 320)
        
        eco_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        eco_entry.place(x = 220,y = 320)
        
        check = tkinter.Button(c,text = "Check",bg = 'green',fg = 'white',command = checking_com_app,font = (g,15))
        check.place(x = 60,y = 370)
        
        
        
        
        done = tkinter.Label(c,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
        done.place(x = 180,y = 470)
        
        c.mainloop()
        
        
        
    def bus_math():
        bus = tkinter.Toplevel()
        bus.geometry('500x500')
        bus.maxsize(500,500)
        bus.config(bg = 'black')
        
        
        
        def checking_busniess():
            t = tam_entry.get()
            e = eng_entry.get()
            ca = com_a_entry.get() 
            ac = acc_entry.get()
            com_ = com_entry.get()
            eco_ = eco_entry.get()
            
            t = eval(t)
            e = eval(e)
            ca = eval(ca)
            ac = eval(ac)
            com_ = eval(com_)
            eco_ = eval(eco_)
            
            total = t + e + ca + ac + com_ + eco_
            per = (total / 600)  * 100
            # print(total)
            # print(per)
            per_round = round(per,2)
            
            
            if(t >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 70)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 70)
            
            if(e >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 120)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 120)
           
            if(ca >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 170)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 170)
            
            if(ac >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 220)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 220)
            
            if(com_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 270)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 270)
            
            if(eco_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 320)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 320)
            
            if( t >= 35 and e >= 35 and ca >= 35 and ac  >= 35 and com_ >= 35 and eco_ >= 35):
                
                examp = tkinter.Label(bus,text = "Examination Passed",fg = 'lightgreen',bg = 'black',font = v,width = 17)
                examp.place(x = 100,y = 420 )
            
            else:
                examf = tkinter.Label(bus,text = "Examination Failed",fg = 'red',bg = 'black',font = v,width = 17)
                examf.place(x = 100,y = 420 )
            
            
            tot = tkinter.Label(bus,text = 'Total',bg = 'white',fg = 'black',font = v)
            tot.place(x = 170,y = 380)
            
            tot_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            tot_.place(x = 230,y = 380)
            tot_.insert(0,total)
            
            
            per_label = tkinter.Label(bus,text = " % ",font = g,fg = 'white',bg = 'black')
            per_label.place(x = 320,y = 380)
            
            per_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            per_.place(x = 350,y = 380)
            per_.insert(0,per_round)
        
        
        ele = tkinter.Label(bus,text = "11 TH",bg = 'white',fg = 'black',font = 'verdana')
        ele.pack()
        
        tam = tkinter.Label(bus,text = "Tamil",bg = 'white',fg = 'black',font = (g,20),width = 10)
        tam.place(x = 30,y = 70)
        
        tam_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        tam_entry.place(x = 220,y = 70)
        
        eng = tkinter.Label(bus,text = "English",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eng.place(x = 30,y = 120)
        
        eng_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eng_entry.place(x = 220,y = 120)
        
        com_a = tkinter.Label(bus,text = "Business Math",bg = 'white',fg = 'black',font = (g,18),width = 11)
        com_a.place(x = 30,y = 170)
        
        com_a_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_a_entry.place(x = 220,y = 170)
        
        acc = tkinter.Label(bus,text = "Accountancy",bg = 'white',fg = 'black',font = (g,20),width = 10)
        acc.place(x = 30,y = 220)
        
        acc_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        acc_entry.place(x = 220,y = 220)
        
        com = tkinter.Label(bus,text = "Commerce",bg = 'white',fg = 'black',font = (g,20),width = 10)
        com.place(x = 30,y = 270)
        
        com_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_entry.place(x = 220,y = 270)
        
        eco = tkinter.Label(bus,text = "Economics",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eco.place(x = 30,y = 320)
        
        eco_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eco_entry.place(x = 220,y = 320)
        
        check = tkinter.Button(bus,text = "Check",bg = 'green',fg = 'white',command = checking_busniess,font = (g,15))
        check.place(x = 60,y = 370)
    
        done = tkinter.Label(bus,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
        done.place(x = 180,y = 470)

        bus.mainloop()
    
        
 
    ######Command########    
    def bio_math():
        bus = tkinter.Toplevel()
        bus.geometry('500x500')
        bus.maxsize(500,500)
        bus.config(bg = 'black')
        
        
        
        def checking_busniess():
            t = tam_entry.get()
            e = eng_entry.get()
            ca = com_a_entry.get() 
            ac = acc_entry.get()
            com_ = com_entry.get()
            eco_ = eco_entry.get()
            
            t = eval(t)
            e = eval(e)
            ca = eval(ca)
            ac = eval(ac)
            com_ = eval(com_)
            eco_ = eval(eco_)
            
            total = t + e + ca + ac + com_ + eco_
            per = (total / 600)  * 100
            # print(total)
            # print(per)
            per_round = round(per,2)
            
            
            if(t >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 70)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 70)
            
            if(e >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 120)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 120)
           
            if(ca >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 170)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 170)
            
            if(ac >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 220)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 220)
            
            if(com_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 270)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 270)
            
            if(eco_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 320)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 320)
            
            if( t >= 35 and e >= 35 and ca >= 35 and ac  >= 35 and com_ >= 35 and eco_ >= 35):
                
                examp = tkinter.Label(bus,text = "Examination Passed",fg = 'lightgreen',bg = 'black',font = v,width = 17)
                examp.place(x = 100,y = 420 )
            
            else:
                examf = tkinter.Label(bus,text = "Examination Failed",fg = 'red',bg = 'black',font = v,width = 17)
                examf.place(x = 100,y = 420 )
            
            
            tot = tkinter.Label(bus,text = 'Total',bg = 'white',fg = 'black',font = v)
            tot.place(x = 170,y = 380)
            
            tot_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            tot_.place(x = 230,y = 380)
            tot_.insert(0,total)
            
            
            per_label = tkinter.Label(bus,text = " % ",font = g,fg = 'white',bg = 'black')
            per_label.place(x = 320,y = 380)
            
            per_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            per_.place(x = 350,y = 380)
            per_.insert(0,per_round)
        
        
        ele = tkinter.Label(bus,text = "11 TH",bg = 'white',fg = 'black',font = 'verdana')
        ele.pack()
        
        tam = tkinter.Label(bus,text = "Tamil",bg = 'white',fg = 'black',font = (g,20),width = 10)
        tam.place(x = 30,y = 70)
        
        tam_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        tam_entry.place(x = 220,y = 70)
        
        eng = tkinter.Label(bus,text = "English",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eng.place(x = 30,y = 120)
        
        eng_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eng_entry.place(x = 220,y = 120)
        
        com_a = tkinter.Label(bus,text = "Mathematics",bg = 'white',fg = 'black',font = (g,18),width = 11)
        com_a.place(x = 30,y = 170)
        
        com_a_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_a_entry.place(x = 220,y = 170)
        
        acc = tkinter.Label(bus,text = "Biology",bg = 'white',fg = 'black',font = (g,20),width = 10)
        acc.place(x = 30,y = 220)
        
        acc_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        acc_entry.place(x = 220,y = 220)
        
        com = tkinter.Label(bus,text = "Physics",bg = 'white',fg = 'black',font = (g,20),width = 10)
        com.place(x = 30,y = 270)
        
        com_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_entry.place(x = 220,y = 270)
        
        eco = tkinter.Label(bus,text = "Chemistry",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eco.place(x = 30,y = 320)
        
        eco_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eco_entry.place(x = 220,y = 320)
        
        check = tkinter.Button(bus,text = "Check",bg = 'green',fg = 'white',command = checking_busniess,font = (g,15))
        check.place(x = 60,y = 370)
    
        done = tkinter.Label(bus,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
        done.place(x = 180,y = 470)

        bus.mainloop()
        
    def computer_science():
        bus = tkinter.Toplevel()
        bus.geometry('500x500')
        bus.maxsize(500,500)
        bus.config(bg = 'black')
        
        
        
        def checking_busniess():
            t = tam_entry.get()
            e = eng_entry.get()
            ca = com_a_entry.get() 
            ac = acc_entry.get()
            com_ = com_entry.get()
            eco_ = eco_entry.get()
            
            t = eval(t)
            e = eval(e)
            ca = eval(ca)
            ac = eval(ac)
            com_ = eval(com_)
            eco_ = eval(eco_)
            
            total = t + e + ca + ac + com_ + eco_
            per = (total / 600)  * 100
            # print(total)
            # print(per)
            per_round = round(per,2)
            
            
            if(t >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 70)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 70)
            
            if(e >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 120)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 120)
           
            if(ca >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 170)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 170)
            
            if(ac >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 220)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 220)
            
            if(com_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 270)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 270)
            
            if(eco_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 320)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 320)
            
            if( t >= 35 and e >= 35 and ca >= 35 and ac  >= 35 and com_ >= 35 and eco_ >= 35):
                
                examp = tkinter.Label(bus,text = "Examination Passed",fg = 'lightgreen',bg = 'black',font = v,width = 17)
                examp.place(x = 100,y = 420 )
            
            else:
                examf = tkinter.Label(bus,text = "Examination Failed",fg = 'red',bg = 'black',font = v,width = 17)
                examf.place(x = 100,y = 420 )
            
            
            tot = tkinter.Label(bus,text = 'Total',bg = 'white',fg = 'black',font = v)
            tot.place(x = 170,y = 380)
            
            tot_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            tot_.place(x = 230,y = 380)
            tot_.insert(0,total)
            
            
            per_label = tkinter.Label(bus,text = " % ",font = g,fg = 'white',bg = 'black')
            per_label.place(x = 320,y = 380)
            
            per_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            per_.place(x = 350,y = 380)
            per_.insert(0,per_round)
        
        
        ele = tkinter.Label(bus,text = "11 TH",bg = 'white',fg = 'black',font = 'verdana')
        ele.pack()
        
        tam = tkinter.Label(bus,text = "Tamil",bg = 'white',fg = 'black',font = (g,20),width = 10)
        tam.place(x = 30,y = 70)
        
        tam_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        tam_entry.place(x = 220,y = 70)
        
        eng = tkinter.Label(bus,text = "English",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eng.place(x = 30,y = 120)
        
        eng_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eng_entry.place(x = 220,y = 120)
        
        com_a = tkinter.Label(bus,text = "Mathematics",bg = 'white',fg = 'black',font = (g,18),width = 11)
        com_a.place(x = 30,y = 170)
        
        com_a_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_a_entry.place(x = 220,y = 170)
        
        acc = tkinter.Label(bus,text = "Computer Sci",bg = 'white',fg = 'black',font = (g,20),width = 10)
        acc.place(x = 30,y = 220)
        
        acc_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        acc_entry.place(x = 220,y = 220)
        
        com = tkinter.Label(bus,text = "Physics",bg = 'white',fg = 'black',font = (g,20),width = 10)
        com.place(x = 30,y = 270)
        
        com_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_entry.place(x = 220,y = 270)
        
        eco = tkinter.Label(bus,text = "Chemistry",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eco.place(x = 30,y = 320)
        
        eco_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eco_entry.place(x = 220,y = 320)
        
        check = tkinter.Button(bus,text = "Check",bg = 'green',fg = 'white',command = checking_busniess,font = (g,15))
        check.place(x = 60,y = 370)
    
        done = tkinter.Label(bus,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
        done.place(x = 180,y = 470)

        bus.mainloop()
        
            
    
    ca = tkinter.Button(e,text = "Commerce with Computer application",bg = 'yellow',fg = 'black',font = ('verdana',13),width = 30)
    ca.place(x = 80,y = 50)
    ca.config(command = computer_app)
   
    
    bm = tkinter.Button(e,text = "Commerce with Business Maths",bg = 'yellow',fg = 'black',font = ('verdana',13),width = 30)
    bm.place(x = 80,y = 120)
    bm.config(command = bus_math)

    bio = tkinter.Button(e,text = "Bio Mathematics",bg = 'yellow',fg = 'black',font = ('verdana',13),width = 30)
    bio.place(x = 80,y = 190)
    bio.config(command = bio_math)

    cs = tkinter.Button(e,text = "Computer Science",bg = 'yellow',fg = 'black',font = ('verdana',13),width = 30)
    cs.place(x = 80,y = 260)
    cs.config(command = computer_science)

    done = tkinter.Label(e,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
    done.place(x = 180,y = 470)


    e.mainloop()
    
    

def twele():
    t = tkinter.Toplevel()
    t.geometry('500x500')
    t.maxsize(500,500)
    t.config(bg = 'black')
    
    
    def computer_app():
        c = tkinter.Toplevel()
        c.geometry('500x500')
        c.maxsize(500,500)                  #ghsgdgsd
        c.config(bg = 'black')
        
        
        def checking_com_app():
            t = tam_entry.get()
            e = eng_entry.get()
            ca = com_a_entry.get() 
            ac = acc_entry.get()
            com_ = com_entry.get()
            eco_ = eco_entry.get()
            
            t = eval(t)
            e = eval(e)
            ca = eval(ca)
            ac = eval(ac)
            com_ = eval(com_)
            eco_ = eval(eco_)
            
            total = t + e + ca + ac + com_ + eco_
            per = (total / 600)  * 100
            # print(total)
            # print(per)
            per_round = round(per,2)
            
            
            if(t >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 70)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 70)
            
            if(e >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 120)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 120)
           
            if(ca >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 170)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 170)
            
            if(ac >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 220)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 220)
            
            if(com_ >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 270)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 270)
            
            if(eco_ >= 35):
                passed = tkinter.Label(c,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 320)
            
            else:
                failed = tkinter.Label(c,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 320)
            
            if( t >= 35 and e >= 35 and ca >= 35 and ac  >= 35 and com_ >= 35 and eco_ >= 35):
                
                examp = tkinter.Label(c,text = "Examination Passed",fg = 'lightgreen',bg = 'black',font = v,width = 17)
                examp.place(x = 100,y = 420 )
            
            else:
                examf = tkinter.Label(c,text = "Examination Failed",fg = 'red',bg = 'black',font = v,width = 17)
                examf.place(x = 100,y = 420 )
            
            
            tot = tkinter.Label(c,text = 'Total',bg = 'white',fg = 'black',font = v)
            tot.place(x = 170,y = 380)
            
            tot_ = tkinter.Entry(c,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            tot_.place(x = 230,y = 380)
            tot_.insert(0,total)
            
            
            per_label = tkinter.Label(c,text = " % ",font = g,fg = 'white',bg = 'black')
            per_label.place(x = 320,y = 380)
            
            per_ = tkinter.Entry(c,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            per_.place(x = 350,y = 380)
            per_.insert(0,per_round)
                
            
        ele = tkinter.Label(c,text = "12 TH",bg = 'white',fg = 'black',font = 'verdana')
        ele.pack()
        
        tam = tkinter.Label(c,text = "Tamil",bg = 'white',fg = 'black',font = (g,20),width = 10)
        tam.place(x = 30,y = 70)
        
        tam_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        tam_entry.place(x = 220,y = 70)
        
        eng = tkinter.Label(c,text = "English",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eng.place(x = 30,y = 120)
        
        eng_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        eng_entry.place(x = 220,y = 120)
        
        com_a = tkinter.Label(c,text = "Computer App",bg = 'white',fg = 'black',font = (g,20),width = 10)
        com_a.place(x = 30,y = 170)
        
        com_a_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        com_a_entry.place(x = 220,y = 170)
        
        acc = tkinter.Label(c,text = "Accountancy",bg = 'white',fg = 'black',font = (g,20),width = 10)
        acc.place(x = 30,y = 220)
        
        acc_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        acc_entry.place(x = 220,y = 220)
        
        com = tkinter.Label(c,text = "Commerce",bg = 'white',fg = 'black',font = (g,20),width = 10)
        com.place(x = 30,y = 270)
        
        com_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        com_entry.place(x = 220,y = 270)
        
        eco = tkinter.Label(c,text = "Economics",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eco.place(x = 30,y = 320)
        
        eco_entry = tkinter.Entry(c,font = (v,20),width = 5,justify = 'center')
        eco_entry.place(x = 220,y = 320)
        
        check = tkinter.Button(c,text = "Check",bg = 'green',fg = 'white',command = checking_com_app,font = (g,15))
        check.place(x = 60,y = 370)
        
        
        
        
        done = tkinter.Label(c,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
        done.place(x = 180,y = 470)
        
        c.mainloop()
        
        
        
    def bus_math():
        bus = tkinter.Toplevel()
        bus.geometry('500x500')
        bus.maxsize(500,500)
        bus.config(bg = 'black')
        
        
        
        def checking_busniess():
            t = tam_entry.get()
            e = eng_entry.get()
            ca = com_a_entry.get() 
            ac = acc_entry.get()
            com_ = com_entry.get()
            eco_ = eco_entry.get()
            
            t = eval(t)
            e = eval(e)
            ca = eval(ca)
            ac = eval(ac)
            com_ = eval(com_)
            eco_ = eval(eco_)
            
            total = t + e + ca + ac + com_ + eco_
            per = (total / 600)  * 100
            # print(total)
            # print(per)
            per_round = round(per,2)
            
            
            if(t >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 70)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 70)
            
            if(e >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 120)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 120)
           
            if(ca >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 170)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 170)
            
            if(ac >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 220)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 220)
            
            if(com_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 270)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 270)
            
            if(eco_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 320)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 320)
            
            if( t >= 35 and e >= 35 and ca >= 35 and ac  >= 35 and com_ >= 35 and eco_ >= 35):
                
                examp = tkinter.Label(bus,text = "Examination Passed",fg = 'lightgreen',bg = 'black',font = v,width = 17)
                examp.place(x = 100,y = 420 )
            
            else:
                examf = tkinter.Label(bus,text = "Examination Failed",fg = 'red',bg = 'black',font = v,width = 17)
                examf.place(x = 100,y = 420 )
            
            
            tot = tkinter.Label(bus,text = 'Total',bg = 'white',fg = 'black',font = v)
            tot.place(x = 170,y = 380)
            
            tot_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            tot_.place(x = 230,y = 380)
            tot_.insert(0,total)
            
            
            per_label = tkinter.Label(bus,text = " % ",font = g,fg = 'white',bg = 'black')
            per_label.place(x = 320,y = 380)
            
            per_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            per_.place(x = 350,y = 380)
            per_.insert(0,per_round)
        
        
        ele = tkinter.Label(bus,text = "12 TH",bg = 'white',fg = 'black',font = 'verdana')
        ele.pack()
        
        tam = tkinter.Label(bus,text = "Tamil",bg = 'white',fg = 'black',font = (g,20),width = 10)
        tam.place(x = 30,y = 70)
        
        tam_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        tam_entry.place(x = 220,y = 70)
        
        eng = tkinter.Label(bus,text = "English",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eng.place(x = 30,y = 120)
        
        eng_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eng_entry.place(x = 220,y = 120)
        
        com_a = tkinter.Label(bus,text = "Business Math",bg = 'white',fg = 'black',font = (g,18),width = 11)
        com_a.place(x = 30,y = 170)
        
        com_a_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_a_entry.place(x = 220,y = 170)
        
        acc = tkinter.Label(bus,text = "Accountancy",bg = 'white',fg = 'black',font = (g,20),width = 10)
        acc.place(x = 30,y = 220)
        
        acc_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        acc_entry.place(x = 220,y = 220)
        
        com = tkinter.Label(bus,text = "Commerce",bg = 'white',fg = 'black',font = (g,20),width = 10)
        com.place(x = 30,y = 270)
        
        com_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_entry.place(x = 220,y = 270)
        
        eco = tkinter.Label(bus,text = "Economics",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eco.place(x = 30,y = 320)
        
        eco_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eco_entry.place(x = 220,y = 320)
        
        check = tkinter.Button(bus,text = "Check",bg = 'green',fg = 'white',command = checking_busniess,font = (g,15))
        check.place(x = 60,y = 370)
    
        done = tkinter.Label(bus,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
        done.place(x = 180,y = 470)

        bus.mainloop()
    
        
 
    ######Command########    
    def bio_math():
        bus = tkinter.Toplevel()
        bus.geometry('500x500')
        bus.maxsize(500,500)
        bus.config(bg = 'black')
        
        
        
        def checking_busniess():
            t = tam_entry.get()
            e = eng_entry.get()
            ca = com_a_entry.get() 
            ac = acc_entry.get()
            com_ = com_entry.get()
            eco_ = eco_entry.get()
            
            t = eval(t)
            e = eval(e)
            ca = eval(ca)
            ac = eval(ac)
            com_ = eval(com_)
            eco_ = eval(eco_)
            
            total = t + e + ca + ac + com_ + eco_
            per = (total / 600)  * 100
            # print(total)
            # print(per)
            per_round = round(per,2)
            
            
            if(t >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 70)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 70)
            
            if(e >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 120)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 120)
           
            if(ca >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 170)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 170)
            
            if(ac >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 220)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 220)
            
            if(com_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 270)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 270)
            
            if(eco_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 320)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 320)
            
            if( t >= 35 and e >= 35 and ca >= 35 and ac  >= 35 and com_ >= 35 and eco_ >= 35):
                
                examp = tkinter.Label(bus,text = "Examination Passed",fg = 'lightgreen',bg = 'black',font = v,width = 17)
                examp.place(x = 100,y = 420 )
            
            else:
                examf = tkinter.Label(bus,text = "Examination Failed",fg = 'red',bg = 'black',font = v,width = 17)
                examf.place(x = 100,y = 420 )
            
            
            tot = tkinter.Label(bus,text = 'Total',bg = 'white',fg = 'black',font = v)
            tot.place(x = 170,y = 380)
            
            tot_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            tot_.place(x = 230,y = 380)
            tot_.insert(0,total)
            
            
            per_label = tkinter.Label(bus,text = " % ",font = g,fg = 'white',bg = 'black')
            per_label.place(x = 320,y = 380)
            
            per_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            per_.place(x = 350,y = 380)
            per_.insert(0,per_round)
        
        
        ele = tkinter.Label(bus,text = "12 TH",bg = 'white',fg = 'black',font = 'verdana')
        ele.pack()
        
        tam = tkinter.Label(bus,text = "Tamil",bg = 'white',fg = 'black',font = (g,20),width = 10)
        tam.place(x = 30,y = 70)
        
        tam_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        tam_entry.place(x = 220,y = 70)
        
        eng = tkinter.Label(bus,text = "English",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eng.place(x = 30,y = 120)
        
        eng_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eng_entry.place(x = 220,y = 120)
        
        com_a = tkinter.Label(bus,text = "Mathematics",bg = 'white',fg = 'black',font = (g,18),width = 11)
        com_a.place(x = 30,y = 170)
        
        com_a_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_a_entry.place(x = 220,y = 170)
        
        acc = tkinter.Label(bus,text = "Biology",bg = 'white',fg = 'black',font = (g,20),width = 10)
        acc.place(x = 30,y = 220)
        
        acc_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        acc_entry.place(x = 220,y = 220)
        
        com = tkinter.Label(bus,text = "Physics",bg = 'white',fg = 'black',font = (g,20),width = 10)
        com.place(x = 30,y = 270)
        
        com_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_entry.place(x = 220,y = 270)
        
        eco = tkinter.Label(bus,text = "Chemistry",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eco.place(x = 30,y = 320)
        
        eco_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eco_entry.place(x = 220,y = 320)
        
        check = tkinter.Button(bus,text = "Check",bg = 'green',fg = 'white',command = checking_busniess,font = (g,15))
        check.place(x = 60,y = 370)
    
        done = tkinter.Label(bus,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
        done.place(x = 180,y = 470)

        bus.mainloop()
        
    def computer_science():
        bus = tkinter.Toplevel()
        bus.geometry('500x500')
        bus.maxsize(500,500)
        bus.config(bg = 'black')
        
        
        
        def checking_busniess():
            t = tam_entry.get()
            e = eng_entry.get()
            ca = com_a_entry.get() 
            ac = acc_entry.get()
            com_ = com_entry.get()
            eco_ = eco_entry.get()
            
            t = eval(t)
            e = eval(e)
            ca = eval(ca)
            ac = eval(ac)
            com_ = eval(com_)
            eco_ = eval(eco_)
            
            total = t + e + ca + ac + com_ + eco_
            per = (total / 600)  * 100
            # print(total)
            # print(per)
            per_round = round(per,2)
            
            
            if(t >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 70)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 70)
            
            if(e >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 120)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 120)
           
            if(ca >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 170)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 170)
            
            if(ac >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 220)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 220)
            
            if(com_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 270)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 270)
            
            if(eco_ >= 35):
                passed = tkinter.Label(bus,text = "Passed",bg = 'lightgreen',fg = 'black',font = v,width = 6)
                passed.place(x = 350,y = 320)
            
            else:
                failed = tkinter.Label(bus,text = 'Failed',bg = 'red',fg = 'black',font = v,width = 6)
                failed.place(x = 350,y = 320)
            
            if( t >= 35 and e >= 35 and ca >= 35 and ac  >= 35 and com_ >= 35 and eco_ >= 35):
                
                examp = tkinter.Label(bus,text = "Examination Passed",fg = 'lightgreen',bg = 'black',font = v,width = 17)
                examp.place(x = 100,y = 420 )
            
            else:
                examf = tkinter.Label(bus,text = "Examination Failed",fg = 'red',bg = 'black',font = v,width = 17)
                examf.place(x = 100,y = 420 )
            
            
            tot = tkinter.Label(bus,text = 'Total',bg = 'white',fg = 'black',font = v)
            tot.place(x = 170,y = 380)
            
            tot_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            tot_.place(x = 230,y = 380)
            tot_.insert(0,total)
            
            
            per_label = tkinter.Label(bus,text = " % ",font = g,fg = 'white',bg = 'black')
            per_label.place(x = 320,y = 380)
            
            per_ = tkinter.Entry(bus,bg = 'white',fg = 'black',font = v,width = 5,justify = 'center')
            per_.place(x = 350,y = 380)
            per_.insert(0,per_round)
        
        
        ele = tkinter.Label(bus,text = "12 TH",bg = 'white',fg = 'black',font = 'verdana')
        ele.pack()
        
        tam = tkinter.Label(bus,text = "Tamil",bg = 'white',fg = 'black',font = (g,20),width = 10)
        tam.place(x = 30,y = 70)
        
        tam_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        tam_entry.place(x = 220,y = 70)
        
        eng = tkinter.Label(bus,text = "English",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eng.place(x = 30,y = 120)
        
        eng_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eng_entry.place(x = 220,y = 120)
        
        com_a = tkinter.Label(bus,text = "Mathematics",bg = 'white',fg = 'black',font = (g,18),width = 11)
        com_a.place(x = 30,y = 170)
        
        com_a_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_a_entry.place(x = 220,y = 170)
        
        acc = tkinter.Label(bus,text = "Computer Sci",bg = 'white',fg = 'black',font = (g,20),width = 10)
        acc.place(x = 30,y = 220)
        
        acc_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        acc_entry.place(x = 220,y = 220)
        
        com = tkinter.Label(bus,text = "Physics",bg = 'white',fg = 'black',font = (g,20),width = 10)
        com.place(x = 30,y = 270)
        
        com_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        com_entry.place(x = 220,y = 270)
        
        eco = tkinter.Label(bus,text = "Chemistry",bg = 'white',fg = 'black',font = (g,20),width = 10)
        eco.place(x = 30,y = 320)
        
        eco_entry = tkinter.Entry(bus,font = (v,20),width = 5,justify = 'center')
        eco_entry.place(x = 220,y = 320)
        
        check = tkinter.Button(bus,text = "Check",bg = 'green',fg = 'white',command = checking_busniess,font = (g,15))
        check.place(x = 60,y = 370)
    
        done = tkinter.Label(bus,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
        done.place(x = 180,y = 470)

        bus.mainloop()
    
    twe = tkinter.Label(t,text = "12 TH",bg = 'white',fg = 'black',font = 'verdana')
    twe.pack()
    
        
    
    
    ca = tkinter.Button(t,text = "Commerce with Computer application",bg = 'green',fg = 'white',font = ('verdana',13),width = 30)
    ca.place(x = 80,y = 50)
    ca.config(command = computer_app)
   
    
    bm = tkinter.Button(t,text = "Commerce with Business Maths",bg = 'green',fg = 'white',font = ('verdana',13),width = 30)
    bm.place(x = 80,y = 120)
    bm.config(command = bus_math)

    bio = tkinter.Button(t,text = "Bio Maths",bg = 'green',fg = 'white',font = ('verdana',13),width = 30)
    bio.place(x = 80,y = 190)
    bio.config(command = bio_math)

    cs = tkinter.Button(t,text = "Computer Science",bg = 'green',fg = 'white',font = ('verdana',13),width = 30)
    cs.place(x = 80,y = 260)
    cs.config(command = computer_science)

    done = tkinter.Label(t,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
    done.place(x = 180,y = 470)

    t.mainloop()
    
ten = tkinter.Button(x,text = "10 th Standard",bg = 'red',fg = 'white',font = ('verdana',15),command = tenth)
ten.place(x = 165,y = 50)

ele = tkinter.Button(x,text = "11 th Standard",bg = 'yellow',fg = 'black',font = ('verdana',15),command = eleven)
ele.place(x = 165,y = 150)


twe = tkinter.Button(x,text = "12 th Standard",bg = 'green',fg = 'white',font = ('verdana',15),command = twele)
twe.place(x = 165,y = 250)




done = tkinter.Label(x,text = 'PROGRAMMED BY PAWAN SRI KANTH',font = 'georgia',bg = 'black',fg = 'white')
done.place(x = 180,y = 470)

x.mainloop()
