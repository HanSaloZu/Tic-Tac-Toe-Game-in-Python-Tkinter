from random import choice


class Game:
    def __init__(self, gui: object):
        self.gui: object = gui
        self.field = gui.grid.field
        self.current_sym: str = choice(["X", "0"])

        for row in range(3):
            for col in range(3):
                btn = self.gui.grid.field[row][col]
                btn["command"] = lambda row=row, col=col: self.click(row, col)

    def click(self, row, col) -> None:
        if self.field[row][col]["text"] == "":
            self.field[row][col]["text"] = self.current_sym
            winner = self.check_win(self.current_sym)

            if winner is not None:
                self.show_winner(winner)
                self.end_game()
            else:
                self.change_current_sym()

    def change_current_sym(self) -> None:
        if self.current_sym == "X":
            self.current_sym = "0"
        else:
            self.current_sym = "X"

    def check_win(self, sym: str):
        for i in range(3):
            if self.check_line(
                self.field[i][0],
                self.field[i][1],
                self.field[i][2],
                sym
            ):
                return (self.field[i][0],
                        self.field[i][1],
                        self.field[i][2])
            elif self.check_line(
                self.field[0][i],
                self.field[1][i],
                self.field[2][i],
                sym
            ):
                return (self.field[0][i],
                        self.field[1][i],
                        self.field[2][i])

        if self.check_line(
            self.field[0][0],
            self.field[1][1],
            self.field[2][2],
            sym
        ):
            return (self.field[0][0],
                    self.field[1][1],
                    self.field[2][2])
        elif self.check_line(
            self.field[2][0],
            self.field[1][1],
            self.field[0][2],
            sym
        ):
            return (self.field[2][0],
                    self.field[1][1],
                    self.field[0][2])

    def check_line(
        self,
        grid_cell1: object,
        grid_cell2: object,
        grid_cell3: object,
        sym: str
    ) -> bool:
        return (grid_cell1["text"] == sym and
                grid_cell2["text"] == sym and
                grid_cell3["text"] == sym)

    def show_winner(self, *grid_cells: tuple) -> None:
        for grid_cell in grid_cells[0]:
            grid_cell["bg"] = grid_cell["activebackground"]

    def end_game(self) -> None:
        self.gui.grid.disable_field(self.current_sym)

    def run(self) -> None:
        self.gui.window.mainloop()
