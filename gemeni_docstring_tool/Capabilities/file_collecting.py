import os
import queue

def collect_ts_files(directory):
    ts_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".ts"):
                ts_files.append(os.path.join(root, file))
    return ts_files

def queue_ts_files(ts_files):
    file_queue = queue.Queue()
    for file_path in ts_files:
        file_queue.put(file_path)
    return file_queue

