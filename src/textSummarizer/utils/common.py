# Utility functions for common operations

import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations     # tstrictly enforces type annotations, helping you catch issues at runtime
from box import ConfigBox                 # alternative to standard dictionaries allows attribute-style access
from pathlib import Path
from typing import Any, List              # List type for type hinting


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox instance.

    Args:
        path_to_yaml (Path): Path to the YAML file. Should be a Path object.

    Raises:
        ValueError: If the YAML file is empty or cannot be read.
        Exception: For any other errors encountered during file processing.

    Returns:
        ConfigBox: A ConfigBox instance containing the YAML file's content.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")  # Ensure the file is not empty
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("Error processing YAML file content")
    
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories specified in the list.

    Args:
        path_to_directories (List[Path]): List of paths where directories should be created. 
                                           Each path should be a Path object.
        verbose (bool, optional): If True, logs the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Create the directory if it does not exist
        if verbose:
            logger.info(f"Directory created at: {path}")




@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a given file in kilobytes (KB).

    Args:
        path (Path): Path to the file. Should be a Path object.

    Returns:
        str: The size of the file in kilobytes, formatted as a string.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Calculate size in KB
    return f"~ {size_in_kb} KB"
