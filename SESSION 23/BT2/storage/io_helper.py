import os


def safe_create_dir(path):
    os.makedirs(
        path,
        exist_ok=True
    )