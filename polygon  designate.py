# 7. Write a GIS based program to draw a polygon (four different places with 5 cm, 7cm, 9cm width) into a GIS image and designate the mark with some a ribute
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QPushButton, QScrollArea, QDesktopWidget
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QMouseEvent


class Page1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Association Page")
        self.setGeometry(100, 100, 1024, 738)
        self.image_path = "prasun.jpg"  # Path to your image
        self.width = 740
        self.height = 600
        self.pixels = None
        self.rgb = 0
        self.frgb = []
        self.fea = []
        self.count = 0
        self.selected_point = None

        # Initialize the UI
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout(self)

        # Left side: Image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap(self.image_path))
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(self.width, self.height)
        self.image_label.mousePressEvent = self.mouse_click_event
        self.image_label.mouseMoveEvent = self.mouse_move_event

        # Right side: Controls
        self.panel = QWidget(self)
        self.panel.setStyleSheet("background-color: rgba(160, 160, 220, 200);")
        panel_layout = QVBoxLayout(self.panel)

        # Feature Selection
        self.feature_combobox = QComboBox(self)
        self.feature_combobox.addItem("      ")
        self.feature_combobox.setStyleSheet("background-color: white;")

        font = QFont("Arial")  # Create QFont with the desired font name
        self.feature_combobox.setFont(font)  # Set the font for the combo box

        panel_layout.addWidget(self.feature_combobox)

        # Color selection
        self.color_label = QLabel("Color", self)
        self.color_field = QLineEdit(self)
        self.color_field.setReadOnly(True)
        panel_layout.addWidget(self.color_label)
        panel_layout.addWidget(self.color_field)

        # Feature name
        self.feature_label = QLabel("Feature", self)
        self.feature_input = QLineEdit(self)
        panel_layout.addWidget(self.feature_label)
        panel_layout.addWidget(self.feature_input)

        # Buttons
        self.go_button = QPushButton("GO", self)
        self.complete_button = QPushButton("COMPLETE", self)

        self.go_button.clicked.connect(self.on_go_button_click)
        self.complete_button.clicked.connect(self.on_complete_button_click)

        panel_layout.addWidget(self.go_button)
        panel_layout.addWidget(self.complete_button)

        # Add components to main layout
        main_layout.addWidget(self.image_label)
        main_layout.addWidget(self.panel)

        # Set up the window
        self.setLayout(main_layout)

        # Draw the rectangles initially
        self.draw_selected_rectangle()

    def mouse_click_event(self, event: QMouseEvent):
        """Handle mouse click on the image."""
        x, y = event.x(), event.y()
        print(f"Mouse clicked at ({x}, {y})")

        # Simulate grabbing pixel data (For now, we don't process the image itself)
        self.rgb = QColor(255, 0, 0).rgb()  # Example RGB (Red)

        self.color_field.setText(f"({self.rgb})")  # Set the color field to the RGB value

        # Check if inside the red rectangle
        if 300 < x < 380 and 220 < y < 300:
            self.selected_point = (x, y)
            self.color_field.setStyleSheet("background-color: red;")
            self.rgb = QColor(255, 0, 0).rgb()  # Set color to red
        # Check if inside the blue rectangle
        elif 450 < x < 550 and 150 < y < 250:
            self.selected_point = (x, y)
            self.color_field.setStyleSheet("background-color: blue;")
            self.rgb = QColor(0, 0, 255).rgb()  # Set color to blue
        else:
            self.selected_point = None
            self.color_field.setStyleSheet("background-color: white;")

    def mouse_move_event(self, event: QMouseEvent):
        """Handle mouse move over the image."""
        # No need to draw anything while moving the mouse since the rectangle is already present
        pass

    def draw_selected_rectangle(self):
        """Draw the rectangle around the selected point initially."""
        # Get the pixmap and prepare to draw on it
        pixmap = self.image_label.pixmap()
        painter = QPainter(pixmap)

        # Set the painter to use red color for the border
        painter.setPen(QColor(255, 0, 0))  # Red color for the border
        painter.setBrush(QColor(255, 0, 0, 50))  # Semi-transparent red brush for fill
        
        # Draw the first rectangle (Red rectangle)
        painter.drawRect(QRect(300, 220, 80, 80))  # Example 80x80 rectangle at (300, 220)

        # Set the painter to use blue color for the second rectangle
        painter.setPen(QColor(0, 0, 255))  # Blue color for the border
        painter.setBrush(QColor(0, 0, 255, 50))  # Semi-transparent blue brush for fill

        # Draw the second rectangle (Blue rectangle)
        painter.drawRect(QRect(450, 150, 100, 100))  # Example 100x100 rectangle at (450, 150)

        # End the drawing
        painter.end()

        # Trigger a repaint of the image label to reflect the changes
        self.image_label.repaint()

    def on_go_button_click(self):
        """Handle 'GO' button click."""
        feature_name = self.feature_input.text()
        if not feature_name:
            print("Feature name is required!")
            return

        if self.rgb == 0:
            print("Please select a feature.")
            return

        if self.rgb in self.frgb:
            print(f"Feature already assigned to color {self.rgb}")
            return

        # Save the feature and its color
        self.frgb.append(self.rgb)
        self.fea.append(feature_name)
        self.count += 1

        print(f"Feature '{feature_name}' assigned to color {self.rgb}")

        # Clear fields
        self.feature_input.clear()
        self.color_field.clear()

    def on_complete_button_click(self):
        """Handle 'COMPLETE' button click."""
        if self.count == 2:
            for i in range(2):
                self.feature_combobox.addItem(self.fea[i])
                print(f"{self.frgb[i]} is for the feature {self.fea[i]}")
        else:
            print("Please assign 2 features before completing.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Page1()
    window.show()
    sys.exit(app.exec_())
