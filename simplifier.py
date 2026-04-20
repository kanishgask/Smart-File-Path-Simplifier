def simplify_path(path):
    stack = []
    steps = []

    parts = path.split("/")

    for part in parts:
        if part == "" or part == ".":
            steps.append(f"Ignored '{part}'")
            continue
        elif part == "..":
            if stack:
                removed = stack.pop()
                steps.append(f"Moved up, removed '{removed}'")
            else:
                steps.append("At root, cannot go up")
        else:
            stack.append(part)
            steps.append(f"Added '{part}' to path")

    simplified = "/" + "/".join(stack)

    return simplified, steps
