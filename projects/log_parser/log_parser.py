import re
import os
import subprocess

class LogEntry:
    log_dir = "log"
    def __init__(self, name, date, ips):
        self.name = name
        self.date = date
        self.ips = ips
    def __str__(self):
        return f"{self.name} (Date: {self.date}, IPs: {(self.ips)})"
    @staticmethod
    def info():
        return "This is a LogEntry class to represent log attributes."
class LogParser(LogEntry):
    def __init__(self):
        super().__init__("Parser", "", [])
        self.entries = []  # List of LogEntry objects for parsed logs
        self.ip_counts= {"unique_ips":0}
    @property
    def total_ips(self):
        unique_ips = set()
        for entry in self.entries:
            unique_ips.update(entry.ips)
        return len(unique_ips)
    @classmethod
    def get_log_dir(cls):
        return cls.log_dir

    def parse_logs(self):
        try:
            os.makedirs(self.log_dir, exist_ok=True)  # Ensure log directory exists
            for filename in os.listdir("."):
                if filename.endswith(".log"):
                    date_match= re.search(r"(\d{4}-\d{2}-\d{2})", filename)
                    if date_match:
                        date= date_match.group()
                        with open(filename, 'r') as file:
                            content= file.read()
                            ips= re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", content)
                        if ips:
                            self.entries.append(LogEntry(filename, date, ips))
                            self.ip_counts["unique_ips"] += len(set(ips))
                            os.makedirs(os.path.join(self.log_dir, date), exist_ok=True)
                            os.rename(filename, os.path.join(self.log_dir, date, filename))
            return f"Parsed {len(self.entries)} log files with {self.total_ips} unique IPs."
        except (OSError, FileNotFoundError):
            return "Error parsing logs."
    def list_logs(self):
        try:
            result= subprocess.run(['dir', self.log_dir], shell=True, capture_output=True, text=True)
            return f"Log files:\n{result.stdout}"
        except subprocess.CalledProcessError:
            return "Error listing log files."
    def display_entries(self):
        result= f"Log Entries (Total Unique IPs: {self.total_ips}):\n"
        for i, entry in enumerate(self.entries):
            result += f"{i}: {entry}\n"
        return result
    def __str__(self):
        return f"LogParser with {len(self.entries)} entries and {self.total_ips} unique IPs."
    @total_ips.setter
    def total_ips(self, value):
        raise AttributeError("total_ips is a read-only property.")

def main():
    parser= LogParser()
    global log_dir
    log_dir= parser.get_log_dir()
    name, date, ips = "example.log", "2023-10-01", "192.168.1.1"
    print(f"Starting with {name}, ({date}): {ips}")
    while True:
        print("\nMenu:"
              "\n1. Parse Logs"
              "\n2. List Log Files"
              "\n3. Display Parsed Entries"
              "\n4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            print(parser.parse_logs())
        elif choice == '2':
            print(parser.list_logs())
        elif choice == '3':
            print(parser.display_entries())
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    print("Log Directory:", log_dir)

if __name__ == "__main__":
    main()
    
