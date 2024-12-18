# 6. Write a program to assign three features in RS-GIS image. Compute how many segments has features of a type.
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import math

class Page1:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Association Page")
        
        self.image_path = "session1.gif"
        self.image = Image.open(self.image_path)
        self.width, self.height = self.image.size
        self.pixels = list(self.image.getdata())  
        
        self.rgb = 0
        self.frgb = []
        self.fea = []
        self.count = 0
        self.ccb = 0
        
        self.image_array = [[0 for _ in range(self.width)] for _ in range(self.height)]

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0, rowspan=4)

        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        self.canvas.bind("<Button-1>", self.mouse_clicked)

        self.panel = tk.Frame(self.root)
        self.panel.grid(row=0, column=1, padx=10, pady=10)

        self.feat_label = tk.Label(self.panel, text="Feature Selection", font=("Verdana", 12), fg="green")
        self.feat_label.grid(row=0, column=0, pady=5)
        
        self.cb1a = ttk.Combobox(self.panel, state="readonly")
        self.cb1a.set("Select Feature")
        self.cb1a.grid(row=1, column=0, pady=5)
        
        self.color_label = tk.Label(self.panel, text="Color", font=("Verdana", 10), fg="green")
        self.color_label.grid(row=2, column=0, pady=5)
        
        self.color_display = tk.Entry(self.panel, state="readonly", width=10)
        self.color_display.grid(row=3, column=0, pady=5)
  
        self.feature_label = tk.Label(self.panel, text="Feature", font=("Verdana", 10), fg="green")
        self.feature_label.grid(row=4, column=0, pady=5)
        
        self.feature_entry = tk.Entry(self.panel, width=10)
        self.feature_entry.grid(row=5, column=0, pady=5)
        

        self.go_button = tk.Button(self.panel, text="GO", command=self.go_button_clicked)
        self.go_button.grid(row=6, column=0, pady=5)
        
        self.complete_button = tk.Button(self.panel, text="COMPLETE", command=self.complete_button_clicked)
        self.complete_button.grid(row=7, column=0, pady=5)
        
        self.find_button = tk.Button(self.panel, text="Find No of segments", command=self.find_segments)
        self.find_button.grid(row=8, column=0, pady=5)
        
        self.segment_count = tk.Entry(self.panel, state="readonly", width=15)
        self.segment_count.grid(row=9, column=0, pady=5)
        
        self.segment_count.grid_forget()  
        self.find_button.grid_forget()  

    def mouse_clicked(self, event):
        x, y = event.x, event.y
        pixel_index = y * self.width + x
        self.rgb = self.pixels[pixel_index]

        self.color_display.config(bg=f'#{self.rgb:06x}')

        for i in range(self.count):
            if self.rgb == self.frgb[i]:
                messagebox.showinfo("Feature Info", f"Feature {self.fea[i]} already selected")
                return
        
    def go_button_clicked(self):
        feature_name = self.feature_entry.get().strip()
        
        if feature_name == "":
            messagebox.showerror("Error", "Please assign a feature name.")
            return
        
        if self.rgb == 0:
            messagebox.showerror("Error", "Please select a feature color first.")
            return
        
        if feature_name in self.fea:
            messagebox.showerror("Error", "Feature name already used.")
            return
        
        self.fea.append(feature_name)
        self.frgb.append(self.rgb)
        self.count += 1
        
        self.feature_entry.delete(0, tk.END)
        self.color_display.config(bg="white")
  
        if self.count == 3:
            self.go_button.config(state=tk.DISABLED)
        
    def complete_button_clicked(self):
        if self.count == 3 and self.ccb == 0:
            for i in range(self.count):
                self.cb1a["values"] = (*self.cb1a["values"], self.fea[i])
            
            self.ccb = 1
            self.find_button.grid()
            self.segment_count.grid()
            
    def find_segments(self):
        if self.rgb == 0:
            messagebox.showerror("Error", "Please click on a feature to find the number of segments.")
            return
     
        visited = [[0] * self.width for _ in range(self.height)]
        labelled = [[0] * self.width for _ in range(self.height)]
        queue = []
        current_label = 1

        for i in range(self.height):
            for j in range(self.width):
                if self.pixels[i * self.width + j] == self.rgb:
                    self.image_array[i][j] = 1
                else:
                    self.image_array[i][j] = 0

        for i in range(self.height):
            for j in range(self.width):
                if self.image_array[i][j] == 1 and visited[i][j] == 0 and labelled[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
                    labelled[i][j] = current_label
                    current_label += 1
                    while queue:
                        x, y = queue.pop(0)
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < self.height and 0 <= ny < self.width and self.image_array[nx][ny] == 1 and visited[nx][ny] == 0:
                                    queue.append((nx, ny))
                                    visited[nx][ny] = 1
                                    labelled[nx][ny] = labelled[x][y]
        
        num_segments = current_label - 1
        self.segment_count.config(state="normal")
        self.segment_count.delete(0, tk.END)
        self.segment_count.insert(0, str(num_segments))
        self.segment_count.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    page1 = Page1(root)
    root.mainloop()
