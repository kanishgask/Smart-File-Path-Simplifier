from simplifier import simplify_path

def run_tests():
    test_paths = [
        "/home/",
        "/a/./b/../../c/",
        "/../",
        "/home//foo/"
    ]

    for path in test_paths:
        result, _ = simplify_path(path)
        print(f"Input: {path} -> Output: {result}")

if __name__ == "__main__":
    run_tests()
