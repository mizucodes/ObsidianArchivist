import os


# function to scan dir and create log of its files
def scan_dir():
    print("Name the directory you would like to scan (entire path)\n")
    dir_path = input("enter: ")
    log_file = str(input(f"Enter name for log file created: ")) + ".txt"
    log_path = os.getcwd() + f"/logs/{log_file}"

    try:
        with open(log_path, "w") as log_file:
            for root, dirs, files in os.walk(dir_path):
                print(f"in dir: {root}")
                log_file.write(f"Directory: {root}\n")  # write the file here
                for name in dirs:
                    log_file.write(f" Subdirectory: {name}\n")
                for name in files:
                    log_file.write(f" File: {name}\n")
            print(f"Log file created")
    except Exception as e:
        print(f"Error: {e}")


scan_dir()
