import tkinter as tk

root = tk.Tk()
root.title("Markdown Notes")
root.geometry("800x600")

# text entry space
text_field = tk.Text(root, wrap="word", font=("", 16))

text_field.pack(expand=True, fill="both")
text_field.focus()
root.mainloop()
