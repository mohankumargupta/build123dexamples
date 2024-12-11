from __future__ import annotations

from build123d import *
from ocp_vscode import *
from typing import Tuple, Optional, Any, Self, Type

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

def main() -> None:
    # Demonstration of point input
    with BuildPoly(start_point=(5.0, 5.0), close=False) as poly:
        line(end_point=(25.0, 5.0))
    
    show(poly, reset_camera=Camera.KEEP)

if __name__ == "__main__":
    main()