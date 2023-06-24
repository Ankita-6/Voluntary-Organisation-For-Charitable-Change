from tkinter import*
from PIL import Image,ImageTk

class CharityManagement:
    def __init__(self,root):
        self.root=root
        self.root.title("NGO activity integration")
        self.root.geometry("1550x800+0+0")
        
        lbltitle=Label(self.root,text="NGO ACTIVITY INTERGRATION",bd=15,relief=RIDGE,bg='white',fg='darkgreen',font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)  

        #img1=Image.open("C:\Users\acer\Pictures\ngologo.jpg")  
        #img1=img1.resize(80,80),Image.ANTIALIAS
        #self.photoimg1=ImageTk.PhotoImage(img1)
        #b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        #b1.place(x=70,y=20)
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=CharityManagement(root)
    root.mainloop()

