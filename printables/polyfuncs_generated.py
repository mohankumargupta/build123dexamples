# Auto-generated module: polyfuncs_generated
from typing import Union

def up(distance: Union[int, float]) -> None:
    """
    Move up a specified distance.

    Args:
        distance (int/float): Number of units to move up.
    """
    print(f"Moving up {distance} units")

def down(distance: Union[int, float]) -> None:
    """
    Move down a specified distance.

    Args:
        distance (int/float): Number of units to move down.
    """
    print(f"Moving down {distance} units")

def left(distance: Union[int, float]) -> None:
    """
    Move left a specified distance.

    Args:
        distance (int/float): Number of units to move left.
    """
    print(f"Moving left {distance} units")

def right(distance: Union[int, float]) -> None:
    """
    Move right a specified distance.

    Args:
        distance (int/float): Number of units to move right.
    """
    print(f"Moving right {distance} units")

def up_down(up_distance: Union[int, float], down_distance: Union[int, float]) -> None:
    """
    Compound move: up -> down

    Args:
    up_distance (int/float): Distance for up
    down_distance (int/float): Distance for down

    up(up_distance)
    down(down_distance)
    """
    up(up_distance)
    down(down_distance)

def up_left(up_distance: Union[int, float], left_distance: Union[int, float]) -> None:
    """
    Compound move: up -> left

    Args:
    up_distance (int/float): Distance for up
    left_distance (int/float): Distance for left

    up(up_distance)
    left(left_distance)
    """
    up(up_distance)
    left(left_distance)

def up_right(up_distance: Union[int, float], right_distance: Union[int, float]) -> None:
    """
    Compound move: up -> right

    Args:
    up_distance (int/float): Distance for up
    right_distance (int/float): Distance for right

    up(up_distance)
    right(right_distance)
    """
    up(up_distance)
    right(right_distance)

def down_up(down_distance: Union[int, float], up_distance: Union[int, float]) -> None:
    """
    Compound move: down -> up

    Args:
    down_distance (int/float): Distance for down
    up_distance (int/float): Distance for up

    down(down_distance)
    up(up_distance)
    """
    down(down_distance)
    up(up_distance)

def down_left(down_distance: Union[int, float], left_distance: Union[int, float]) -> None:
    """
    Compound move: down -> left

    Args:
    down_distance (int/float): Distance for down
    left_distance (int/float): Distance for left

    down(down_distance)
    left(left_distance)
    """
    down(down_distance)
    left(left_distance)

def down_right(down_distance: Union[int, float], right_distance: Union[int, float]) -> None:
    """
    Compound move: down -> right

    Args:
    down_distance (int/float): Distance for down
    right_distance (int/float): Distance for right

    down(down_distance)
    right(right_distance)
    """
    down(down_distance)
    right(right_distance)

def left_up(left_distance: Union[int, float], up_distance: Union[int, float]) -> None:
    """
    Compound move: left -> up

    Args:
    left_distance (int/float): Distance for left
    up_distance (int/float): Distance for up

    left(left_distance)
    up(up_distance)
    """
    left(left_distance)
    up(up_distance)

def left_down(left_distance: Union[int, float], down_distance: Union[int, float]) -> None:
    """
    Compound move: left -> down

    Args:
    left_distance (int/float): Distance for left
    down_distance (int/float): Distance for down

    left(left_distance)
    down(down_distance)
    """
    left(left_distance)
    down(down_distance)

def left_right(left_distance: Union[int, float], right_distance: Union[int, float]) -> None:
    """
    Compound move: left -> right

    Args:
    left_distance (int/float): Distance for left
    right_distance (int/float): Distance for right

    left(left_distance)
    right(right_distance)
    """
    left(left_distance)
    right(right_distance)

def right_up(right_distance: Union[int, float], up_distance: Union[int, float]) -> None:
    """
    Compound move: right -> up

    Args:
    right_distance (int/float): Distance for right
    up_distance (int/float): Distance for up

    right(right_distance)
    up(up_distance)
    """
    right(right_distance)
    up(up_distance)

