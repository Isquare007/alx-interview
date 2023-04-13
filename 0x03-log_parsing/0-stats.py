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

def print_stat():
    """prints the infos"""
    print("File size: {}".format(total_size))
    for key, value in sorted(stats.items()):
        if value > 0:
            print("{}: {}".format(key, value))

if __name__ == "__main__":
    line_count = 0
    try:
        for line in sys.stdin:
            parts = line.split()
            try:
                status_Code = parts[7]
                file_size = int(parts[8])

                if status_Code in stats.keys():
                    stats[status_Code] += 1

                total_size += int(parts[-1])
                line_count += 1
            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_stat()
            
    except KeyboardInterrupt as e:
        print_stat()
        raise
