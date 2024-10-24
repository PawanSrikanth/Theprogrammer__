import tkinter.scrolledtext
import customtkinter
from customtkinter import *
import ctkdlib
from CTkToolTip import *
from hPyT import *
import tkinter
from CTkMessagebox import CTkMessagebox
app = customtkinter.CTk()
app.title('Theprogrammer__')
app.geometry('550x510')
app.geometry('+200+70')
maximize_button.disable(app)

import os


from ctkentrymsg import CTkEntryMsg

g= CTkFont(family='georgia')

title = CTkLabel(app,text = 'Theprogrammer__ Sign Up Form'
,font = g,text_color = 'black')
title.place(x = 125,y = 10)


def confirmation():
    name_p  = name_.get()
    Email_p = Email_.get()
    Emailtype =Email_option.get()
    day_p   = day.get()
    month_p = month.get()
    year_p = year.get() 
    gendering = gender_select.get()
    # print(gendering)   
    mobile_type=mobile_number.get()
    mobile_p =mobile_number_entry.get()
    skills_p = skills_entry.get()
    DATEOFBIRTH = (f'{day_p} - {month_p} - {year_p}' )
    
    ID =  1
    Name_final = 'Name : ' + name_p
    print(Name_final)
    Email_fin  = 'Email : ' + Email_p + Emailtype
    print(Email_fin)
    D_O_B_fin = 'Date of birth : ',DATEOFBIRTH
    print(D_O_B_fin)
    gender_fin = 'Gender : ' + gendering
    print(gender_fin)
    mobile_fin = 'Mobile Number : ',mobile_type + mobile_p
    print(mobile_fin)
    skills_fin = 'Skills :' + skills_p
    print(skills_fin)

    id_num = ID_ENTRY.get()
    id_num = str(id_num)
    id_fin = (id_num + ' - ' + name_p + '.txt')
    file = open(f'D:\\Form_Data_Python\\{id_fin}','w')

    
    

    data_saved = CTkMessagebox(app,title= id_fin,message= 'Data Saved Successfully in Form_Data_Python folder',option_1= 'Ok')
    response = data_saved.get()
    if response == 'Ok':
        name_.delete(0,END)
        Email_.delete(0,END)
        Email_option.set('Select Email')
        day.delete(0,END)
        month.set('Select Month')
        year.delete(0,END)
        male.deselect()
        female.deselect()
        mobile_number.set('Code')
        mobile_number_entry.delete(0,END)
        skills_entry.delete(0,END)

    q = ID_ENTRY.get()
    q = int(q)
    xx = q + 1
    ID_ENTRY.delete(0,END)
    ID_ENTRY.insert(0,xx )



ID_ENTRY = customtkinter.CTkEntry(app,justify = RIGHT,fg_color= 'transparent')
ID_ENTRY.place(x = 400,y = 10)
ID_ENTRY.insert(0,1)

name = CTkLabel(app,text = 'Name',text_color = 'black',font = g)
name.place(x = 50,y = 50)

name_ = CTkEntryMsg(app,text_color = 'black',font = g,border_color = 'black'
,width= 250,fg_color = 'transparent')
name_.place(x = 120,y = 50)

Email = CTkLabel(app,text = 'Email',text_color = 'black',font = g)
Email.place(x = 50,y = 100)

Email_ = CTkEntryMsg(app,text_color = 'black',font = g,border_color = 'black'
,width= 250,fg_color = 'transparent')
Email_.place(x = 120,y = 100)

Email_option = CTkOptionMenu(app,values= ['@gmail.com','@outlook.com'],font= g
,fg_color = 'grey60',text_color='black',width = 100,dropdown_font = g,button_color = 'grey50'
,button_hover_color = 'lightsteelblue3')
Email_option.place(x = 380,y = 100)
Email_option.set(' Select Email')

DOB = CTkLabel(app,text = 'DOB',text_color = 'black',font = g)
DOB.place(x = 50,y = 150)
Dateofbirth = CTkToolTip(DOB,message = 'Date Of Birth - (DD/MM/YYYY)',bg_color = 'white')

month_names_list   = ['January','February','March','April','May','June','July'
,'August','September','October','November','December']

