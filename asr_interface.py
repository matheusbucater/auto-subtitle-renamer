from tkinter import filedialog
import tkinter as tk
import auto_subtitle_renamer as asr


# im too lazy to validate these
def executeAsrMainWithGivenDirectory():
	asr.main(directory_entry.get())
def updateRenameConfirmation():
	ok_text.config(text='OK!')

def renameButtonClicked():
	executeAsrMainWithGivenDirectory()
	updateRenameConfirmation()


# im too lazy to validate these 
def updateDirectoryOnScreen():
	directory_on_screen_text.config(text=directory_entry.get())
def updateCofirmButtonColor():
	confirm_btn.config(background='#a6fc9d')

def confirmButtonClicked():
	updateDirectoryOnScreen()
	updateCofirmButtonColor()

app = tk.Tk()
app.title('Auto Subtitle Renamer')
app.geometry('450x150')
app.configure(background='#c4c4c4')

label = tk.Label(app, text='Directory', background='#e0e0e0', foreground='#000', anchor='w')
label.place(x=10, y=10, width=100, height=20)

directory_entry = tk.Entry(app)
directory_entry.place(x=10, y=35, width=350, height=30)

confirm_btn = tk.Button(app, text='Corfirm', command=confirmButtonClicked)
confirm_btn.place(x=370, y=35, width=70, height=30)

directory_on_screen_text = tk.Label(app, background='#e0e0e0', foreground='#000', anchor='w')
directory_on_screen_text.place(x=10, y=70, width=350, height=30)

exit_btn = tk.Button(app, text='Exit', command=app.destroy)
exit_btn.place(x=10, y=110, width=100, height=30)

rename_btn = tk.Button(app, text='Rename', command=executeAsrMainWithGivenDirectory)
rename_btn.place(x=130, y=110, width=100, height=30)

ok_text = tk.Label(app, background='#c4c4c4', foreground='#000', anchor='w')
ok_text.place(x=250, y=110, width=50, height=30)

app.mainloop()

