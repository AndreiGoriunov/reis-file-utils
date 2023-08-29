import PySimpleGUI as sg

from reis_file_utils.thread_handlers import folder_organizer_handler
from reis_file_utils.window_config import *


class GUI:
    def __init__(self):
        self.current_window = MAIN_MENU
        self.location = None
        self._create_new_window()
        self._main_loop()

    def _create_new_window(self):
        window_details = LAYOUT_CONFIG.get(self.current_window, {})
        title = window_details.get("title", "")
        layout = window_details.get("layout", [])()
        # Create the window without specifying the location
        if self.location:
            self.window = sg.Window(title, layout, location=self.location)
        else:
            self.window = sg.Window(title, layout)

    def _main_loop(self):
        while True:
            self.event, self.values = self.window.read()
            if not self.event == sg.WINDOW_CLOSED:
                self.location = self.window.CurrentLocation()
            # Handle the event
            if self.event == sg.WINDOW_CLOSED:
                self.window.close()
                break
            elif self.event == "Organize":
                folder_organizer_handler(self.window, self.values)
            elif self.event in LAYOUT_CONFIG:
                self.window.close()
                self.current_window = self.event
                self._create_new_window()
            else:
                pass
