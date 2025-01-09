import time
from datetime import datetime

# Get the current time in seconds since January 1, 1970
current_time = time.time()

# Format the seconds into a readable format
seconds_formatted = f"Seconds since January 1, 1970: {current_time:.4f} or {current_time:.2e} in scientific notation"

# Get the current date in "MMM DD YYYY" format
current_date = datetime.now().strftime("%b %d %Y")

# Print the formatted output
print(seconds_formatted)
print(current_date)
