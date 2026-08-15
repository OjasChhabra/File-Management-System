import os

FILE_OPTION = ["Read", "Update", "Delete", "Rename", "Back"]
FOLDER_OPTION = ["Open", "Rename", "Delete", "Back"]


class Function:
    def __init__(self):
        self.path = "home"
        self.contents = []

    def display_contents(self):
        if not os.path.isdir(self.path):
            print("Current location does not exist.")
            self.path = "home"
            return

        print(f"\n🏠 {self.path}")
        self.contents = os.listdir(self.path)

        for i, item in enumerate(self.contents, start=1):
            item_path = os.path.join(self.path, item)

            if os.path.isdir(item_path):
                emoji = "📂"
            elif os.path.isfile(item_path):
                emoji = "📄"
            else:
                emoji = "❓"

            print(f"{i}. {emoji} {item}")

        if self.path != "home":
            self.contents.append("Back")
            print(f"{len(self.contents)}. 🔙 Back")

    def function(self, num):
        if not self.contents:
            return

        if num not in range(1, len(self.contents) + 1):
            print("Enter a Valid Response")
            return

        selected = self.contents[num - 1]

        if selected == "Back":
            self.back()
            return

        selected_path = os.path.join(self.path, selected)

        if os.path.isfile(selected_path):
            self.file_function(selected_path, selected)
        elif os.path.isdir(selected_path):
            self.folder_function(selected_path, selected)
        else:
            print("The selected item no longer exists.")

    def back(self):
        if self.path != "home":
            self.path = os.path.dirname(self.path)

    def file_function(self, file_path, file_name):
        print(f"\nWhat do you want to do with 📄 {file_name}")
        for i, option in enumerate(FILE_OPTION, start=1):
            print(f"{i}. {option}")

        try:
            choice = int(input("What function do you want to do (Enter the num): "))
        except ValueError:
            print("Enter a Valid Response")
            return

        if choice == 1:
            self.read_file(file_path)
        elif choice == 2:
            self.update_file(file_path)
        elif choice == 3:
            self.delete_file(file_path)
            self.path = os.path.dirname(file_path)
        elif choice == 4:
            self.rename_file(file_path)
            self.path = os.path.dirname(file_path)
        elif choice == 5:
            self.path = os.path.dirname(file_path)
        else:
            print("Enter a Valid Response")

    def folder_function(self, folder_path, folder_name):
        print(f"\nWhat do you want to do with 📂 {folder_name}")
        for i, option in enumerate(FOLDER_OPTION, start=1):
            print(f"{i}. {option}")

        try:
            choice = int(input("What function do you want to do (Enter the num): "))
        except ValueError:
            print("Enter a Valid Response")
            return

        if choice == 1:
            self.path = folder_path
        elif choice == 2:
            self.rename_file(folder_path)
            self.path = os.path.dirname(folder_path)
        elif choice == 3:
            self.delete_folder(folder_path)
            self.path = os.path.dirname(folder_path)
        elif choice == 4:
            self.path = os.path.dirname(folder_path)
        else:
            print("Enter a Valid Response")

    def read_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read()
            print("\n----- FILE CONTENT -----")
            print(content if content else "(empty file)")
            print("------------------------")
            input("Press Enter to continue...")
        except OSError as error:
            print(f"Could not read the file: {error}")

    def update_file(self, file_path):
        new_content = input("Enter the new content: ")
        try:
            with open(file_path, "w") as file:
                file.write(new_content)
            print("File updated successfully.")
        except OSError as error:
            print(f"Could not update the file: {error}")

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
            print("File deleted successfully.")
        except OSError as error:
            print(f"Could not delete the file: {error}")

    def rename_file(self, old_path):
        new_name = input("Enter the new name: ").strip()
        if not new_name:
            print("Name cannot be empty.")
            return

        new_path = os.path.join(os.path.dirname(old_path), new_name)

        if os.path.exists(new_path):
            print("An item with that name already exists.")
            return

        try:
            os.rename(old_path, new_path)
            print("Renamed successfully.")
        except OSError as error:
            print(f"Could not rename the item: {error}")

    def delete_folder(self, folder_path):
        try:
            if os.listdir(folder_path):
                print("Folder is not empty. Empty it before deleting it in V1.")
                return
            os.rmdir(folder_path)
            print("Folder deleted successfully.")
        except OSError as error:
            print(f"Could not delete the folder: {error}")
