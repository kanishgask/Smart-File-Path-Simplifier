def validate_path(path):
    if not path.startswith("/"):
        print("Warning: Not an absolute path!")
    return True
