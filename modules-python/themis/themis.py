# First party imports
import os
from pathlib import Path
import yaml

class Themis:
    """
    Class to handle YAML configuration files. Themis provides a simple
    interface to read and write configuration data from YAML files.
    Automatically creates files if they don't exist.
    """
    
    def __init__(self, config_file_path: str):
        """
        Class constructor, define the configuration file path.
        
        Args:
            config_file_path (str): Path to the YAML configuration file
        """
        self.config_file_path = config_file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """
        Ensure the configuration file exists. Create it with empty content if it doesn't.
        """
        file_path = Path(self.config_file_path)
        
        # Create parent directories if they don't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create empty YAML file if it doesn't exist
        if not file_path.exists():
            with open(file_path, 'w') as f:
                yaml.dump({}, f, default_flow_style=False)
    
    def read(self, config_key: str = None):
        """
        Read configuration data from the YAML file.
        
        Args:
            config_key (str, optional): Specific key to read. If None, returns entire config.
        
        Returns:
            dict or any: Configuration data. Returns entire config if key is None,
                        returns value for specific key if provided.
        """
        with open(self.config_file_path, 'r') as f:
            config_data = yaml.safe_load(f) or {}
        
        if config_key is None:
            return config_data
        else:
            return config_data.get(config_key)
    
    def write(self, config_key: str, config_value: str):
        """
        Write a configuration value to the YAML file.
        
        Args:
            config_key (str): The configuration key to write
            config_value (str): The value to write (will be stored as string)
        """
        # Read existing config
        config_data = self.read()
        
        # Update with new value (convert to string)
        config_data[config_key] = str(config_value)
        
        # Write back to file
        with open(self.config_file_path, 'w') as f:
            yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
    
    def write_dict(self, config_dict: dict):
        """
        Write multiple configuration values at once from a dictionary.
        
        Args:
            config_dict (dict): Dictionary of key-value pairs to write
        """
        # Read existing config
        config_data = self.read()
        
        # Update with new values (convert all to strings)
        for key, value in config_dict.items():
            config_data[key] = str(value)
        
        # Write back to file
        with open(self.config_file_path, 'w') as f:
            yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
    
    def delete(self, config_key: str):
        """
        Delete a configuration key from the YAML file.
        
        Args:
            config_key (str): The configuration key to delete
        """
        # Read existing config
        config_data = self.read()
        
        # Remove key if it exists
        if config_key in config_data:
            del config_data[config_key]
            
            # Write back to file
            with open(self.config_file_path, 'w') as f:
                yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
    
    def exists(self, config_key: str) -> bool:
        """
        Check if a configuration key exists in the YAML file.
        
        Args:
            config_key (str): The configuration key to check
        
        Returns:
            bool: True if key exists, False otherwise
        """
        config_data = self.read()
        return config_key in config_data
    
    def clear(self):
        """
        Clear all configuration data from the YAML file.
        """
        with open(self.config_file_path, 'w') as f:
            yaml.dump({}, f, default_flow_style=False)

