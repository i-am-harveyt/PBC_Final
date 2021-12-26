import tkinter as tk
from functions.controller import Controller


if __name__ == "__main__":
    root = tk.Tk()

    # # Gets the requested values of the height and widht.
    # windowWidth = root.winfo_reqwidth()
    # windowHeight = root.winfo_reqheight()
    #
    # # Gets both half the screen width/height and window width/height
    # positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    # positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
    #
    # # Positions the window in the center of the page.
    # root.geometry("+{}+{}".format(positionRight, positionDown))

    Controller(root)
    root.mainloop()
