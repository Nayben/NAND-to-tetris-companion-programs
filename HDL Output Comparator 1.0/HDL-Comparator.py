from tkinter import *
import time

root = Tk()

root.geometry("450x200")
root.title("HDL Output Comparator 1.0")
#Trying to find the icon for the program, but continuing as normal if not found
try:
    root.iconbitmap("letter-h-16.ico")
except:
    pass
#First button press | Collects first file input, changes some labels
def cmplbb():
    global cmpinde
    cmpinde = strlname.get()
    cmpin.delete(0,END)
        
    cmplb.config(text="Please enter your OUT file here. (Include file extention)")
    nxtsec1.config(command=outlbb, text = "Calculate Results")
    
#Second button press | Collects second file input, checks if the file1 and file2 are equal to eachother and outputs accordingly. Makes the Show File Details button visible
def outlbb():
    global outin
    global file1D
    global file2D
    outin = strlname.get()
    cmpin.delete(0,END)
    showdesc.pack(side="left")
    file1 = open(cmpinde)
    file1D = file1.readlines()
    file2 = open(outin)
    file2D = file2.readlines()
    nxtsec1.config(state = DISABLED, text = "Calculation Complete; Please refer to the details below")
    if file1D == file2D:
        Result.config(text="Files are a MATCH.", fg = "Green")
        Filenames.config(text=cmpinde + " == " + outin)

            
        
    else:
        Result.config(text="Files are NOT a match", fg = "Red")
        Filenames.config(text=cmpinde + " != " + outin)
#Show File Details button | Puts contents of file1 and file2 in the Text boxes and makes them visible for comparing. Changes size of window.       
def filedetails():
    global file1D
    global file2D
    CMP.pack(side="bottom")
    CMP.insert(INSERT, file2D)
    CMP2.pack(side="bottom")
    CMP2.insert(INSERT, file1D)
    root.geometry("700x650")
    
    showdesc.config(text = "Hide File Details", command=filedetailshide)
#Hide File Details button | Hides text boxes and changes the size of window back to normal
def filedetailshide():
    root.geometry("450x200")
    CMP.delete(1.0,END)
    CMP2.delete(1.0,END)
    CMP.pack_forget()
    CMP2.pack_forget()
    showdesc.config(text = "Show File Details", command=filedetails)
    




strlname = StringVar()

#Visual components of the GUI
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

#packing everything to make visible in the GUI
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
