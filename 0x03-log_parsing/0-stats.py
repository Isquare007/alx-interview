#!/usr/bin/python3
"""a script that reads stdin line by line and compute metrics"""
import sys


stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}

total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            ip_address = parts[0]
            data = parts[2][1:]
            request = parts[4][1:]
            status_Code = parts[7]
            file_size = int(parts[8])

        except Exception:
            continue

        if status_Code in stats:
            stats[status_Code] += 1

        total_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))

            for stat in sorted(stats.keys()):
                if stats[stat] > 0:
                    print("{}: {}".format(stat, stats[stat]))

except KeyboardInterrupt:
    print("keyboard interupted")
