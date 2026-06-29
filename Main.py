# Version 3 of this application

import tkinter as Gui
import ctypes
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
from PIL import Image, ImageTk

MainMenu = Gui.Tk()
width = MainMenu.winfo_screenwidth()
height = MainMenu.winfo_screenheight()
MainMenu.title("Custom Crosshairs")
MainMenu.geometry("500x600")
MainMenu.config(bg="#313131")

OverlayMenu = Gui.Toplevel()
OverlayMenu.overrideredirect(True)
OverlayMenu.attributes('-topmost', True, '-alpha', 0.5)
OverlayMenu.title("Overlay")

centerx = int(width / 2 - 200 / 2)
centery = int(height / 2 - 200 / 2)

OverlayMenu.geometry(f"200x200+{centerx}+{centery}")
OverlayMenu.withdraw()

OverlayMenu.update()

file_path = ""

Style = ttk.Style()

Style.theme_use('alt')
Style.configure("Button.TButton", foreground="#FFFFFF", font=('Impact', 16), padding=10, background="#6E6E6E")
Style.configure("ImportButton.TButton", foreground="#FFFFFF", font=('Impact', 16), padding=100, background="#6E6E6E")


def ChoseFile():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select a File",
        initialdir="/",
        filetypes=[("Images .png", "*.png"), ("All files", "*.*")]
)

def VerifyFile():
    if file_path:
        print(Path(file_path).name)
        global ImageDisplay
        ImageDisplay = Gui.PhotoImage(file=(Path(file_path)))
        ImageLabel = ttk.Label(OverlayMenu, image=ImageDisplay)
        ImageLabel.pack()
        OverlayMenu.deiconify()

ImportButton = ttk.Button(MainMenu,text="Import new picture",command=lambda: ChoseFile(),style="ImportButton.TButton")
ImportButton.pack(padx=10, pady=150)

UpdateButton = ttk.Button(MainMenu,text="Update",command=lambda: VerifyFile(),style="Button.TButton")
UpdateButton.pack(side="bottom", anchor="s", padx=10, pady=0) 


print(width)
print(height)
MainMenu.mainloop()
