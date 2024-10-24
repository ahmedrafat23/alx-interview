#!/usr/bin/python3
import sys
import signal
import re

# Dictionary to store counts of different status codes
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_file_size = 0
line_count = 0

# Regular expression to match the input log format
log_pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+) - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)")

def print_metrics():
    """Print the aggregated metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def handle_interrupt(signum, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_metrics()
    sys.exit(0)

# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

# Read input line by line from stdin
for line in sys.stdin:
    match = log_pattern.match(line)
    if match:
        status_code = match.group(2)
        file_size = int(match.group(3))

        # Accumulate file size
        total_file_size += file_size

        # Count the status code if it's one of the tracked ones
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # After every 10 lines, print the metrics
        if line_count % 10 == 0:
            print_metrics()

# Final print after all input has been processed
print_metrics()

