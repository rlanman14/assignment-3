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

# time period from last 6 months
start_date = datetime(1995, 4, 11)  # April 11, 1995
end_date = datetime(1995, 10, 12)   # October 11, 1995

total_requests_in_6_months = 0  # Initialize the variable to hold the count

for log_entry in log_data:
    if "[" in log_entry:
        date_str = log_entry.split("[")[1].split(" ")[0]
    log_date = datetime.strptime(date_str, "%d/%b/%Y:%H:%M:%S")

    if start_date <= log_date <= end_date:
        total_requests_in_6_months += 1  # Increment the count if it falls within the period

# Now 'total_requests_in_6_months' contains the total requests made in the 6 months
print(f"Total requests made in the last 6 months: {total_requests_in_6_months}")
