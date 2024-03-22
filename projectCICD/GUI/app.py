""" This file hosts the GUI elements

"""

from typing import Tuple
import customtkinter
import os
from PIL import Image


class AppLogos(customtkinter.CTkImage):
    def __init__(self):
        super().__init__()
        # Finding the path of the logos
        current_path = os.path.dirname(os.path.realpath(__file__))
        concept_cicd_dir = os.path.abspath(os.path.join(current_path, os.pardir))
        image_path = os.path.join(concept_cicd_dir, "data", "Images", "Logos")
        path_to_images = Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png"))
        # initializing images
        self.logo_image = path_to_images
        self.logo_image.size(26, 26)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Set the name of the window
        self.title("image_example.py")
        self.resizable(width=True, height=True)

        # Set the layout of the window (1x2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # new frame for testing images
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # new images objects
        self.all_logos = AppLogos()
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Image Example", image=self.all_logos.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
