import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from typing import Any
from box import ConfigBox
from pathlib import Path
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Returns:
        ConfigBox: ConfigBox object containing the yaml file contents
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise e
    except Exception as e:
        raise e 

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """Creates list of directories

    Args:
        path_to_directories (list[Path]): List of directory paths to be created
    """
    for path_to_directory in path_to_directories:
        os.makedirs(path_to_directory, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path_to_directory}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a json file

    Args:
        path (Path): Path to the json file
        data (dict): Data to be saved
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a json file and returns a ConfigBox object

    Args:
        path (Path): Path to the json file

    Returns:
        ConfigBox: ConfigBox object containing the json file contents
    """
    with open(path) as json_file:
        content = json.load(json_file)
    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file using joblib

    Args:
        data (Any): Data to be saved
        path (Path): Path to the binary file
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib

    Args:
        path (Path): Path to the binary file
    Returns:
        Any: Data loaded from the binary file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    logger.info(f"File size for {path} is {size_in_kb} KB")
    return f"{size_in_kb} KB"

@ensure_annotations
def decodeImage(imgstring, fileName):
    """Decodes a base64 encoded image string and saves it to a file

    Args:
        imgstring (str): Base64 encoded image string
        fileName (str): Path to the file where the image will be saved
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
    logger.info(f"Image decoded and saved to {fileName}")
    
def encodeImageIntoBase64(croppedImagePath):
    """Encodes an image file to a base64 string

    Args:
        croppedImagePath (str): Path to the image file

    Returns:
        str: Base64 encoded image string
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())