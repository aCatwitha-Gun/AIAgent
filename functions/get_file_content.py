import os
from .config import *
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}'
    
    try:
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        # if the file has another character after the first 10000, add the note at the end
            if f.read(1):
                truncation_message = f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                file_content_string += truncation_message
        
        return file_content_string
    
    except FileNotFoundError:
        return f"Error: The file was not found at {file_path}"
    except Exception as e:
        return f"Error: Failure to open or read file {file_path}. Reason: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"]
    ),
)