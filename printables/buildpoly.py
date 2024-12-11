from build123d import *
from ocp_vscode import *
from typing import Tuple

class BuildPoly(BuildLine):

    _current_manager = None

    def __init__(self, workplane = Plane.XY, mode = Mode.ADD, start_point: Tuple[float, float] = None, close: bool = True):
        self.start_point = start_point
        self.current_point = self.start_point
        self.close = close
        super().__init__(workplane, mode)

    def __enter__(self):
        super().__enter__()
        BuildPoly._current_manager = self
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        return super().__exit__(exception_type, exception_value, traceback)

    def lineto(self, end_point: Tuple[float, float]):
        Line(self.current_point, end_point)
        self.current_point = end_point

    @classmethod
    def _get_manager(cls):
        """
        Get the current active BuildPoly context manager.
        
        Raises:
            RuntimeError if no active context manager exists.
        """
        try:
            return cls._current_manager
        except AttributeError:
            raise RuntimeError("No active BuildPoly context. Use 'with BuildPoly() as poly:' first.")

def line(end_point: Tuple[float, float]):
    return BuildPoly._get_manager().lineto(end_point)

def main():
    with BuildPoly(start_point=(5,5), close=False) as poly:
        line(end_point=(25,5))
        
    show(poly, reset_camera=Camera.KEEP)

if __name__ == "__main__":
    main()