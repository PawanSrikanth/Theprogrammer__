import tkinter
from idlelib.tooltip import Hovertip
from tkinter import ttk
from tkinter import messagebox
x = tkinter.Tk()
x.geometry('700x500')
x.geometry('+300+200')

x.title('theprogrammer__')
x.configure(bg = 'white',highlightbackground = 'black',highlightthickness = 1,highlightcolor= 'black')

back = tkinter.PhotoImage(file = 'D:\ZOHO PROJECTS\Flight\A2.png')
bb = tkinter.Label(x,image = back)
bb.pack()

g = 'georgia'
v = 'verdana'

def go_inside():
    x2 = tkinter.Toplevel()
    x2.geometry('700x500')
    x2.geometry('+300+200')
    
    
    
    bg2 = tkinter.PhotoImage(file = 'D:\ZOHO PROJECTS\Flight\A7.png')
    flight2 = tkinter.Label(x2,image = bg2)
    flight2.pack()
    
    search_flights = tkinter.Label(x2,text = 'SEARCH FLIGHTS ',bg =  'white',fg = 'black',font = ('Britannic',20))
    search_flights.place(x = 30,y = 30)
    
            ################################
    
    def one_to_one():
        
        
        fro = tkinter.Label(x2,text = 'From',bg = 'white',fg = 'black',font = g)
        fro.place(x = 40,y= 130)
        
        from_1 = ttk.Combobox(x2,width = 13)
        from_1['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        from_1.place(x = 40,y = 155)
        
        to = tkinter.Label(x2,text = 'To',bg = 'white',fg = 'black',font = g)
        to.place(x = 160,y= 130)
        
        to_1 = ttk.Combobox(x2,width = 13)
        to_1['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        to_1.place(x = 160,y = 155)
        
        depart_ = tkinter.Label(x2,text = 'Depart',fg = 'black',bg = 'white',font = g)
        depart_.config(highlightbackground = 'black',highlightcolor = 'green3',highlightthickness  = 1)
        depart_.place(x = 40,y = 200)
        
        depart_1 = tkinter.Entry(x2,bg = 'white',fg = 'black',font = v,width = 12,justify = 'center') 
        depart_1.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness  = 1)
        depart_1.place(x = 110,y = 200)
        
        
        pas_ = tkinter.Label(x2,text = 'Passenger(s)',bg = 'white',fg = 'black',font = g)
        pas_.config(highlightbackground = 'black',highlightcolor = 'green3',highlightthickness  = 1)
        pas_.place(x = 40,y = 240)
        
        adult = tkinter.Label(x2,text = 'Adult',font = g,bg = 'white',fg = 'black')
        adult.config(highlightbackground = 'red',highlightthickness  = 1)
        adult.place(x = 150,y = 240)
        
        adultspin = tkinter.Spinbox(x2,bg = 'white',fg = 'black',font = g)
        adultspin.config(from_ = 1,to = 10,width = 3,highlightbackground = 'red',highlightthickness  = 1)
        adultspin.place(x = 200,y = 240)
        
        child = tkinter.Label(x2,text = 'Children',font = g,bg = 'white',fg = 'black')
        child.config(highlightbackground = 'green3',highlightthickness  = 1)
        child.place(x = 270,y = 240)
        
        childspin = tkinter.Spinbox(x2,bg = 'white',fg = 'black',font = g)
        childspin.config(from_ = 0,to = 10,width = 3,highlightbackground = 'green3',highlightthickness  = 1)
        childspin.place(x = 340,y = 240)
        
        infant = tkinter.Label(x2,text = 'Infant',font = g,bg = 'white',fg = 'black')
        infant.config(highlightbackground = 'blue',highlightthickness  = 1)
        infant.place(x = 405,y = 240)
        
        infantspin = tkinter.Spinbox(x2,bg = 'white',fg = 'black',font = g)
        infantspin.config(from_ = 0,to = 10,width = 3,highlightbackground = 'blue',highlightthickness  = 1)
        infantspin.place(x = 460,y = 240)
        
        class_ = tkinter.Label(x2,text = 'Class',font = g,bg = 'white',fg = 'black')
        class_.config(highlightbackground = 'black',highlightthickness  = 1)
        class_.place(x = 40,y = 280)
        
        class_1 = ttk.Combobox(x2,width = 15,font = g)
        class_1['values'] = ('Economy','Premium Economy','Business','First')
        class_1.insert(0,'Economy')
        class_1.place(x = 90,y = 280)
        
        con_ = tkinter.Label(x2,text = 'Concession Type',font = g,bg = 'white',fg = 'black')
        con_.config(highlightbackground = 'black',highlightthickness  = 1)
        con_.place(x = 280,y = 280)
        
        con_1 = ttk.Combobox(x2,width = 10,font = g)
        con_1['values'] = ('None','Armed Forces','Student','Senior Citizen')
        con_1.insert(0,'None')
        con_1.place(x = 413,y = 280)
        
        
        payby_ = tkinter.Label(x2,text = 'Pay By',font = g,bg = 'white',fg = 'black')
        payby_.config(highlightbackground = 'black',highlightthickness  = 1)
        payby_.place(x = 40,y = 320)
        
        payby_1 = ttk.Combobox(x2,width = 10,font = g)
        payby_1['values'] = ('Cash','Cash + Points','Points')
        payby_1.insert(0,'Cash')
        payby_1.place(x = 105,y = 320)
        
        
        def showing_the_flights():   #show flight
            
            if(from_1.get() == to_1.get()):
                messagebox.showinfo('Error','Your Beginning and Destination are Same Location , choose a Different Location')
                x.geometry('0x0')
                x.geometry('+0+0')
                
            
            else:
                x3 = tkinter.Toplevel()
                x3.geometry('700x500')
                x3.geometry('+300+200')
                
               
                
                
                stf = tkinter.PhotoImage(file = 'D:\ZOHO PROJECTS\Flight\A4.png')
                
                stf_bg = tkinter.Label(x3,image = stf)
                stf_bg.pack()
                
                desti = tkinter.Label(x3,text = from_1.get() + ' to ' + to_1.get() ,bg = 'white',fg = 'black',font = ('Britannic',20))
                desti.config(highlightcolor = 'black',highlightbackground = 'black',highlightthickness = 3)
                desti.place(x = 220,y = 30)
                
                
                
                
                date = tkinter.Button(x3,text = 'Flights on ' + depart_1.get(),bg = 'white',fg = 'black',font = v)
                date.place(x = 50,y = 100)
                
                
                
                
                
                def z1():
                    x.geometry('0x0')
                    x.geometry('+0+0')
                    x2.geometry('0x0')
                    x2.geometry('+0+0')

                    
                    ax = int(adultspin.get())
                    cx = int(childspin.get())
                    ix = int(infantspin.get())
                    
                    tt = ax + cx + ix
                    # print(tt)
                    tt = str(tt)
                    
                    if(tt == 1 or tt == '1'):
                        state = 'Are you sure to book your ticket for ' + tt  + ' passenger' 
                        mb = messagebox.askyesno('Confirm your booking',state )
                        
                        if mb:
                            messagebox.showinfo('Booked',' you have booked Your ticket you will get a notification later thanking you for booking')
                            
                        
                    else:
                        state = 'Are you sure to book your tickets for ' + tt  + ' passengers' 
                        mb = messagebox.askyesno('Confirm your booking',state )
                        
                        if mb:
                            messagebox.showinfo('Booked',' You have booked your tickets You will get a notification later thanking you for booking')
                        
                       
                        
                    
                
                zoho1 = tkinter.Button(x3,text = 'Zoho 00001 Aeroplane at 4 : 45 AM',bg = 'white',fg = 'black',font = g,width = 30,command = z1)
                zoho1.place(x = 180,y = 190)
                
                zoho2 = tkinter.Button(x3,text = 'Zoho 00002 Aeroplane at 11 : 30 AM',bg = 'white',fg = 'black',font = g,width = 30,command = z1)
                zoho2.place(x = 180,y = 250)
                
                zoho3 = tkinter.Button(x3,text = 'Zoho 00003 Aeroplane at 7 : 30 PM',bg = 'white',fg = 'black',font = g,width = 30,command = z1)
                zoho3.place(x = 180,y = 310)
                
                
                
                ######
                
                x3.mainloop()
           
                # if oneway:
                #     return_.destroy()
                #     return_1.destroy()
        
        
        show_flight = tkinter.Button(x2,text = 'Show Flight',bg = 'green',fg = 'white',command = showing_the_flights)
        show_flight.config(font = g,width = 20)
        show_flight.place(x = 240,y = 400)
        
        
        
        ##########################
    one_to_one()
    ################################
    
    
    
    
    def create_one():
        if oneway:
            xreturn_.destroy()
            xreturn_1.destroy()
        one_to_one()
    
    
   
    def create_round():      # Round Trip
    
        global xreturn_
        global xreturn_1
        
        xfro = tkinter.Label(x2,text = 'From',bg = 'white',fg = 'black',font = g)
        xfro.place(x = 40,y= 130)
        
        xfrom_1 = ttk.Combobox(x2,width = 13)
        xfrom_1['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        xfrom_1.place(x = 40,y = 155)
        
        xto = tkinter.Label(x2,text = 'To',bg = 'white',fg = 'black',font = g)
        xto.place(x = 160,y= 130)
        
        xto_1 = ttk.Combobox(x2,width = 13)
        xto_1['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        xto_1.place(x = 160,y = 155)
        
        xdepart_ = tkinter.Label(x2,text = 'Depart',fg = 'black',bg = 'white',font = g)
        xdepart_.config(highlightbackground = 'black',highlightcolor = 'green3',highlightthickness  = 1)
        xdepart_.place(x = 40,y = 200)
        
        xdepart_1 = tkinter.Entry(x2,bg = 'white',fg = 'black',font = v,width = 12,justify = 'center') 
        xdepart_1.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness  = 1)
        xdepart_1.place(x = 110,y = 200)
        
        
        xreturn_ = tkinter.Label(x2,text = 'Return',fg = 'black',bg = 'white',font = g) ########################################
        xreturn_.config(highlightbackground = 'black',highlightcolor = 'green3',highlightthickness  = 1)
        xreturn_.place(x = 270,y = 200)
        
        xreturn_1 = tkinter.Entry(x2,bg = 'white',fg = 'black',font = v,width = 12,justify = 'center') 
        xreturn_1.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness  = 1)
        xreturn_1.place(x = 340,y = 200)
       
        
        
        
        xpas_ = tkinter.Label(x2,text = 'Passenger(s)',bg = 'white',fg = 'black',font = g)
        xpas_.config(highlightbackground = 'black',highlightcolor = 'green3',highlightthickness  = 1)
        xpas_.place(x = 40,y = 240)
        
        xadult = tkinter.Label(x2,text = 'Adult',font = g,bg = 'white',fg = 'black')
        xadult.config(highlightbackground = 'red',highlightthickness  = 1)
        xadult.place(x = 150,y = 240)
        
        xadultspin = tkinter.Spinbox(x2,bg = 'white',fg = 'black',font = g)
        xadultspin.config(from_ = 1,to = 10,width = 3,highlightbackground = 'red',highlightthickness  = 1)
        xadultspin.place(x = 200,y = 240)
        
        xchild = tkinter.Label(x2,text = 'Children',font = g,bg = 'white',fg = 'black')
        xchild.config(highlightbackground = 'green3',highlightthickness  = 1)
        xchild.place(x = 270,y = 240)
        
        xchildspin = tkinter.Spinbox(x2,bg = 'white',fg = 'black',font = g)
        xchildspin.config(from_ = 0,to = 10,width = 3,highlightbackground = 'green3',highlightthickness  = 1)
        xchildspin.place(x = 340,y = 240)
        
        xinfant = tkinter.Label(x2,text = 'Infant',font = g,bg = 'white',fg = 'black')
        xinfant.config(highlightbackground = 'blue',highlightthickness  = 1)
        xinfant.place(x = 405,y = 240)
        
        xinfantspin = tkinter.Spinbox(x2,bg = 'white',fg = 'black',font = g)
        xinfantspin.config(from_ = 0,to = 10,width = 3,highlightbackground = 'blue',highlightthickness  = 1)
        xinfantspin.place(x = 460,y = 240)
        
        xclass_ = tkinter.Label(x2,text = 'Class',font = g,bg = 'white',fg = 'black')
        xclass_.config(highlightbackground = 'black',highlightthickness  = 1)
        xclass_.place(x = 40,y = 280)
        
        xclass_1 = ttk.Combobox(x2,width = 15,font = g)
        xclass_1['values'] = ('Economy','Premium Economy','Business','First')
        xclass_1.insert(0,'Economy')
        xclass_1.place(x = 90,y = 280)
        
        xcon_ = tkinter.Label(x2,text = 'Concession Type',font = g,bg = 'white',fg = 'black')
        xcon_.config(highlightbackground = 'black',highlightthickness  = 1)
        xcon_.place(x = 280,y = 280)
        
        xcon_1 = ttk.Combobox(x2,width = 10,font = g)
        xcon_1['values'] = ('None','Armed Forces','Student','Senior Citizen')
        xcon_1.insert(0,'None')
        xcon_1.place(x = 413,y = 280)
        
        
        xpayby_ = tkinter.Label(x2,text = 'Pay By',font = g,bg = 'white',fg = 'black')
        xpayby_.config(highlightbackground = 'black',highlightthickness  = 1)
        xpayby_.place(x = 40,y = 320)
        
        xpayby_1 = ttk.Combobox(x2,width = 10,font = g)
        xpayby_1['values'] = ('Cash','Cash + Points','Points')
        xpayby_1.insert(0,'Cash')
        xpayby_1.place(x = 105,y = 320)
        
        
        
        def showing_the_flights_xx():   #show flight
            
            if(xfrom_1.get() == xto_1.get()):
                messagebox.showinfo('Error','Your Beginning and Destination are Same Location , choose a Different Location')
                x.geometry('0x0')
                x.geometry('+0+0')
                
            
            else:
                x4 = tkinter.Toplevel()
                x4.geometry('700x500')
                x4.geometry('+300+200')
                
               
                
                
                stf = tkinter.PhotoImage(file = 'D:\ZOHO PROJECTS\Flight\A4.png')
                
                stf_bg = tkinter.Label(x4,image = stf)
                stf_bg.pack()
                
                desti = tkinter.Label(x4,text = xfrom_1.get() + ' to ' + xto_1.get() ,bg = 'white',fg = 'black',font = ('Britannic',20))
                desti.config(highlightcolor = 'black',highlightbackground = 'black',highlightthickness = 3)
                desti.place(x = 20,y = 30)
                
                
                date = tkinter.Button(x4,text = 'Flights on ' + xdepart_1.get(),bg = 'white',fg = 'black',font = v)
                date.place(x = 50,y = 100)
                
                return_date = tkinter.Button(x4,text = 'Return on ' + xreturn_1.get(),bg = 'white',fg = 'black',font = v)
                return_date.place(x = 450,y = 100)
                
                def z1():
                    x.geometry('0x0')
                    x.geometry('+0+0')
                    x2.geometry('0x0')
                    x2.geometry('+0+0')

                    
                    ax = int(xadultspin.get())
                    cx = int(xchildspin.get())
                    ix = int(xinfantspin.get())
                    
                    tt = ax + cx + ix
                    # print(tt)
                    tt = str(tt)
                    
                    if(tt == 1 or tt == '1'):
                        state = 'Are you sure to book your ticket for ' + tt  + ' passenger' 
                        mb = messagebox.askyesno('Confirm your booking',state )
                        
                        if mb:
                            messagebox.showinfo('Booked',' you have booked Your ticket you will get a notification later thanking you for booking')
                            
                        
                    else:
                        state = 'Are you sure to book your tickets for ' + tt  + ' passengers' 
                        mb = messagebox.askyesno('Confirm your booking',state )
                        
                        if mb:
                            messagebox.showinfo('Booked',' You have booked your tickets You will get a notification later thanking you for booking')
                        
                       
                        
                    
                
                zoho4 = tkinter.Button(x4,text = 'Zoho 00004 Aeroplane at 4 : 45 AM',bg = 'white',fg = 'black',font = g,width = 30,command = z1)
                zoho4.place(x = 30,y = 190)
                
                zoho5 = tkinter.Button(x4,text = 'Zoho 00005 Aeroplane at 11 : 30 AM',bg = 'white',fg = 'black',font = g,width = 30,command = z1)
                zoho5.place(x = 30,y = 250)
                
                zoho6 = tkinter.Button(x4,text = 'Zoho 00006 Aeroplane at 7 : 30 PM',bg = 'white',fg = 'black',font = g,width = 30,command = z1)
                zoho6.place(x = 30,y = 310)
                
                
                zoho7 = tkinter.Button(x4,text = 'Zoho 00007 Aeroplane at 6 : 45 AM',bg = 'white',fg = 'black',font = g,width = 30,command = z1)
                zoho7.place(x = 410,y = 190)
                
                zoho8 = tkinter.Button(x4,text = 'Zoho 00008 Aeroplane at 1 : 30 PM',bg = 'white',fg = 'black',font = g,width = 30,command = z1)
                zoho8.place(x = 410,y = 250)
                
                zoho9 = tkinter.Button(x4,text = 'Zoho 00009 Aeroplane at 9 : 30 PM',bg = 'white',fg = 'black',font = g,width = 30,command = z1)
                zoho9.place(x = 410,y = 310)
                
                
                ######
                
                x4.mainloop()
                
            
        show_flight = tkinter.Button(x2,text = 'Show Flight',bg = 'green',fg = 'white',command = showing_the_flights_xx)
        show_flight.config(font = g,width = 20)
        show_flight.place(x = 240,y = 400)
                
        
    
    oneway = tkinter.Radiobutton(x2,text = 'One Way',font = g,bg = 'white',fg = 'black',activeforeground = 'green3',command = create_one)
    oneway.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness = 2)
    oneway.config(value = 1)
    oneway.place(x = 40,y = 90)
    
    roundtrip = tkinter.Radiobutton(x2,text = 'Round Trip',font = g,bg = 'white',fg = 'black',value = 2,activeforeground = 'green3',command = create_round)
    roundtrip.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness = 2)
    roundtrip.config(value = 2)
    roundtrip.place(x = 160,y = 90)
    
    
    
    def multi_flight():
        m = tkinter.Toplevel()
        m.geometry('700x500')
        m.geometry('+300+200')
        
        
        mbg = tkinter.PhotoImage(file = 'D:\ZOHO PROJECTS\Flight\A6.png')
        
        m_bg = tkinter.Label(m,image = mbg)
        m_bg.pack()
        
        
        def showing_the_flights_multi():
            mm = tkinter.Toplevel()
            mm.geometry('700x500')
            mm.geometry('+300+200')
            
            
            mmbg = tkinter.PhotoImage(file = 'D:\ZOHO PROJECTS\Flight\A4.png')
            
            mm_bg = tkinter.Label(mm,image = mmbg)
            mm_bg.pack()
            
            f1 = from_1.get()
            f2 = from_2.get()
            f3 = from_3.get()
            f4 = from_4.get()
            f5 = from_5.get()
            
            t1 = to_1.get()
            t2 = to_2.get()
            t3 = to_3.get()
            t4 = to_4.get()
            t5 = to_5.get()
            
            d1 = depart_1.get()
            d2 = depart_2.get()
            d3 = depart_3.get()
            d4 = depart_4.get()
            d5 = depart_5.get()
            
            journey = tkinter.Label(mm,text = 'Journey Starts',font = g,bg = 'white',fg = 'black')
            journey.place(x = 300,y = 10)
            
            fli_1 = tkinter.Button(mm,text = f1 + ' to ' + t1 + ' on ' + d1  + ' at 3:25 am ',bg = 'white',fg = 'black',font = v,width = 45)
            fli_1.place(x = 110,y = 60)
            
            if(f2 == "" and t2 == "" and d2 == ""):
                print('no travel')
            
            else:
                fli_2 = tkinter.Button(mm,text = f2 + ' to ' + t2 + ' on ' + d2  + ' at 7:35 am ',bg = 'white',fg = 'black',font = v,width = 45)
                fli_2.place(x = 110,y = 130)
            
            if(f3 == "" and t3 == "" and d3 == ""):
                print('no travel')
            
            else:
                fli_3 = tkinter.Button(mm,text = f3 + ' to ' + t3 + ' on ' + d3  + ' at 3:35 pm ',bg = 'white',fg = 'black',font = v,width = 45)
                fli_3.place(x = 110,y = 190)
                
            if(f4 == "" and t4 == "" and d4 == ""):
                print('no travel')
            
            else:
                fli_4 = tkinter.Button(mm,text = f4 + ' to ' + t4 + ' on ' + d4  + ' at 12:05 am ',bg = 'white',fg = 'black',font = v,width = 45)
                fli_4.place(x = 110,y = 250)
            
            if(f5 == "" and t5 == "" and d5 == ""):
                print('no travel')
            
            else:
                fli_5 = tkinter.Button(mm,text = f5 + ' to ' + t5 + ' on ' + d5  + ' at 7:35 am ',bg = 'white',fg = 'black',font = v,width = 45)
                fli_5.place(x = 110,y = 310)
            
            def final_():
                x.geometry('0x0')
                x.geometry('+0+0')
                x2.geometry('0x0')
                x2.geometry('+0+0')
                state = 'Are you sure to book your tickets' 
                mb = messagebox.askyesno('Confirm your booking',state )
                
                if mb:
                    messagebox.showinfo('Booked',' you have booked Your ticket you will get a notification later thanking you for booking')
                    
                
                
            
            book = tkinter.Button(mm,text = 'Confirm your Booking',bg = 'green3',fg = 'white',font = g,command = final_)
            book.place(x = 250,y = 400)
            
            
            
            mm.mainloop()
        
        
        
        fl_1 = tkinter.Label(m,text = 'Flight 1',bg = 'white',fg = 'black',font = g)
        fl_1.place(x = 40,y = 20)
        
        fro_1 = tkinter.Label(m,text = 'From',bg = 'white',fg = 'black',font = g)
        fro_1.place(x = 40,y= 50)
        
        from_1 = ttk.Combobox(m,width = 13)
        from_1['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        from_1.place(x = 40,y = 75)
        
        to = tkinter.Label(m,text = 'To',bg = 'white',fg = 'black',font = g)
        to.place(x = 160,y= 50)
        
        to_1 = ttk.Combobox(m,width = 13)
        to_1['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        to_1.place(x = 160,y = 75)
        
        depart_ = tkinter.Label(m,text = 'Depart',fg = 'black',bg = 'white',font = g)
        depart_.config(highlightbackground = 'black',highlightcolor = 'green3',highlightthickness  = 1)
        depart_.place(x = 40,y = 120)
        
        depart_1 = tkinter.Entry(m,bg = 'white',fg = 'black',font = v,width = 12,justify = 'center') 
        depart_1.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness  = 1)
        depart_1.place(x = 110,y = 120)
        
        # flight 2
        fl_2 = tkinter.Label(m,text = 'Flight 2',bg = 'white',fg = 'black',font = g)
        fl_2.place(x = 40,y = 170)
        
        fro_2 = tkinter.Label(m,text = 'From',bg = 'white',fg = 'black',font = g)
        fro_2.place(x = 40,y= 200)
        
        from_2 = ttk.Combobox(m,width = 13)
        from_2['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        from_2.place(x = 40,y = 225)
        
        to_ = tkinter.Label(m,text = 'To',bg = 'white',fg = 'black',font = g)
        to_.place(x = 160,y= 200)
        
        to_2 = ttk.Combobox(m,width = 13)
        to_2['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        to_2.place(x = 160,y = 225)
        
        depart_ = tkinter.Label(m,text = 'Depart',fg = 'black',bg = 'white',font = g)
        depart_.config(highlightbackground = 'black',highlightcolor = 'green3',highlightthickness  = 1)
        depart_.place(x = 40,y = 265)
        
        depart_2 = tkinter.Entry(m,bg = 'white',fg = 'black',font = v,width = 12,justify = 'center') 
        depart_2.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness  = 1)
        depart_2.place(x = 110,y = 265)
        
        # flight 3
        fl_3 = tkinter.Label(m,text = 'Flight 3',bg = 'white',fg = 'black',font = g)
        fl_3.place(x = 40,y = 320)
        
        fro_3 = tkinter.Label(m,text = 'From',bg = 'white',fg = 'black',font = g)
        fro_3.place(x = 40,y= 350)
        
        from_3 = ttk.Combobox(m,width = 13)
        from_3['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        from_3.place(x = 40,y = 375)
        
        to_ = tkinter.Label(m,text = 'To',bg = 'white',fg = 'black',font = g)
        to_.place(x = 160,y= 350)
        
        to_3 = ttk.Combobox(m,width = 13)
        to_3['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        to_3.place(x = 160,y = 375)
        
        depart_ = tkinter.Label(m,text = 'Depart',fg = 'black',bg = 'white',font = g)
        depart_.config(highlightbackground = 'black',highlightcolor = 'green3',highlightthickness  = 1)
        depart_.place(x = 40,y = 420)
        
        depart_3 = tkinter.Entry(m,bg = 'white',fg = 'black',font = v,width = 12,justify = 'center') 
        depart_3.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness  = 1)
        depart_3.place(x = 110,y = 420)
        
        # flight 4
        fl_4 = tkinter.Label(m,text = 'Flight 4',bg = 'white',fg = 'black',font = g)
        fl_4.place(x = 380,y = 20)
        
        fro_4 = tkinter.Label(m,text = 'From',bg = 'white',fg = 'black',font = g)
        fro_4.place(x = 380,y= 50)
        
        from_4 = ttk.Combobox(m,width = 13)
        from_4['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        from_4.place(x = 380,y = 75)
        
        to_ = tkinter.Label(m,text = 'To',bg = 'white',fg = 'black',font = g)
        to_.place(x = 500,y= 50)
        
        to_4 = ttk.Combobox(m,width = 13)
        to_4['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        to_4.place(x = 500,y = 75)
        
        depart_ = tkinter.Label(m,text = 'Depart',fg = 'black',bg = 'white',font = g)
        depart_.config(highlightbackground = 'black',highlightcolor = 'green3',highlightthickness  = 1)
        depart_.place(x = 380,y = 120)
        
        depart_4 = tkinter.Entry(m,bg = 'white',fg = 'black',font = v,width = 12,justify = 'center') 
        depart_4.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness  = 1)
        depart_4.place(x = 450,y = 120)
        
        # flight 5
        fl_5 = tkinter.Label(m,text = 'Flight 5',bg = 'white',fg = 'black',font = g)
        fl_5.place(x = 380,y = 170)
        
        fro_5 = tkinter.Label(m,text = 'From',bg = 'white',fg = 'black',font = g)
        fro_5.place(x = 380,y= 200)
        
        from_5 = ttk.Combobox(m,width = 13)
        from_5['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        from_5.place(x = 380,y = 225)
        
        to_ = tkinter.Label(m,text = 'To',bg = 'white',fg = 'black',font = g)
        to_.place(x = 500,y= 200)
        
        to_5 = ttk.Combobox(m,width = 13)
        to_5['values'] = ('Chennai','Mumbai','Hyderabad','Madurai','Kolkata','Delhi','Bangalore')   # PLaces
        to_5.place(x = 500,y = 225)
        
        depart_ = tkinter.Label(m,text = 'Depart',fg = 'black',bg = 'white',font = g)
        depart_.config(highlightbackground = 'black',highlightcolor = 'green3',highlightthickness  = 1)
        depart_.place(x = 380,y = 265)
        
        depart_5 = tkinter.Entry(m,bg = 'white',fg = 'black',font = v,width = 12,justify = 'center') 
        depart_5.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness  = 1)
        depart_5.place(x = 450,y = 265)
        
        show_flight = tkinter.Button(m,text = 'Show Flight',bg = 'green',fg = 'white',command = showing_the_flights_multi)
        show_flight.config(font = g,width = 20)
        show_flight.place(x = 380,y = 400)
        
        m.mainloop()
        
    
    
    multi = tkinter.Radiobutton(x2,text = 'Multi City',font = g,bg = 'white',fg = 'black',activeforeground = 'green3',command = multi_flight)
    multi.config(highlightbackground = 'black',highlightcolor = 'black',highlightthickness = 2)
    multi.config(value = 3)
    multi.place(x = 280,y = 90)
    

    
    x2.mainloop()

Bg1 = tkinter.PhotoImage(file = 'D:\ZOHO PROJECTS\Flight\A1.png')
flight = tkinter.Button(x,image = Bg1,bg = 'white',highlightthickness= 0,borderwidth = 4,command = go_inside)
flight.place(x = 280,y = 330)
f = Hovertip(flight,'Click this to Open the Application')

x.mainloop()
