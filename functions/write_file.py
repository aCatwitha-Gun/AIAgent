import os
from google.genai import types


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
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)