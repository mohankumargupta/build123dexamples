# Stub file for polyfuncs
from typing import Union
def up(distance: Union[int, float]) -> str: ...
def down(distance: Union[int, float]) -> str: ...
def left(distance: Union[int, float]) -> str: ...
def right(distance: Union[int, float]) -> str: ...
def up_down(up: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: up -> down

    Args:
    up (int/float): Distance for up
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_left(up: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: up -> left

    Args:
    up (int/float): Distance for up
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_right(up: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: up -> right

    Args:
    up (int/float): Distance for up
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_up(down: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: down -> up

    Args:
    down (int/float): Distance for down
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_left(down: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: down -> left

    Args:
    down (int/float): Distance for down
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_right(down: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: down -> right

    Args:
    down (int/float): Distance for down
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_up(left: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: left -> up

    Args:
    left (int/float): Distance for left
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_down(left: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: left -> down

    Args:
    left (int/float): Distance for left
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_right(left: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: left -> right

    Args:
    left (int/float): Distance for left
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_up(right: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: right -> up

    Args:
    right (int/float): Distance for right
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_down(right: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: right -> down

    Args:
    right (int/float): Distance for right
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_left(right: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: right -> left

    Args:
    right (int/float): Distance for right
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_down_left(up: Union[int, float], down: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: up -> down -> left

    Args:
    up (int/float): Distance for up
    down (int/float): Distance for down
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_down_right(up: Union[int, float], down: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: up -> down -> right

    Args:
    up (int/float): Distance for up
    down (int/float): Distance for down
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_left_down(up: Union[int, float], left: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: up -> left -> down

    Args:
    up (int/float): Distance for up
    left (int/float): Distance for left
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_left_right(up: Union[int, float], left: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: up -> left -> right

    Args:
    up (int/float): Distance for up
    left (int/float): Distance for left
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_right_down(up: Union[int, float], right: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: up -> right -> down

    Args:
    up (int/float): Distance for up
    right (int/float): Distance for right
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_right_left(up: Union[int, float], right: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: up -> right -> left

    Args:
    up (int/float): Distance for up
    right (int/float): Distance for right
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_up_left(down: Union[int, float], up: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: down -> up -> left

    Args:
    down (int/float): Distance for down
    up (int/float): Distance for up
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_up_right(down: Union[int, float], up: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: down -> up -> right

    Args:
    down (int/float): Distance for down
    up (int/float): Distance for up
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_left_up(down: Union[int, float], left: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: down -> left -> up

    Args:
    down (int/float): Distance for down
    left (int/float): Distance for left
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_left_right(down: Union[int, float], left: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: down -> left -> right

    Args:
    down (int/float): Distance for down
    left (int/float): Distance for left
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_right_up(down: Union[int, float], right: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: down -> right -> up

    Args:
    down (int/float): Distance for down
    right (int/float): Distance for right
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_right_left(down: Union[int, float], right: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: down -> right -> left

    Args:
    down (int/float): Distance for down
    right (int/float): Distance for right
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_up_down(left: Union[int, float], up: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: left -> up -> down

    Args:
    left (int/float): Distance for left
    up (int/float): Distance for up
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_up_right(left: Union[int, float], up: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: left -> up -> right

    Args:
    left (int/float): Distance for left
    up (int/float): Distance for up
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_down_up(left: Union[int, float], down: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: left -> down -> up

    Args:
    left (int/float): Distance for left
    down (int/float): Distance for down
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_down_right(left: Union[int, float], down: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: left -> down -> right

    Args:
    left (int/float): Distance for left
    down (int/float): Distance for down
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_right_up(left: Union[int, float], right: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: left -> right -> up

    Args:
    left (int/float): Distance for left
    right (int/float): Distance for right
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_right_down(left: Union[int, float], right: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: left -> right -> down

    Args:
    left (int/float): Distance for left
    right (int/float): Distance for right
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_up_down(right: Union[int, float], up: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: right -> up -> down

    Args:
    right (int/float): Distance for right
    up (int/float): Distance for up
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_up_left(right: Union[int, float], up: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: right -> up -> left

    Args:
    right (int/float): Distance for right
    up (int/float): Distance for up
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_down_up(right: Union[int, float], down: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: right -> down -> up

    Args:
    right (int/float): Distance for right
    down (int/float): Distance for down
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_down_left(right: Union[int, float], down: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: right -> down -> left

    Args:
    right (int/float): Distance for right
    down (int/float): Distance for down
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_left_up(right: Union[int, float], left: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: right -> left -> up

    Args:
    right (int/float): Distance for right
    left (int/float): Distance for left
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_left_down(right: Union[int, float], left: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: right -> left -> down

    Args:
    right (int/float): Distance for right
    left (int/float): Distance for left
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_down_left_right(up: Union[int, float], down: Union[int, float], left: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: up -> down -> left -> right

    Args:
    up (int/float): Distance for up
    down (int/float): Distance for down
    left (int/float): Distance for left
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_down_right_left(up: Union[int, float], down: Union[int, float], right: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: up -> down -> right -> left

    Args:
    up (int/float): Distance for up
    down (int/float): Distance for down
    right (int/float): Distance for right
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_left_down_right(up: Union[int, float], left: Union[int, float], down: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: up -> left -> down -> right

    Args:
    up (int/float): Distance for up
    left (int/float): Distance for left
    down (int/float): Distance for down
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_left_right_down(up: Union[int, float], left: Union[int, float], right: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: up -> left -> right -> down

    Args:
    up (int/float): Distance for up
    left (int/float): Distance for left
    right (int/float): Distance for right
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_right_down_left(up: Union[int, float], right: Union[int, float], down: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: up -> right -> down -> left

    Args:
    up (int/float): Distance for up
    right (int/float): Distance for right
    down (int/float): Distance for down
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def up_right_left_down(up: Union[int, float], right: Union[int, float], left: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: up -> right -> left -> down

    Args:
    up (int/float): Distance for up
    right (int/float): Distance for right
    left (int/float): Distance for left
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_up_left_right(down: Union[int, float], up: Union[int, float], left: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: down -> up -> left -> right

    Args:
    down (int/float): Distance for down
    up (int/float): Distance for up
    left (int/float): Distance for left
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_up_right_left(down: Union[int, float], up: Union[int, float], right: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: down -> up -> right -> left

    Args:
    down (int/float): Distance for down
    up (int/float): Distance for up
    right (int/float): Distance for right
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_left_up_right(down: Union[int, float], left: Union[int, float], up: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: down -> left -> up -> right

    Args:
    down (int/float): Distance for down
    left (int/float): Distance for left
    up (int/float): Distance for up
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_left_right_up(down: Union[int, float], left: Union[int, float], right: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: down -> left -> right -> up

    Args:
    down (int/float): Distance for down
    left (int/float): Distance for left
    right (int/float): Distance for right
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_right_up_left(down: Union[int, float], right: Union[int, float], up: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: down -> right -> up -> left

    Args:
    down (int/float): Distance for down
    right (int/float): Distance for right
    up (int/float): Distance for up
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def down_right_left_up(down: Union[int, float], right: Union[int, float], left: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: down -> right -> left -> up

    Args:
    down (int/float): Distance for down
    right (int/float): Distance for right
    left (int/float): Distance for left
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_up_down_right(left: Union[int, float], up: Union[int, float], down: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: left -> up -> down -> right

    Args:
    left (int/float): Distance for left
    up (int/float): Distance for up
    down (int/float): Distance for down
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_up_right_down(left: Union[int, float], up: Union[int, float], right: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: left -> up -> right -> down

    Args:
    left (int/float): Distance for left
    up (int/float): Distance for up
    right (int/float): Distance for right
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_down_up_right(left: Union[int, float], down: Union[int, float], up: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: left -> down -> up -> right

    Args:
    left (int/float): Distance for left
    down (int/float): Distance for down
    up (int/float): Distance for up
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_down_right_up(left: Union[int, float], down: Union[int, float], right: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: left -> down -> right -> up

    Args:
    left (int/float): Distance for left
    down (int/float): Distance for down
    right (int/float): Distance for right
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_right_up_down(left: Union[int, float], right: Union[int, float], up: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: left -> right -> up -> down

    Args:
    left (int/float): Distance for left
    right (int/float): Distance for right
    up (int/float): Distance for up
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def left_right_down_up(left: Union[int, float], right: Union[int, float], down: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: left -> right -> down -> up

    Args:
    left (int/float): Distance for left
    right (int/float): Distance for right
    down (int/float): Distance for down
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_up_down_left(right: Union[int, float], up: Union[int, float], down: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: right -> up -> down -> left

    Args:
    right (int/float): Distance for right
    up (int/float): Distance for up
    down (int/float): Distance for down
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_up_left_down(right: Union[int, float], up: Union[int, float], left: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: right -> up -> left -> down

    Args:
    right (int/float): Distance for right
    up (int/float): Distance for up
    left (int/float): Distance for left
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_down_up_left(right: Union[int, float], down: Union[int, float], up: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: right -> down -> up -> left

    Args:
    right (int/float): Distance for right
    down (int/float): Distance for down
    up (int/float): Distance for up
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_down_left_up(right: Union[int, float], down: Union[int, float], left: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: right -> down -> left -> up

    Args:
    right (int/float): Distance for right
    down (int/float): Distance for down
    left (int/float): Distance for left
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_left_up_down(right: Union[int, float], left: Union[int, float], up: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: right -> left -> up -> down

    Args:
    right (int/float): Distance for right
    left (int/float): Distance for left
    up (int/float): Distance for up
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    ...

def right_left_down_up(right: Union[int, float], left: Union[int, float], down: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: right -> left -> down -> up

    Args:
    right (int/float): Distance for right
    left (int/float): Distance for left
    down (int/float): Distance for down
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    ...

