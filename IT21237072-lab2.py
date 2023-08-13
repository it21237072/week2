#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("User Profile")

# Create labels and input components for user profile
label_name = ttk.Label(root, text="Name:")
label_age = ttk.Label(root, text="Age:")
entry_name = ttk.Entry(root)
entry_age = ttk.Entry(root)

# Create function to browse and display profile image
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((100, 100))  # Resize image for display
        photo = ImageTk.PhotoImage(image=image)
        label_image.config(image=photo)
        label_image.image = photo

# Button for browsing profile image
button_browse = ttk.Button(root, text="Browse Image", command=browse_image)

# Layout input components
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name.grid(row=0, column=1, padx=10, pady=5)
label_age.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_age.grid(row=1, column=1, padx=10, pady=5)
button_browse.grid(row=2, columnspan=2, padx=10, pady=10)

# Create label for displaying profile image
label_image = ttk.Label(root)
label_image.grid(row=3, columnspan=2, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()

# OpenCV image manipulation
input_image = cv2.imread("profile_image.png")

# Access image properties
height, width, channels = input_image.shape
print(f"Image Properties - Height: {height}, Width: {width}, Channels: {channels}")

# Access and modify pixel values
x, y = 100, 150
pixel_value = input_image[y, x]
input_image[y, x] = [255, 0, 0]  # Modify pixel value to blue

# Resize the image
new_width, new_height = 200, 300
resized_image = cv2.resize(input_image, (new_width, new_height))
cv2.imwrite("resized_image.jpg", resized_image)

# Rotate the resized image
rotation_angle = 90
rotated_image = cv2.rotate(resized_image, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("rotated_image.jpg", rotated_image)

# Pillow image manipulation
input_image_pillow = Image.open("profile_image.png")
input_image_pillow.show()

# Print image information
print("Image Information:")
print("Filename:", input_image_pillow.filename)
print("Format:", input_image_pillow.format)
print("Size:", input_image_pillow.size)
print("Width:", input_image_pillow.width)
print("Height:", input_image_pillow.height)

# Print color mode
print("Color Mode:", input_image_pillow.mode)

# Rotate the image
rotated_image_pillow = input_image_pillow.rotate(180)
rotated_image_pillow.show()

