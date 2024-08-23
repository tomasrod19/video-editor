from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class VideoEditorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
  
        self.setWindowTitle("Video Editor")
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel("Welcome to the Video Editor!", self)
        self.label.setGeometry(50, 50, 300, 50)

        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(50, 100, 100, 50)

        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.label.setText("Button clicked!")