import os
from itertools import permutations
from typing import List

def generate_function_file(module_name: str, output_path: str = None) -> None:
    """
    Generate a Python source file with all movement functions.

    Args:
        module_name: Name of the module (e.g., 'polyfuncs').
        output_path: Optional path to save the generated .py file. Defaults to the current directory.
    """
    # Basic movements
    base_moves = ["up", "down", "left", "right"]

    # Start building the Python source code
    file_lines = [
        f"# Auto-generated module: {module_name}\n",
        "from typing import Union\n\n",
    ]

    # Add base movement functions
    for move in base_moves:
        file_lines.append(
            f"def {move}(distance: Union[int, float]) -> str:\n"
            f"    \"\"\"\n"
            f"    Move {move} a specified distance.\n\n"
            f"    Args:\n"
            f"        distance (int/float): Number of units to move {move}.\n\n"
            f"    Returns:\n"
            f"        A string describing the {move} movement.\n"
            f"    \"\"\"\n"
            f"    return f\"Moving {move} {{distance}} units\"\n\n"
        )

    # Generate compound movements
    for i in range(2, len(base_moves) + 1):
        for combination in permutations(base_moves, i):
            func_name = "_".join(combination)
            parameters = ", ".join(f"{direction}: Union[int, float]" for direction in combination)
            docstring = "\n    ".join(f"{direction} (int/float): Distance for {direction}" for direction in combination)
            move_sequence = " + ', then '.join([" + ", ".join(f"{direction}({direction})" for direction in combination) + "])"

            # Add function definition
            file_lines.append(
                f"def {func_name}({parameters}) -> str:\n"
                f"    \"\"\"\n"
                f"    Compound move: {' -> '.join(combination)}\n\n"
                f"    Args:\n    {docstring}\n\n"
                f"    Returns:\n"
                f"        A string describing the movement sequence.\n"
                f"    \"\"\"\n"
                f"    return {move_sequence}\n\n"
            )

    # Add __all__ for better module exports
    all_functions = [f'"{move}"' for move in base_moves] + [
        f'"{"_".join(combination)}"' for i in range(2, len(base_moves) + 1) for combination in permutations(base_moves, i)
    ]
    file_lines.append(f"__all__ = [{', '.join(all_functions)}]\n")

    # Determine the output path for the .py file
    if output_path is None:
        output_path = f"{module_name}.py"
    else:
        output_path = os.path.join(output_path, f"{module_name}.py")

    # Write the .py file
    with open(output_path, "w") as py_file:
        py_file.writelines(file_lines)

    print(f"Python source file generated at {output_path}")


# Generate the Python source file
generate_function_file("polyfuncsgenerated")
