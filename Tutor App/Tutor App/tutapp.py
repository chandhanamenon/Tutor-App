import tkinter
import MainAppWindow
class tutapp(tkinter.Frame):

    # The constructor for the Login Window
    def __init__(self,root):
        super().__init__(root)
        self.root = root        

        xloc = (root.winfo_screenwidth() - 500)//2;
        yloc = (root.winfo_screenheight() - 280)//2;

        self.root.geometry("500x280+" + str(xloc) + "+" + str(yloc)) # "WxH+x+y"
        self.root.resizable(0,0)
        self.root.title("Tutor App - Login")

        self.create_ui()
        

    # The method to create the UI for the login window
    def create_ui(self):

        self.place(width=500,height=280);
        
        headingFont = ("Arial", "14", "bold");
        labelFont = ("Arial", "10", "bold");
        heading = tkinter.Label(self,text="Welcome to the Tutor App",font=headingFont)
        heading.place(x=50,y=15,width=400,height=30)

        self.messageLabel = tkinter.Label(self,text="Please enter your credentails to login",anchor="w",fg="blue")
        self.messageLabel.place(x=40,y=50,width=400,height=25)
        
        label = tkinter.Label(self,text="User Id",anchor="w",font=labelFont)
        label.place(x=40,y=90,width=100,height=25)
        self.useridText = tkinter.Entry(self)
        self.useridText.place(x=140,y=90,width=320,height=25)

        label = tkinter.Label(self,text="Password",anchor="w",font=labelFont)
        label.place(x=40,y=140,width=100,height=25)
        self.passwordVar = tkinter.StringVar()
        self.passwordText = tkinter.Entry(self,show="*",textvariable=self.passwordVar)
        self.passwordText.place(x=140,y=140,width=320,height=25)

        loginButton = tkinter.Button(self,text="Login",font=labelFont,command=self.handleLogin)
        loginButton.place(x=350,y=190,width=75,height=30)

        cancelButton = tkinter.Button(self,text="Cancel",font=labelFont,command=self.handleCancel)
        cancelButton.place(x=250,y=190,width=75,height=30)

        bottomLabel = tkinter.Label(self,text="App developed by SGIT Academy - Copyright 2020")
        bottomLabel.place(x=40,y=250,width=420,height=25)
        

    def handleLogin(self):
        user_id = self.useridText.get()
        password = self.passwordText.get()
        
        if len(user_id) == 0 or user_id.isspace():
            self.showError("Please enter a valid user id")
        elif len(password) == 0 or password.isspace():
            self.showError("Please enter a valid password")
        else:
            if(user_id == "testuser" and password=="testpwd"):
                self.destroy()
                mainWin = MainAppWindow.MainAppWindow(self.root)                
                self.root.update()
            else:
                self.showError("Invalid credentials entered. Please try again!")
                self.passwordVar.set("")

    def handleCancel(self):
        self.root.destroy()

    # The method to display an error message
    def showError(self,message):
        self.messageLabel["fg"] = "red"
        self.messageLabel["text"] = message

# Do not run this code if imported in another file
if __name__ == "__main__":
    root = tkinter.Tk()
    
    app = tutapp(root)
    app.mainloop()
