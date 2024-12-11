# Auto-generated module: polyfuncsgenerated
from typing import Union

def up(distance: Union[int, float]) -> str:
    """
    Move up a specified distance.

    Args:
        distance (int/float): Number of units to move up.

    Returns:
        A string describing the up movement.
    """
    return f"Moving up {distance} units"

def down(distance: Union[int, float]) -> str:
    """
    Move down a specified distance.

    Args:
        distance (int/float): Number of units to move down.

    Returns:
        A string describing the down movement.
    """
    return f"Moving down {distance} units"

def left(distance: Union[int, float]) -> str:
    """
    Move left a specified distance.

    Args:
        distance (int/float): Number of units to move left.

    Returns:
        A string describing the left movement.
    """
    return f"Moving left {distance} units"

def right(distance: Union[int, float]) -> str:
    """
    Move right a specified distance.

    Args:
        distance (int/float): Number of units to move right.

    Returns:
        A string describing the right movement.
    """
    return f"Moving right {distance} units"

def up_down(up: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: up -> down

    Args:
    up (int/float): Distance for up
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([up(up), down(down)])

def up_left(up: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: up -> left

    Args:
    up (int/float): Distance for up
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([up(up), left(left)])

def up_right(up: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: up -> right

    Args:
    up (int/float): Distance for up
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([up(up), right(right)])

def down_up(down: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: down -> up

    Args:
    down (int/float): Distance for down
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([down(down), up(up)])

def down_left(down: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: down -> left

    Args:
    down (int/float): Distance for down
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([down(down), left(left)])

def down_right(down: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: down -> right

    Args:
    down (int/float): Distance for down
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([down(down), right(right)])

def left_up(left: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: left -> up

    Args:
    left (int/float): Distance for left
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([left(left), up(up)])

def left_down(left: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: left -> down

    Args:
    left (int/float): Distance for left
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([left(left), down(down)])

def left_right(left: Union[int, float], right: Union[int, float]) -> str:
    """
    Compound move: left -> right

    Args:
    left (int/float): Distance for left
    right (int/float): Distance for right

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([left(left), right(right)])

def right_up(right: Union[int, float], up: Union[int, float]) -> str:
    """
    Compound move: right -> up

    Args:
    right (int/float): Distance for right
    up (int/float): Distance for up

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([right(right), up(up)])

def right_down(right: Union[int, float], down: Union[int, float]) -> str:
    """
    Compound move: right -> down

    Args:
    right (int/float): Distance for right
    down (int/float): Distance for down

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([right(right), down(down)])

def right_left(right: Union[int, float], left: Union[int, float]) -> str:
    """
    Compound move: right -> left

    Args:
    right (int/float): Distance for right
    left (int/float): Distance for left

    Returns:
        A string describing the movement sequence.
    """
    return  + ', then '.join([right(right), left(left)])

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
    return  + ', then '.join([up(up), down(down), left(left)])

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
    return  + ', then '.join([up(up), down(down), right(right)])

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
    return  + ', then '.join([up(up), left(left), down(down)])

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
    return  + ', then '.join([up(up), left(left), right(right)])

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
    return  + ', then '.join([up(up), right(right), down(down)])

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
    return  + ', then '.join([up(up), right(right), left(left)])

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
    return  + ', then '.join([down(down), up(up), left(left)])

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
    return  + ', then '.join([down(down), up(up), right(right)])

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
    return  + ', then '.join([down(down), left(left), up(up)])

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
    return  + ', then '.join([down(down), left(left), right(right)])

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
    return  + ', then '.join([down(down), right(right), up(up)])

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
    return  + ', then '.join([down(down), right(right), left(left)])

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
    return  + ', then '.join([left(left), up(up), down(down)])

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
    return  + ', then '.join([left(left), up(up), right(right)])

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
    return  + ', then '.join([left(left), down(down), up(up)])

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
    return  + ', then '.join([left(left), down(down), right(right)])

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
    return  + ', then '.join([left(left), right(right), up(up)])

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
    return  + ', then '.join([left(left), right(right), down(down)])

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
    return  + ', then '.join([right(right), up(up), down(down)])

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
    return  + ', then '.join([right(right), up(up), left(left)])

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
    return  + ', then '.join([right(right), down(down), up(up)])

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
    return  + ', then '.join([right(right), down(down), left(left)])

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
    return  + ', then '.join([right(right), left(left), up(up)])

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
    return  + ', then '.join([right(right), left(left), down(down)])

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
    return  + ', then '.join([up(up), down(down), left(left), right(right)])

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
    return  + ', then '.join([up(up), down(down), right(right), left(left)])

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
    return  + ', then '.join([up(up), left(left), down(down), right(right)])

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
    return  + ', then '.join([up(up), left(left), right(right), down(down)])

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
    return  + ', then '.join([up(up), right(right), down(down), left(left)])

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
    return  + ', then '.join([up(up), right(right), left(left), down(down)])

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
    return  + ', then '.join([down(down), up(up), left(left), right(right)])

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
    return  + ', then '.join([down(down), up(up), right(right), left(left)])

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
    return  + ', then '.join([down(down), left(left), up(up), right(right)])

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
    return  + ', then '.join([down(down), left(left), right(right), up(up)])

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
    return  + ', then '.join([down(down), right(right), up(up), left(left)])

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
    return  + ', then '.join([down(down), right(right), left(left), up(up)])

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
    return  + ', then '.join([left(left), up(up), down(down), right(right)])

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
    return  + ', then '.join([left(left), up(up), right(right), down(down)])

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
    return  + ', then '.join([left(left), down(down), up(up), right(right)])

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
    return  + ', then '.join([left(left), down(down), right(right), up(up)])

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
    return  + ', then '.join([left(left), right(right), up(up), down(down)])

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
    return  + ', then '.join([left(left), right(right), down(down), up(up)])

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
    return  + ', then '.join([right(right), up(up), down(down), left(left)])

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
    return  + ', then '.join([right(right), up(up), left(left), down(down)])

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
    return  + ', then '.join([right(right), down(down), up(up), left(left)])

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
    return  + ', then '.join([right(right), down(down), left(left), up(up)])

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
    return  + ', then '.join([right(right), left(left), up(up), down(down)])

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
    return  + ', then '.join([right(right), left(left), down(down), up(up)])

__all__ = ["up", "down", "left", "right", "up_down", "up_left", "up_right", "down_up", "down_left", "down_right", "left_up", "left_down", "left_right", "right_up", "right_down", "right_left", "up_down_left", "up_down_right", "up_left_down", "up_left_right", "up_right_down", "up_right_left", "down_up_left", "down_up_right", "down_left_up", "down_left_right", "down_right_up", "down_right_left", "left_up_down", "left_up_right", "left_down_up", "left_down_right", "left_right_up", "left_right_down", "right_up_down", "right_up_left", "right_down_up", "right_down_left", "right_left_up", "right_left_down", "up_down_left_right", "up_down_right_left", "up_left_down_right", "up_left_right_down", "up_right_down_left", "up_right_left_down", "down_up_left_right", "down_up_right_left", "down_left_up_right", "down_left_right_up", "down_right_up_left", "down_right_left_up", "left_up_down_right", "left_up_right_down", "left_down_up_right", "left_down_right_up", "left_right_up_down", "left_right_down_up", "right_up_down_left", "right_up_left_down", "right_down_up_left", "right_down_left_up", "right_left_up_down", "right_left_down_up"]
