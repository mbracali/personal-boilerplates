import os
import importlib

def register_services():
    """
    Dynamically imports all modules in the services directory.
    This ensures that all tools, resources, and prompts decorated with @mcp
    are registered automatically.
    """
    services_dir = os.path.dirname(__file__)
    for filename in os.listdir(services_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f".{filename[:-3]}"
            # Use relative import within the package
            importlib.import_module(module_name, package=__package__)

# Trigger registration on import
register_services()
