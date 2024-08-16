import os
from pathlib import Path  # pathlib is used for handling file system paths in an OS-agnostic way.
import logging  # logging is used to track events that happen during runtime, providing useful insights.

# Configure logging to display timestamps and messages for better tracking.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Specify the project name to be used in file paths.
project_name = "textSummarizer"

# List of file paths to be created. These paths include both files and directories that may be needed for the project.
list_of_files = [
    ".github/workflows/.gitkeep",  # .gitkeep is often used to track empty folders in Git repositories.
    f"src/{project_name}/__init__.py",  # Initialize the main project package.
    f"src/{project_name}/components/__init__.py",  # Subpackage for components like models, modules, or logic units.
    f"src/{project_name}/utils/__init__.py",  # Subpackage for utility functions.
    f"src/{project_name}/utils/common.py",  # Common utility functions shared across the project.
    f"src/{project_name}/logging/__init__.py",  # Custom logging configurations (if needed).
    f"src/{project_name}/config/__init__.py",  # Configuration-related files and scripts.
    f"src/{project_name}/config/configuration.py",  # Configuration settings management script.
    f"src/{project_name}/pipeline/__init__.py",  # Pipeline-related scripts for processing flows.
    f"src/{project_name}/entity/__init__.py",  # Entity classes or data structures used in the project.
    f"src/{project_name}/constants/__init__.py",  # Constants that might be reused across the project.
    "config/config.yaml",  # Configuration file in YAML format for easy human-readable settings.
    "params.yaml",  # YAML file to hold parameter values for various processes.
    "app.py",  # Main application script for running the project.
    "main.py",  # Entry point script for execution.
    "Dockerfile",  # Dockerfile for containerizing the project.
    "requirements.txt",  # List of dependencies needed for the project.
    "setup.py",  # Setup script for packaging and distributing the project.
    "research/trials.ipynb",  # Jupyter notebook for research and experimentation.
    "test.py", # Script for unit testing or running simple test cases for the project.
    ".env"
]

# Iterate over each file path in the list.
for filepath in list_of_files:
    filepath = Path(filepath)  # Converts the string path to a Path object, making it OS-agnostic.
    filedir, filename = os.path.split(filepath)  # Splits the path into directory and file components.

    # If the directory path is not empty, create the necessary directories.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the directory (and parent directories if needed). Use exist_ok=True to avoid errors if it already exists.
        logging.info(f"Creating directory: {filedir} for the file: {filename}")  # Log the creation of the directory.

    # If the file does not exist or is empty, create it.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Create an empty file.
        logging.info(f"Creating empty file: {filepath}")  # Log the creation of the file.

    else:
        # If the file already exists and is not empty, log that information.
        logging.info(f"{filename} already exists")
