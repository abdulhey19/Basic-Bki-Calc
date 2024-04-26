from tkinter import *

window=Tk()
window.title("Beden Kitle İndeksi")
window.minsize(200,200)

def calcBki():
    weight=entryWidth.get()
    height=entryHeight.get()

    if weight=='' or height=='' or not weight.isdigit() or not height.isdigit():
        lbl3.configure(text="Please Correct Enter Weight and Height")
    else:
        result=float(weight)*10000/(float(height)*float(height))
        if result<18.5:
            lbl3.configure(text=f"Result: {result}/Zayıf")
        elif result<24.9:
            lbl3.configure(text=f"Result: {result}/normal")
        elif result<29.9:
            lbl3.configure(text=f"Result: {result}/kilolu")
        elif result<34.9:
            lbl3.configure(text=f"Result: {result}/1.Derece Obezite")
        else:
            lbl3.configure(text=f"Result: {result}/2.Derece Obezite")


#label
lbl1=Label(text="Enter Your Weight:")
lbl2=Label(text="Enter Your Height:")
lbl3=Label()

lbl1.configure(padx=10)
lbl2.configure(padx=10)
lbl3.configure(padx=10)



#entry
entryWidth=Entry(width=20)
entryHeight=Entry(width=20)




#button
btnCalculate=Button(text='Show', command=calcBki)


lbl1.pack()
entryWidth.pack()
lbl2.pack()
entryHeight.pack()
btnCalculate.pack()
lbl3.pack()
window.mainloop()