from tkinter import *
from tkinter import messagebox
import random
import datetime
from datetime import date

tk = Tk()

tk.geometry("1500x1000")
tk.minsize(1500,1000)

tk.config(bg="white")

def login():
    global e1
    global e2
    e1_data = e1.get()
    e2_data = e2.get()
    if e1_data == 'user':
        if e2_data == '123':

            root = Tk()
            root.geometry("1500x1000")
            root.minsize(1500, 1000)
            root.config(bg="white")

            r = random.randint(1111, 9999)

            def billing():
                global r
                r = random.randint(1111, 9999)
                noi = (int(numberofitem.get())) * (int(costofeachitem.get()))
                x1 = f"\nbilling Number : {r}"
                x2 = f"\nCustomer Name : {costmername.get()}        Date : {d}|{m}|{y}"
                x3 = f"\nName of the item : {nameofitem.get()}      Time : {t}"
                x4 = f"\nNumber of item : {numberofitem.get()}          Day : {thisday}"
                x5 = f"\nCost of each item : {costofeachitem.get()}"
                x6 = f"\nTotal : {noi}"
                x7 = f"\n--------------------------------------------------------------------------------------------------"
                billing_data = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x7
                filex = open("data.txt", "a")
                filex.writelines(billing_data)
                filex.close()
                r = random.randint(1111, 9999)
                bill_number12.config(text=f"{r}")
                nameofitem.delete(0, 'end')
                costmername.delete(0, 'end')
                numberofitem.delete(0, 'end')
                costofeachitem.delete(0, 'end')
                totalcost.config(text="Total : Rs0")
                c = datetime.datetime.now()
                tc = c.strftime("%H:%M:%S")
                time.config(text=f"Time: {tc}")

            def add():
                noi = (int(numberofitem.get())) * (int(costofeachitem.get()))
                totalcost.config(text=f"Total : Rs{noi}")

            def delete():
                nameofitem.delete(0, 'end')
                costmername.delete(0, 'end')
                numberofitem.delete(0, 'end')
                costofeachitem.delete(0, 'end')

            title = Label(root, text="Vending Machine Managing System", font="helivetica 50", width=1500, bg="orange",fg="white").pack()

            bill_number = Label(root, text="Bill Number:", font="helivetivca 25 bold", bg="white").place(x=100,y=150)
            costmer_name = Label(root, text="Customer Name:", font="helivetivca 25 bold", bg="white").place(x=100,y=250)
            name_of_item = Label(root, text="Name of the item:", font="helivetivca 25 bold", bg="white").place(x=100,y=350)
            number_of_item = Label(root, text="Number of item:", font="helivetivca 25 bold", bg="white").place(x=100,y=450)
            cost_of_each_item = Label(root, text="Cost of each item:", font="helivetivca 25 bold", bg="white").place(x=100, y=550)

            bill_number12 = Label(root, text=f"{r}", font="helivetivca 25 bold", bg="white")
            bill_number12.focus_set()
            bill_number12.place(x=500, y=150)
            costmername = Entry(root, font="helivetivca 25 bold", bg="white")
            costmername.focus_set()
            costmername.place(x=500, y=250)

            nameofitem = Entry(root, font="helivetivca 25 bold", bg="white")
            nameofitem.focus_set()
            nameofitem.place(x=500, y=350)

            numberofitem = Entry(root, font="helivetivca 25 bold", bg="white")
            numberofitem.focus_set()
            numberofitem.place(x=500, y=450)
            costofeachitem = Entry(root, font="helivetivca 25 bold", bg="white")
            costofeachitem.focus_set()
            costofeachitem.place(x=500, y=550)

            totalcost = Label(root, text="Total : Rs0", font="helivetivca 25 bold", bg="white")
            totalcost.focus_set()
            totalcost.place(x=1000, y=150)

            bill = Button(root, text="Bill", font="helivetica 30 bold", bg="orange", fg="white", width=10,command=billing).place(x=710, y=650)
            Add = Button(root, text="Total", font="helivetica 30 bold", bg="orange", fg="white", width=10,command=add).place(x=450, y=650)
            reset = Button(root, text="Reset", font="helivetica 30 bold", bg="orange", fg="white", width=10,command=delete).place(x=190, y=650)

            x = datetime.datetime.now()
            y = x.strftime("%y")
            m = x.strftime("%m")
            d = x.strftime("%d")

            t = x.strftime("%H:%M:%S")

            date1 = Label(root, text=f"Date: {d}|{m}|{y}", font="helivetica 30", bg="white")
            date1.focus_set()
            date1.place(x=1000, y=250)
            time = Label(root, text=f"Time: {t}", font="helivetica 30", bg="white")
            time.focus_set()
            time.place(x=1000, y=350)

            today = date.today()

            if today.weekday() == 0:
                thisday = "Monday"
            elif today.weekday() == 1:
                thisday = "Tuesday"
            elif today.weekday() == 2:
                thisday = "Wednesday"
            elif today.weekday() == 3:
                thisday = "Thursday"
            elif today.weekday() == 4:
                thisday = "Friday"
            elif today.weekday() == 5:
                thisday = "Saturday"
            else:
                thisday = "Sunday"

            day = Label(root, text=f"Day: {thisday}", font="helivetica 30", bg="white")
            day.focus_set()
            day.place(x=1000, y=450)

            root.mainloop()
        else:
            messagebox.showerror("!?","Wrong Password")
    else:
        messagebox.showerror("!?", "Wrong User Name")


l1 = Label(tk,text="Log-In",font="helivetica 50 bold",bg="sky blue",width=400,fg="white").pack()

l2 = Label(tk,text="User Name:",font="helivetica 40",bg="white").place(x=300,y=200)
l3 = Label(tk,text="Password:",font="helivetica 40",bg="white").place(x=300,y=300)

e1 = Entry(tk,font="helivetica 40",bg="white")
e1.place(x=650,y=200)
e1.focus_set()
e2 = Entry(tk,font="helivetica 40",bg="white")
e2.place(x=650,y=300)
e2.focus_set()

b1 = Button(tk,text="Continue",font="helivetica 35 bold",bg="sky blue",fg="white",command=login).place(x=600,y=600)

tk.mainloop()
