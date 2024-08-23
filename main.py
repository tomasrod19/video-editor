from PyQt5.QtWidgets import QApplication
from gui import VideoEditorGUI

def main():
    app = QApplication([])

    window = VideoEditorGUI()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()
