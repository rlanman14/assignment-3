from datetime import datetime

# define log file path

log_file_path = 'log.txt'

# initialize list to store log entries
log_data = []

# read log entries from the log.txt file

try:
    with open(log_file_path, 'r') as file:
        log_data = file.readlines()
except FileNotFoundError:
    print(f"The file '{log_file_path}' does not exist or cannot be accessed.")

# total time period 
start_date = datetime(1994, 10, 24)  # October 24, 1994
end_date = datetime(1995, 10, 11)   # October 11, 1995

total_requests = 0  # Initialize the variable to hold the count

for log_entry in log_data:
    if "[" in log_entry:
        date_str = log_entry.split("[")[1].split(" ")[0]
        log_date = datetime.strptime(date_str, "%d/%b/%Y:%H:%M:%S")

    if start_date <= log_date <= end_date:
        total_requests += 1  # Increment the count if it falls within the period

print(f"Total requests made in the time period: {total_requests}")
