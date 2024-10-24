from customtkinter import *
from tkinter import *
import tkinter
from CTkToolTip import *
from hPyT import *
from titlebarctk import *
import ctkdlib
from ctkdlib import *

app = CTk()
app.title('Theprogrammer__')
app.geometry('700x500')
app.geometry('+340+100')
maximize_button.disable(app)




g = ('georgia')
gc = CTkFont(family= 'georgia',size= 20,slant='italic')
gc_15 = CTkFont(family= 'georgia',size= 15,slant='italic')

Name_label = Label(app,text = 'String Functions - GUI',font= (g,20),fg = 'black'
,highlightbackground= 'black',highlightthickness=4)
Name_label.place(x = 215,y = 20)

def replace_form():
    r = CTkToplevel(app)
    r.title('Replace')
    r.geometry('300x300')
    r.attributes('-topmost',True)
    r.geometry('+350+200')

    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 40)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Spiderman')
    word_entry.place(x = 130,y = 40)

    old_word = CTkLabel(r,text = 'Old Word',font = (gc_15))
    old_word.place(x = 20,y = 90)

    old_word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Spider')
    old_word_entry.place(x = 130,y = 90)

    new_word = CTkLabel(r,text = 'New Word',font = (gc_15))
    new_word.place(x = 20,y = 140)

    new_word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Bat')
    new_word_entry.place(x = 130,y = 140)

    edited = CTkLabel(r,text = 'Edited',font = (gc_15))
    edited.place(x = 20,y = 190)

    edit_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Batman')
    edit_entry.place(x = 130,y = 190)

    def replacer_work():
        word = word_entry.get()
        old = old_word_entry.get()
        new = new_word_entry.get()
        final = word.replace(old,new)
        edit_entry.delete(0,END)
        edit_entry.insert(0,final)
    
    def clearing():
        word_entry.delete(0,END)
        old_word_entry.delete(0,END)
        new_word_entry.delete(0,END)
        edit_entry.delete(0,END)

    replace = CTkButton(r,text = 'Replace',font = gc,hover_color=('blue4'),width= len('text')
    ,fg_color= 'blue',text_color= 'white',corner_radius = 15,command= replacer_work)
    replace.place(x = 50,y = 240)
    
    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',corner_radius = 15,command= clearing)
    clear.place(x = 170,y = 240)

# Replace
replacer = CTkButton(app,text = 'Replace',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command = replace_form)
replacer.place(x = 40,y = 100)
rt = CTkToolTip(widget= replacer,message= 'Replace the Particular given word',bg_color= 'lightblue')


def capitalize_form():
    r = CTkToplevel(app)
    r.title('Capitalize')
    r.geometry('300x220')
    r.attributes('-topmost',True)
    r.geometry('+540+200')

    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 40)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. captain america')
    word_entry.place(x = 130,y = 40)

    result_label = CTkLabel(r,text = 'Result',font = (gc_15))
    result_label.place(x = 20,y = 90)

    result_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Captain america')
    result_entry.place(x = 130,y = 90)

    def replacer_work():
        word = word_entry.get()
        r = word.capitalize()
        result_entry.delete(0,END)
        result_entry.insert(0,r)
    
    def clearing():
        word_entry.delete(0,END)
        result_entry.delete(0,END)

    replace = CTkButton(r,text = 'Capitalize',font = gc,hover_color=('blue4'),width= len('text')
    ,fg_color= 'blue',text_color= 'white',corner_radius = 15,command= replacer_work)
    replace.place(x = 40,y = 160)
    

    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',corner_radius = 15,command= clearing)
    clear.place(x = 180,y = 160)


# Captilize
capitalizer = CTkButton(app,text = 'Capitalize',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command= capitalize_form)
capitalizer.place(x = 200,y = 100)
ct = CTkToolTip(widget= capitalizer,message= 'Capitalize the first letter in a word',bg_color= 'lightblue')



