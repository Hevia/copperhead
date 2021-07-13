from typing import Iterator
import json

class IterFile:
    """ Creates an iterator from a file. """
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
    
    def __iter__(self) -> Iterator:
        if not isinstance(file_path, str):
            raise TypeError(f"Please make sure file_path is a string!")

        try:
            with open(self.file_path) as fp:
                for line in fp:
                    yield line
        except Exception as e:
            raise Exception(f"Error reading file at: {file_path} with exception: {e}")

def open_file(file_path: str) -> str:
    """ Opens up a file and loads it into memory as a string. """
    if not isinstance(file_path, str):
        raise TypeError(f"Please make sure file_path is a string!")
    try:
        _file = ""
        with open(file_path, "r") as fp:
            _file = fp.read()
        return _file
    except Exception as e:
        raise Exception(f"Error reading file at: {file_path} with exception: {e}")

def load_JSON(self, file_path) -> dict:
    """ Opens up a file and loads it into memory as a dict. """
    if not isinstance(file_path, str):
        raise TypeError(f"Please make sure file_path is a string!")

    try:
        with open(file_path) as json_data:
            data = json.load(json_data)
        return data
    except Exception as e:
        raise Exception(f"Could not open file located at: {file_path} with exception: {e}")

def save_file(data, file_path: str) -> None:
    """ Saves a file to disk. """
    if not isinstance(file_path, str):
        raise TypeError(f"Please make sure file_path is a string!")

    if data == None:
        raise TypeError(f"Please make sure data is not None!")
    
    try:
        with open(file_path, "w+") as fp:
            fp.write(data)
    except Exception as e:
        raise Exception(f"Error with trying to save file at: {file_path} with exception: {e}")

def save_JSON(data, file_path: str) -> None:
    """ Saves JSON to disk """
    if not isinstance(file_path, str):
        raise TypeError(f"Please make sure file_path is a string!")

    if data == None:
        raise TypeError(f"Please make sure data is not None!")
    
    try:
        with open(file_path, "w+") as fp:
            json.dump(data, fp, indent=4)
    except Exception as e:
        raise Exception(f"Error with trying to save file at: {file_path} with exception: {e}")


