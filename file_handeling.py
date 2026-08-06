import os
import csv

def reader(directory, file_path):
    directory.clear()
    try:
        with open(file_path, "r", newline="") as f:
            for row in csv.reader(f):
                if row and len(row) >= 3:          # safety check
                    content_id = row[0]
                    directory[content_id] = row[1:]  # stores all trailing columns
    except FileNotFoundError:
        pass   # file doesn't exist yet – that's fine


def writer(directory, file_path):
    with open(file_path, "w", newline="") as f:
        w = csv.writer(f)
        for content_id, data in directory.items():
            w.writerow([content_id] + data)




