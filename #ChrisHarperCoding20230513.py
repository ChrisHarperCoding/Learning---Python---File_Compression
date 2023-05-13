#ChrisHarperCoding20230513
import os
import time
import zipfile
import logging
from io import BytesIO
import tkinter as tk
from tkinter import filedialog

def compress_file(file_path, log_file='log.txt'):
    start_time = time.time()
    try:
        with open(file_path, 'r') as f:
            data = f.read().encode('utf-8')
    except FileNotFoundError:
        logging.error(f"The file {file_path} was not found.")
        return
    except IOError:
        logging.error(f"There was an error reading the file {file_path}.")
        return

    compressed_data = zipfile.ZipFile(file_path + '.zip', 'w')
    try:
        compressed_data.writestr(os.path.basename(file_path), data)
    except IOError:
        logging.error(f"There was an error writing the compressed file {file_path}.zip.")
        return

    # Log the compression and time taken.
    elapsed_time = time.time() - start_time
    log_info = f"Compressed {file_path} in {elapsed_time} seconds."

    # Write the log information into the log file within the compressed file.
    compressed_data.writestr(log_file, log_info.encode('utf-8'))

    compressed_data.close()

    logging.info(log_info)
    return log_info

def browse_file():
    file_path = filedialog.askopenfilename()
    log_info = compress_file(file_path)
    result_label.config(text=log_info)

root = tk.Tk()
root.title('File Compressor')

browse_button = tk.Button(root, text='Browse File', command=browse_file)
browse_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()