import time

start_time = time.gmtime(0)

current_time = time.time()

start_time_sec = start_time.tm_mday * 24 * 60 * 60\
                + start_time.tm_mon * 30 * 24 * 60 * 60\
                + start_time.tm_year * 365 * 24 * 60 * 60

difference = start_time_sec - current_time

print(f"Seconds since January 1, 1970: {difference:.4f} or {difference:.2e} in scientific notation.")

print(f"{time.strftime('%b %d %Y', time.gmtime(current_time))}")
