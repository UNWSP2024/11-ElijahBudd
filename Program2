# Elijah Budd
# 4/8/2025
# Program2: My Information
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.window = tkinter.Tk()

        self.my_button = tkinter.Button(self.window, text="Show Info", command=self.show_info, font=("Arial, 20"))
        self.quit_button = tkinter.Button(self.window, text="Quit", command=self.window.quit, font=("Arial, 20"))

        self.my_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def show_info(self):
        tkinter.messagebox.showinfo(title="Info", message="name: Elijah Budd\n Address: 9709 205th ave NE, Wyoming, MN 55092")

if __name__ == '__main__':
    my_gui = MyGUI()
