
def open_file(file_path: str) -> str:
    if not isinstance(file_path, str):
        raise Exception(f"Please make sure file_path is a string!")
    try:
            _file = ""
            with open(file_path, "r") as fp:
                _file = fp.read()
            return _file
        except Exception:
            raise Exception(f"Error reading file at: {file_path}")