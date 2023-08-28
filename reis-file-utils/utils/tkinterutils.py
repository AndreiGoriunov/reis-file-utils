import tkinter as tk
from tkinter import filedialog
from typing import Callable, List, TypedDict


def get_root():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    root.attributes("-topmost", True)
    return root


def select_folder(prompt: str = "Select a folder") -> str:
    root = get_root()
    folder_path = filedialog.askdirectory(title=prompt, parent=root)
    root.destroy()
    return folder_path


def select_file(prompt: str = "Select a file") -> str:
    root = get_root()
    file_path = filedialog.askopenfilename(title=prompt, parent=root)
    root.destroy()
    return file_path


class Widget(TypedDict):
    display_name: str
    function: Callable


class ReisGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        colors = {"bg":"#27374D"}
        self.title("Rei's File Utils")
        self["background"] = colors.get("bg")

    def create_widgets(self, widgets: List[Widget]):
        for widget in widgets:
            display_name = widget.get("display_name")
            fucntion = widget.get("function")
            btn = tk.Button(
                self, text=display_name, command=fucntion, width=30, height=2
            )
            btn.pack(pady=10)

        exit_btn = tk.Button(
            self, text="Exit", command=self.quit_app, width=30, height=2
        )
        exit_btn.pack(pady=20)

    def quit_app(self):
        self.destroy()

    def run(self):
        self.mainloop()
