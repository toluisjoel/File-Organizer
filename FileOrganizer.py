import os
import shutil

files = os.listdir('Your downloads folder path')  # mine is /Users/toelu/Downloads/
file_extensions = {
    "Pictures": [".jpg", ".png", ".jpeg", ".gif", ".ico", ".svg", ],
    "Videos": [".mp4", ".mkv", ".srt"],
    "Audios": [".mp3", ".wav"],
    "Zips": [".zip", ".tgz", ".rar", ".tar"],
    "Documents": [".pdf", ".epub", ".pages", ".rtf",
                  ".docx", ".doc", ".csv", ".xlsx", ".pptx", ".html", ".css", ".doc", ".ppt", ".xls", ".txt"],
    "InatallationFiles": [".dmg", ".pkg"],
    "Projects/PythonScripts": [".py"],
}


def sort_file(file_name):
    for name, extensions in file_extensions.items():
        for extension in extensions:
            if file_name.endswith(extension):
                return name


if __name__ == '__main__':
    for file in files:
        file_destination = sort_file(file)
        try:
            if file_destination:
                shutil.move(f'/Users/toelu/Downloads/{file}', f"/Users/toelu/Documents/{file_destination}")
            else:
                shutil.move(f'/Users/toelu/Downloads/{file}', "/Users/toelu/Documents/Others")
        except shutil.Error:
            print(f'{file} already exists 😒')
