
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FallOutTransition
from Sudoku import Sudoku

class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.difficulty = 0
        self.cols = 1
        self.sm = ScreenManager(transition=FallOutTransition())
        self.playScreen = PlayScreen(0, name="play")
        mainScreen = MainMenu(name="main")
        diffScreen = DifficultyScreen(name="diff")
        quitScreen = QuitScreen(name="quit")
        aboutScreen = AboutScreen(name="about")
        rulesScreen = RulesScreen(name="rules")
        container = GridLayout()
        container.cols = 1
        
        diffLabel = Label(text="Choose a Difficulty", font_size=50)
        begBtn = Button(text="Beginner", font_size=30, on_press=self.beginner)
        easyBtn = Button(text="Easy", font_size=40, on_press=self.easy)
        normBtn = Button(text="Normal", font_size=50, on_press=self.normal)
        hardBtn = Button(text="Hard", font_size=60, on_press=self.hard)
        senpaiBtn = Button(text="Senpai", font_size=70, on_press=self.senpai)
        senseiBtn = Button(text="Sensei!", font_size=90, on_press=self.sensei)

        container.add_widget(diffLabel)
        container.add_widget(begBtn)
        container.add_widget(easyBtn)
        container.add_widget(normBtn)
        container.add_widget(hardBtn)
        container.add_widget(senpaiBtn)
        container.add_widget(senseiBtn)
        diffScreen.add_widget(container)
        self.sm.add_widget(mainScreen)
        self.sm.add_widget(diffScreen)
        self.sm.add_widget(aboutScreen)
        self.sm.add_widget(rulesScreen)
        self.sm.add_widget(self.playScreen)
        self.sm.add_widget(quitScreen)
        self.add_widget(self.sm)

    def beginner(self, event):
        self.newGame(5)
    
    def easy(self, event):
        self.newGame(4)

    def normal(self, event):
        self.newGame(3)

    def hard(self, event):
        self.newGame(2)
    
    def senpai(self, event):
        self.newGame(1)

    def sensei(self, event):
        self.newGame(0)

    def newGame(self, difficulty):
        self.sm.remove_widget(self.playScreen)
        self.playScreen = PlayScreen(difficulty, name="play")
        self.sm.add_widget(self.playScreen)
        self.sm.current = "play"


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        container = GridLayout()
        container.cols = 1
        lab1 = Label(text="Sudoku Mobile", font_size=90, size_hint=(1.5, 1.5))
        lab2 = Label(text="By: Ryan Gill", font_size=60)
        container.add_widget(lab1)
        container.add_widget(lab2)
        rulesBtn = Button(text="Rules", font_size=60, on_press=self.toRules)
        aboutButton = Button(text="About", font_size=60, on_press=self.toAbout)
        newBtn = Button(text="New Game", font_size=60, on_press=self.toDiff)
        exitbutton = Button(text="Exit", font_size=60, on_press=self.exitGame)
        container.add_widget(newBtn)
        container.add_widget(rulesBtn)
        container.add_widget(aboutButton)
        container.add_widget(exitbutton)
        self.add_widget(container)
        

    def toDiff(self, event):
        self.parent.current = "diff"

    def toAbout(self, event):
        self.parent.current = "about"

    def toRules(self, event):
        self.parent.current = "rules"

    def exitGame(self, event):
        exit()
    

class DifficultyScreen(Screen):
    def __init__(self, **kwargs):
        super(DifficultyScreen, self).__init__(**kwargs)

class QuitScreen(Screen):
    def __init__(self, **kwargs):
        super(QuitScreen, self).__init__(**kwargs)
        container = GridLayout()
        container.cols = 1
        lab = Label(text="Quit Current Game?", font_size=60)
        yesBtn = Button(text="Yes", font_size=100, on_press=self.yes)
        noBtn = Button(text="No", font_size=100, on_press=self.no)
        container.add_widget(lab)
        container.add_widget(yesBtn)
        container.add_widget(noBtn)
        self.add_widget(container)
        
    def yes(self, event):
        self.parent.current = "main"

    def no(self, event):
        self.parent.current = "play"


class PlayScreen(Screen):
    def __init__(self, diff, **kwargs):
        super(PlayScreen, self).__init__(**kwargs)
        self.difficulty = diff
        self.container = GridLayout()
        self.container.cols = 1
        gs = GameScreen(self.difficulty)
        btn = Button(text="Quit", on_press=self.goToMain, font_size=60, size_hint=(.1, .1))
        self.container.add_widget(gs)
        self.container.add_widget(btn)
        self.add_widget(self.container)

    def goToMain(self, event):
        self.parent.current = "quit"


class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        container = GridLayout()
        container.cols = 1
        title = Label(text="About this application:", size_hint=(.25, .25), font_size=70)

        bodyText = "This mobile app was created using the Kivy\nframework and a backend Sudoku" \
            " algorithm\nthat I wrote. The player can choose their difficulty\nand then play a board and check their solution.\n" \
            "Specifically, the Sudoku algorithm will procedurally\ngenerate a new, valid Sudoku board so that\neach game is diffenent. " \
            "Then, it will hide a set number\n of tiles based on the players chosen difficulty."

        body = Label(text=bodyText)
        backBtn = Button(text="Back", font_size=60, size_hint=(.2, .2), on_press=self.goToMain)
        container.add_widget(title)
        container.add_widget(body)
        container.add_widget(backBtn)
        self.add_widget(container)

    def goToMain(self, event):
        self.parent.current = "main"

