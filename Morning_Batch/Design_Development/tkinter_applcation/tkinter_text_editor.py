from tkinter import *
from tkinter import filedialog

#Fonts############################
def fontHelvetica():
	global text
	text.config(font="Helvetica")

def fontArial():
	global text
	text.config(font="Arial")

def fontTNR():
	global text
	text.config(font=("Times New Roman",))

def fontGothic():
	global text
	text.config(font="Gothic")

#Hotkeys
def newFileHK(self):
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

def saveFileHK(self):
	global filename
	if filename == None:
		saveAs(self)
	else:
		t = text.get(0.0, END)
		f = open(filename, "w")
		f.write(t)
		f.close()

def saveAsHK(self):
	f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title ="UPS", message="Could not save file")

def openFileHK(self):
	f = filedialog.askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

#Loops commands
filename = None

def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

def saveFile():
	global filename
	if filename == None:
		saveAs(self)
	else:
		t = text.get(0.0, END)
		f = open(filename, "w")
		f.write(t)
		f.close()

def saveAs():
	f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title ="UPS", message="Could not save file")

def openFile():
	f = filedialog.askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)
######################################################################

#Main GUI
root = Tk()
root.title("Ele")
root.minsize(width=800, height=500)
root.maxsize(width=800, height=500)

text = Text(root, width=500, height=500)
text.pack()

###############################################################################
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile, accelerator="Ctrl+N")
filemenu.add_command(label="Open", command=openFile, accelerator="Ctrl+O")
filemenu.add_command(label="Save", command=saveFile, accelerator="Ctrl+S")
filemenu.add_command(label="Save as...", command=saveAs, accelerator="Ctrl+A")
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit, accelerator="Ctrl+Q")
menubar.add_cascade(label="File", menu=filemenu)
###############################################################################

#####Hot-Keys#######################
root.bind("<Control-n>", newFileHK)
root.bind("<Control-o>", openFileHK)
root.bind("<Control-s>", saveFileHK)
root.bind("<Control-a>", saveAsHK)
root.bind("<Control-q>", quit)
####################################

###################################################################
formatOptions = Menu(menubar)
formatOptions.add_command(label="Arial", command=fontArial)
formatOptions.add_command(label="Helvetica", command=fontHelvetica)
formatOptions.add_command(label="Times New Roman", command=fontTNR)
formatOptions.add_command(label="Gothic", command=fontGothic)
menubar.add_cascade(label="Font", menu=formatOptions)
###################################################################

root.config(menu=menubar)
root.mainloop()