def capitalize_form():
    r = CTkToplevel(app)
    r.title('Capitalize')
    r.geometry('300x220')
    r.attributes('-topmost',True)
    r.geometry('+640+200')

    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 40)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Soldier Boy')
    word_entry.place(x = 130,y = 40)

    result_label = CTkLabel(r,text = 'Result',font = (gc_15))
    result_label.place(x = 20,y = 90)

    result_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. soldier boy')
    result_entry.place(x = 130,y = 90)

    def replacer_work():
        word = word_entry.get()
        r = word.casefold()
        result_entry.delete(0,END)
        result_entry.insert(0,r)
    
    def clearing():
        word_entry.delete(0,END)
        result_entry.delete(0,END)

    replace = CTkButton(r,text = 'Casefold',font = gc,hover_color=('blue4'),width= len('text')
    ,fg_color= 'blue',text_color= 'white',corner_radius = 15,command= replacer_work)
    replace.place(x = 40,y = 160)
    

    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',corner_radius = 15,command= clearing)
    clear.place(x = 180,y = 160)


#casefold
casefolder = CTkButton(app,text = 'Casefold',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command= capitalize_form)
casefolder.place(x = 360,y = 100)
cft = CTkToolTip(widget= casefolder,message= 'Converts to lowercase,\nignoring case & special chars'
,bg_color= 'lightblue',x_offset= -100,y_offset= 20)



def capitalize_form():
    r = CTkToplevel(app)
    r.title('Capitalize')
    r.geometry('300x220')
    r.attributes('-topmost',True)
    r.geometry('+730+200')

    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 40)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. black panther')
    word_entry.place(x = 130,y = 40)

    result_label = CTkLabel(r,text = 'Result',font = (gc_15))
    result_label.place(x = 20,y = 90)

    result_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Black Panther')
    result_entry.place(x = 130,y = 90)

    def replacer_work():
        word = word_entry.get()
        r = word.title()
        result_entry.delete(0,END)
        result_entry.insert(0,r)
    
    def clearing():
        word_entry.delete(0,END)
        result_entry.delete(0,END)

    replace = CTkButton(r,text = ' Title ',font = gc,hover_color=('blue4'),width= len('text')
    ,fg_color= 'blue',text_color= 'white',command= replacer_work)
    replace.place(x = 60,y = 160)
    

    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',command= clearing)
    clear.place(x = 150,y = 160)


#title
titler = CTkButton(app,text = 'Title',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command= capitalize_form)
titler.place(x = 520,y = 100)
cft = CTkToolTip(widget= titler,message= 'Capitalize first letter of each word'
,bg_color= 'lightblue',x_offset= -200,y_offset= 20)



def capitalize_form():
    r = CTkToplevel(app)
    r.title('Start/Ends with')
    r.geometry('360x250')
    r.attributes('-topmost',True)
    r.geometry('+350+280')

    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 40)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Starlight')
    word_entry.place(x = 190,y = 40)

    def starting(choice):
        if start_end.get() == 'Endswith':
            word_entry.configure(placeholder_text = 'e.g. Starlight')
            st_entry.configure(placeholder_text = 'e.g. t')
            res_entry.configure(placeholder_text = 'e.g. True')
            
            
        else:
            word_entry.configure(placeholder_text = 'e.g. Starlight')
            st_entry.configure(placeholder_text = 'e.g. S')
            res_entry.configure(placeholder_text = 'e.g. True')
            


    start_end = CTkComboBox(r,values = ['Startswith','Endswith'],border_color= 'black'
                            ,width= 150,font= gc_15,command= starting)
    start_end.place(x = 20,y = 90)

    st_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. S')
    st_entry.place(x = 190,y = 90)

    res_label = CTkLabel(r,text = 'Result',font = (gc_15))
    res_label.place(x = 20,y = 140)

    res_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. True')
    res_entry.place(x = 190,y = 140)

    def replacer_work():
        word = word_entry.get()
        combo_start = start_end.get()
        st_e = st_entry.get()
        res_entry.delete(0,END)
        if len(word) == 0:
            print('')
            res_entry.configure(placeholder_text = 'e.g. True')

        elif combo_start == 'Startswith':
            tf = word.startswith(st_e)
            if tf == 1:
                res_entry.insert(0,'True')
            elif tf == 0:
                res_entry.insert(0,'False')
            else:
                print('')
        
        elif combo_start == 'Endswith':
            tf = word.endswith(st_e)
            if tf == 1:
                res_entry.insert(0,'True')
            elif tf == 0:
                res_entry.insert(0,'False')
            else:
                print('')



        
        
    def clearing():
        word_entry.delete(0,END)
        st_entry.delete(0,END)
        res_entry.delete(0,END)

    replace = CTkButton(r,text = ' Run ',font = gc,hover_color=('blue4'),width= len('text')
    ,fg_color= 'blue',text_color= 'white',command= replacer_work,corner_radius= 20)
    replace.place(x = 60,y = 200)
    

    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',command= clearing,corner_radius= 20)
    clear.place(x = 180,y = 200)



