from tkinter import *
from tkinter import ttk
main =Tk()
main.title("Weight Conversion")
main.geometry("500x300")

def conversion():
    entry_value = entry1.get()
    try:
        gram = round(float(entry1.get())*1000,2)
        label_5 = ttk.Label(main, text=gram, font="Times 15").place(x =30 ,y =100)
        pound = round(float(entry1.get())*2.20462,2)
        label_6 = ttk.Label(main, text=pound, font="Times 15").place(x =220 ,y =100)
        ounce = round(float(entry1.get())*35.274,2)
        label_7 = ttk.Label(main, text=ounce, font="Times 15").place(x =400 ,y =100)
    except:
        print("Vui lòng nhập vào kiểu số")
    print(gram)


label_1 = ttk.Label(main, text = "Nhập vào kg:" ,font="Times 15 bold").place(x = 20,y = 20)  
entry1 = ttk.Entry(main)
entry1.place(x = 140, y = 25 , width=300, height=20)  
buton1 = ttk.Button(main, text="Conversion", command=conversion).place(x=220, y = 50)
label_2 = ttk.Label(main, text="Gram" , font="Times 15 bold").place(x =30 ,y =80)
label_3 = ttk.Label(main, text="Pound" , font="Times 15 bold").place(x =220 ,y =80)
label_4 = ttk.Label(main, text="Ounce" , font="Times 15 bold").place(x =400 ,y =80)




main.mainloop()