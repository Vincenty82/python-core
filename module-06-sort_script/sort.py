### IMPORT SECTION ###

import os
import re
import shutil

### VARIABLE DECLARATION SECTION ###

ascii_chars = "AaCcEeLlNnOoSsZzZz"
polish_chars = "ĄąĆćĘęŁłŃńÓóŚśŻżŹź"
translation_table = str.maketrans(polish_chars, ascii_chars,)
sorted_directories = ["images", "documents", "audio", "video", "archives"]
file_types = {
    "images": ("JPEG", "PNG", 'JPG', 'SVG'),
    "video": ("AVI", "MP4", "MOV", "MKV"),
    "documents": ("DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"),
    "audio": ("MP3", "OGG", "WAV", "AMR"),
    "archives": ("ZIP", "GZ", "TAR"),
}
archive_types = {"ZIP": "zip", "GZ": "gztar", "TAR": "tar"}

### FUNCTIONS SECTION ###

def normalize(input_string, is_file = False):
    file_name = input_string
    if is_file:
        file_name, file_extension = os.path.splitext(input_string)                                 # Dla pliku odzielam nazwę od rozszerzenia
        file_extension = file_extension.lower().removeprefix(".")
    new_name = file_name.translate(translation_table)
    new_name = re.sub(r"[^A-Za-z0-9]", "_", new_name)
    if is_file:
        return ".".join((new_name, file_extension))                                                # Dla pliku zwraca nową nazwę z rozszerzeniem
    else:
        return new_name                                                                            # Dla folderu zwraca tylko nową nazwę

def sort_folders(directory_path):
    for sorted_directory in sorted_directories:
        directory_to_create = os.path.join(argument_path, sorted_directory)
        os.makedirs(directory_to_create, exist_ok = True)
    
    for root, directories, files in os.walk(directory_path):                                      # 
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = normalize(file, True)
            new_file_path = os.path.join(root, new_file_name)
            os.rename(old_file_path, new_file_path)

            file_name, file_extension = os.path.splitext(new_file_name)
            file_extension = file_extension.upper().removeprefix(".")

            for extension_folder, known_extensions in file_types.items():
                if file_extension in known_extensions:
                    destination_directory = os.path.join(argument_path, extension_folder)
                    os.makedirs(destination_directory, exist_ok=True)
                    shutil.move(new_file_path, os.path.join(destination_directory, new_file_name))

                    
            if file_extension.upper() in archive_types:
                archive_format = archive_types[file_extension]
                if os.path.isfile(new_file_path):
                    destination_directory = os.path.join(argument_path, "archives")
                    os.makedirs(destination_directory, exist_ok=True)
                    shutil.unpack_archive(new_file_path, os.path.join(destination_directory, file_name), archive_format)



        for directory in directories:
            old_directory_name = os.path.join(root, directory)
            if directory in sorted_directories:
                break
            elif os.listdir(old_directory_name):
                new_directory_name = os.path.join(root, normalize(directory))
                os.rename(old_directory_name, new_directory_name)
                sort_folders(new_directory_name)
            else:
                os.rmdir(old_directory_name)
    return

### MAIN SECTION ###

if __name__ == "__main__":
    import sys
    from pathlib import Path
    argument_path = (sys.argv[1] if len(sys.argv) > 1 else None)                                        # Sprawdzanie argumentu wiersza poleceń.
    argument_path = "." + argument_path
    if argument_path and Path(argument_path).is_dir():
        sort_folders(argument_path)   
    else:
        print(f"Argument {argument_path} is not a valid catalogue")