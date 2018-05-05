from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master,cnf={'borderwidth':5})
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self,text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()

app = Application()
app.master.title('Hello World')
app.master.maxsize(500,400)
app.master.minsize(300,200)
app.mainloop()