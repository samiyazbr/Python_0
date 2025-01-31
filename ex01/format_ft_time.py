import time
import datetime

# Get the current time in seconds since January 1, 1970
current_time_seconds = time.time()

# Format the time in seconds (plain and scientific notation)
plain_seconds = f"{current_time_seconds:,.4f}"
scientific_seconds = f"{current_time_seconds:.2e}"

# Get the current date in the desired format
current_date = datetime.datetime.now().strftime("%b %d %Y")

# Print the formatted output
print(f"Seconds since January 1, 1970: {plain_seconds} or \
{scientific_seconds} in scientific notation")
print(current_date)
