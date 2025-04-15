# Elijah Budd
# 4/7/2025
# Program1: My Favorite Saying

import tkinter

def saying():
    main_window = tkinter.Tk()

    main_window.title("Saying")

    text1 = tkinter.Label(main_window, text='"Two things are infinite: the universe and human stupidity;', font=("Times New Roman", 20))
    text2 = tkinter.Label(main_window, text='and I\'m not sure about the universe."', font=("Times New Roman", 20))

    text1.pack()
    text2.pack()

    main_window.mainloop()

if __name__ == '__main__':
    saying()
