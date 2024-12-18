# 10. Write a GIS application program that will do the following: a) It will open an image in a panel. b) An option will be there for labeling region in the current image depending on the pixel color. c) After completion of step 2, the user can ask for percentage of particular region in the current image. Program should be able to show the percentage value of the region with respect to the whole image. d) The above stated problem in step 3, should be implemented for an image where same color pixels are scattered. 
import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QPushButton, QComboBox, QLineEdit, QMessageBox, QDesktopWidget, QScrollArea
)
from PyQt5.QtGui import QPixmap, QColor, QImage
from PyQt5.QtCore import Qt


class Page1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Association Page")
        self.setGeometry(100, 100, 1024, 738)

        # Image setup
        self.image_label = QLabel(self)
        self.image = QPixmap("session1.gif")
        self.image_label.setPixmap(self.image)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.mousePressEvent = self.mouse_clicked

        # Image dimensions and pixel data
        self.height = self.image.height()
        self.width = self.image.width()
        self.image_data = QImage(self.image.toImage())

        # Feature data
        self.features = [None] * 3
        self.feature_colors = [None] * 3
        self.count = 0
        self.selected_color = None

        # Layouts and widgets
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        # Feature selection panel
        self.feature_selection_combo = QComboBox()
        self.feature_selection_combo.setEditable(False)
        self.feature_selection_combo.addItem("      ")
        layout.addWidget(QLabel("Feature Selection"))
        layout.addWidget(self.feature_selection_combo)

        # Color display
        self.color_display = QLineEdit()
        self.color_display.setReadOnly(True)
        layout.addWidget(QLabel("Color"))
        layout.addWidget(self.color_display)

        # Feature name input
        self.feature_input = QLineEdit()
        layout.addWidget(QLabel("Feature Name"))
        layout.addWidget(self.feature_input)

        # Buttons
        self.go_button = QPushButton("GO")
        self.go_button.clicked.connect(self.assign_feature)
        layout.addWidget(self.go_button)

        self.complete_button = QPushButton("COMPLETE")
        self.complete_button.clicked.connect(self.complete_assignment)
        layout.addWidget(self.complete_button)

        self.find_percentage_button = QPushButton("Find Percentage")
        self.find_percentage_button.clicked.connect(self.calculate_percentage)
        self.find_percentage_button.setVisible(False)
        layout.addWidget(self.find_percentage_button)

        self.percentage_display = QLineEdit()
        self.percentage_display.setReadOnly(True)
        self.percentage_display.setVisible(False)
        layout.addWidget(self.percentage_display)

        # Set main widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def mouse_clicked(self, event):
        x, y = event.x(), event.y()
        if 0 <= x < self.width and 0 <= y < self.height:
            color = self.image_data.pixelColor(x, y)
            self.selected_color = color.rgb()
            self.color_display.setStyleSheet(f"background-color: {color.name()};")

    def assign_feature(self):
        if self.count >= 3:
            QMessageBox.warning(self, "Notification", "Assignment completed before")
            return

        feature_name = self.feature_input.text().strip()
        if not feature_name:
            QMessageBox.warning(self, "Notification", "Please assign a feature name")
            return

        if self.selected_color is None:
            QMessageBox.warning(self, "Notification", "Please select a feature")
            return

        for i in range(self.count):
            if self.selected_color == self.feature_colors[i]:
                QMessageBox.warning(self, "Notification", "Please select a new feature")
                return

            if feature_name.lower() == self.features[i].lower():
                QMessageBox.warning(self, "Notification", "Feature name used before")
                self.feature_input.clear()
                return

        self.features[self.count] = feature_name
        self.feature_colors[self.count] = self.selected_color
        self.count += 1
        self.color_display.setStyleSheet("background-color: white;")
        self.feature_input.clear()

        if self.count == 3:
            self.go_button.setVisible(False)

    def complete_assignment(self):
        if self.count == 3:
            for feature in self.features:
                self.feature_selection_combo.addItem(feature)
            self.find_percentage_button.setVisible(True)
            self.percentage_display.setVisible(True)

    def calculate_percentage(self):
        if self.selected_color is None:
            QMessageBox.warning(self, "Notification", "Please click on a feature to find the percentage")
            return

        count = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.image_data.pixelColor(x, y).rgb() == self.selected_color:
                    count += 1

        total_pixels = self.width * self.height
        percentage = (count / total_pixels) * 100
        self.percentage_display.setText(f"{percentage:.2f}%")
        print(f"Count: {count}, Percentage: {percentage:.2f}%")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Page1()
    window.show()
    sys.exit(app.exec_())
