import os
from collections import Counter

def parse_log_file(file_path):
    if os.path.getsize(file_path) > 100 * 1024 * 1024:
        print("Error: File exceeds 100 MB limit.")
        return

    ip_counter = Counter()
    code_counter = Counter()
    url_counter = Counter()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
 
                if len(parts) < 9:
                    continue

                ip = parts[0]
                code = parts[-2]  
                url = parts[6] if len(parts) > 6 else "UNKNOWN"

                ip_counter[ip] += 1
                code_counter[code] += 1
                url_counter[url] += 1

    except FileNotFoundError:
        print("Error: File not found.")
        return
    except Exception as e:
        print(f"Error while reading file: {e}")
        return
 
    print("\n=== Log Analysis Summary ===")
    print("\nTop 5 IP Addresses:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip} → {count} requests")

    print("\nTop 5 HTTP Response Codes:")
    for code, count in code_counter.most_common(5):
        print(f"{code} → {count} times")

    print("\nTop 5 URLs Accessed:")
    for url, count in url_counter.most_common(5):
        print(f"{url} → {count} times")
 
file_path = input("Enter log file path: ")
parse_log_file(file_path)
