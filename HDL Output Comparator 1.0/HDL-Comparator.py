from tkinter import *
import time

root = Tk()

root.geometry("450x200")
root.title("HDL Output Comparator 1.0")

try:
    root.iconbitmap("letter-h-16.ico")
except:
    pass

def cmplbb():
    global cmpinde
    cmpinde = strlname.get()
    cmpin.delete(0,END)
        
    cmplb.config(text="Please enter your OUT file here. (Include file extention)")
    nxtsec1.config(command=outlbb, text = "Calculate Results")
    

def outlbb():
    global outin
    global file1D
    global file2D
    outin = strlname.get()
    print(cmpinde)
    print(outin)
    cmpin.delete(0,END)
    showdesc.pack(side="left")

    file1 = open(cmpinde)
    file1D = file1.readlines()
    file2 = open(outin)
    file2D = file2.readlines()
    count = 0
    nxtsec1.config(state = DISABLED, text = "Calculation Complete; Please refer to the details below")
    if file1D == file2D:
        Result.config(text="Files are a MATCH.", fg = "Green")
        Filenames.config(text=cmpinde + " == " + outin)

            
        
    else:
        Result.config(text="Files are NOT a match", fg = "Red")
        Filenames.config(text=cmpinde + " != " + outin)
        
def filedetails():
    count = 0
    global file1D
    global file2D
    CMP.pack(side="bottom")
    CMP.insert(INSERT, file2D)
    CMP2.pack(side="bottom")
    CMP2.insert(INSERT, file1D)
    root.geometry("700x650")
    
    showdesc.config(text = "Hide File Details", command=filedetailshide)
    
def filedetailshide():
    root.geometry("450x200")
    CMP.delete(1.0,END)
    CMP2.delete(1.0,END)
    CMP.pack_forget()
    CMP2.pack_forget()
    showdesc.config(text = "Show File Details", command=filedetails)
    




strlname = StringVar()


label = Label(root, text = "HDL Output Comparator 1.0")
cmplb = Label(root, text= "Please enter your CMP file here. (Include file extention)")
cmpin = Entry(root, textvariable = strlname, bg = "light yellow")
nxtsec1 = Button(root, text = "Next Section", command=cmplbb)
Detail = Label(root, text="Result:")
Result = Label(root, text="UNKNOWN", fg = "Grey")
Filenames = Label(root,text="")
showdesc = Button(root, text = "Show File Details", command=filedetails)
CMP = Text(root, width = 70, height = 10)
CMP2 = Text(root, width = 70, height = 10)


label.config(font=('Helvetica bold',20))
Result.config(font=('Helvetica bold',15))
label.pack()
cmplb.pack()
cmpin.pack()
nxtsec1.pack()
Detail.pack()
Result.pack()
Filenames.pack()
showdesc.pack_forget()
CMP.pack_forget()
CMP2.pack_forget()


root.mainloop()
