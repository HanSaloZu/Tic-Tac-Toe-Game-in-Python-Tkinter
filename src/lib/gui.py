from tkinter import Tk, Button

from .grid import Grid


class Gui:
    window: object = Tk()

    def __init__(self, title: str = "Tic-Tac-Toe") -> None:
        self.window.geometry("606x602")
        self.window.title(title)

        self.grid = Grid(self.window)

        restart_button = Button(
            self.window,
            text="Restart",
            height=2,
            font=("Courier", 24, "bold"),
            bg="#000",
            fg="#FFF",
            activebackground="#171717",
            activeforeground="#FFF",
            bd=0,
            command=lambda: self.grid.clear_field()
        )
        restart_button.grid(row=3, column=0, columnspan=3, sticky="nsew")
