# Import necessary modules
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfWriter, PdfReader
import os

# Create a Tkinter window
root = Tk()
root.title("PDF Guard")
root.geometry("600x430+300+100")

# Function to open a file dialog and select a PDF file
def browse():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select PDF File",
        filetypes=(('PDF File', '*.pdf'), ('All Files', '*.*'))
    )
    entry1.delete(0, END)  # Clear the entry field before inserting the new filename
    entry1.insert(END, filename)

# Function to protect a PDF file with a password
def protect_pdf():
    mainfile = source.get()
    protectfile = target.get()
    code = password.get()

    # Check if any of the input fields are empty
    if mainfile == "" or protectfile == "" or code == "":
        messagebox.showerror("Invalid", "All entries are empty!!")
    # Check if the source PDF file exists
    elif not os.path.isfile(mainfile):
        messagebox.showerror("Invalid", "Source PDF file does not exist")
    else:
        try:
            pdf_writer = PdfWriter()
            pdf_reader = PdfReader(mainfile)

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            # Password protect the PDF
            pdf_writer.encrypt(code)

            with open(protectfile, "wb") as f:
                pdf_writer.write(f)

            messagebox.showinfo("Success", "PDF file protected successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Set the window icon
image_icon = PhotoImage(file="Image/icon.png")
root.iconphoto(False, image_icon)

# Create the main window
Top_image = PhotoImage(file="Image/top image.png")
Label(root, image=Top_image).pack()

frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE)
frame.place(x=10, y=130)

# Source PDF Entry
source = StringVar()
Label(frame, text="Source PDF file:", font="arial 10 bold", fg="#4c4542").place(x=30, y=50)
entry1 = Entry(frame, width=30, textvariable=source, font="arial 15", bd=1)
entry1.place(x=150, y=48)

Button_icon = PhotoImage(file="Image/button image.png")
Button(frame, image=Button_icon, width=35, height=24, bg="#d3cdcd", command=browse).place(x=500, y=47)

# Target PDF Entry
target = StringVar()
Label(frame, text="Target PDF File:", font="arial 10 bold", fg="#4c4542").place(x=30, y=100)
entry2 = Entry(frame, width=30, textvariable=target, font="arial 15", bd=1)
entry2.place(x=150, y=100)

# Password Entry
password = StringVar()
Label(frame, text="Set User Password:", font="arial 10 bold", fg="#4c4542").place(x=15, y=150)
entry3 = Entry(frame, width=30, textvariable=password, font="arial 15", bd=1)
entry3.place(x=150, y=150)

# Protect PDF Button
button_icon = PhotoImage(file="Image/button.png")
Protect = Button(root, text="Protect PDF File", compound=LEFT, image=button_icon, width=230, height=50, bg="#bfb9b9", font="arial 14 bold", command=protect_pdf)
Protect.pack(side=BOTTOM, pady=40)

# Start the Tkinter event loop
root.mainloop()
