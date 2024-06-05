import tkinter as tk
from time import strftime


def update_time():
    current_time = strftime('%H:%M:%S:%p')
    label.config(text=current_time)
    label.after(1000, update_time)


root = tk.Tk()
root.title("Digital clock")
root.geometry("300x150")
root.config(bg='black')
label = tk.Label(root, font=('Helvetica', 40, 'bold'), background='black', foreground='cyan')
label.pack(expand=True)
label.bind('<Button-1>', lambda e: root.geometry(""))
update_time()
root.mainloop()