def right_down(right_distance: Union[int, float], down_distance: Union[int, float]) -> None:
    """
    Compound move: right -> down

    Args:
    right_distance (int/float): Distance for right
    down_distance (int/float): Distance for down

    right(right_distance)
    down(down_distance)
    """
    right(right_distance)
    down(down_distance)

def right_left(right_distance: Union[int, float], left_distance: Union[int, float]) -> None:
    """
    Compound move: right -> left

    Args:
    right_distance (int/float): Distance for right
    left_distance (int/float): Distance for left

    right(right_distance)
    left(left_distance)
    """
    right(right_distance)
    left(left_distance)

def up_down_left(up_distance: Union[int, float], down_distance: Union[int, float], left_distance: Union[int, float]) -> None:
    """
    Compound move: up -> down -> left

    Args:
    up_distance (int/float): Distance for up
    down_distance (int/float): Distance for down
    left_distance (int/float): Distance for left

    up(up_distance)
    down(down_distance)
    left(left_distance)
    """
    up(up_distance)
    down(down_distance)
    left(left_distance)

def up_down_right(up_distance: Union[int, float], down_distance: Union[int, float], right_distance: Union[int, float]) -> None:
    """
    Compound move: up -> down -> right

    Args:
    up_distance (int/float): Distance for up
    down_distance (int/float): Distance for down
    right_distance (int/float): Distance for right

    up(up_distance)
    down(down_distance)
    right(right_distance)
    """
    up(up_distance)
    down(down_distance)
    right(right_distance)

def up_left_down(up_distance: Union[int, float], left_distance: Union[int, float], down_distance: Union[int, float]) -> None:
    """
    Compound move: up -> left -> down

    Args:
    up_distance (int/float): Distance for up
    left_distance (int/float): Distance for left
    down_distance (int/float): Distance for down

    up(up_distance)
    left(left_distance)
    down(down_distance)
    """
    up(up_distance)
    left(left_distance)
    down(down_distance)

def up_left_right(up_distance: Union[int, float], left_distance: Union[int, float], right_distance: Union[int, float]) -> None:
    """
    Compound move: up -> left -> right

    Args:
    up_distance (int/float): Distance for up
    left_distance (int/float): Distance for left
    right_distance (int/float): Distance for right

    up(up_distance)
    left(left_distance)
    right(right_distance)
    """
    up(up_distance)
    left(left_distance)
    right(right_distance)

def up_right_down(up_distance: Union[int, float], right_distance: Union[int, float], down_distance: Union[int, float]) -> None:
    """
    Compound move: up -> right -> down

    Args:
    up_distance (int/float): Distance for up
    right_distance (int/float): Distance for right
    down_distance (int/float): Distance for down

    up(up_distance)
    right(right_distance)
    down(down_distance)
    """
    up(up_distance)
    right(right_distance)
    down(down_distance)

def up_right_left(up_distance: Union[int, float], right_distance: Union[int, float], left_distance: Union[int, float]) -> None:
    """
    Compound move: up -> right -> left

    Args:
    up_distance (int/float): Distance for up
    right_distance (int/float): Distance for right
    left_distance (int/float): Distance for left

    up(up_distance)
    right(right_distance)
    left(left_distance)
    """
    up(up_distance)
    right(right_distance)
    left(left_distance)

def down_up_left(down_distance: Union[int, float], up_distance: Union[int, float], left_distance: Union[int, float]) -> None:
    """
    Compound move: down -> up -> left

    Args:
    down_distance (int/float): Distance for down
    up_distance (int/float): Distance for up
    left_distance (int/float): Distance for left

    down(down_distance)
    up(up_distance)
    left(left_distance)
    """
    down(down_distance)
    up(up_distance)
    left(left_distance)

