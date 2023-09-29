import os

CACHE_DIR = "cache"

def get_cache_file(file_name):
    file_path = os.path.join(CACHE_DIR, file_name)
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {str(e)}")
        return None

def put_cache_file(file_name, data):
    file_path = os.path.join(CACHE_DIR, file_name)
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while writing {file_path}: {str(e)}")
