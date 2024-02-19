### IMPORT SECTION ###

import os
import re
import shutil

### VARIABLE DECLARATION SECTION ###

TRANSLATION_TABLE = str.maketrans("ĄąĆćĘęŁłŃńÓóŚśŻżŹź", "AaCcEeLlNnOoSsZzZz")
SORTED_DIRECTORIES = ["images", "documents", "audio", "video", "archives"]
FILE_TYPES = {
    "images": ("JPEG", "PNG", 'JPG', 'SVG'),
    "video": ("AVI", "MP4", "MOV", "MKV"),
    "documents": ("DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"),
    "audio": ("MP3", "OGG", "WAV", "AMR"),
    "archives": ("ZIP", "GZ", "TAR"),
}
ARCHIVE_TYPES = {"ZIP": "zip", "GZ": "gztar", "TAR": "tar"}

### FUNCTIONS SECTION ###

def normalize(input_string, is_file = False):
    file_name = input_string
    if is_file:
        file_name, file_extension = os.path.splitext(input_string)                                 # Dla pliku odzielam nazwę od rozszerzenia
        file_extension = file_extension.lower().removeprefix(".")
    new_name = file_name.translate(TRANSLATION_TABLE)
    new_name = re.sub(r"[^A-Za-z0-9]", "_", new_name)
    if is_file:
        # print(f"      Renaming \"{file_name}.{file_extension}\" to \"{new_name}.{file_extension}\"")
        return ".".join((new_name, file_extension))                                                # Dla pliku zwraca nową nazwę z rozszerzeniem
    else:
        # print(f"      Renaming \"{file_name}\" to \"{new_name}\"")
        return new_name                                                                            # Dla folderu zwraca tylko nową nazwę

def create_sorted_directories(argument_path, sorted_directories):
    for sorted_directory in sorted_directories:
        directory_to_create = os.path.join(argument_path, sorted_directory)
        os.makedirs(directory_to_create, exist_ok = True)
        # print(f"    Creating folder -> {directory_to_create}")

def process_files(root, files, argument_path, FILE_TYPES, ARCHIVE_TYPES, SORTED_DIRECTORIES):
    if os.path.basename(root) in SORTED_DIRECTORIES and os.path.basename(root) != 'archives':      # Quick and dirty solution. Still need to work on this. Might need to walk archives and extract separately. 
        return
    for file in files:
        old_file_name_path = os.path.join(root, file)
        new_file_name = normalize(file, True)
        new_file_name_path = os.path.join(root, new_file_name)
        os.rename(old_file_name_path, new_file_name_path)
        file_name, file_extension = os.path.splitext(new_file_name)
        file_extension = file_extension.upper().removeprefix(".")

        for extension_folder, known_extensions in FILE_TYPES.items():
            if file_extension in known_extensions:
                destination_directory = os.path.join(argument_path, extension_folder)
                os.makedirs(destination_directory, exist_ok=True)
                shutil.move(new_file_name_path, os.path.join(destination_directory, new_file_name))                         # Move the known file
                # print(f"        Moving \"{new_file_name}\" to \"{destination_directory}\"")

        if file_extension.upper() in ARCHIVE_TYPES:
            archive_format = ARCHIVE_TYPES[file_extension]
            if os.path.isfile(new_file_name_path):
                destination_directory = os.path.join(argument_path, "archives")
                os.makedirs(destination_directory, exist_ok=True)
                shutil.unpack_archive(new_file_name_path, os.path.join(destination_directory, file_name), archive_format)   # Unpack the known archive
                # print(f"        Unpacking \"{file}\" to \"{destination_directory}\"")

def process_directories(root, directories, SORTED_DIRECTORIES):
    for directory in directories:
            if directory in SORTED_DIRECTORIES:
                continue
            old_directory_name = os.path.join(root, directory)
            if os.listdir(old_directory_name):
                new_directory_name = os.path.join(root, normalize(directory))
                os.rename(old_directory_name, new_directory_name)
                # print(f"      Rename directory \"{old_directory_name}\" to \"{new_directory_name}\"")
                # sort_folders(new_directory_name)
            else:
                os.rmdir(old_directory_name)
                # print(f"      deleting directory \"{old_directory_name}\"")

def sort_folders(argument_path):
    create_sorted_directories(argument_path, SORTED_DIRECTORIES)
    for root, directories, files in os.walk(argument_path):                                      # Walk and sort
        process_files(root, files, argument_path, FILE_TYPES, ARCHIVE_TYPES, SORTED_DIRECTORIES)
        process_directories(root, directories, SORTED_DIRECTORIES)
    return

def clean_folder_start():
    import sys
    from pathlib import Path
    argument_path = (sys.argv[1] if len(sys.argv) > 1 else ".")                                        # Sprawdzanie argumentu wiersza poleceń.
    relative_path = Path(argument_path).resolve()
    if relative_path.is_dir():
        print(f"\nCleaning folder -> {relative_path}")
        sort_folders(relative_path)   
    else:
        print(f"Folder -> {relative_path} does not seem to exist.")

### MAIN SECTION ###

if __name__ == "__main__":
    clean_folder_start()