def down_up_right(down_distance: Union[int, float], up_distance: Union[int, float], right_distance: Union[int, float]) -> None:
    """
    Compound move: down -> up -> right

    Args:
    down_distance (int/float): Distance for down
    up_distance (int/float): Distance for up
    right_distance (int/float): Distance for right

    down(down_distance)
    up(up_distance)
    right(right_distance)
    """
    down(down_distance)
    up(up_distance)
    right(right_distance)

def down_left_up(down_distance: Union[int, float], left_distance: Union[int, float], up_distance: Union[int, float]) -> None:
    """
    Compound move: down -> left -> up

    Args:
    down_distance (int/float): Distance for down
    left_distance (int/float): Distance for left
    up_distance (int/float): Distance for up

    down(down_distance)
    left(left_distance)
    up(up_distance)
    """
    down(down_distance)
    left(left_distance)
    up(up_distance)

def down_left_right(down_distance: Union[int, float], left_distance: Union[int, float], right_distance: Union[int, float]) -> None:
    """
    Compound move: down -> left -> right

    Args:
    down_distance (int/float): Distance for down
    left_distance (int/float): Distance for left
    right_distance (int/float): Distance for right

    down(down_distance)
    left(left_distance)
    right(right_distance)
    """
    down(down_distance)
    left(left_distance)
    right(right_distance)

def down_right_up(down_distance: Union[int, float], right_distance: Union[int, float], up_distance: Union[int, float]) -> None:
    """
    Compound move: down -> right -> up

    Args:
    down_distance (int/float): Distance for down
    right_distance (int/float): Distance for right
    up_distance (int/float): Distance for up

    down(down_distance)
    right(right_distance)
    up(up_distance)
    """
    down(down_distance)
    right(right_distance)
    up(up_distance)

def down_right_left(down_distance: Union[int, float], right_distance: Union[int, float], left_distance: Union[int, float]) -> None:
    """
    Compound move: down -> right -> left

    Args:
    down_distance (int/float): Distance for down
    right_distance (int/float): Distance for right
    left_distance (int/float): Distance for left

    down(down_distance)
    right(right_distance)
    left(left_distance)
    """
    down(down_distance)
    right(right_distance)
    left(left_distance)

def left_up_down(left_distance: Union[int, float], up_distance: Union[int, float], down_distance: Union[int, float]) -> None:
    """
    Compound move: left -> up -> down

    Args:
    left_distance (int/float): Distance for left
    up_distance (int/float): Distance for up
    down_distance (int/float): Distance for down

    left(left_distance)
    up(up_distance)
    down(down_distance)
    """
    left(left_distance)
    up(up_distance)
    down(down_distance)

def left_up_right(left_distance: Union[int, float], up_distance: Union[int, float], right_distance: Union[int, float]) -> None:
    """
    Compound move: left -> up -> right

    Args:
    left_distance (int/float): Distance for left
    up_distance (int/float): Distance for up
    right_distance (int/float): Distance for right

    left(left_distance)
    up(up_distance)
    right(right_distance)
    """
    left(left_distance)
    up(up_distance)
    right(right_distance)

def left_down_up(left_distance: Union[int, float], down_distance: Union[int, float], up_distance: Union[int, float]) -> None:
    """
    Compound move: left -> down -> up

    Args:
    left_distance (int/float): Distance for left
    down_distance (int/float): Distance for down
    up_distance (int/float): Distance for up

    left(left_distance)
    down(down_distance)
    up(up_distance)
    """
    left(left_distance)
    down(down_distance)
    up(up_distance)

def left_down_right(left_distance: Union[int, float], down_distance: Union[int, float], right_distance: Union[int, float]) -> None:
    """
    Compound move: left -> down -> right

    Args:
    left_distance (int/float): Distance for left
    down_distance (int/float): Distance for down
    right_distance (int/float): Distance for right

    left(left_distance)
    down(down_distance)
    right(right_distance)
    """
    left(left_distance)
    down(down_distance)
    right(right_distance)

