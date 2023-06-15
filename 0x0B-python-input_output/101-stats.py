#!/usr/bin/python3
'''Provides fns to read from stdin and compute metrics'''


import sys


def print_stats(size, status_codes):
    """
    Print the computed statistics.

    Args:
        size (int): Total file size.
        status_codes (dict): Dict containing the count of each status code.

    Returns:
        None

    """
    print("Total file size: {}".format(size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def compute_metrics():
    """
    Read stdin line by line and compute the metrics.

    Returns:
        None

    """
    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if line[-2] not in status_codes:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise


compute_metrics()
