import os


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'

    # if the file_path doesn't exist, create it
    try:
        directory = os.path.dirname(target_file)
        # attempt to make the directory/file_path, ignore error if file path already exists
        os.makedirs(directory, exist_ok=True)  
    except Exception as e:
        return f'Error: Failure to create directory for "{file_path}". Reason: {e}'
    
    # overwrite content to file_path
    try:
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failure to write to "{file_path}". Reason: {e}'
    
