import tkinter
import TutorAppDB
from tkinter import messagebox
import os
from functools import partial
import AddBatchWindow

class BatchTable(tkinter.Canvas):
    # The Constructor
    def __init__(self,root):

        super().__init__(root)
        self.root = root

        self.config(background="white")
        self.config(scrollregion=(0,0,978,1900))

        self.frame = tkinter.Frame(self,background="white")
        self.frame.place(x=0,y=0,width=978,height=900)
        self.create_window(0, 0, window=self.frame, anchor="nw")    

        self.action_images = []
        self.create_ui()


    def create_ui(self):
        headingFont = ("Arial", "14", "bold");
        labelFont = ("Arial", "10", "bold");

        db = TutorAppDB.TutorAppDB()
        batch_data = db.get_active_batches()
                
        label = tkinter.Label(self.frame, text="Manage Batches",background="white",font=headingFont)        
        label.grid(row=0,column=0,columnspan=4,pady=(10,20))        

        label = tkinter.Label(self.frame, text='                 Batch Name                  ',font=labelFont)
        label.grid(row=1,column=0,padx=(15,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='                                                 Batch Description                                                 ',font=labelFont)
        label.grid(row=1,column=1,padx=(1,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='                   Actions                   ',font=labelFont)
        label.grid(row=1,column=2,padx=(1,1),pady=(0,10),columnspan=2)        
        
        filepath = os.path.join(os.path.dirname(__file__),"images/edit.gif")
        edit_image = tkinter.PhotoImage(file=filepath)
        self.action_images.append(edit_image)
        
        filepath = os.path.join(os.path.dirname(__file__),"images/delete.gif")
        delete_image = tkinter.PhotoImage(file=filepath)
        self.action_images.append(delete_image)

        # populate the frame
        for i in range(len(batch_data)):
            batch = batch_data[i]
            for j in range(len(batch)-1):
                label_text = (batch[j][:78] + '..') if len(batch[j]) > 80 else batch[j]                        
                label = tkinter.Label(self.frame, text=label_text,background="white")
                if j==0:
                    label.grid(row=i+2,column=j,padx=(15,5),pady=(0,5))
                else:                                        
                    label.grid(row=i+2,column=j,padx=(5,5),pady=(0,5))
            
            button = tkinter.Button(self.frame,
                                    image=edit_image,
                                    relief="flat",
                                    background="white",
                                    command= partial(self.edit_batch,batch[len(batch)-1],i))
            button.grid(row=i+2,column=len(batch)-1,sticky="e",padx=(0,15))

            button = tkinter.Button(self.frame, image=delete_image, relief="flat",background="white",
                                            command= partial(self.delete_batch,batch[len(batch)-1],i))
            button.grid(row=i+2,column=len(batch),sticky="w")
        
    def edit_batch(self,batch_id,row):
        print("edit_batch",batch_id,row)

        # Open the batch dialog in edit mode
        print("Opening edit batch")
        addWin = AddBatchWindow.AddBatchWindow(self.root,self.root,batch_id)        


    def delete_batch(self,batch_id,row):
        print("delete_batch",batch_id,row)
        
        # Get an user confirmation for the delete
        response = tkinter.messagebox.askquestion(message="Do you really want to delete the batch?")
        if response == "yes":
            # If the user confirms delete exeute the query
            db = TutorAppDB.TutorAppDB()
            db.deactvate_batch(batch_id)

            # refesh the view
            self.root.manage_batches()
        
