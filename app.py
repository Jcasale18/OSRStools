import tkinter as tk
import sendsms
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title('GUI')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self,width=100)
        self.entry.pack(side = 'right')
        self.send = tk.Button(self,text = 'send',command = lambda:self.sendbody(None))#Fake event parameter
        self.send.pack(side="left")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        #self.entry.bind('<Enter>',self.sendbody)

        

    def sendbody(self,event):
        values = self.entry.get()
        print(values)
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()