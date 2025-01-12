import re
import os
from collections import Counter

def parse_logs(log_file):
    """
    Parses a log file to extract useful information like IP addresses, error messages, and request types.

    Parameters:
        log_file (str): Path to the log file.

    Returns:
        dict: A summary of the log analysis.
    """
    try:
        with open(log_file, 'r') as file:
            logs = file.readlines()

        # Extract IP addresses
        ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
        ip_addresses = [ip_pattern.search(line).group() for line in logs if ip_pattern.search(line)]

        # Count unique IPs
        unique_ips = Counter(ip_addresses)

        # Extract HTTP methods
        method_pattern = re.compile(r'"(GET|POST|PUT|DELETE|HEAD|OPTIONS)')
        http_methods = [method_pattern.search(line).group(1) for line in logs if method_pattern.search(line)]

        # Count methods
        method_counts = Counter(http_methods)

        # Extract error messages (status codes 4xx and 5xx)
        error_pattern = re.compile(r'"\s(4\d{2}|5\d{2})\s')
        errors = [error_pattern.search(line).group(1) for line in logs if error_pattern.search(line)]

        # Count errors
        error_counts = Counter(errors)

        return {
            "total_lines": len(logs),
            "unique_ips": unique_ips,
            "http_methods": method_counts,
            "error_codes": error_counts
        }

    except FileNotFoundError:
        print("Log file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_summary(summary):
    """
    Displays the summary of log analysis in a readable format.

    Parameters:
        summary (dict): The log analysis summary.
    """
    print("\n=== Log Analysis Summary ===")
    print(f"Total Lines in Log: {summary['total_lines']}")

    print("\nUnique IP Addresses:")
    for ip, count in summary['unique_ips'].most_common():
        print(f"{ip}: {count}")

    print("\nHTTP Methods:")
    for method, count in summary['http_methods'].items():
        print(f"{method}: {count}")

    print("\nError Codes:")
    for code, count in summary['error_codes'].items():
        print(f"{code}: {count}")

if __name__ == "__main__":
    log_path = input("Enter the path to the log file: ")

    if os.path.exists(log_path):
        analysis_summary = parse_logs(log_path)
        if analysis_summary:
            display_summary(analysis_summary)
    else:
        print("The specified log file does not exist.")
