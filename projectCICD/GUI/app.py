""" This file hosts the GUI elements

"""

import customtkinter
# import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Set the name of the window
        self.title("image_example.py")
        self.resizable(width=True, height=True)

        # Set the layout of the window (1x2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # this a test to track my commits
