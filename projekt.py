import tkinter as tk
root = tk.Tk()
root.title("kalkulator")
class Aplication:
    
    def __init__(self,r):

        x = tk.StringVar()
        size = 7

        e1 = tk.Entry(r,width=size*5,textvariable=x)
        e1.grid(row=0,column=1,columnspan=4)
        b1 = tk.Button(r,text=1,command=lambda:self.dodaj(1,x,e1),width=size, height= int(size/2))
        b1.grid(row=1,column=1)
        b2 = tk.Button(r,text=2,command=lambda:self.dodaj(2,x,e1),width=size, height= int(size/2))
        b2.grid(row=1,column=2)
        b3 = tk.Button(r,text=3,command=lambda:self.dodaj(3,x,e1),width=size, height= int(size/2))
        b3.grid(row=1,column=3)
        b4 = tk.Button(r,text=4,command=lambda:self.dodaj(4,x,e1),width=size, height= int(size/2))
        b4.grid(row=2,column=1)
        b5 = tk.Button(r,text=5,command=lambda:self.dodaj(5,x,e1),width=size, height= int(size/2))
        b5.grid(row=2,column=2)
        b6 = tk.Button(r,text=6,command=lambda:self.dodaj(6,x,e1),width=size, height= int(size/2))
        b6.grid(row=2,column=3)
        b7 = tk.Button(r,text=7,command=lambda:self.dodaj(7,x,e1),width=size, height= int(size/2))
        b7.grid(row=3,column=1)
        b8 = tk.Button(r,text=8,command=lambda:self.dodaj(8,x,e1),width=size, height= int(size/2))
        b8.grid(row=3,column=2)
        b9 = tk.Button(r,text=9,command=lambda:self.dodaj(9,x,e1),width=size, height= int(size/2))
        b9.grid(row=3,column=3)
        bplus = tk.Button(r,text="+",command=lambda:self.dodaj("+",x,e1),width=size, height= int(size/2))
        bplus.grid(row=4,column=1)
        b0 = tk.Button(r,text=0,command=lambda:self.dodaj(0,x,e1),width=size, height= int(size/2))
        b0.grid(row=4,column=2)
        bminus = tk.Button(r,text="-",command=lambda:self.dodaj("-",x,e1),width=size, height= int(size/2))
        bminus.grid(row=4,column=3)
       
        bmul = tk.Button(r,text="*",command=lambda:self.dodaj("*",x,e1),width=size, height= int(size))
        bmul.grid(row=1,column=4,rowspan=2)
        bdiv = tk.Button(r,text="/",command=lambda:self.dodaj("/",x,e1),width=size, height= int(size))
        bdiv.grid(row=3,column=4,rowspan=2)
        bcl = tk.Button(r,text="cl",command=lambda:self.dodaj("clear",x,e1),width=size*2, height= int(size/2))
        bcl.grid(row=5,column=0,columnspan=3)
        be = tk.Button(r,text="=",command=lambda:self.dodaj("=",x,e1),width=size*2, height= int(size/2))
        be.grid(row=5,column=3,columnspan=4)
        

    def dodaj(self,n,x,b):
        if 1 == isinstance(n,int):
            x.set(x.get() + str(n))
            
        elif n == "*" or  n == "-" or  n == "+" or  n == "/":
             x.set(x.get() + n)
        elif n =="clear":
            x.set("")   
        elif n == "=":
            t = b.get()
            x.set(str(eval(str(t)))) 
            
            
app = Aplication(root)

root.mainloop()