# Starts with and Endswith
setwtith = CTkButton(app,text = 'Starts/Ends',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command= capitalize_form)
setwtith.place(x = 40,y = 180)
stw = CTkToolTip(widget= setwtith,message= 'Check if string with Specified Prefix/Suffix'
,bg_color= 'lightblue')



def capitalize_form(): #Count
    r = CTkToplevel(app)
    r.title('Count')
    r.geometry('300x250')
    r.attributes('-topmost',True)
    r.geometry('+530+250')

    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 40)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. OPTIMUS PRIME')
    word_entry.place(x = 130,y = 40)

    count_ = CTkLabel(r,text = 'Enter a Letter',font = (gc_15))
    count_.place(x = 20,y = 100)

    count_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. P')
    count_entry.place(x = 130,y = 100)

    result_label = CTkLabel(r,text = 'Result',font = (gc_15))
    result_label.place(x = 20,y = 160)

    result_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. 1')
    result_entry.place(x = 130,y = 160)

    def replacer_work():  #count
        word = word_entry.get()
        c = count_entry.get()
        r = word.count(c)
        result_entry.delete(0,END)
        result_entry.insert(0,r)
    
    def clearing():
        word_entry.delete(0,END)
        count_entry.delete(0,END)
        result_entry.delete(0,END)

    replace = CTkButton(r,text = ' Count ',font = gc,hover_color=('blue4'),width= len('text')
    ,fg_color= 'blue',text_color= 'white',command= replacer_work,corner_radius= 15)
    replace.place(x = 60,y = 210)
    

    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',command= clearing,corner_radius= 15)
    clear.place(x = 170,y = 210)


# count
count = CTkButton(app,text = 'Count',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command= capitalize_form)
count.place(x = 200,y = 180)
count_ = CTkToolTip(widget= count,message= 'Returns the number of occurrences\nof a substring in the string'
,bg_color= 'lightblue')

def capitalize_form(): #find
    r = CTkToplevel(app)
    r.title('Find')
    r.geometry('300x250')
    r.attributes('-topmost',True)
    r.geometry('+630+250')

    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 40)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Aang')
    word_entry.place(x = 130,y = 40)

    count_ = CTkComboBox(r,values = ['Find','RFind'],width= 100,border_color= 'black',font = (gc_15))
    count_.place(x = 20,y = 100)

    count_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. a')
    count_entry.place(x = 130,y = 100)

    result_label = CTkLabel(r,text = 'Result',font = (gc_15))
    result_label.place(x = 20,y = 160)

    result_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. 1')
    result_entry.place(x = 130,y = 160)

    def replacer_work():  #find
        word = word_entry.get()
        c = count_entry.get()
        if count_.get() == 'Find':
            r = word.find(c)
            result_entry.delete(0,END)
            result_entry.insert(0,r)
        if count_.get() == 'RFind':
            r = word.rfind(c)
            result_entry.delete(0,END)
            result_entry.insert(0,r)
    
    def clearing():
        word_entry.delete(0,END)
        count_entry.delete(0,END)
        result_entry.delete(0,END)

    replace = CTkButton(r,text = ' Find ',font = gc,hover_color=('blue4'),width= len('text')
    ,fg_color= 'blue',text_color= 'white',command= replacer_work,corner_radius= 15)
    replace.place(x = 60,y = 210)
    

    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',command= clearing,corner_radius= 15)
    clear.place(x = 170,y = 210)


# count
titler = CTkButton(app,text = 'Find',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command= capitalize_form)
titler.place(x = 360,y = 180)
cft = CTkToolTip(widget= titler,message= 'Finds substring and return index'
,bg_color= 'lightblue')

