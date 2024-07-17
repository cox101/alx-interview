#!/usr/bin/python3
import sys
import signal

total_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

def print_stats():
    global total_size, status_counts
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def parse_line(line):
    parts = line.split()
    if len(parts) < 7:
        return None
    try:
        ip = parts[0]
        date = parts[3] + " " + parts[4]
        method = parts[5][1:]
        url = parts[6]
        protocol = parts[7][:-1]
        status_code = int(parts[8])
        file_size = int(parts[9])
    except (ValueError, IndexError):
        return None

    if method == "GET" and url == "/projects/260" and protocol == "HTTP/1.1":
        return status_code, file_size
    return None

line_count = 0
for line in sys.stdin:
    result = parse_line(line)
    if result:
        status_code, file_size = result
        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1
    line_count += 1
    if line_count % 10 == 0:
        print_stats()

print_stats()
