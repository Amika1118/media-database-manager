import csv
import os


def reader(directory, file_path):
    directory.clear()
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                content_id = row[0]
                title = row[1]
                comment = row[2]
                directory[content_id] = [title] + [comment]


def writer(directory, file_path):
    with open(file_path, "w", newline="") as csvfile:  # clear file safely

        writer = csv.writer(csvfile)
        for content_id in directory:
            print(f"{content_id}, {directory[content_id]}")
            writer.writerow([content_id] + directory[content_id])