def DOB_(values): # month widget command <
    mm = month.get()
    # print(mm)
    for _ in range(1,13):
        if mm == month_names_list[_-1]:
            month_num = _            
            if len(year.get()) == 0:
                year.showerror(msg = 'Fill the Year Box',timeout= 5000)
            year_num  = int(year.get())
                
            c = CTkToplevel() # calendar toplevel
            c.title('DATE')
            c.attributes('-topmost',True)
            c.geometry('250x250')
            c.maxsize(0,0)
            c.geometry('+300+190')
            maximize_button.disable(c)
            minimize_button.disable(c)
            
            def DATE(calendar_):
                print(calendar_)
                day_final = calendar_[0]
                day.delete(0,customtkinter.END) # to be continued
                day.insert(0,day_final)     

            calendar_ = ctkdlib.CTkCalendar(c,command = DATE)
            calendar_.set([00,month_num,year_num])
            calendar_.pack()
            
            day_num   = int(day.get())                
            # print(month_num)
            day_month_year = {'Day' :day_num ,'Month' :month_num ,'Year':year_num}
            print(day_month_year)
                   
day = CTkEntryMsg(app,placeholder_text = 'Day',border_color = 'black',width = 50
,justify = 'center')
day.place(x = 120,y = 150)

month = CTkComboBox(app,border_color = 'black',values= month_names_list,width = 120,
font= g,justify= 'center',command = DOB_,dropdown_font= g)
month.place(x = 180,y = 150)
month.set('Select Month')

year = CTkEntryMsg(app,placeholder_text = 'Year',border_color = 'black',width = 80
,default_msg= 'Fill the Year first',justify = 'center',highlight_error_color = 'white'
,msg_warn_color= 'white',msg_pos= 'bottom',msg_default_color= 'blue')
year.place(x = 310,y = 150)

gender = CTkLabel(app,text = 'Gender',font = g)
gender.place(x = 40,y = 200)

gender_select = customtkinter.StringVar(value ='')


    
    

male = CTkRadioButton(app,text = 'Male',font= g,variable= gender_select,value = 'Male'
,fg_color= 'royalblue',hover_color='green3')
male.place(x = 130,y = 200)


female = CTkRadioButton(app,text = 'Female',font= g,text_color = 'black',variable = gender_select,value= 'Female'
,fg_color= 'purple',hover_color='green3')
female.place(x = 200,y = 200)



codes_num = ['India +91','USA +1','UK +44','China +86','Canada +1','Australia +61'
,'Russia +7','Japan +81']

mobile_label = CTkLabel(app,text = 'Mobile')
mobile_label.place(x = 40,y = 250)

mobile_number = CTkOptionMenu(app,values = codes_num,width=0,fg_color = 'grey60'
,text_color='black',dropdown_font = g,button_color = 'grey50'
,button_hover_color = 'lightsteelblue3')
mobile_number.place(x = 100,y = 250)
mobile_number.set('Code')

mobile_number_entry = CTkEntryMsg(app,width = 150,border_color = 'black',fg_color = 'transparent')
mobile_number_entry.place(x = 230,y = 250)

skills = CTkLabel(app,text = 'Skills')
skills.place(x = 40,y = 300)

skills_entry = CTkEntryMsg(app,width = 300,border_color = 'black',fg_color = 'transparent')
skills_entry.place(x = 100,y = 300)

# os
#folder = os.mkdir('D:\\Form_Data_Python')
if os.path.exists('D:\\Form_Data_Python'):
    print('Folder already exists')
else:
    folder = os.mkdir('D:\\Form_Data_Python')

    
    

    
   
    
    

   
    


confirm = CTkButton(app,text = 'Confirm',fg_color = 'green3',text_color= 'black'
,font=g,hover_color= 'darkgreen',command = confirmation)
confirm.place(x = 120,y = 350)

def clearing():
    name_.delete(0,END)
    Email_.delete(0,END)
    Email_option.set('Select Email')
    day.delete(0,END)
    month.set('Select Month')
    year.delete(0,END)
    male.deselect()
    female.deselect()
    mobile_number.set('Code')
    mobile_number_entry.delete(0,END)
    skills_entry.delete(0,END)

clear = CTkButton(app,text = 'Clear',fg_color = 'red',text_color= 'black'
,font=g,hover_color= 'darkred',width = 100,command= clearing)
clear.place(x = 290,y = 350)


g2 = CTkFont(family='georgia',size= 20,slant= 'italic')

copyright_ = customtkinter.CTkLabel(app,text = 
'Programmed by D.Pawan sri kanth',font= (g2))
copyright_.place(x = 200,y = 460)

app.mainloop()
