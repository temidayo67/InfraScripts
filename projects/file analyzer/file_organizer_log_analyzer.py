import os
import subprocess # type: ignore
import re # type: ignore

# Optionally set the working directory
#os.chdir("C:\\Users\\DELL")
print("Current Directory:", os.getcwd())
# Represents a file with name, extension, and size
class File:
    base_dir= "files"
    def __init__(self, name, ext, size):
        self.name = name
        self.ext = ext
        self.size = size
    def __str__(self):
        return f"{self.name}.{self.ext} - {self.size} bytes"
    @staticmethod
    def info():
        return "This is a File class to represent file attributes."

# Organizes files by extension, analyzes logs, and provides file stats
class FileOrganizer(File):
    def __init__(self):
        super().__init__("Manager", "", 0)
        self.files = []  # List of File objects for organized files
        # Supported extensions and their counts
        self.ext_counts= {
            "txt":0, "jpg":0, "png":0, "pdf":0, "docx":0, "xlsx":0, "xls":0, "rar":0, "zip":0, "exe":0, "video":0, "other":0
        }
    @property
    def total_files(self):
        return len(self.files)
    @property
    def total_size(self):
        return sum(file.size for file in self.files)
    @classmethod
    def get_base_dir(cls):
        return cls.base_dir

    # Organize files in the current directory by extension
    def organize_files(self):
        try:
            self.files.clear()  # Clear tracked files before each organize
            os.makedirs(self.base_dir, exist_ok=True)  # Ensure base directory exists
            for filename in os.listdir('.'):
                if os.path.isfile(filename):
                    # Skip files already in the base_dir (organized files)
                    if os.path.abspath(filename).startswith(os.path.abspath(self.base_dir)):
                        continue
                    name, ext = os.path.splitext(filename)
                    ext = ext[1:].lower()
                    # Group mp4 and mkv as 'video'
                    if ext in ["mp4", "mkv"]:
                        folder = "video"
                        self.ext_counts["video"] += 1
                    elif ext in self.ext_counts:
                        folder = ext
                        self.ext_counts[ext] += 1
                    else:
                        folder = "other"
                        self.ext_counts["other"] += 1
                    # Track the file
                    self.files.append(File(name, ext, os.path.getsize(filename)))
                    os.makedirs(os.path.join(self.base_dir, folder), exist_ok=True)
                    dest = os.path.join(self.base_dir, folder, filename)
                    counter = 1
                    # Avoid overwriting files with the same name
                    while os.path.exists(dest):
                        name_only, ext_only = os.path.splitext(filename)
                        dest = os.path.join(self.base_dir, folder, f"{name_only}_{counter}{ext_only}")
                        counter += 1
                    if os.path.exists(filename):  # Check file still exists before moving
                        try:
                            os.rename(filename, dest)
                        except OSError as e:
                            print(f"OSError moving {filename} to {dest}: {e}")
            return f"organized {len(self.files)} files."
        except OSError as e:
            print(f"OSError (outer): {e}")
            return "Error organizing files."

    # Analyze .log files for errors and timestamps in the organized log folder
    def analyze_logs(self):
        result = "Log analysis:\n"
        log_dir = os.path.join(self.base_dir, 'log')
        if os.path.exists(log_dir):
            for fname in os.listdir(log_dir):
                if fname.endswith('.log'):
                    try:
                        with open(os.path.join(log_dir, fname), 'r') as f:
                            content = f.read()
                            if re.search(r"Error", content):
                                result += f"{fname} contains errors.\n"
                            timestamps = re.findall(r"\d{4}-\d{2}-\d{2}", content)
                            if timestamps:
                                result += f"{fname}: Timestamps: {timestamps}\n"
                    except FileNotFoundError:
                        result += f"{fname}: File not found\n"
        if result == "Log analysis:\n":
            return "No log files found."
        return result

    # List all files in the organized base directory
    def list_organized_files(self):
        try:
            result= subprocess.run(['dir', self.base_dir], shell=True, capture_output=True, text=True)
            return f"Directory Listing: \n{result.stdout}"
        except subprocess.CalledProcessError:
            return "Error listing files."

    # Display all tracked files and their sizes
    def display_files(self):
        result = f"Files (Total Size: {self.total_size} bytes):\n"
        for i, file in enumerate(self.files):
            result += f"{i}: {file}\n"
        return result
    def __str__(self):
        return f"File Organizer - Extensions: {self.ext_counts}"

# Main program loop
def main():
    fo = FileOrganizer()
    base_dir = fo.get_base_dir()
    name, ext, size = "test", ".txt", 1024
    print(f"Starting with {name}{ext}: {size} bytes")
    # Main menu loop for user interaction
    while True:
        print("\n1: Organize Files, 2: Analyze Logs, 3: List Files, 4: View Files, 5: Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            print(fo.organize_files())
            print(f"File counts by type: {fo.ext_counts}")
        elif choice == "2":
            print(fo.analyze_logs())
        elif choice == "3":
            print(fo.list_organized_files())
        elif choice == "4":
            print(fo.display_files())
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
    print(f"Base Directory: {base_dir}")

if __name__ == "__main__":
    main()