def left_right_up(left_distance: Union[int, float], right_distance: Union[int, float], up_distance: Union[int, float]) -> None:
    """
    Compound move: left -> right -> up

    Args:
    left_distance (int/float): Distance for left
    right_distance (int/float): Distance for right
    up_distance (int/float): Distance for up

    left(left_distance)
    right(right_distance)
    up(up_distance)
    """
    left(left_distance)
    right(right_distance)
    up(up_distance)

def left_right_down(left_distance: Union[int, float], right_distance: Union[int, float], down_distance: Union[int, float]) -> None:
    """
    Compound move: left -> right -> down

    Args:
    left_distance (int/float): Distance for left
    right_distance (int/float): Distance for right
    down_distance (int/float): Distance for down

    left(left_distance)
    right(right_distance)
    down(down_distance)
    """
    left(left_distance)
    right(right_distance)
    down(down_distance)

def right_up_down(right_distance: Union[int, float], up_distance: Union[int, float], down_distance: Union[int, float]) -> None:
    """
    Compound move: right -> up -> down

    Args:
    right_distance (int/float): Distance for right
    up_distance (int/float): Distance for up
    down_distance (int/float): Distance for down

    right(right_distance)
    up(up_distance)
    down(down_distance)
    """
    right(right_distance)
    up(up_distance)
    down(down_distance)

def right_up_left(right_distance: Union[int, float], up_distance: Union[int, float], left_distance: Union[int, float]) -> None:
    """
    Compound move: right -> up -> left

    Args:
    right_distance (int/float): Distance for right
    up_distance (int/float): Distance for up
    left_distance (int/float): Distance for left

    right(right_distance)
    up(up_distance)
    left(left_distance)
    """
    right(right_distance)
    up(up_distance)
    left(left_distance)

def right_down_up(right_distance: Union[int, float], down_distance: Union[int, float], up_distance: Union[int, float]) -> None:
    """
    Compound move: right -> down -> up

    Args:
    right_distance (int/float): Distance for right
    down_distance (int/float): Distance for down
    up_distance (int/float): Distance for up

    right(right_distance)
    down(down_distance)
    up(up_distance)
    """
    right(right_distance)
    down(down_distance)
    up(up_distance)

def right_down_left(right_distance: Union[int, float], down_distance: Union[int, float], left_distance: Union[int, float]) -> None:
    """
    Compound move: right -> down -> left

    Args:
    right_distance (int/float): Distance for right
    down_distance (int/float): Distance for down
    left_distance (int/float): Distance for left

    right(right_distance)
    down(down_distance)
    left(left_distance)
    """
    right(right_distance)
    down(down_distance)
    left(left_distance)

def right_left_up(right_distance: Union[int, float], left_distance: Union[int, float], up_distance: Union[int, float]) -> None:
    """
    Compound move: right -> left -> up

    Args:
    right_distance (int/float): Distance for right
    left_distance (int/float): Distance for left
    up_distance (int/float): Distance for up

    right(right_distance)
    left(left_distance)
    up(up_distance)
    """
    right(right_distance)
    left(left_distance)
    up(up_distance)

def right_left_down(right_distance: Union[int, float], left_distance: Union[int, float], down_distance: Union[int, float]) -> None:
    """
    Compound move: right -> left -> down

    Args:
    right_distance (int/float): Distance for right
    left_distance (int/float): Distance for left
    down_distance (int/float): Distance for down

    right(right_distance)
    left(left_distance)
    down(down_distance)
    """
    right(right_distance)
    left(left_distance)
    down(down_distance)

__all__ = ["up", "down", "left", "right", "up_down", "up_left", "up_right", "down_up", "down_left", "down_right", "left_up", "left_down", "left_right", "right_up", "right_down", "right_left", "up_down_left", "up_down_right", "up_left_down", "up_left_right", "up_right_down", "up_right_left", "down_up_left", "down_up_right", "down_left_up", "down_left_right", "down_right_up", "down_right_left", "left_up_down", "left_up_right", "left_down_up", "left_down_right", "left_right_up", "left_right_down", "right_up_down", "right_up_left", "right_down_up", "right_down_left", "right_left_up", "right_left_down"]
