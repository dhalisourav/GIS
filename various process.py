# 4. Write a program to show various process to open GIS image into desktop (at least three) with resizing it mark some por on of the image with some color and point it with a ribute. 
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import colorchooser
from PIL import Image, ImageTk
import numpy as np

class Option3App:
    def __init__(self, root):
        self.root = root
        self.root.title("Style 3 Image Selector")
        
        self.count = 0
        self.features = []
        self.feature_colors = []
        
        # Load image
        self.image_path = "prasun.jpg"  # Provide your image path here
        self.image = Image.open(self.image_path)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.img_width, self.img_height = self.image.size
        
        # Create the main frame for image display
        self.canvas = tk.Canvas(self.root, width=self.img_width, height=self.img_height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        self.canvas.pack()
        
        # Feature selection frame (right panel)
        self.panel = tk.Frame(self.root, width=250, height=self.img_height, bg="#A0A0DC", relief="sunken")
        self.panel.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.create_feature_selection_ui()
        
        # Bind mouse events for color picking
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Motion>", self.on_mouse_move)
    
    def create_feature_selection_ui(self):
        """Create the feature selection UI components."""
        label = tk.Label(self.panel, text="Feature Selection", font=("Verdana", 14, "bold"), fg="green")
        label.pack(pady=10)
        
        self.cb1a = tk.OptionMenu(self.panel, tk.StringVar(), "Choose a Feature")
        self.cb1a.config(width=20, height=1)
        self.cb1a.pack(pady=5)
        
        self.color_label = tk.Label(self.panel, text="Color", font=("Verdana", 10), fg="green")
        self.color_label.pack(pady=5)
        
        self.color_entry = tk.Entry(self.panel, state="readonly", width=20, bg="white")
        self.color_entry.pack(pady=5)
        
        self.feature_name_label = tk.Label(self.panel, text="Feature Name", font=("Verdana", 10), fg="green")
        self.feature_name_label.pack(pady=5)
        
        self.feature_name_entry = tk.Entry(self.panel, width=20)
        self.feature_name_entry.pack(pady=5)
        
        self.go_button = tk.Button(self.panel, text="GO", bg="pink", command=self.assign_feature)
        self.go_button.pack(pady=5)
        
        self.complete_button = tk.Button(self.panel, text="COMPLETE", bg="yellow", command=self.complete_features)
        self.complete_button.pack(pady=5)
    
    def on_click(self, event):
        """Handles mouse click to select color and assign features."""
        x, y = event.x, event.y
        pixel = self.image.getpixel((x, y))
        
        # Check if the click is inside specific polygon areas (you can define your own areas)
        # Example: red, green, blue polygons
        # Polygon coordinates are hardcoded for illustration
        polygon1 = [(130, 400), (180, 420), (150, 380)]
        polygon2 = [(300, 300), (340, 300), (340, 260), (300, 260)]
        polygon3 = [(200, 280), (230, 280), (240, 260), (230, 240), (210, 235), (180, 250)]
        
        contain1 = self.point_in_polygon(x, y, polygon1)
        contain2 = self.point_in_polygon(x, y, polygon2)
        contain3 = self.point_in_polygon(x, y, polygon3)
        
        if contain1:
            color = "red"
            self.color_entry.config(bg="red")
        elif contain2:
            color = "green"
            self.color_entry.config(bg="green")
        elif contain3:
            color = "blue"
            self.color_entry.config(bg="blue")
        else:
            color = self.rgb_to_hex(pixel)
            self.color_entry.config(bg=color)
        
        self.selected_color = color
        self.selected_pixel = pixel
        
        # Display RGB value in the console
        print(f"Selected Color: {color} - RGB: {pixel}")
    
    def on_mouse_move(self, event):
        """Displays color highlights on mouse move."""
        x, y = event.x, event.y
        self.canvas.delete("highlight")
        
        # Draw highlight polygons (same as in Java code)
        self.canvas.create_polygon([(130, 400), (180, 420), (150, 380)], outline="red", fill="red", tags="highlight")
        self.canvas.create_polygon([(300, 300), (340, 300), (340, 260), (300, 260)], outline="green", fill="green", tags="highlight")
        self.canvas.create_polygon([(200, 280), (230, 280), (240, 260), (230, 240), (210, 235), (180, 250)], outline="blue", fill="blue", tags="highlight")
    
    def assign_feature(self):
        """Assigns the feature and validates inputs."""
        feature_name = self.feature_name_entry.get()
        
        if len(feature_name) == 0:
            messagebox.showerror("Error", "Please enter a feature name.")
            return
        
        if self.count >= 3:
            messagebox.showinfo("Completed", "You have assigned 3 features already.")
            return
        
        if self.selected_color == "white" or not hasattr(self, 'selected_color'):
            messagebox.showerror("Error", "Please select a feature area on the image.")
            return
        
        if feature_name in self.features:
            messagebox.showerror("Error", "Feature name already used.")
            return
        
        self.features.append(feature_name)
        self.feature_colors.append(self.selected_color)
        self.cb1a['menu'].add_command(label=feature_name)
        
        self.count += 1
        self.feature_name_entry.delete(0, tk.END)
        self.color_entry.config(bg="white")
    
    def complete_features(self):
        """Displays a message with all assigned features."""
        if self.count < 3:
            messagebox.showwarning("Incomplete", "You need to assign at least 3 features.")
            return
        
        assigned_features = "\n".join([f"{color}: {name}" for name, color in zip(self.features, self.feature_colors)])
        messagebox.showinfo("Assigned Features", assigned_features)
    
    def point_in_polygon(self, x, y, polygon):
        """Checks if a point (x, y) is inside the given polygon."""
        n = len(polygon)
        inside = False
        p1x, p1y = polygon[0]
        for i in range(n + 1):
            p2x, p2y = polygon[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside
    
    def rgb_to_hex(self, rgb):
        """Converts RGB tuple to hex color."""
        return '#%02x%02x%02x' % rgb


if __name__ == "__main__":
    root = tk.Tk()
    app = Option3App(root)
    root.mainloop()
