import os
import shutil



def display_help():
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


def display_directory_contents(directory):
    print("Directory of", directory)
    for item in os.listdir(directory):
        print(item)


def change_directory(directory):
    try:
        os.chdir(directory)
        print("Directory changed to", os.getcwd())
    except FileNotFoundError:
        print("Directory not found.")


def copy_files(source, destination):
    try:
        shutil.copy(source, destination)
        print("File copied successfully.")
    except FileNotFoundError:
        print("File not found.")


def delete_dir(file_path):
    try:
        os.rmdir(file_path)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")


def delete_file(file_path):
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")


def create_directory(directory):
    try:
        os.mkdir(directory)
        print("Directory created successfully.")
    except FileExistsError:
        print("Directory already exists.")


def create_file(filename):
    try:
        if os.path.exists(filename):
            print(f"The file '{filename}' already exists.")
        else:
            with open(filename, 'w') as file:
                file.write("")
        print(f"File '{filename}' created successfully.")
    except FileExistsError:
        print("Directory already exists.")


def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print("File moved successfully.")
    except FileNotFoundError:
        print("File not found.")


def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print("File renamed successfully.")
    except FileNotFoundError:
        print("File not found.")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    while True:
        command = input(">>>").upper()
        if command == "HELP":
            display_help()
        elif command == "DIR":
            display_directory_contents(os.getcwd())
        elif command.startswith("CD "):
            directory = command[3:]
            change_directory(directory)
        elif command.startswith("COPY "):
            source, destination = command[5:].split()
            copy_files(source, destination)
        elif command.startswith("DEL "):
            file_path = command[4:]
            delete_dir(file_path)
        elif command.startswith('DELFL '):
            file_path = command[6:]
            delete_file(file_path)
        elif command.startswith("MKDIR "):
            directory = command[6:]
            create_directory(directory)
        elif command.startswith("MKFL "):
            file = command[5:]
            create_file(file)
        elif command.startswith("MOVE "):
            source, destination = command[5:].split()
            move_file(source, destination)
        elif command.startswith("REN "):
            old_name, new_name = command[4:].split()
            rename_file(old_name, new_name)
        elif command == "CLS":
            clear_screen()
        elif command == "EXIT":
            break
        else:
            print("Invalid command. Type 'HELP' for assistance.")
