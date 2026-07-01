# import and global variable 
from pathlib import Path
import shutil

base_dir = Path("/home/mehdi/Downloads")
target_dir = Path("/run/media/mehdi/New Volume2")

# declare categories and extensions
FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".ico"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp", ".csv"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".tgz"],
    "packages": [".deb", ".rpm", ".snap", ".flatpak", ".appimage"],
    "scripts": [".sh", ".bash", ".py", ".pl", ".rb", ".php"],    
    "configs": [".conf", ".config", ".yaml", ".yml", ".json", ".ini", ".xml"] 
}
# create directory for each category
def create_direcory():
    for categories, _ in FILE_CATEGORIES.items():
       (target_dir / "sorted_downloaded_files"/ categories).mkdir(parents=True, exist_ok=True)

# search file and copy file to each directory
def search_and_copy_files():
    files = base_dir.rglob("*")
    for file in files:
        for categories, extensions in FILE_CATEGORIES.items():
            if file.suffix in extensions:
                shutil.copy(file, target_dir / "sorted_downloaded_files"/ categories )
