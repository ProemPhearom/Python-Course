from tkinter import *





root = Tk()
root.title("calulator")
root.resizable(width=False, height=False)
frame =Frame(root)
frame.grid(padx=5, pady=5)



textDisplay =Entry(frame, font=("arial", 20,"bold"), bd=15, bg="powder blue", width=25, justify=RIGHT)
textDisplay.grid()
textDisplay.insert(0, "0")






root.mainloop()
