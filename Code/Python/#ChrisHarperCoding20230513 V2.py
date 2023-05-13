#Detect a user's specs and adjust the speed to compression ratio accordingly? 
#   E.g. someone with a 13900K can probably have the compression set to the highest 
#       Versus someone with a lower spec CPU:
def compress_file(file_path, compression_type, log_file='log.txt'):
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

    if compression_type == ".zip":
        compressed_data = zipfile.ZipFile(file_path + compression_type, 'w')
    elif compression_type == ".tar.gz":
        compressed_data = tarfile.open(file_path + compression_type, 'w:gz')
    elif compression_type == ".tar.bz2":
        compressed_data = tarfile.open(file_path + compression_type, 'w:bz2')
    else:
        logging.error(f"Unsupported compression type {compression_type}.")
        return

    try:
        compressed_data.add(file_path)
    except IOError:
        logging.error(f"There was an error writing the compressed file {file_path}{compression_type}.")
        return

    # Log the compression and time taken.
    elapsed_time = time.time() - start_time
    log_info = f"Compressed {file_path} in {elapsed_time} seconds with {compression_type}."

    # Write the log information into the log file.
    with open(log_file, 'w') as log:
        log.write(log_info)

    # Add the log file to the compressed file.
    try:
        compressed_data.add(log_file)
    except IOError:
        logging.error(f"There was an error adding the log file to the compressed file {file_path}{compression_type}.")
        return

    compressed_data.close()

    logging.info(log_info)
    return log_info
