import PySimpleGUI as sg

# Styles
TITLE = "Rei's File Utils"
TITLE_FONT = ("Any", 13, "bold")
BUTTON_FONT = ("Any", 13)
MIN_WIDTH = 50
ICON = "icon.ico"
# Pages
MAIN_MENU = "Main Menu"
FOLDER_ORGANIZER = "Folder Organizer"
FILE_TRANSLITERATION = "File Transliteration"
DELETE_EMPTY_DIRS = "Delete Empty Directories"


def main_menu_layout():
    return [
        [sg.Text(MAIN_MENU, font=TITLE_FONT)],
        [sg.Text("", size=(MIN_WIDTH, 0))],
        [sg.Button(FOLDER_ORGANIZER, font=BUTTON_FONT)],
        [sg.Button(FILE_TRANSLITERATION, font=BUTTON_FONT)],
        [sg.Button(DELETE_EMPTY_DIRS, font=BUTTON_FONT)],
    ]


def folder_organizer_layout():
    return [
        [sg.Text(FOLDER_ORGANIZER, font=TITLE_FONT)],
        [sg.Text("", size=(MIN_WIDTH, 0))],
        [
            sg.Text("Select a File:", size=(12, 1)),
            sg.InputText(key="-FILE-"),
            sg.FileBrowse(),
        ],
        [
            sg.Text("Select a Folder:", size=(12, 1)),
            sg.InputText(key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Button("Organize", key="Organize"),
            sg.Text("", size=(20, 0), key="-FEEDBACK-"),
        ],
        [sg.Button("Back", key=MAIN_MENU, font=BUTTON_FONT)],
    ]


def file_transliteration_layout():
    return [
        [sg.Text(FILE_TRANSLITERATION, font=TITLE_FONT)],
        [sg.Text("", size=(MIN_WIDTH, 0))],
        [sg.Button("Back", key=MAIN_MENU, font=BUTTON_FONT)],
    ]


def delete_empty_dirs_layout():
    return [
        [sg.Text(DELETE_EMPTY_DIRS, font=TITLE_FONT)],
        [sg.Text("", size=(MIN_WIDTH, 0))],
        [sg.Button("Back", key=MAIN_MENU, font=BUTTON_FONT)],
    ]


LAYOUT_CONFIG = {
    MAIN_MENU: {"title": TITLE, "layout": main_menu_layout},
    FOLDER_ORGANIZER: {"title": TITLE, "layout": folder_organizer_layout},
    FILE_TRANSLITERATION: {
        "title": TITLE,
        "layout": file_transliteration_layout,
    },
    DELETE_EMPTY_DIRS: {"title": TITLE, "layout": delete_empty_dirs_layout},
}
