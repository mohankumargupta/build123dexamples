import functools
import importlib
import sys
from contextlib import contextmanager
from typing import Optional, Any

class CADVisualizationHelper:
    @staticmethod
    def import_optional_module(module_name: str):
        """
        Safely import an optional module, returning None if it can't be imported.
        
        Args:
            module_name (str): Name of the module to import
        
        Returns:
            The imported module or None if import fails
        """
        try:
            return importlib.import_module(module_name)
        except ImportError:
            print(f"Optional module {module_name} could not be imported.")
            return None

    @contextmanager
    def cad_context(self, 
                    show: bool = True, 
                    reset_camera: Optional[Any] = None, 
                    modules_to_import: list = None):
        """
        A context manager for CAD operations that handles imports and visualization.
        
        Args:
            show (bool): Whether to show the model. Defaults to True.
            reset_camera (Optional[Any]): Camera reset option. 
            modules_to_import (list): List of modules to import dynamically
        """
        # Dynamic imports
        imported_modules = {}
        if modules_to_import:
            for module_name in modules_to_import:
                module = self.import_optional_module(module_name)
                if module:
                    # Add to global namespace
                    module_short_name = module_name.split('.')[-1]
                    globals()[module_short_name] = module
                    imported_modules[module_short_name] = module
        
        try:
            yield self
        finally:
            # Optionally show the model if requested
            if show:
                ocp_vscode = imported_modules.get('ocp_vscode')
                if ocp_vscode:
                    camera_enum = getattr(ocp_vscode, 'Camera', None)
                    show_func = getattr(ocp_vscode, 'show_all', None)
                    
                    if show_func:
                        # Use provided reset_camera or default to KEEP if available
                        camera_arg = reset_camera if reset_camera is not None else (
                            camera_enum.KEEP if camera_enum else None
                        )
                        
                        if camera_arg is not None:
                            show_func(reset_camera=camera_arg)
                        else:
                            show_func()

    def visualize(self, 
                  show: bool = True, 
                  reset_camera: Optional[Any] = None, 
                  modules_to_import: list = None):
        """
        Decorator for CAD visualization that wraps the function in a context manager.
        
        Args:
            show (bool): Whether to show the model. Defaults to True.
            reset_camera (Optional[Any]): Camera reset option. 
            modules_to_import (list): List of modules to import dynamically
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                with self.cad_context(show, reset_camera, modules_to_import):
                    return func(*args, **kwargs)
            return wrapper
        return decorator

# Create a global instance for easy use
cad_helper = CADVisualizationHelper()

# Convenience decorators
def cad_visualize(show: bool = True, 
                  reset_camera: Optional[Any] = None, 
                  modules_to_import: list = None):
    """
    Convenience function to use the visualize decorator with default global helper
    """
    return cad_helper.visualize(show, reset_camera, modules_to_import)