def capitalize_form(): #index
    r = CTkToplevel(app)
    r.title('Index')
    r.geometry('300x250')
    r.attributes('-topmost',True)
    r.geometry('+730+250')

    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 40)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Marvel')
    word_entry.place(x = 130,y = 40)

    count_ = CTkComboBox(r,values = ['Index','RIndex'],width= 100,border_color= 'black',font = (gc_15))
    count_.place(x = 20,y = 100)
    count_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. a')
    count_entry.place(x = 130,y = 100)

    result_label = CTkLabel(r,text = 'Result',font = (gc_15))
    result_label.place(x = 20,y = 160)

    result_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. 1')
    result_entry.place(x = 130,y = 160)

    def replacer_work():  #find
        word = word_entry.get()
        c = count_entry.get()
        if count_.get() == 'Index':
            r = word.index(c)

            result_entry.delete(0,END)
            result_entry.insert(0,r)
        if count_.get() == 'RIndex':
            r = word.rindex(c)
            result_entry.delete(0,END)
            result_entry.insert(0,r)
        
        result_entry.delete(0,END)
        result_entry.insert(0,r)
    
    def clearing():
        word_entry.delete(0,END)
        count_entry.delete(0,END)
        result_entry.delete(0,END)

    replace = CTkButton(r,text = ' Index ',font = gc,hover_color=('blue4'),width= len('text')
    ,fg_color= 'blue',text_color= 'white',command= replacer_work,corner_radius= 15)
    replace.place(x = 60,y = 210)
    

    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',command= clearing,corner_radius= 15)
    clear.place(x = 170,y = 210)


# index
titler = CTkButton(app,text = 'Index',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command= capitalize_form)
titler.place(x = 520,y = 180)
cft = CTkToolTip(widget= titler,message= 'Returns index of occurrence\n of specified value'
,bg_color= 'lightblue',x_offset= -200)



def capitalize_form(): #swapcase
    r = CTkToplevel(app)
    r.title('Swapcase')
    r.geometry('300x250')
    r.attributes('-topmost',True)
    r.geometry('+350+250')

    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 40)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. Multiverse')
    word_entry.place(x = 130,y = 40)

    
    result_label = CTkLabel(r,text = 'Result',font = (gc_15))
    result_label.place(x = 20,y = 110)

    result_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. mULTIVERSE')
    result_entry.place(x = 130,y = 110)

    def replacer_work():  #find
        word = word_entry.get()
        r = word.swapcase()
        result_entry.delete(0,END)
        result_entry.insert(0,r)
    
    def clearing():
        word_entry.delete(0,END)
        
        result_entry.delete(0,END)

    replace = CTkButton(r,text = ' Swaps ',font = gc,hover_color=('blue4'),width= len('text')
    ,fg_color= 'blue',text_color= 'white',command= replacer_work,corner_radius= 15)
    replace.place(x = 60,y = 180)
    

    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',command= clearing,corner_radius= 15)
    clear.place(x = 170,y = 180)


# swapcase
titler = CTkButton(app,text = 'Swapcase',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command= capitalize_form)
titler.place(x = 40,y = 260)
cft = CTkToolTip(widget= titler,message= 'Swaps uppercase letters to lowercase and back'
,bg_color= 'lightblue')


def capitalize_form(): #zfill
    r = CTkToplevel(app)
    r.title('Zfill')
    r.geometry('300x300')
    r.attributes('-topmost',True)
    r.geometry('+450+250')

    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 40)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. 7')
    word_entry.place(x = 130,y = 40)

    word_fil = CTkLabel(r,text = 'Enter Width',font = (gc_15))
    word_fil.place(x = 20,y = 110)

    word_entry_fil = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. 7')
    word_entry_fil.place(x = 130,y = 110)

    
    result_label = CTkLabel(r,text = 'Result',font = (gc_15))
    result_label.place(x = 20,y = 170)

    result_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. 0000007')
    result_entry.place(x = 130,y = 170)

    def replacer_work():  #zfill
        word = word_entry.get()
        filler = word_entry_fil.get()
        r = word.zfill(filler)
        result_entry.delete(0,END)
        result_entry.insert(0,r)
    
    def clearing():
        word_entry.delete(0,END)
        word_entry_fil.delete(0,END)
        
        result_entry.delete(0,END)

    replace = CTkButton(r,text = ' Zfill ',font = gc,hover_color=('blue4'),width= len('text')
    ,fg_color= 'blue',text_color= 'white',command= replacer_work,corner_radius= 15)
    replace.place(x = 60,y = 240)
    

    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',command= clearing,corner_radius= 15)
    clear.place(x = 170,y = 240)


# zfill
titler = CTkButton(app,text = 'Zfill',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command= capitalize_form)
titler.place(x = 200,y = 260)
cft = CTkToolTip(widget= titler,message= 'Pads a string with leading zeros\nuntil it reaches the specified width'
,bg_color= 'lightblue')



