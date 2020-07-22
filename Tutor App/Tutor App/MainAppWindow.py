import tkinter
from tkinter import messagebox
import os
import AddBatchWindow
import BatchTable
import AddStudentWindow
import StudentTable
import attendanceTable
import FeeTable


class MainAppWindow(tkinter.Frame):

    # The constructor for the main window
    def __init__(self,root):

        super().__init__(root)
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.file_exit)

        self.config(background="white")

        self.place(width=1000,height=600)

        self.toolbar_images = []
        
        xloc = (self.root.winfo_screenwidth() - 1000)//2
        yloc = 50;
        self.root.geometry("1000x600+" + str(xloc) + "+" + str(yloc))
        self.root.resizable(0,0)
        self.root.title("Tutor App - Main Window")

        self.create_menubar()

        self.create_toolbar()

        self.create_statusbar()

        self.current_table = self.manage_students()
        

    # Method that creates the menubar for the application
    def create_menubar(self):

        menubar = tkinter.Menu(self.root)
        self.root["menu"] = menubar

        fileMenu = tkinter.Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Add Batch",command=self.file_add_batch,underline=4)
        fileMenu.add_command(label="Add Student",command=self.file_add_student,underline=4)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit",command=self.file_exit,underline=1,accelerator="Ctrl+X")
        self.root.bind("<Control-x>",self.file_exit)
        menubar.add_cascade(label="File",menu=fileMenu,underline=0)

        viewMenu = tkinter.Menu(menubar, tearoff=0)
        viewMenu.add_command(label="Batches",command=self.manage_batches,underline=0,accelerator="Ctrl+B")
        self.root.bind("<Control-b>",self.manage_batches)
        viewMenu.add_command(label="Students",command=self.manage_students,underline=0,accelerator="Ctrl+S")
        self.root.bind("<Control-s>",self.manage_students)
        viewMenu.add_separator()
        viewMenu.add_command(label="Fees",command=self.manage_fees,underline=0,accelerator="Ctrl+F")
        self.root.bind("<Control-f>",self.manage_fees)
        viewMenu.add_command(label="Attendance",command=self.manage_attendance,underline=0,accelerator="Ctrl+A")
        self.root.bind("<Control-a>",self.manage_attendance)
        menubar.add_cascade(label="Manage",menu=viewMenu,underline=0)



    # The method that creates the toolbar
    def create_toolbar(self):

        toolbar = tkinter.Frame(self)

        filepath = os.path.join(os.path.dirname(__file__),"images/batches.gif")
        image = tkinter.PhotoImage(file=filepath)
        self.toolbar_images.append(image)
        button = tkinter.Button(toolbar, image=image,command=self.manage_batches)
        button.grid(row=0,column=0,padx=(5,0))
        
        filepath = os.path.join(os.path.dirname(__file__),"images/students.gif")
        image = tkinter.PhotoImage(file=filepath)
        self.toolbar_images.append(image)
        button = tkinter.Button(toolbar, image=image,command=self.manage_students)
        button.grid(row=0,column=1)

        filepath = os.path.join(os.path.dirname(__file__),"images/fees.gif")
        image = tkinter.PhotoImage(file=filepath)
        self.toolbar_images.append(image)
        button = tkinter.Button(toolbar, image=image,command=self.manage_fees)
        button.grid(row=0,column=2,padx=(5,0))
        
        filepath = os.path.join(os.path.dirname(__file__),"images/attend.gif")
        image = tkinter.PhotoImage(file=filepath)
        self.toolbar_images.append(image)
        button = tkinter.Button(toolbar, image=image,command=self.manage_attendance)
        button.grid(row=0,column=3)

        
        filepath = os.path.join(os.path.dirname(__file__),"images/exit.gif")
        image = tkinter.PhotoImage(file=filepath)
        self.toolbar_images.append(image)
        button = tkinter.Button(toolbar, image=image,command=self.file_exit)
        button.grid(row=0,column=4,padx=(5,0))

        toolbar.place(x=0,y=0,width=1000,height=25)


    # Method to create the status bar
    def create_statusbar(self):
        self.statusbar = tkinter.Label(self,text="Ready...",anchor="w",relief="sunken")
        self.statusbar.place(x=0,y=575,width=1000,height=25)        

    # The Event Handlers
    def file_add_batch(self):
        addWin = AddBatchWindow.AddBatchWindow(self.root,self)

    def file_add_student(self):
        addstudent = AddStudentWindow.AddStudentWindow(self.root,self)

    def file_exit(self, *ignore):
        response = tkinter.messagebox.askquestion(message="Do you really want to exit the application?")
        if response == "yes":
            self.root.destroy()

    def manage_batches(self, *ignore):

        if self.current_table != None:
            self.current_table.destroy()

        self.current_table = BatchTable.BatchTable(self)
        self.current_table.place(x=0,y=26,width=978,height=550)
        
        self.vScrollbar = tkinter.Scrollbar(self,orient=tkinter.VERTICAL,command=self.current_table.yview)
        self.vScrollbar.place(x=975,y=26,width=22,height=550)

        self.current_table.config(yscrollcommand=self.vScrollbar.set)
        

    def manage_students(self, *ignore):

        self.current_table = StudentTable.StudentTable(self)
        self.current_table.place(x=0,y=26,width=978,height=550)
        
        self.vScrollbar = tkinter.Scrollbar(self,orient=tkinter.VERTICAL,command=self.current_table.yview)
        self.vScrollbar.place(x=975,y=26,width=22,height=550)

        self.current_table.config(yscrollcommand=self.vScrollbar.set)

    def manage_fees(self, *ignore):
        if self.current_table != None:
            self.current_table.destroy()

        self.current_table = FeeTable.FeeTable(self)
        self.current_table.place(x=0,y=26,width=978,height=550)
        
        self.vScrollbar = tkinter.Scrollbar(self,orient=tkinter.VERTICAL,command=self.current_table.yview)
        self.vScrollbar.place(x=975,y=26,width=22,height=550)

        self.current_table.config(yscrollcommand=self.vScrollbar.set)

    def manage_attendance(self, *ignore):
        
        if self.current_table != None:
            self.current_table.destroy()

        self.current_table = attendanceTable.attendanceTable(self)
        self.current_table.place(x=0,y=26,width=978,height=550)
        
        self.vScrollbar = tkinter.Scrollbar(self,orient=tkinter.VERTICAL,command=self.current_table.yview)
        self.vScrollbar.place(x=975,y=26,width=22,height=550)

        self.current_table.config(yscrollcommand=self.vScrollbar.set)
