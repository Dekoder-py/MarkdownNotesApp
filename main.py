import tkinter as tk
from tkinter import filedialog


def save(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown Files", "*.md"), ("All Files", "*.*")])
    
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            content = text_field.get(1.0, tk.END)
            file.write(content)



root = tk.Tk()

root.title("Markdown Notes")
root.geometry("800x600")


# text entry space
text_field = tk.Text(root, wrap="word", font=("", 16))

text_field.pack(expand=True, fill="both")
text_field.focus()

root.bind("<Control-s>", save)
root.bind("<Command-s>", save)

root.mainloop()
