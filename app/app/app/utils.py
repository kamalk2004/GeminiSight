import os

def file_exists(path):
return os.path.exists(path)

def load_file(path):
with open(path, "rb") as f:
return f.read()
