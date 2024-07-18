#!/usr/bin/python3

import sys
import signal

total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def print_metrics():
    """Print the collected metrics."""
    global total_file_size, status_code_counts
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C) and print metrics."""
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        total_file_size += file_size

        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)

