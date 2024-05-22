""""
Program: favicon_converter.py
Author: khilfienite
This program is used to fetch an image from specified URL and store it as a favicon image in this directory.
"""

import tkinter as tk
import requests
from os import remove

from PIL import Image
  

def submit_data():
  """
  Fetch and store image as ICO file.
  """
  with open("favicon.jpg", "wb") as handle:
    img = requests.get(entry_widget1.get(), stream=True).content
    handle.write(img)

  with Image.open("favicon.jpg", "r") as favicon:
    favicon.save("favicon.ico")
  
  # Clear the entry widgets after data is submitted 
  remove("favicon.jpg")
  app.destroy()


# GUI setup
app = tk.Tk()   

# Main window
canvas_widget = tk.Canvas(app, width=500, height=500) 
canvas_widget.pack() 

# Label
label_widget1 = tk.Label(app, text="Image URL: ") 
canvas_widget.create_window(150, 160, window=label_widget1) 

# Input field
entry_widget1 = tk.Entry(app) 
canvas_widget.create_window(300, 160, window=entry_widget1, width=200)
  
# Submit button
button_widget = tk.Button(text='Submit', command=submit_data) 
canvas_widget.create_window(225, 250, window=button_widget)

app.mainloop()
