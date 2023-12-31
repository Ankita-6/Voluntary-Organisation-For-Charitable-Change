from tkinter import *
from tkinter import messagebox
import tempfile
import os

root=Tk()
root.title('Donate for a cause')
root.geometry('1280x720')
bg_color='gray'


#=====================variables===================
Cloth=IntVar()
Veggies=IntVar()
Rice=IntVar()
Milk=IntVar()
Total=IntVar()

cc=StringVar()
cv=StringVar()
cr=StringVar()
cm=StringVar()
total_cost=StringVar()
# ===========Function===============
def total():
    if Cloth.get()==0 and Veggies.get()==0 and Rice.get()==0 and Milk.get()==0:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Cloth.get()
        w=Veggies.get()
        r=Rice.get()
        g=Milk.get()

        t=float(b*200.00+w*150.00+r*300.00+g*100.00)
        Total.set(b + w + r + g)
        total_cost.set('Rs ' + str(round(t, 2)))

        cc.set('Rs ' +str(round(b * 200.00, 2)))
        cv.set('Rs '+str(round(w*150.00,2)))
        cr.set('Rs '+str(round(r*300.00,2)))
        cm.set('Rs '+str(round(g*100.00,2)))






def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,' Items\tNumber of Items\t  Cost of Items\n')
    textarea.insert(END,f'\nClothes\t\t{Cloth.get()}\t  {cc.get()}')
    textarea.insert(END,f'\n\nVegetables\t\t{Veggies.get()}\t  {cv.get()}')
    textarea.insert(END,f'\n\nRice\t\t{Rice.get()}\t  {cr.get()}')
    textarea.insert(END,f'\n\nMilk\t\t{Milk.get()}\t  {cm.get()}')
    textarea.insert(END, f"\n\n================================")
    textarea.insert(END,f'\nTotal Price\t\t{Total.get()}\t{total_cost.get()}')
    textarea.insert(END, f"\n================================")
    textarea.insert(END, "\nThank you for donating!!")


def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,'Print')


def reset():
    textarea.delete(1.0,END)
    Cloth.set(0)
    Veggies.set(0)
    Rice.set(0)
    Milk.set(0)
    Total.set(0)

    cc.set('')
    cv.set('')
    cr.set('')
    cm.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()

title=Label(root,pady=5,text="DONATE FOR A CAUSE",bd=12,bg=bg_color,fg='white',font=('times new roman', 35 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#===============Product Details=================
F1 = LabelFrame(root, text='Choose products to donate', font=('times new romon', 18, 'bold'), fg='black',bg=bg_color,bd=15,relief=RIDGE)
F1.place(x=5, y=90,width=800,height=500)

#=====================Heading==========================
itm=Label(F1, text='Items', font=('Helvetic',25, 'bold','underline'), fg='black',bg=bg_color)
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1, text='Quantity of Items', font=('Helvetic',25, 'bold','underline'), fg='black',bg=bg_color)
n.grid(row=0,column=1,padx=30,pady=15)

cost=Label(F1, text='Cost of Items', font=('Helvetic',25, 'bold','underline'), fg='black',bg=bg_color)
cost.grid(row=0,column=2,padx=30,pady=15)

#===============Product============

cloth=Label(F1, text='Clothes', font=('times new rommon',20, 'bold'), fg='blue',bg=bg_color)
cloth.grid(row=1,column=0,padx=20,pady=15)
b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Cloth,justify=CENTER)
b_txt.grid(row=1,column=1,padx=20,pady=15)
cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cc,justify=CENTER)
cb_txt.grid(row=1,column=2,padx=20,pady=15)

veggies=Label(F1, text='Vegetables', font=('times new rommon',20, 'bold'), fg='blue',bg=bg_color)
veggies.grid(row=2,column=0,padx=20,pady=15)
w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Veggies,justify=CENTER)
w_txt.grid(row=2,column=1,padx=20,pady=15)
cw_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cv,justify=CENTER)
cw_txt.grid(row=2,column=2,padx=20,pady=15)

rice=Label(F1, text='Rice', font=('times new rommon',20, 'bold'), fg='blue',bg=bg_color)
rice.grid(row=3,column=0,padx=20,pady=15)
r_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Rice,justify=CENTER)
r_txt.grid(row=3,column=1,padx=20,pady=15)
cr_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cr,justify=CENTER)
cr_txt.grid(row=3,column=2,padx=20,pady=15)

milk=Label(F1, text='Milk', font=('times new rommon',20, 'bold'), fg='blue',bg=bg_color)
milk.grid(row=4,column=0,padx=20,pady=15)
g_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Milk,justify=CENTER)
g_txt.grid(row=4,column=1,padx=20,pady=15)
cg_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cm,justify=CENTER)
cg_txt.grid(row=4,column=2,padx=20,pady=15)

t=Label(F1, text='Total', font=('times new rommon',20, 'bold'), fg='blue',bg=bg_color)
t.grid(row=5,column=0,padx=20,pady=15)
t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Total,justify=CENTER)
t_txt.grid(row=5,column=1,padx=20,pady=15)
totalcost_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=total_cost,justify=CENTER)
totalcost_txt.grid(row=5,column=2,padx=20,pady=15)

#=====================Bill areea====================
F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=500)
bill_title=Label(F2,text='Donation Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F2,orient=VERTICAL)
scrol_y.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)



#=====================Buttons========================
F3 =Frame(root,bg=bg_color,bd=15,relief=RIDGE)
F3.place(x=5, y=590,width=1270,height=120)

btn1 = Button(F3, text='Total', font='arial 25 bold', padx=5, pady=5, bg='magenta',fg='white',width=10,command=total)
btn1.grid(row=0,column=0,padx=20,pady=10)

btn2 = Button(F3, text='Receipt', font='arial 25 bold', padx=5, pady=5, bg='pink',fg='black',width=10,command=receipt)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3 = Button(F3, text='Print', font='arial 25 bold', padx=5, pady=5, bg='magenta',fg='white',width=10,command=print)
btn3.grid(row=0,column=2,padx=10,pady=10)

btn4 = Button(F3, text='Reset', font='arial 25 bold', padx=5, pady=5, bg='pink',fg='black',width=10,command=reset)
btn4.grid(row=0,column=3,padx=10,pady=10)

btn5 = Button(F3, text='Exit', font='arial 25 bold', padx=5, pady=5, bg='purple',fg='white',width=10,command=exit)
btn5.grid(row=0,column=4,padx=10,pady=10)





root.mainloop()