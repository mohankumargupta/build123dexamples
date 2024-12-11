from __future__ import annotations

from build123d import *
from ocp_vscode import *
from typing import Tuple, Optional, Any, Self, Type, Union

class BuildPoly(BuildLine):
    # Class variable with Optional type
    _current_manager: Optional[BuildPoly] = None

    def __init__(
        self, 
        workplane: Plane = Plane.XY, 
        mode: Mode = Mode.ADD, 
        start_point: Optional[Tuple[float, float]] = None, 
        close: bool = True
    ):
        # Explicitly type annotate instance variables
        self.start_point: Optional[Tuple[float, float]] = start_point
        self.current_point: Optional[Tuple[float, float]] = self.start_point
        self.close: bool = close
        
        # Call parent constructor with explicit type checking
        super().__init__(workplane, mode)

    def __enter__(self: Self) -> Self:
        # Ensure type safety for context manager entry
        super().__enter__()
        BuildPoly._current_manager = self
        return self
    
    def __exit__(
        self, 
        exception_type: Optional[Type[BaseException]], 
        exception_value: Optional[BaseException], 
        traceback: Optional[Any]
    ) -> Optional[bool]:
        # More precise type annotations for exit method
        return super().__exit__(exception_type, exception_value, traceback)

    def lineto(self, end_point: Tuple[float, float]) -> Line:
        """
        Create a line to the specified end point
        
        Args:
            end_point: Destination point of the line
        """
        # Create the line
        l = Line(self.current_point, end_point)
        self.current_point = end_point
        return l

    @classmethod
    def _get_manager(cls) -> BuildPoly:
        """
        Get the current active BuildPoly context manager.
        
        Returns:
            The current active context manager
        
        Raises:
            RuntimeError: If no active context manager exists
        """
        if cls._current_manager is None:
            raise RuntimeError("No active BuildPoly context. Use 'with BuildPoly() as poly:' first.")
        return cls._current_manager

def line(end_point: Tuple[float, float]) -> Line:
    """
    Create a line from the current point to the specified end point.
    
    Args:
        end_point: The destination point of the line
    """
    return BuildPoly._get_manager().lineto(end_point)

def up(distance: float) -> Line:
    """
    Move up (along positive Y-axis) by the specified distance
    
    Args:
        distance: Distance to move up
    
    Returns:
        The created Line object
    """
    manager = BuildPoly._get_manager()
    x,y = manager.current_point
    return line((x, y + distance))

def down(distance: float) -> Line:
    """
    Move down (along negative Y-axis) by the specified distance
    
    Args:
        distance: Distance to move down
    
    Returns:
        The created Line object
    """
    manager = BuildPoly._get_manager()
    x,y = manager.current_point    
    return line((x, y - distance))

def left(distance: float) -> Line:
    """
    Move left (along negative X-axis) by the specified distance
    
    Args:
        distance: Distance to move left
    
    Returns:
        The created Line object
    """
    manager = BuildPoly._get_manager()
    x,y = manager.current_point   
    return line((x - distance, y))

def right(distance: float) -> Line:
    """
    Move right (along positive X-axis) by the specified distance
    
    Args:
        distance: Distance to move right
    
    Returns:
        The created Line object
    """
    manager = BuildPoly._get_manager()
    x,y = manager.current_point   
    return line((x + distance, y))

def main() -> None:
    # Demonstration of direction functions
    with BuildPoly(start_point=(5.0, 5.0), close=False) as poly:
        right(20.0)
        up(10.0)
        left(20.0)
        down(10.0)

    face = make_face(poly.wires())
    part = extrude(face, amount=10)    
    show_all(reset_camera=Camera.KEEP)

if __name__ == "__main__":
    main()