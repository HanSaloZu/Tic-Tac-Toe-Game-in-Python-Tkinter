from tkinter import Button, DISABLED, NORMAL


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
                                activeforeground="#FFF",
                                bd=1)
                button.grid(row=row, column=col, sticky="nsew")
                line.append(button)
            self.field.append(line)

    def disable_field(self, winner: str) -> None:
        for row in range(3):
            for col in range(3):
                if self.field[row][col]["text"] != winner:
                    self.field[row][col]["state"] = DISABLED

    def clear_field(self) -> None:
        for row in range(3):
            for col in range(3):
                self.field[row][col]["text"] = ""
                self.field[row][col]["state"] = NORMAL
                self.field[row][col]["bg"] = "#000"
