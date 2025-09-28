import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    # guard rails :D
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    # try running the python file with the given args, time out after 30 seconds
    try:
        commands = ["python", target_file]
        if args:
            commands.extend(args)

        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=working_directory,
        )
        output = []
        
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        
        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: Executing Python file: {e}"

