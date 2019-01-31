import os as _os


# TODO actions for optimize work in Storage class


def find_abs_path(path:str) -> str:
    return _os.path.abspath(path)

def rename(abs_path:str, new_name:str) -> None:
    pass

def move_file(abs_path:str, new_abs_path:str) -> None:
    pass