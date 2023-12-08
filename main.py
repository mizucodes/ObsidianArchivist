import os


# function to scan dir and create log of its files
def scan_dir(dir_path, log_path):
    try:
        with open(log_path, "w") as log_file:
            for root, dirs, files in os.walk(dir_path):
                log_file.write(f"Directory: {root}\n")  # write the file here
                for name in dirs:
                    log_file.write(f" Subdirectory: {name}\n")
                for name in files:
                    log_file.write(f" File: {name}\n")
            print(f"Log done")
    except Exception as e:
        print(f"Error: {e}")


dir_to_scan = ""
log_file = "log.txt"

scan_dir(dir_to_scan, log_file)