class RulesScreen(Screen):
    def __init__(self, **kwargs):
        super(RulesScreen, self).__init__(**kwargs)
        container = GridLayout()
        container.cols = 1
        title = Label(text="Rules", size_hint=(.15, .15), font_size=70)
        title2 = Label(text="Gameplay", size_hint=(.15, .15), font_size=70)
        rules_text = "The \'One Rule\' of Sudoku:\n\nUse Numbers 1 - 9. For each row, column\nand box (9 spaces each) needs to be\n" \
            "filled in with numbers 1 - 9 without repeating\nany numbers within a row, column or box\n\nBeginner difficulty only has" \
            " 3\nsquares left, try to beat it!"
        gameplay_text = "Press each square to cycle through numbers.\n\nPress \"Check Solution\" to see if" \
            "you solved the\nboard correctly.\n\nPress \"Clear Board\" to reset the game\n\nPress \"New Game\" to exit"
        body1 = Label(text=rules_text)
        body2 = Label(text=gameplay_text)
        backBtn = Button(text="Back", font_size=60, size_hint=(.3, .3), on_press=self.goToMain)
        container.add_widget(title)
        container.add_widget(body1)
        container.add_widget(title2)
        container.add_widget(body2)
        container.add_widget(backBtn)
        self.add_widget(container)

    def goToMain(self, event):
        self.parent.current = "main"

class GameScreen(GridLayout):
    def __init__(self, diff, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.difficulty = diff
        self.rows = 4
        self.cols = 1
        self.board = GameBoard(self.difficulty)
        self.solveLabel = Label(text='Sudoku Mobile', size_hint=(.4, .4), font_size=90)
        self.solveButton = Button(text='Check Solution', size_hint=(.15, .15), font_size=60, on_press=self.checkSolution)
        self.clearButton = Button(text="Clear Board", size_hint=(.15, .15), font_size=60, on_press=self.clearBoard)
        self.add_widget(self.solveLabel)
        self.add_widget(self.board)
        self.add_widget(self.solveButton)
        self.add_widget(self.clearButton)
        
    def checkSolution(self, event):
        solved = True
        corners = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        for square in self.board.squares:
            text = square.text
            if text == '':
                value = 0
            else:
                value = int(text)
            self.board.puzzle[square.puzRow, square.puzCol] = value

        #check every row
        for i in range(9):
            found = []
            for j in range(9):
                val = self.board.puzzle[i, j]
                if val == 0:
                    solved = False
                if val in found:
                    solved = False
                else:
                    found.append(val)
        
        #check every column
        for i in range(9):
            found = []
            for j in range(9):
                val = self.board.puzzle[j, i]
                if val in found:
                    solved = False
                else:
                    found.append(val)
        
        #check every box
        for cor in corners:
            found = []
            for i in range(3):
                for j in range(3):
                    row = i + cor[0]
                    col = j + cor[1]
                    val = self.board.puzzle[row, col]
                    if val in found:
                        solved = False
                    else:
                        found.append(val)

        if solved:
            self.solveLabel.color = [0,1,0,1]
            self.solveLabel.text = "Congratulations!!!"
        else:
            self.solveLabel.color = [1, 0, 0, 1]
            self.solveLabel.text = "Try Again"

    def clearBoard(self, event):
        for square in self.board.validSquares:
            square.text = ''
            self.board.puzzle[square.puzRow, square.puzCol] = 0
        self.solveLabel.text = "Sudoku Mobile"
        self.solveLabel.color = [1,1,1,1]

class GameBoard(GridLayout):
    def __init__(self, diff, **kwargs):
        super(GameBoard, self).__init__(**kwargs)
        self.difficulty = diff
        self.squares = []
        self.validSquares = []
        self.cols = 3
        self.rows = 3
        puz = Sudoku(self.difficulty)
        self.puzzle = puz.puzzle
        corners = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        for corner in corners:
            new_box = GameBox(padding=3)
            for i in range(3):
                for j in range(3):
                    row = i + corner[0]
                    col = j + corner[1]
                    if self.puzzle[row, col] == 0:
                        square = GameSquare(text="")
                        square.puzRow = row
                        square.puzCol = col
                        square.color = [0,0,0,1]
                        square.background_color = [3,3,3,1]
                        self.squares.append(square)
                        self.validSquares.append(square)
                        self.squares[-1].on_press = self.squares[-1].updateSquare
                    else:
                        square = GameSquare(text=str(self.puzzle[row, col]))
                        square.puzRow = row
                        square.puzCol = col
                        square.color = [0,0,0,1]
                        square.background_color = [2.5, 2.5, 2.5, 1]
                        self.squares.append(square)
                    new_box.add_widget(square)
            self.add_widget(new_box)
        
class GameBox(GridLayout):
    def __init__(self, **kwargs):
        super(GameBox, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 3

class GameSquare(Button):
    def __init__(self, **kwargs):
        super(GameSquare, self).__init__(**kwargs)
        self.puzRow = None
        self.puzCol = None
        self.font_size = 50

    def updateSquare(self):
        if self.text == '':
            self.text = '1'
        elif self.text == '9':
            self.text = ''
        else:
            self.text = str(int(self.text) + 1)

class SudokuMobileApp(App):
    def build(self):
        return RootWidget()

#entry point
if __name__ == "__main__":
    SudokuMobileApp().run()

