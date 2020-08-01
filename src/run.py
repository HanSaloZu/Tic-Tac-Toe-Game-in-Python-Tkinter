from lib.gui import Gui
from lib.game import Game


def main():
    gui = Gui(title="Tic-Tac-Toe")
    game = Game(gui=gui)
    game.run()


if __name__ == "__main__":
    main()
