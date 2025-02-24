import time
import datetime

current_time_seconds = time.time()

plain_seconds = f"{current_time_seconds:,.4f}"
scientific_seconds = f"{current_time_seconds:.2e}"

current_date = datetime.datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {plain_seconds} or \
{scientific_seconds} in scientific notation")
print(current_date)
