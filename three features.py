# 1. Write a program to assign three features in RS-GIS image.
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QGridLayout, QPushButton,
    QComboBox, QDesktopWidget, QScrollArea, QLineEdit, QWidget, QMessageBox
)
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt

class Page1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Association Page")
        self.count = 0
        self.ccb = 0
        self.frgb = [None] * 4
        self.fea = [None] * 4
        self.rgb = None

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QVBoxLayout(self.central_widget)

        self.image_label = QLabel(self)
        pixmap = QPixmap("session1.gif")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.mousePressEvent = self.mouse_clicked

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.image_label)
        main_layout.addWidget(scroll_area)

        panel_layout = QGridLayout()

        self.feature_combo = QComboBox(self)
        self.feature_combo.addItem("      ")
        panel_layout.addWidget(QLabel("Feature Selection:"), 0, 0)
        panel_layout.addWidget(self.feature_combo, 0, 1)

        self.color_field = QLineEdit(self)
        self.color_field.setReadOnly(True)
        panel_layout.addWidget(QLabel("Color:"), 1, 0)
        panel_layout.addWidget(self.color_field, 1, 1)

        self.feature_field = QLineEdit(self)
        panel_layout.addWidget(QLabel("Feature:"), 2, 0)
        panel_layout.addWidget(self.feature_field, 2, 1)

        self.go_button = QPushButton("GO", self)
        self.go_button.clicked.connect(self.assign_feature)
        panel_layout.addWidget(self.go_button, 3, 0)

        self.complete_button = QPushButton("COMPLETE", self)
        self.complete_button.clicked.connect(self.complete_assignment)
        panel_layout.addWidget(self.complete_button, 3, 1)

        main_layout.addLayout(panel_layout)
        self.resize(1024, 738)

    def mouse_clicked(self, event):
        x, y = event.x(), event.y()
        color = QColor.fromRgb(160, 160, 220)  
        self.rgb = color.rgb()
        self.color_field.setStyleSheet(f"background-color: {color.name()}")
        print(f"Clicked at ({x}, {y}), RGB: {self.rgb}")

    def assign_feature(self):
        if self.count == 4:
            QMessageBox.critical(self, "Notification", "Assignment completed before")
            return
        feature_name = self.feature_field.text()
        if not feature_name:
            QMessageBox.critical(self, "Notification", "Please Assign Feature Name")
            return
        if not self.rgb:
            QMessageBox.critical(self, "Notification", "Please Select Feature")
            return

        for i in range(self.count):
            if self.rgb == self.frgb[i] or feature_name.lower() == self.fea[i].lower():
                QMessageBox.critical(self, "Notification", "Duplicate Feature Name or Color")
                return

        self.frgb[self.count] = self.rgb
        self.fea[self.count] = feature_name
        self.count += 1
        self.color_field.clear()
        self.feature_field.clear()

        if self.count == 4:
            QMessageBox.information(self, "Notification", "Assignment completed")
            self.feature_field.setReadOnly(True)

    def complete_assignment(self):
        if self.count == 4 and self.ccb == 0:
            for feature in self.fea:
                self.feature_combo.addItem(feature)
            print(f"Assigned Features: {self.fea}")
            self.ccb = 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Page1()
    window.show()
    sys.exit(app.exec_())