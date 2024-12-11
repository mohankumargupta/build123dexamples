from typing import Callable, Union
import sys

def generate_movement_functions() -> None:
    """
    Generate movement functions and add them to the current module with full IntelliSense support.
    """
    def up(distance: Union[int, float]) -> str:
        return f"Moving up {distance} units"

    def down(distance: Union[int, float]) -> str:
        return f"Moving down {distance} units"

    def left(distance: Union[int, float]) -> str:
        return f"Moving left {distance} units"

    def right(distance: Union[int, float]) -> str:
        return f"Moving right {distance} units"

    # Basic movements
    basic_moves = {"up": up, "down": down, "left": left, "right": right}
    
    # Add basic moves to module
    current_module = sys.modules[__name__]
    for name, func in basic_moves.items():
        setattr(current_module, name, func)

    # Generate compound moves with explicit signatures
    moves = list(basic_moves.keys())
    function_definitions = []

    for i in range(2, len(moves) + 1):
        from itertools import permutations
        for combination in permutations(moves, i):
            func_name = "_".join(combination)
            parameters = ", ".join(f"{direction}: Union[int, float]" for direction in combination)
            docstring = "\n".join(
                f"    {direction} (int/float): Distance for {direction}" for direction in combination
            )
            body = 'print(f"{func_name}")'
            #body = "''.join(["
            #body += ", ".join(f"getattr(sys.modules[__name__], '{direction}')({direction})" for direction in combination)
            #body += "])"

            # Generate function code
            func_code = f"""
def {func_name}({parameters}) -> str:
    \"\"\"
    Compound move: {' -> '.join(combination)}
    
    Args:
{docstring}
    
    Returns:
        A string describing the movement sequence.
    \"\"\"
    return {body}
"""
            function_definitions.append(func_code)

    # Execute all generated function definitions
    for func_code in function_definitions:
        exec(func_code, globals())

    # Add all compound moves to module
    for func_code in function_definitions:
        func_name = func_code.split("def ")[1].split("(")[0]
        setattr(current_module, func_name, eval(func_name))

    # Define __all__ for the module
    current_module.__all__ = list(basic_moves.keys()) + [
        func_code.split("def ")[1].split("(")[0] for func_code in function_definitions
    ]

# Generate movement functions
generate_movement_functions()
