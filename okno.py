from tkinter import *
from tkinter import ttk

# Create Window

root=Tk()
root.title("регистрация")
root.geometry("600x470")
root.resizable(False,False)
# end of Create Window

# Create First Frame
content=Frame(root)

acc_lable=ttk.Label(content,foreground="orange",text="Account",font=("Arial", 14))
acc_lable.pack(padx=40,side=TOP,fill=X)

name_entry=ttk.Entry(content,textvariable="Full name")
name_entry.insert(0,"Full name")
name_entry.pack(pady=7,padx=40,side=TOP,fill=X)

email_entry=ttk.Entry(content,textvariable="Email")
email_entry.insert(0,"Email")
email_entry.pack(pady=7,padx=40,side=TOP,fill=X)

password_entry=ttk.Entry(content,textvariable="Password")
password_entry.insert(0,"Password")
password_entry.pack(pady=7,padx=40,side=TOP,fill=X)

gen_lable=ttk.Label(content,foreground="orange",text="Gender",font=("Arial", 14))
gen_lable.pack(pady=5,padx=40,side=TOP,fill=X)

content.pack(side=TOP, fill=X)
# end of Create First Frame

# Create Second Frame
content_2=Frame(root)

lang = StringVar(value="Male")

gender_but=ttk.Radiobutton(content_2,text="Male",value="Male", variable=lang)
gender_but.pack(pady=5,padx=40,side=LEFT)

gender_but_2=ttk.Radiobutton(content_2,value="Female", variable=lang,text="Female")
gender_but_2.pack(pady=5,padx=40,side=LEFT)

content_2.pack(fill=X)
# end of Create Second Frame

# Create Third Frame
content_3=Frame(root)

prog_lable=ttk.Label(content_3,foreground="orange",text="Programming language",font=("Arial", 14))
prog_lable.grid(pady=5,padx=40,row=1,column=1,columnspan=5,sticky=W)

python = IntVar()
py_check=ttk.Checkbutton(content_3,text="Python",variable=python)
py_check.grid(pady=5,padx=40,row=2,column=1)

java = IntVar()
java_check=ttk.Checkbutton(content_3,text="Java",variable=java)
java_check.grid(pady=5,padx=20,row=2,column=2)

cpp = IntVar()
cpp_check=ttk.Checkbutton(content_3,text="C++",variable=cpp)
cpp_check.grid(pady=5,padx=20,row=2,column=3)

c = IntVar()
c_check=ttk.Checkbutton(content_3,text="C#",variable=c)
c_check.grid(pady=5,padx=20,row=2,column=4)

javas = IntVar()
jv_chekc=ttk.Checkbutton(content_3,text="JavaScript",variable=javas)
jv_chekc.grid(pady=5,padx=20,row=2,column=5)

content_3.pack(fill=X)
# end of Create Third Frame

# Create Fourth Frame
content_4=Frame(root)

sub_bth=Button(content_4,text="Submit",bg="orange",fg="black",width=30)
sub_bth.grid(pady=15,padx=40,row=3,column=1,sticky=W)

content_4.pack(fill=X)
# end of Create Fourth Frame

# Run App
root.mainloop()
# end of Run