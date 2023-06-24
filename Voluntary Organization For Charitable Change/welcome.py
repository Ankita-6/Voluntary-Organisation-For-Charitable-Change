from tkinter import *
from tkinter import messagebox
import tempfile
import os

class Don:
    def donation(self,root):
        self.root=Tk()
        self.root.title('Donate for a cause')
        self.root.geometry('1280x720')

        self.Bread=IntVar()
        self.Wine=IntVar()
        self.Rice=IntVar()
        self.Gal=IntVar()
        self.Total=IntVar()

        self.cb=StringVar()
        self.cw=StringVar()
        self.cr=StringVar()
        self.cg=StringVar()
        self.total_cost=StringVar()

        def total():
            if self.Bread.get()==0 and self.Wine.get()==0 and self.Rice.get()==0 and self.Gal.get()==0:
                messagebox.showerror('Error','Please select number of quantity')
            else:
                b=self.Bread.get()
                w=self.Wine.get()
                r=self.Rice.get()
                g=self.Gal.get()

                t=float(b*200.00+w*150.00+r*300.00+g*100.00)
                self.Total.set(b + w + r + g)
                self.total_cost.set('Rs ' + str(round(t, 2)))

                self.cb.set('Rs ' +str(round(b * 200.00, 2)))
                self.cw.set('Rs '+str(round(w*150.00,2)))
                self.cr.set('Rs '+str(round(r*300.00,2)))
                self.cg.set('Rs '+str(round(g*100.00,2)))
        def receipt():
                
            self.textarea.insert(END,' Items\tNumber of Items\t  Cost of Items\n')
            self.textarea.insert(END,f'\nBread\t\t{self.Bread.get()}\t  {self.cb.get()}')
            self.textarea.insert(END,f'\n\nWine\t\t{self.Wine.get()}\t  {self.cw.get()}')
            self.textarea.insert(END,f'\n\nRice\t\t{self.Rice.get()}\t  {self.cr.get()}')
            self.textarea.insert(END,f'\n\nMilk\t\t{self.Gal.get()}\t  {self.cg.get()}')
            self.textarea.insert(END, f"\n\n================================")
            self.textarea.insert(END,f'\nTotal Price\t\t{self.Total.get()}\t{self.total_cost.get()}')
            self.textarea.insert(END, f"\n================================")
            self.textarea.insert(END, "\nThank you for donating to the NGO")
        
        def print():
            q=self.textarea.get('1.0','end-1c')
            filename=tempfile.mktemp('.txt')
            open(filename,'w').write(q)
            os.startfile(filename,'Print')

        def reset():
            self.textarea.delete(1.0,END)
            self.Bread.set(0)
            self.Wine.set(0)
            self.Rice.set(0)
            self.Gal.set(0)
            self.Total.set(0)

            self.cb.set('')
            self.cw.set('')
            self.cr.set('')
            self.cg.set('')
            self.total_cost.set('')


   

        root=Tk()
        ob=Don(root)
        root.mainloop()
        self.root.mainloop()
