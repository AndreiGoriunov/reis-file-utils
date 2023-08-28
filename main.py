from reis-file-utils import folder_organizer, translitiration, delete_empty_dirs
from reis-file-utils.utils.tkinterutils import ReisGUI


def main_menu():
    print("Rei's KXA File Utils")
    print("===========================")
    print("1. Transliterate File Names")
    print("2. Folder Organizer")
    print("3. Delete Empty Dirs")
    print("4. Exit")
    print("===========================")

    while True:
        choice: str = input("Enter util # to use: ")
        if choice == "1":
            print("Transliterate File Names")
            translitiration.run()
            break
        if choice == "2":
            print("Folder Organizer")
            folder_organizer.run()
            break
        if choice == "3":
            print("Delete Empty Directories")
            delete_empty_dirs.run()
            break
        if choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # try:
    #     main_menu()
    # except PermissionError as e:
    #     print("Permission Error. Try running 'reis_file_utils.exe' with admin rights.\n", e)
    # input("Enter any key to continue...")
    app = ReisGUI()
    app.create_widgets(
        [
            {"display_name": "Transliteraion", "function": translitiration.run},
            {"display_name": "Folder Organizer", "function": folder_organizer.run},
            {"display_name": "Delete Empty Directories","function": delete_empty_dirs.run}
        ]
    )
    app.run()
