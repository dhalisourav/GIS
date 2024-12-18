# 8. Write a program to draw line(4cm,5cm, 6cm) in three different places and point into a GIS image so that they can form a triangle. 
import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk

class TriangleDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing on an image")
        self.root.geometry("1024x738")

        # Load the image using Pillow
        self.image = Image.open("prasun.jpg")
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a canvas to display the image
        self.canvas = Canvas(self.root, width=self.image.width, height=self.image.height)
        self.canvas.pack()

        # Add the image to the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Bind mouse events
        self.canvas.bind("<ButtonPress-1>", self.mouse_pressed)
        self.canvas.bind("<B1-Motion>", self.mouse_dragged)

        # Create a label for debugging or other purposes
        self.label = tk.Label(self.root, text="Mouse Events")
        self.label.pack()

    def mouse_pressed(self, event):
        # Draw the triangle when the mouse is pressed
        self.draw_triangle()

    def mouse_dragged(self, event):
        # Optionally handle dragging, currently no action for dragging
        pass

    def draw_triangle(self):
        # Draw the triangle (red, green, blue lines as in original code)
        self.canvas.create_line(300, 300, 200, 300, fill="red", width=2)
        self.canvas.create_line(200, 300, 200, 500, fill="green", width=2)
        self.canvas.create_line(300, 300, 200, 500, fill="blue", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleDrawingApp(root)
    root.mainloop()
