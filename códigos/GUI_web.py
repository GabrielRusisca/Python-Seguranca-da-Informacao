import webbrowser
import tkinter as tk

root = tk.Tk()
root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = tk.Button(root, text='Abrir o Google', command=google).pack(pady=20)

root.mainloop()