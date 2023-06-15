#!/usr/bin/python3
'''Provides fns to read from stdin and compute metrics'''


import sys


def print_metrics(total_size, status_codes):
    """
    Print the computed metrics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dict containing the count of each status code.

    Returns:
        None

    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    """
    Parse a line and update the metrics.

    Args:
        line (str): The line to parse.
        total_size (int): Current total file size.
        status_codes (dict): Dict containing the count of each status code.

    Returns:
        int: Updated total file size.

    """
    fields = line.split()
    if len(fields) >= 7:
        size = int(fields[-1])
        code = fields[-2]
        total_size += size
        if code in status_codes:
            status_codes[code] += 1
    return total_size


def compute_metrics():
    """
    Read stdin line by line and compute the metrics.

    Returns:
        None

    """
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            total_size = parse_line(line, total_size, status_codes)
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise


compute_metrics()