def capitalize_form(): #is
    r = CTkToplevel(app)
    r.title('IS')
    r.geometry('300x250')
    r.attributes('-topmost',True)
    r.geometry('+550+140')


    word_ = CTkLabel(r,text = 'Enter a Word',font = (gc_15))
    word_.place(x = 20,y = 20)

    word_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. something')
    word_entry.place(x = 130,y = 20)

    
    result_label = CTkLabel(r,text = 'Result',font = (gc_15))
    result_label.place(x = 20,y = 90)

    result_entry = CTkEntry(r,font = (gc_15),width = 160,border_color= 'black',placeholder_text= 'e.g. True/false')
    result_entry.place(x = 130,y = 90)

    def replacer_work(choice):  #find
        word = word_entry.get()

        if combo_is.get() == 'isdecimal':
            z = word.isdecimal()
            result_entry.delete(0,END)
            if z == 1:
                result_entry.insert(0,'True')
            elif z == 0:
                result_entry.insert(0,'False')
            
        
        if combo_is.get() == 'isdigit':
            z = word.isdigit()
            result_entry.delete(0,END)
            if z == 1:
                result_entry.insert(0,'True')
            elif z == 0:
                result_entry.insert(0,'False')
        
        if combo_is.get() == 'isalnum':
            z = word.isalnum()
            result_entry.delete(0,END)
            if z == 1:
                result_entry.insert(0,'True')
            elif z == 0:
                result_entry.insert(0,'False')
        
        if combo_is.get() ==  'isspace':
            z = word.isspace()
            result_entry.delete(0,END)
            if z == 1:
                result_entry.insert(0,'True')
            elif z == 0:
                result_entry.insert(0,'False')
        
        if combo_is.get() == 'istitle':
            z = word.istitle()
            result_entry.delete(0,END)
            if z == 1:
                result_entry.insert(0,'True')
            elif z == 0:
                result_entry.insert(0,'False')
        
        if combo_is.get() == 'isidentifier':
            z = word.isidentifier()
            result_entry.delete(0,END)
            if z == 1:
                result_entry.insert(0,'True')
            elif z == 0:
                result_entry.insert(0,'False')
        
        if combo_is.get() == 'isnumeric':
            z = word.isnumeric()
            result_entry.delete(0,END)
            if z == 1:
                result_entry.insert(0,'True')
            elif z == 0:
                result_entry.insert(0,'False')
        
        if combo_is.get() == 'isprintable':
            z = word.isprintable()
            result_entry.delete(0,END)
            if z == 1:
                result_entry.insert(0,'True')
            elif z == 0:
                result_entry.insert(0,'False')
        
        if combo_is.get() == 'isupper':
            z = word.isupper()
            result_entry.delete(0,END)
            if z == 1:
                result_entry.insert(0,'True')
            elif z == 0:
                result_entry.insert(0,'False')
            
        if combo_is.get() == 'islower':
            z = word.islower()
            result_entry.delete(0,END)
            if z == 1:
                result_entry.insert(0,'True')
            elif z == 0:
                result_entry.insert(0,'False')
        
        

    def clearing():
        word_entry.delete(0,END)
        
        result_entry.delete(0,END)
    
    combo_is = CTkComboBox(r,values= ['isdecimal','isdigit','isalnum','isspace','istitle','isidentifier','isnumeric'
    ,'isprintable','isupper','islower'],font= gc_15,border_color= 'black',width = 120,command= replacer_work)
    combo_is.place(x = 40,y = 150)
    


    # replace = CTkButton(r,text = ' Swaps ',font = gc,hover_color=('blue4'),width= len('text')
    # ,fg_color= 'blue',text_color= 'white',command= replacer_work,corner_radius= 15)
    # replace.place(x = 60,y = 180)
    

    clear = CTkButton(r,text = ' Clear ',font = gc,hover_color=('red4'),width= len('text')
    ,fg_color= 'red',text_color= 'white',command= clearing,corner_radius= 15)
    clear.place(x = 170,y = 150)


# swapcase
titler = CTkButton(app,text = 'Is...',font = gc,hover_color=('green4')
,fg_color= 'green',text_color= 'white',command= capitalize_form)
titler.place(x = 360,y = 260)
cft = CTkToolTip(widget= titler,message= 'Return true or Flase'
,bg_color= 'lightblue')


