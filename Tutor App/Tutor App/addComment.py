import tkinter
import TutorAppDB

class addComment(tkinter.Frame):

    # The constructor
    def __init__(self,root,parent,student_id=None):
        self.root = root
        self.parent = parent
        self.student_id = student_id
        
        self.dialog = tkinter.Toplevel(root)
        super().__init__(self.dialog)
        
        self.dialog.protocol("WM_DELETE_WINDOW", self.handleCancel)

        diaHeight = 300
        
        self.place(width=600,height=diaHeight);
        
        xloc = (self.root.winfo_screenwidth() - 600)//2
        yloc = (self.root.winfo_screenheight() - diaHeight)//2
        self.dialog.geometry("600x" + str(diaHeight) + "+" + str(xloc) + "+" + str(yloc))
        self.dialog.resizable(0,0)

        windowTitle = "Tutor App - Manage Attendance"
            
        self.dialog.title(windowTitle)

        self.create_ui()

    def create_ui(self):

        helpLabel = "Absent"

        labelFont = ("Arial", "10", "bold");
        heading = tkinter.Label(self,text=helpLabel,
                                font=labelFont,anchor="w", fg="red")
        heading.place(x=15,y=15,width=400,height=25)


        messageLabel = tkinter.Label(self,
                                          text="Please enter the Attendnace details :",
                                          anchor="w",fg="blue")
        messageLabel.place(x=40,y=50,width=400,height=25)

        label = tkinter.Label(self,text="Date*",anchor="w",font=labelFont)
        label.place(x=40,y=90,width=100,height=25)
        self.dateVar = tkinter.StringVar()
        self.date = tkinter.Entry(self,textvariable=self.dateVar)
        self.date.place(x=140,y=90,width=420,height=25)

        label = tkinter.Label(self,text="Reason*",anchor="w",font=labelFont)
        label.place(x=40,y=140,width=100,height=25)
        self.reason = tkinter.Text(self,height=4)
        self.reason.place(x=140,y=140,width=420)

        addButton = tkinter.Button(self,text="Submit",
                                   font=labelFont,command=self.handleAdd)
        addButton.place(x=450,y=240,width=100,height=30)

        cancelButton = tkinter.Button(self,text="Cancel",
                                      font=labelFont,
                                      command=self.handleCancel)
        cancelButton.place(x=325,y=240,width=100,height=30)

        self.val1 = tkinter.StringVar()
        self.val2 = tkinter.StringVar()

        db = TutorAppDB.TutorAppDB()
        student_data = db.get_attendnace(self.student_id)
        
        self.val1.set(student_data[0][0])   ## getting studentid from the database variable student_data
        self.val2.set(student_data[0][1])   ## getting batchid from the database variable student_data
        

    def handleAdd(self):
        a_date = self.date.get()
        a_reason = self.reason.get("1.0","end-1c");
        a_studentid = self.val1.get()
        a_batchid = self.val2.get()


        if len(a_date) == 0 or a_date.isspace():
            tkinter.messagebox.showerror(message="Please specify date.")
        else:

            if len(a_reason) == 0 or a_reason.isspace():
                a_reason=""

            db = TutorAppDB.TutorAppDB()
            db.save_attendance(a_date,a_studentid,a_batchid,a_reason)
            tkinter.messagebox.showinfo(message="Attendance Updated")
            self.dialog.destroy()

                

    def handleCancel(self):
        self.dialog.destroy()

        
# Do not run this code if imported in another file
if __name__ == "__main__":
    root = tkinter.Tk()
    app = addComment(root)
    app.mainloop()
        

        
