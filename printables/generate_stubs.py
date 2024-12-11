from typing import Union
import os

def generate_stub_file(module_name: str, output_path: str = None) -> None:
    """
    Generate a .pyi stub file for the given module.
    
    Args:
        module_name: Name of the module (e.g., 'polyfuncs').
        output_path: Optional path to save the generated .pyi file. Defaults to the module's location.
    """
    # Base movements
    base_moves = ["up", "down", "left", "right"]

    # Start building the .pyi content
    stub_lines = [
        f"# Stub file for {module_name}\n",
        "from typing import Union\n",
    ]
    
    # Add base movement functions
    for move in base_moves:
        stub_lines.append(
            f"def {move}(distance: Union[int, float]) -> str: ...\n"
        )

    # Generate compound movements
    from itertools import permutations

    for i in range(2, len(base_moves) + 1):
        for combination in permutations(base_moves, i):
            func_name = "_".join(combination)
            parameters = ", ".join(f"{direction}: Union[int, float]" for direction in combination)
            docstring = "\n    ".join(f"{direction} (int/float): Distance for {direction}" for direction in combination)
            
            # Add function signature
            stub_lines.append(
                f"def {func_name}({parameters}) -> str:\n"
                f'    """\n'
                f"    Compound move: {' -> '.join(combination)}\n\n"
                f"    Args:\n    {docstring}\n\n"
                f"    Returns:\n        A string describing the movement sequence.\n"
                f'    """\n'
                f"    ...\n\n"
            )

    # Determine the output path for the .pyi file
    if output_path is None:
        output_path = f"{module_name}.pyi"
    else:
        output_path = os.path.join(output_path, f"{module_name}.pyi")

    # Write the .pyi file
    with open(output_path, "w") as stub_file:
        stub_file.writelines(stub_lines)

    print(f"Stub file generated at {output_path}")

# Generate the stub file for the current module
generate_stub_file("polyfuncs")
