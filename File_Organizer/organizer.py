import os
import shutil

# Define file type categories
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.csv', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz'],
    'Others': []
}

def get_folder_category(file_extension):
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def organize_files(directory):
    if not os.path.isdir(directory):
        print("Invalid folder path. Please try again.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            category = get_folder_category(ext)
            target_folder = os.path.join(directory, category)

            try:
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} → {category}/")
            except Exception as e:
                print(f"Error moving file {filename}: {e}")

def main():
    folder = input("Enter full path to the folder to organize: ").strip()
    organize_files(folder)

if __name__ == '__main__':
    main()
