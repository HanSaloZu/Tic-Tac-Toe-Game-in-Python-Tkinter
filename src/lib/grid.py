from tkinter import Button


class Grid:
    field: list = []

    def __init__(self, window: object) -> None:
        for row in range(3):
            line = []

            for col in range(3):
                button = Button(window, text="", width=11, height=6,
                                font=("Courier", 20, "bold"),
                                bg="#000",
                                activebackground="#171717",
                                fg="#FFF",
                                bd=0)
                button.grid(row=row, column=col, sticky="nsew")
                line.append(button)
            self.field.append(line)
