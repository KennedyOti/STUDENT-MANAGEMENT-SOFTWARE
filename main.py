from tkinter import *
from tkinter import ttk
import pymysql


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,font=("sans-serif", 40, "bold"), bg="lavender", fg="black")
        title.pack(side=TOP, fill=X)
        # =============all variables===================
        self.adm_var = StringVar()
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.gender_var = StringVar()
        self.age_var = StringVar()
        self.class_var = StringVar()
        self.parent_var = StringVar()

        self.search_by =StringVar()
        self.search_text =StringVar()

        # ===================== Manage Frame================================

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#57e7ec", border=round(7))
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        mtitle = Label(Manage_Frame, text="Manage Students", bg='#57e7ec', fg='black',
                       font=("times new roman", 20, "bold"))
        mtitle.grid(row=0, columnspan=2, pady=20)

        # ==============ADMISSION NUMBER======================================
        lbl_admn = Label(Manage_Frame, text="Admission Number", bg="#57e7ec", fg="black",
                         font=("times new roman", 10, "bold"))
        lbl_admn.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        admn_text = Entry(Manage_Frame, textvariable=self.adm_var, font=("times new roman", '15', "bold"), bd=5,
                          relief=GROOVE)
        admn_text.grid(row=1, column=1, pady=10, padx=25, sticky="w")

        # =============FIRST NAME=============================================
        lbl_sfname = Label(Manage_Frame, text="First Name", bg="#57e7ec", fg="black",
                           font=("times new roman", 10, "bold"))
        lbl_sfname.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        sfname_text = Entry(Manage_Frame, textvariable=self.fname_var, font=("times new roman", '15', "bold"), bd=5,
                            relief=GROOVE)
        sfname_text.grid(row=2, column=1, pady=10, padx=25, sticky="w")

        # =============LAST NAME=============================================
        lbl_slname = Label(Manage_Frame, text="Last Name", bg="#57e7ec", fg="black",
                           font=("times new roman", 10, "bold"))
        lbl_slname.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        slname_text = Entry(Manage_Frame, textvariable=self.lname_var, font=("times new roman", '15', "bold"), bd=5,
                            relief=GROOVE)
        slname_text.grid(row=3, column=1, pady=10, padx=25, sticky="w")

        # =============STUDENT GENDER===========================================
        lbl_gender = Label(Manage_Frame, text="Gender", bg="#57e7ec", fg="black", font=("times new roman", 10, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 14, "bold"),
                                    state='readonly')
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, pady=10, padx=25, sticky="w")

        # =============STUDENT AGE===========================================
        lbl_age = Label(Manage_Frame, text="Student Age", bg="#57e7ec", fg="black",
                        font=("times new roman", 10, "bold"))
        lbl_age.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        age_text = Entry(Manage_Frame, textvariable=self.age_var, font=("times new roman", '15', "bold"), bd=5,
                         relief=GROOVE)
        age_text.grid(row=5, column=1, pady=10, padx=25, sticky="w")

        # =============STUDENT CLASS===========================================
        lbl_class = Label(Manage_Frame, text="Class/Form", bg="#57e7ec", fg="black",
                          font=("times new roman", 10, "bold"), )
        lbl_class.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        class_text = Entry(Manage_Frame, textvariable=self.class_var, font=("times new roman", '15', "bold"), bd=5,
                           relief=GROOVE)
        class_text.grid(row=6, column=1, pady=10, padx=25, sticky="w")

        # =============STUDENT PARENT===========================================
        lbl_parent = Label(Manage_Frame, text="Parent Name", bg="#57e7ec", fg="black",
                           font=("times new roman", 10, "bold"))
        lbl_parent.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        parent_text = Entry(Manage_Frame, textvariable=self.parent_var, font=("times new roman", '15', "bold"), bd=5,
                            relief=GROOVE)
        parent_text.grid(row=7, column=1, pady=10, padx=25, sticky="w")

        # ===========Button Frames===============================================
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="#57e7ec")
        btn_Frame.place(x=5, y=500, width=430)

        addButton = Button(btn_Frame, text='Add', width=10, command=self.add_students).grid(row=0, column=0, padx=10,
                                                                                            pady=10, )
        resetButton = Button(btn_Frame, text='Reset', width=10, command=self.clear).grid(row=0, column=1, padx=10,
                                                                                         pady=10)
        updateButton = Button(btn_Frame, text='Update', width=10, command=self.update_data).grid(row=0, column=2,
                                                                                                 padx=10, pady=10)
        deleteButton = Button(btn_Frame, text='Delete', width=10, command=self.delete_data).grid(row=0, column=3, padx=10, pady=10)

        # ====================== Details Frame===================================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#338588")
        Detail_Frame.place(x=500, y=100, width=840, height=580)

        # =====================combo search======================================
        lbl_search = Label(Detail_Frame, text='Search By', bg='#338588', fg='white',font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')
        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font=("times new roman", 14, "bold"), state='readonly')
        combo_search['values'] = ("STUDENT_ID", "FIRST_NAME", "CLASS")
        combo_search.grid(row=0, column=1, pady=10, padx=25, sticky="w")

        # ====================search entry======================================
        search_text = Entry(Detail_Frame, textvariable=self.search_text, width=15, font=("times new roman", '10', "bold"), bd=5, relief=GROOVE)
        search_text.grid(row=0, column=2, pady=10, padx=25, sticky="w")

        # ====================search button=====================================
        searchButton = Button(Detail_Frame, text='Search', width=10, command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showButton = Button(Detail_Frame, text='Show All', width=10).grid(row=0, column=4, padx=10, pady=10)

        # ===================Table Frame========================================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="white")
        Table_Frame.place(x=10, y=70, width=820, height=500)

        scrol_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scrol_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_Table = ttk.Treeview(Table_Frame, columns=(
        "Admission Number", "First Name", "LastName", "Gender", "Age", "Class", "Parent"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set, )

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_x.config(command=self.Student_Table.xview)
        scrol_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading("Admission Number", text="Admission Number", )
        self.Student_Table.heading("First Name", text="First Name")
        self.Student_Table.heading("LastName", text="Last Name")
        self.Student_Table.heading("Gender", text="Gender")
        self.Student_Table.heading("Age", text="Age")
        self.Student_Table.heading("Class", text="Class")
        self.Student_Table.heading("Parent", text="Parent")

        self.Student_Table['show'] = 'headings'
        self.Student_Table.column("Admission Number", width=20)
        self.Student_Table.column("First Name", width=25)
        self.Student_Table.column("LastName", width=25)
        self.Student_Table.column("Gender", width=25)
        self.Student_Table.column("Age", width=15)
        self.Student_Table.column("Class", width=10)
        self.Student_Table.column("Parent", width=40)
        self.Student_Table.pack(fill=BOTH, expand=1)
        self.Student_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentspy_db")
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (
            self.adm_var.get(),
            self.fname_var.get(),
            self.lname_var.get(),
            self.gender_var.get(),
            self.age_var.get(),
            self.class_var.get(),
            self.parent_var.get()

        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    # fetch data functuin

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentspy_db")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('', END, values=row)
            con.commit()
        con.close()

    # data reset function
    def clear(self):
        self.adm_var.set(""),
        self.fname_var.set(""),
        self.lname_var.set(""),
        self.gender_var.set(""),
        self.age_var.set(""),
        self.class_var.set(""),
        self.parent_var.set("")

    # the get cursor function which allows for highlighting of the data to updated or deleted
    def get_cursor(self, ev):
        cursor_row = self.Student_Table.focus()
        contents = self.Student_Table.item(cursor_row)
        row = contents['values']
        print(row)

        self.adm_var.set(row[0]),
        self.fname_var.set(row[1]),
        self.lname_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.age_var.set(row[4]),
        self.class_var.set(row[5]),
        self.parent_var.set(row[6])

    # data update function
    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentspy_db")
        cur = con.cursor()
        cur.execute("update students set first_name=%s,last_name=%s,gender=%s,age=%s,class=%s,parent=%s where student_id=%s", (
                self.fname_var.get(),
                self.lname_var.get(),
                self.gender_var.get(),
                self.age_var.get(),
                self.class_var.get(),
                self.parent_var.get(),
                self.adm_var.get()
            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    # the delete data function
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentspy_db")
        cur = con.cursor()
        cur.execute("delete from students where student_id=%s", self.adm_var.get())

        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    # the search data function
    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="studentspy_db")
        cur = con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('', END, values=row)
            con.commit()
        con.close()




root = Tk()
ob = Student(root)
root.mainloop()
