
import tkinter as tk
from tkinter import filedialog
from textblob import TextBlob
from pypdf import PdfReader

def upload_file():
    filename = filedialog.askopenfilename()
    print(filename)
    class spell_checker():
        def __init__(self,reader):
            self.reader=reader

        def analyze(self):
            page = self.reader.pages[0]
            a =page.extract_text()
            b = TextBlob(a)
            text=b.correct()
    checker=spell_checker(PdfReader(filename))
    checker.analyze()
            
            
    
root = tk.Tk()
root.title("Upload File")

upload_button = tk.Button(root, text="Upload File", command=upload_file)
upload_button.pack(padx=200, pady=50)

root.mainloop()




