from tkinter import *
import tkinter.font as tkFont
from Scraper import get_pricedata
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title('GUI')
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.fontstyle = tkFont.Font(family = 'times',size=30)
        self.label = Label(self,justify = CENTER ,padx = 10,pady=10,bg = "black",fg = "Yellow",text = "Type in an item",font = self.fontstyle).pack(side="top",fill = X)
        self.entry = Entry(self,width=180)
        self.entry.pack(side = 'left',pady=10)
        self.send = Button(self,text = 'send',command = lambda:self.sendbody(None))#Fake event parameter
        self.send.pack(side="left",pady=10)
        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="right",pady=10)
        root.bind("<Return>",lambda event:self.sendbody(None))
        
    def sendbody(self,event):
        self.values = self.entry.get()
        self.ID = self.get_ID(self.values)
        self.data = get_pricedata(self.ID)
        return self.data
        
    def get_ID(self,value):
        with open('tradeableitems.txt','r') as file:
            for row in file:
                if row.split(',')[1].replace('\n','').lower().strip() == value:
                    ID = row.split(',')[0]
                    return ID
                    
root = Tk()
app = Application(master=root)
app.master.minsize(width = '1000',height = '750')
img = PhotoImage(file = "connectlost.gif")
canvas = Canvas(root,width = 1000,height = 220)
canvas.pack(side = 'bottom', fill = X)
canvas.create_image(1000,100,anchor = E ,image = img)
app.mainloop()