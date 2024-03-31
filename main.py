import os
import shutil


class CommandPrompt:
    def display_help(self):
        print("""
Available commands:
DIR             Displays a list of files and subdirectories in a directory.
CD              Changes the current directory.
COPY            Copies one or more files to another location.
DEL             Deletes one or more folders.
DELFL           Deletes one or more files.
MKDIR           Creates a new directory.
MKFL            Creates a new File.
MOVE            Moves one or more files from one directory to another.
REN             Renames a file or directory.
CLS             Clears the screen.
EXIT            Quits the program.
HELP            Provides help information for commands.
""")

    def display_directory_contents(self, directory):
        print("Directory of", directory)
        for item in os.listdir(directory):
            print(item)

    def change_directory(self, directory):
        try:
            os.chdir(directory)
            print("Directory changed to", os.getcwd())
        except FileNotFoundError:
            print("Directory not found.")

    def copy_files(self, source, destination):
        try:
            shutil.copy(source, destination)
            print("File copied successfully.")
        except FileNotFoundError:
            print("File not found.")

    def delete_dir(self, file_path):
        try:
            i = input(f"Are you sure to delete this Folder '{
                      file_path}' ? Y,N: ")
            if i == 'Y':
                os.rmdir(file_path)
            else:
                return
            print("Folder deleted successfully.")
        except FileNotFoundError:
            print("Folder not found.")

    def delete_file(self, file_path):
        try:
            i = input(f"Are you sure to delete this file {file_path} ? Y,N: ")
            if i == 'Y':
                os.remove(file_path)
            else:
                return
            print("File deleted successfully.")
        except FileNotFoundError:
            print("File not found.")

    def create_directory(self, directory):
        try:
            os.mkdir(directory)
            print("Directory created successfully.")
        except FileExistsError:
            print("Directory already exists.")

    def create_file(self, filename):
        try:
            if os.path.exists(filename):
                print(f"The file '{filename}' already exists.")
            else:
                with open(filename, 'w') as file:
                    file.write("")
            print(f"File '{filename}' created successfully.")
        except FileExistsError:
            print("Directory already exists.")

    def move_file(self, source, destination):
        try:
            shutil.move(source, destination)
            print("moved successfully.")
        except FileNotFoundError:
            print("not found.")

    def rename_file(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print("renamed successfully.")
        except FileNotFoundError:
            print("not found.")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run_command_prompt(self):

        while True:
            try:
                command = input(">>>").upper()
                if command == "HELP":
                    self.display_help()
                elif command == "DIR":
                    self.display_directory_contents(os.getcwd())
                elif command.startswith("CD "):
                    directory = command[3:]
                    self.change_directory(directory)
                elif command.startswith("COPY "):
                    source, destination = command[5:].split()
                    self.copy_files(source, destination)
                elif command.startswith("DEL "):
                    file_path = command[4:]
                    self.delete_dir(file_path)
                elif command.startswith('DELFL '):
                    file_path = command[6:]
                    self.delete_file(file_path)
                elif command.startswith("MKDIR "):
                    directory = command[6:]
                    self.create_directory(directory)
                elif command.startswith("MKFL "):
                    file = command[5:]
                    self.create_file(file)
                elif command.startswith("MOVE "):
                    source, destination = command[5:].split()
                    self.move_file(source, destination)
                elif command.startswith("REN "):
                    old_name, new_name = command[4:].split()
                    self.rename_file(old_name, new_name)
                elif command == "CLS":
                    self.clear_screen()
                elif command == "EXIT":
                    break
                else:
                    print("Invalid command. Type 'HELP' for assistance.")
            except:
                print('error')


if __name__ == "__main__":
    command_prompt = CommandPrompt()
    command_prompt.run_command_prompt()
