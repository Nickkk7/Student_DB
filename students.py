from tkinter import *
import  tkinter
#from tkinter import messagebox
import pymysql

window = tkinter.Tk()

window.geometry("750x450")

L = Label(window, text = "Enter Student Id",font=('arial',30), fg= 'blue' )
L.grid(row=0, column=0)
E = Entry(window, bd=5 , width = 50)
E.grid(row=0, column=1)

L1 = Label(window, text = "Enter Student Name",font=('arial',30), fg= 'blue' )
L1.grid(row=1, column=0)
E1 = Entry(window, bd=5 , width = 50)
E1.grid(row=1, column=1)

L2 = Label(window, text = "Enter Student Address",font=('arial',30), fg= 'blue' )
L2.grid(row=2, column=0)
E2 = Entry(window, bd=5 , width = 50)
E2.grid(row=2, column=1)



def myButtonEvent(selection):
    print("Student id is  : ",E.get())
    print("Student Name is  : ",E1.get())
    print("Student address is  : ",E2.get())

    id=E.get()
    name=E1.get()
    address=E2.get()

    if selection in ("Insert"):
        con = pymysql.connect("localhost", "root", "root",  "test")
        cur = con.cursor()
     #cur.execute("select version()")
    #data = cur.fetchone()
    #print("my Database version" , data)

        query = "create table IF NOT EXISTS student (id INT NOT NULL, \
                                                 name char(30) ,\
                                                 address char(20))"

        cur.execute(query)
        con.commit()
        print(" table student cerated successfully")
        '''except Error as e:
        rint("Error occured at database table creation",e)
        con.rollback()
        con.close() '''

        insQuery="insert into student (id,name,address) \
            values('%s','%s','%s')"%(id,name,address)

        try:
            cur.execute(insQuery)
            con.commit()
            print("student saved to B table",id,",",name,",",address)

        except :
            print("Error occured at database data insrtion")
            con.rollback()
            con.close()
    elif selection in ("Update"):
        try:
            query = "update student set name='%s'" % (name) + ",address='%s'" \
                  % (address) + "where id = '%s' " % (id)
            con = pymysql.connect("localhost", "root", "root", "test")
            cur = con.cursor()
            cur.execute (query)
            con.commit()
            con.close()
            print("student updated successfully", id)
        except :
            print("error occured at data base data updation")
            con.rollback()
            con.close()

    elif selection in ("Delete"):
        try:
            query = "Delete from student  where id = '%s'  AND name = '%s'"%(id,name)
            con = pymysql.connect("localhost", "root", "root", "test")
            cur = con.cursor()
            cur.execute (query)
            con.commit()
            con.close()
            print("student deletion successfully", id)
        except :
            print("error occured at data base data deletion")
            con.rollback()
            con.close()

    else :
        try:
            query = "select * from student where id='%s' "%(id)
            con = pymysql.connect("localhost", "root", "root", "test")
            cur = con.cursor()
            cur.execute(query)

            rows = cur.fetchall()
            address1 = ''
            name1 = ''
            id1 = ''
            for row in rows:
                id1 = row[0]
                name1 = row[1]
                address1 = row[2]

            E.delete(0, END)
            E1.delete(0, END)
            E2.delete(0, END)

            E.insert(0, id1)
            E1.insert(0, name1)
            E2.insert(0, address1)

            con.close()
            print("stuent selection done successfully",id)
        except:
            print("error occured at selection of database")
            con.close()








B1 = tkinter.Button(text='Insert', fg='black' ,bg='orange',
                    font=('ar ial',20,'bold'),command= lambda : myButtonEvent('Insert'))
B1.grid(row=5, column=0)

B2 = tkinter.Button(text='Update', fg='black', bg='yellow',
                    font=('arial',20,'bold', ), command = lambda : myButtonEvent('Update'))
B2.grid(row=5, column=1)


B3 = tkinter.Button(text='Delete', fg='red', bg='white',
                    font=('arial',20,'bold'), command= lambda:myButtonEvent('Delete'))
B3.grid(row=6, column=0)


B4 = tkinter.Button(text='Select', fg='yellow', bg='blue',
                    font=('arial',20,'bold'), command=lambda:myButtonEvent('Select'))
B4.grid(row=6, column=1)

window.mainloop()