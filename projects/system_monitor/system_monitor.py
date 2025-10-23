import os
import subprocess
import re

class Report:
    report_dir= "reports"
    def __init__(self, date, cpu_usage, disk_usage):
        self.date = date
        self.cpu_usage = cpu_usage
        self.disk_usage = disk_usage
    def __str__(self):
        return f"Report(Date: {self.date}, CPU Usage: {self.cpu_usage}%, Disk Usage: {self.disk_usage}%)"
    @staticmethod
    def info():
        return "System resource reports"

class SystemMonitor(Report):
    def __init__(self):
        super().__init__("", 0, 0)
        self.reports= []
        self.metrics= {"cpu_usage": 0.0, "disk_usage": 0.0}
    @property
    def total_reports(self):
        return len(self.reports)
    @total_reports.setter
    def total_reports(self, value):
        raise AttributeError("Cannot set total_reports directly")
    @classmethod
    def get_report_dir(cls):
        return cls.report_dir

    def generate_report(self, date="2025-09-09"):
        try:
            os.makedirs(os.path.join(self.report_dir, date), exist_ok=True)
            report_file = os.path.join(self.report_dir, date, "system_report.txt")
            with open(report_file, "w") as f:
                f.write(f"System Report ({date})\n")
                f.write(f"Total Reports: {self.total_reports}\n")
                for i, report in enumerate(self.reports):
                    f.write(f"{i}: {report}\n")
                f.write(f"Average Metrics: {self.metrics}\n")
            return f"Generated report: {report_file}"
        except OSError:
            return "Error generating report!"
    def list_reports(self):
        try:
            result = subprocess.run(["dir", "/s", self.report_dir], capture_output=True, text=True, shell=True)
            return f"Report Directory Listing:\n{result.stdout}"
        except subprocess.CalledProcessError:
            return "Error listing reports!"
    def display_reports(self):
        result = f"Reports (Total: {self.total_reports}):\n"
        for i, report in enumerate(self.reports):
            result += f"{i}: {report}\n"
        return result
    def __str__(self):
        return f"System Monitor - Metrics: {self.metrics}"

def main():
    monitor = SystemMonitor()
    global report_dir
    report_dir = monitor.get_report_dir()
    date, cpu, disk = "2025-09-09", 5.0, 50.0
    print(f"Starting with report on {date}: CPU {cpu}%, Disk {disk}%")
    while True:
        print("\n1: Monitor System, 2: Generate Report, 3: List Reports, 4: View Reports, 5: Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            print(monitor.monitor_system())
        elif choice == "2":
            print(monitor.generate_report())
        elif choice == "3":
            print(monitor.list_reports())
        elif choice == "4":
            print(monitor.display_reports())
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
    print(f"Report Directory: {report_dir}")
if __name__ == "__main__":
    main()    
