def explain_steps(steps):
    explanation = ""

    for step in steps:
        if "Ignored" in step:
            explanation += "Ignored current or empty directory.\n"
        elif "Moved up" in step:
            explanation += "Handled parent directory using stack pop.\n"
        elif "Added" in step:
            explanation += "Added valid directory to stack.\n"

    explanation += "\nFinal result built from stack."

    return explanation
