# 9. Draw Point, Line, Polygon, text, oval and gradient on the image.
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPolygonF
from PyQt5.QtCore import Qt, QPointF


class LP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing on an Image")
        self.setGeometry(100, 100, 1024, 738)

        # Load the image
        self.image_label = QLabel(self)
        self.image = QPixmap("prasun.jpg")
        self.image_label.setPixmap(self.image)
        self.image_label.setStyleSheet("border: 5px solid blue;")
        self.image_label.setAlignment(Qt.AlignCenter)

        # Set mouse events
        self.image_label.setMouseTracking(True)
        self.image_label.mouseMoveEvent = self.mouse_moved

        # Layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        # Container widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def mouse_moved(self, event):
        # Create a painter to draw on the image
        painter = QPainter(self.image_label.pixmap())

        # Draw an oval
        painter.setPen(QColor("red"))
        painter.drawEllipse(300, 200, 260, 108)

        # Draw a line
        painter.setPen(QColor("green"))
        painter.drawLine(150, 210, 340, 370)

        # Draw text
        painter.setPen(QColor("black"))
        painter.drawText(300, 300, "SOURAV DHALI")

        # Draw a filled polygon
        polygon = QPolygonF([
            QPointF(150, 300),
            QPointF(150, 380),
            QPointF(250, 410),
            QPointF(220, 320)
        ])
        painter.setBrush(QColor(200, 13, 40))
        painter.setPen(Qt.NoPen)
        painter.drawPolygon(polygon)

        painter.end()

        # Repaint the label to update the changes
        self.image_label.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LP()
    window.show()
    sys.exit(app.exec_())