def create_info_():
    iform = CTkToplevel(app)
    iform.title('Information')

    opacity.set(iform,0.9)
    
    iform.geometry('620x495')
    iform.attributes('-topmost',True)
    iform.geometry('+380+103')
    maximize_button.disable(iform
                            )

    c  = CTkFont(family='Cooper', size= 13,weight= 'bold',slant= 'italic')

    label_1 = CTkLabel(iform,text= 'Replace() : Returns a string where a specified value is replaced with a specified value'
    ,font= c)
    label_1.place(x = 10,y = 5)

    label_2 = CTkLabel(iform,text= 'Capitalize() : Converts the first character to upper case'
    ,font= c)
    label_2.place(x = 10,y = 30)

    label_3 = CTkLabel(iform,text= 'Casefold() : Converts string into lower case'
    ,font= c)
    label_3.place(x = 10,y = 55)

    label_4 = CTkLabel(iform,text= 'Title() : Converts the first character of each word to upper case'
    ,font= c)
    label_4.place(x = 10,y = 80)

    label_5 = CTkLabel(iform,text= 'Startswith() : Returns true if the string starts with the specified value'
    ,font= c)
    label_5.place(x = 10,y = 105)

    label_6 = CTkLabel(iform,text= 'Endswith() : Returns true if the string ends with the specified value'
    ,font= c)
    label_6.place(x = 10,y = 130)

    
    label_7 = CTkLabel(iform,text= 'Count() : Returns the number of times a specified value occurs in a string'
    ,font= c)
    label_7.place(x = 10,y = 155)

    
    label_8 = CTkLabel(iform,text= 'Find() : Searches the string for a specified value and returns the position of where it was found'
    ,font= c)
    label_8.place(x = 10,y = 180)

    label_9 = CTkLabel(iform,text= 'Index() : Searches the string for a specified value and returns the position of where it was found'
    ,font= c)
    label_9.place(x = 10,y = 205)

    
    label_10 = CTkLabel(iform,text= 'Swapcase() : Swaps cases, lower case becomes upper case and upper case becomes lower case'
    ,font= c)
    label_10.place(x = 10,y = 230)

    label_11 = CTkLabel(iform,text= 'Zfill() : Fills the string with a specified number of 0 values at the beginning'
    ,font= c)
    label_11.place(x = 10,y = 255)

    label_12 = CTkLabel(iform,text= 'isdecimal() : Returns True if all characters in the string are decimals'
    ,font= c)
    label_12.place(x = 10,y = 280)

    label_13 = CTkLabel(iform,text= 'isdigit() : Returns True if all characters in the string are digits'
    ,font= c)
    label_13.place(x = 10,y = 305)

    label_14 = CTkLabel(iform,text= 'isalnum() : Returns True if all characters in the string are alphanumeric'
    ,font= c)
    label_14.place(x = 10,y = 330)

    label_15 = CTkLabel(iform,text= 'issapce() : Returns True if all characters in the string are whitespaces'
    ,font= c)
    label_15.place(x = 10,y = 355)

    label_16 = CTkLabel(iform,text= 'istitle() : Returns True if the string follows the rules of a title'
    ,font= c)
    label_16.place(x = 10,y = 380)

    label_17 = CTkLabel(iform,text= 'isidentifier() : Returns True if the string is an identifier'
    ,font= c)
    label_17.place(x = 10,y = 405)

    label_18 = CTkLabel(iform,text= 'isnumeric() : Returns True if all characters in the string are numeric'
    ,font= c)
    label_18.place(x = 10,y = 430)

    label_19 = CTkLabel(iform,text= 'isprintable() : Returns True if all characters in the string are printable'
    ,font= c)
    label_19.place(x = 10,y = 455)

    label_20 = CTkLabel(iform,text= 'isupper() : Returns True if all characters in the string are upper case'
    ,font= c)
    label_20.place(x = 10,y = 455)

    label_21 = CTkLabel(iform,text= 'islower() : Returns True if all characters in the string are lower case'
    ,font= c)
    label_21.place(x = 10,y = 475)


info = CTkButton(app,text = 'Information',font = gc,hover_color=('blue2')
,fg_color= 'blue',text_color= 'white',command= create_info_)
info.place(x = 520,y = 260)
cft = CTkToolTip(widget= info,message= 'Information about this string function'
,bg_color= 'lightblue',x_offset= -200)






pawan = CTkLabel(app,text = 'Programmed by D.Pawan srikanth',font= (gc))
pawan.place(x = 330,y = 450)


app.mainloop()


