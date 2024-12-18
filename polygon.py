# 2. Write a GIS based program to draw a polygon (four different places with 2 cm, 6cm, 8cm width) into a GIS image.
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QGraphicsPolygonItem, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPolygonF, QColor
from PyQt5.QtCore import Qt, QPointF


class Poly(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing on an Image")
        self.setGeometry(100, 100, 1024, 738)

        self.image_label = QLabel(self)
        self.image = QPixmap("prasun.jpg")
        self.image_label.setPixmap(self.image)
        self.image_label.setStyleSheet("border: 5px solid blue;")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.mouseMoveEvent = self.mouse_moved

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def mouse_moved(self, event):
        painter = QPainter(self.image_label.pixmap())

        self.draw_polygon(painter, [(300, 300), (300, 380), (350, 410), (430, 320)], QColor(200, 13, 40))
        self.draw_polygon(painter, [(200, 300), (200, 450), (250, 500), (230, 320)], QColor(100, 13, 40))
        self.draw_polygon(painter, [(400, 100), (400, 200), (450, 300), (430, 120)], QColor(40, 100, 40))
        self.draw_polygon(painter, [(100, 100), (100, 350), (150, 500), (200, 320)], QColor(80, 10, 130))

        painter.end()
        self.image_label.repaint()

    def draw_polygon(self, painter, points, color):
        polygon = QPolygonF([QPointF(x, y) for x, y in points])
        painter.setBrush(color)
        painter.setPen(Qt.NoPen)
        painter.drawPolygon(polygon)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Poly()
    window.show()
    sys.exit(app.exec_())

