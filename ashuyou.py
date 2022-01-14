from pytube import YouTube
from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Youtube downloader")
root.resizable(0,0)
root.wm_iconbitmap("youtubeashu.ico")

def download():
	if entr.get()=='':
		messagebox.showerror('Error','Give link')
	else:
		try:
			YouTube(entr.get()).streams.first().download()
			messagebox.showinfo('Complete','Video Download Successful')
			entr.set('')
		except Exception:
			root.update()
			messagebox.showerror('Error','Invalid link,Please Enter correct link')
			entr.set('')

Label(root, text="YouTube Video Downloader", bg="black", fg="cyan", font="Ds-Digital 50").pack(pady=10, padx=10)

Label(root, text="Enter the link below", bg="black", fg="cyan", font="Ds-Digital 30").pack(pady=25)

entr = StringVar()
entry = Entry(root, textvariable=entr, font="Lucida 20", width=45).pack(pady=15)

def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

Button(root, text="Download", bg="black", fg="cyan", font="Ds-Digital 30", command=download).pack(pady=15)
root.mainloop()