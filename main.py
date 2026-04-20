from simplifier import simplify_path
from visualizer import show_steps
from explainer import explain_steps

def run():
    print("=== Smart Path Simplifier ===")
    path = input("Enter path: ")

    result, steps = simplify_path(path)

    print("\n--- Simplified Path ---")
    print(result)

    print("\n--- Step Visualization ---")
    show_steps(steps)

    print("\n--- Explanation ---")
    print(explain_steps(steps))

if __name__ == "__main__":
    run()
