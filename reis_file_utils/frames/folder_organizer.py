import os
import shutil

from reis_file_utils.utils.reis_gui import AppFrame
from ..utils.reis_gui import AppGUI, Widget
from ..utils.color_printer import Cprint
from ..utils.yamlutils import load_yaml


def get_unique_filename(target_folder, filename):
    base_name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(target_folder, new_filename)):
        new_filename = f"{base_name}_{counter}{ext}"
        counter += 1

    return new_filename


def organize_files(category_folder, extensions, folder_path):
    if not extensions:
        return
    for ext in extensions:
        for file in os.listdir(folder_path):
            if file.lower().endswith(ext.lower()):
                base_name, file_ext = os.path.splitext(file)
                lowercase_ext = file_ext.lower()
                new_filename = f"{base_name}{lowercase_ext}"
                unique_filename = get_unique_filename(category_folder, new_filename)
                shutil.move(
                    os.path.join(folder_path, file),
                    os.path.join(category_folder, unique_filename),
                )


def organize_folder(yaml_map: dict, folder_path: str):
    for category, value in yaml_map.items():
        if isinstance(value, list):
            category_folder = os.path.join(folder_path, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
            organize_files(category_folder, value, folder_path)
        elif isinstance(value, dict):
            for subcategory, extensions in value.items():
                subcategory_folder = os.path.join(folder_path, category, subcategory)
                if not os.path.exists(subcategory_folder):
                    os.makedirs(subcategory_folder)
                organize_files(subcategory_folder, extensions, folder_path)


# def run():
#     yaml_path = AppGUI.select_file("Select yaml mapping file")
#     if yaml_path == "":
#         return
#     folder_path = AppGUI.select_folder("Select folder to organize")
#     if folder_path == "":
#         return
#     userApproved = (
#         True
#         if input(
#             f"Using map from '{yaml_path}' to organize files in '{folder_path}' (Y/N):\n"
#         ).upper()
#         == "Y"
#         else False
#     )

#     if userApproved:
#         yaml_map = load_yaml(yaml_path)
#         organize_folder(yaml_map, folder_path)
#         Cprint.print("Folder organized.", Cprint.GREEN)


class FolderOrganizerFrame(AppFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        widgets = [
            Widget(widget_type="file_prompt", display_name="Select map file:"),
            Widget(widget_type="folder_prompt", display_name="Select folder:"),
            Widget(widget_type="button", display_name="Organize", function=None)
        ]
        self.create_widgets(widgets)

    