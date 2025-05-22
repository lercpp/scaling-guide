from tkinter import *
from tkinter import ttk
from functions import (len_arr,max_arr,min_arr,avg_arr,num_1_arr,num_2_arr)


def button_handler(func):
    def find():
        string = num_entry.get().split(', ')
        try:
            lst = [int(s) for s in string]
            result = func(lst)
            assert result is not None
        except (ValueError, AssertionError):
            num_entry.config(text='При вычислении произошла ошибка, убедитесь\nЧто все написано по шаблону.')
        else:

                len_arr==True
                max_arr==True
                min_arr==True
                avg_arr==True
                num_1_arr==True
                num_2_arr==True

                if len_arr==True:
                    len_r_lable.config(text=f'({result})')

                if max_arr==True:
                    max_r_lable.config(text=f'({result})')

                if min_arr==True:    
                    min_r_lable.config(text=f'({result})')

                if avg_arr==True:
                    avg_r_lable.config(text=f'({result})')
                
                if num_1_arr==True:
                    num_1_r_lable.config(text=f'({result})')

                if num_2_arr==True:
                    num_2_r_lable.config(text=f'({result})')
                
    return find

# Create Window

root=Tk()
root.title("массивы")
root.geometry("600x470")
root.resizable(False,False)
# end of Create Window


# Create First Frame
content=Frame(root)

calk_lable=ttk.Label(content,foreground="orange",text="Calculator Arrays",font=("Arial", 14))
calk_lable.pack(padx=40,side=TOP,fill=X)

num_entry=ttk.Entry(content)
num_entry.insert(0,"Input array")
num_entry.pack(pady=7,padx=40,side=TOP,fill=X)

content.pack(side=TOP, fill=X)
# end of Create First Frame

# Create Second Frame
content_2=Frame(root)

len_lable=ttk.Label(content_2,foreground="black",text="Length:",font=("Arial", 10),width=56)
len_lable.grid(pady=5,padx=40,row=1,column=1,columnspan=5,sticky=W)

len_r_lable=ttk.Label(content_2,foreground="black",text="(result)",font=("Arial", 10))
len_r_lable.grid(pady=5,padx=40,row=1,column=20,sticky=E)


max_lable=ttk.Label(content_2,foreground="black",text="Max elem:",font=("Arial", 10),width=56)
max_lable.grid(pady=5,padx=40,row=2,column=1,columnspan=5,sticky=W)

max_r_lable=ttk.Label(content_2,foreground="black",text="(result)",font=("Arial", 10))
max_r_lable.grid(pady=5,padx=40,row=2,column=20,sticky=E)


min_lable=ttk.Label(content_2,foreground="black",text="Min elem:",font=("Arial", 10),width=56)
min_lable.grid(pady=5,padx=40,row=3,column=1,columnspan=5,sticky=W)

min_r_lable=ttk.Label(content_2,foreground="black",text="(result)",font=("Arial", 10))
min_r_lable.grid(pady=5,padx=40,row=3,column=20,sticky=E)


avg_lable=ttk.Label(content_2,foreground="black",text="Avg:",font=("Arial", 10),width=56)
avg_lable.grid(pady=5,padx=40,row=4,column=1,columnspan=5,sticky=W)

avg_r_lable=ttk.Label(content_2,foreground="black",text="(result)",font=("Arial", 10))
avg_r_lable.grid(pady=5,padx=40,row=4,column=20,sticky=E)


num_1_lable=ttk.Label(content_2,foreground="black",text="Number of even:",font=("Arial", 10),width=56)
num_1_lable.grid(pady=5,padx=40,row=5,column=1,columnspan=5,sticky=W)

num_1_r_lable=ttk.Label(content_2,foreground="black",text="(result)",font=("Arial", 10))
num_1_r_lable.grid(pady=5,padx=40,row=5,column=20,sticky=E)


num_2_lable=ttk.Label(content_2,foreground="black",text="Number of uneven:",font=("Arial", 10),width=56)
num_2_lable.grid(pady=5,padx=40,row=6,column=1,columnspan=5,sticky=W)

num_2_r_lable=ttk.Label(content_2,foreground="black",text="(result)",font=("Arial", 10))
num_2_r_lable.grid(pady=5,padx=40,row=6,column=20,sticky=E)

sub_bth=Button(content_2,text="Subnit",bg="orange",fg="black",width=30,command=button_handler)
sub_bth.grid(pady=15,padx=40,row=7,column=1,sticky=W)


content_2.pack(fill=X)
# end of Create Second Frame

# Run App
root.mainloop()
# end of Run