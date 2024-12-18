# 3. Write a program to draw line(4cm, 5cm, 6cm) in three different places and point into a GIS image.

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt


class LP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing on an Image")
        self.setGeometry(100, 100, 1024, 738)

        self.image_label = QLabel(self)
        self.image = QPixmap("prasun.jpg")
        self.image_label.setPixmap(self.image)
        self.image_label.setStyleSheet("border: 5px solid blue;")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.image_label.setMouseTracking(True)
        self.image_label.mouseMoveEvent = self.mouse_moved

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def mouse_moved(self, event):
        # Create a painter to draw on the image
        painter = QPainter(self.image_label.pixmap())

        painter.setPen(QColor("red"))
        painter.drawLine(300, 200, 260, 108)

        painter.setPen(QColor("green"))
        painter.drawLine(350, 310, 541, 370)

        painter.setPen(QColor("blue"))
        painter.drawLine(410, 238, 342, 530)

        painter.end()

        # Repaint the label to update the changes
        self.image_label.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LP()
    window.show()
    sys.exit(app.exec_())

