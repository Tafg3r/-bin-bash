import os
import platform
import psutil

def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM Total": f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
    }
    return system_info

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return {
        "Total Disk Space": f"{disk_usage.total / (1024**3):.2f} GB",
        "Used Disk Space": f"{disk_usage.used / (1024**3):.2f} GB",
        "Free Disk Space": f"{disk_usage.free / (1024**3):.2f} GB",
        "Disk Usage Percentage": f"{disk_usage.percent} %"
    }

def main():
    print("System Information:")
    for key, value in get_system_info().items():
        print(f"{key}: {value}")
    
    print("\nDisk Usage:")
    for key, value in get_disk_usage().items():
        print(f"{key}: {value}")
    
if __name__ == "__main__":
    main()
