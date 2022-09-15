import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width = 600, height = 300)
canvas.grid(columnspan=3, rowspan = 3)              #canvas.pack()

#logo
logo = Image.open("logo.png")   #otvorenie obrázku
logo = ImageTk.PhotoImage(logo)    #mením formát obrázku na tk   #niečo magické aby program vedel pracovať s obrázkom
logo_label = tk.Label(image = logo)     #posielame tam logo       #niečo magické aby program vedel pracovať s obrázkom
logo_label.image = logo                   #niečo magické aby program vedel pracovať s obrázkom
logo_label.grid(column=1, row=0)

#instructions
instruction = tk.Label(root, text = "Zadaj cestu k PDF")
instruction.grid(columnspan = 3, column = 0, row = 1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode = "rb", title = "Choose a file", filetype=[("PDF file","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        #text box
        text_box = tk.text(root, height = 10, width = 50, padx = 15, pady = 15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center",justify="center")
        text_box.tag_add("center",1.0,"and")
        text_box.grid(column = 1, row = 3)

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable = browse_text, command = lambda:open_file(), bg = "#20bebe", fg = "white", height = 2, width = 15)
browse_text.set("Browse")
browse_btn.grid(column = 1, row = 2)

canvas = tk.Canvas(root, width = 600, height = 250)
canvas.grid(columnspan=3)


root.mainloop()
