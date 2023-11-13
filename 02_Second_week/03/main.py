import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("calc.ui")

def main():
    try:

        app = QApplication(sys.argv)
        calc = Calc()
        calc.show()
        sys.exit(app.exec_())
        
    except Exception as err :
        print("error: {0}".format(err))

if __name__ == "__main__":
    main()