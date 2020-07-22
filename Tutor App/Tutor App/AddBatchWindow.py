import tkinter
import TutorAppDB

class AddBatchWindow(tkinter.Frame):

    # The constructor
    def __init__(self,root,parent,batch_id=None):
        self.root = root
        self.parent = parent
        self.batch_id = batch_id
        
        self.dialog = tkinter.Toplevel(root)
        super().__init__(self.dialog)
        
        self.dialog.protocol("WM_DELETE_WINDOW", self.handleCancel)

        diaHeight = 300
        
        self.place(width=600,height=diaHeight);
        
        xloc = (self.root.winfo_screenwidth() - 600)//2
        yloc = (self.root.winfo_screenheight() - diaHeight)//2
        self.dialog.geometry("600x" + str(diaHeight) + "+" + str(xloc) + "+" + str(yloc))
        self.dialog.resizable(0,0)

        windowTitle = "Tutor App - Add Batch Window"
        if(self.batch_id != None):
            windowTitle = "Tutor App - Udate Batch Window"
            
        self.dialog.title(windowTitle)

        self.create_ui()


    def create_ui(self):

        buttonLabel = "Add Batch"
        helpLabel = "Add New Batch"

        if(self.batch_id != None):
            buttonLabel = "Update Batch"
            helpLabel = "Update Batch"
            
        labelFont = ("Arial", "10", "bold");
        heading = tkinter.Label(self,text=helpLabel,font=labelFont,anchor="w")
        heading.place(x=15,y=15,width=400,height=25)

        self.messageLabel = tkinter.Label(self,text="Please enter the batch details",anchor="w",fg="blue")
        self.messageLabel.place(x=40,y=50,width=400,height=25)

        label = tkinter.Label(self,text="Batch Name*",anchor="w",font=labelFont)
        label.place(x=40,y=90,width=100,height=25)
        self.batchNameVar = tkinter.StringVar()
        self.batchName = tkinter.Entry(self,textvariable=self.batchNameVar)
        self.batchName.place(x=140,y=90,width=420,height=25)

        label = tkinter.Label(self,text="Description",anchor="w",font=labelFont)
        label.place(x=40,y=140,width=100,height=25)
        self.batchDesc = tkinter.Text(self,height=4)
        self.batchDesc.place(x=140,y=140,width=420)

        label = tkinter.Label(self,text="Fee*",anchor="w",font=labelFont)
        label.place(x=40,y=210,width=100,height=25)
        self.batchFeeVar = tkinter.StringVar()
        self.batchFee = tkinter.Entry(self,textvariable=self.batchFeeVar)
        self.batchFee.place(x=140,y=210,width=420,height=25)
            
        addButton = tkinter.Button(self,text=buttonLabel,font=labelFont,command=self.handleAdd)
        addButton.place(x=450,y=240,width=100,height=30)

        cancelButton = tkinter.Button(self,text="Cancel",font=labelFont,command=self.handleCancel)
        cancelButton.place(x=325,y=240,width=100,height=30)

        if(self.batch_id != None):
            db = TutorAppDB.TutorAppDB()
            batch_data = db.get_batch(self.batch_id)            
            self.batchNameVar.set(batch_data[0][0])
            self.batchDesc.insert("end-1c",batch_data[0][1])
            self.batchFeeVar.set(batch_data[0][2])
            
        
    def handleAdd(self):
        batch_name = self.batchName.get()
        batch_desc = self.batchDesc.get("1.0","end-1c");
        batch_fee = self.batchFee.get()

        if len(batch_name) == 0 or batch_name.isspace():
            tkinter.messagebox.showerror(message="Please specify a batch name")
        else:

            if len(batch_desc) == 0 or batch_desc.isspace():
                batch_desc=""

            db = TutorAppDB.TutorAppDB()
               
            if(self.batch_id == None):    
                # Save the data to the database                
                db.save_batch(batch_name, batch_desc, batch_fee)
                self.dialog.destroy()
                tkinter.messagebox.showinfo(message="Batch Saved")
            else:
                # Update the data to the database
                db.update_batch(batch_name, batch_desc, self.batch_id, batch_fee)
                tkinter.messagebox.showinfo(message="Batch Updated")
                self.dialog.destroy()                

            self.parent.manage_batches()
            

    def handleCancel(self):
        self.dialog.destroy()
        

# Do not run this code if imported in another file
if __name__ == "__main__":
    root = tkinter.Tk()
    app = AddBatchWindow(root)
    app.mainloop()
