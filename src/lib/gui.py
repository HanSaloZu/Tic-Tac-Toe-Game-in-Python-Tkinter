from tkinter import Tk, Button


class Gui:
    window: object = Tk()

    def __init__(self, title: str = "Tic-Tac-Toe-AI") -> None:
        self.window.geometry("606x602")
        self.window.title(title)
