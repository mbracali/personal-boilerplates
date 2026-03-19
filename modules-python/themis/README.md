# Themis - YAML Configuration Manager

Themis is a simple and intuitive library for managing YAML configuration files. It provides an easy-to-use interface for reading and writing configuration data, with automatic file creation and directory management.

## Features

- 📝 **Simple API** - Easy to use with minimal code
- 🆕 **Auto-Create Files** - Automatically creates YAML files and directories if they don't exist
- 🔒 **Safe Operations** - Uses `yaml.safe_load()` for secure YAML parsing
- 📦 **String Storage** - All values are stored as strings for consistency
- 🗂️ **Directory Management** - Automatically creates parent directories when needed
- 🔍 **Key Management** - Check existence, delete keys, and clear entire configs

## Installation

### Prerequisites

Themis requires the `PyYAML` library. Install it using pip:

```bash
pip install pyyaml
```

### Setup

Place the `themis.py` file in your project directory or add it to your Python path.

## Basic Usage

### Import Themis

```python
from themis.themis import Themis
```

### Initialize a Configuration Manager

```python
# Initialize with a config file path
config = Themis('config.yaml')

# File will be created automatically if it doesn't exist
# Parent directories will also be created if needed
config = Themis('/path/to/my/config.yaml')
```

### Write Configuration Values

```python
# Write a single configuration value
config.write('database_host', 'localhost')
config.write('database_port', '5432')
config.write('api_key', 'your-secret-key-here')

# Write multiple values at once
config.write_dict({
    'app_name': 'My Application',
    'version': '1.0.0',
    'debug': 'False'
})
```

### Read Configuration Values

```python
# Read a specific configuration key
host = config.read('database_host')
print(host)  # Output: localhost

# Read entire configuration
all_config = config.read()
print(all_config)
# Output: {'database_host': 'localhost', 'database_port': '5432', ...}
```

### Check if Key Exists

```python
if config.exists('api_key'):
    api_key = config.read('api_key')
    print("API key found!")
else:
    print("API key not configured")
```

### Delete Configuration Keys

```python
# Delete a specific key
config.delete('old_setting')

# Clear all configuration
config.clear()
```

## API Reference

### `__init__(config_file_path: str)`

Initialize a Themis configuration manager.

**Parameters:**
- `config_file_path` (str): Path to the YAML configuration file

**Behavior:**
- Automatically creates the file if it doesn't exist
- Creates parent directories if they don't exist
- Initializes empty YAML file if creating new file

**Example:**
```python
config = Themis('my_config.yaml')
```

### `read(config_key: str = None)`

Read configuration data from the YAML file.

**Parameters:**
- `config_key` (str, optional): Specific key to read. If `None`, returns entire config dictionary.

**Returns:**
- If `config_key` is provided: The value for that key (or `None` if key doesn't exist)
- If `config_key` is `None`: Dictionary containing all configuration data

**Example:**
```python
# Read specific key
port = config.read('database_port')

# Read all config
all_settings = config.read()
```

### `write(config_key: str, config_value: str)`

Write a single configuration value to the YAML file.

**Parameters:**
- `config_key` (str): The configuration key to write
- `config_value` (str): The value to write (will be converted to string)

**Behavior:**
- Converts value to string before storing
- Preserves existing configuration data
- Updates existing keys or creates new ones

**Example:**
```python
config.write('timeout', '30')
config.write('max_retries', '3')
```

### `write_dict(config_dict: dict)`

Write multiple configuration values at once from a dictionary.

**Parameters:**
- `config_dict` (dict): Dictionary of key-value pairs to write

**Behavior:**
- Converts all values to strings
- Preserves existing configuration data
- Updates existing keys or creates new ones

**Example:**
```python
settings = {
    'host': 'localhost',
    'port': '8080',
    'ssl': 'True'
}
config.write_dict(settings)
```

### `delete(config_key: str)`

Delete a configuration key from the YAML file.

**Parameters:**
- `config_key` (str): The configuration key to delete

**Behavior:**
- Only deletes if key exists
- Preserves all other configuration data

**Example:**
```python
config.delete('old_setting')
```

### `exists(config_key: str) -> bool`

Check if a configuration key exists in the YAML file.

**Parameters:**
- `config_key` (str): The configuration key to check

**Returns:**
- `bool`: `True` if key exists, `False` otherwise

**Example:**
```python
if config.exists('api_key'):
    key = config.read('api_key')
```

### `clear()`

Clear all configuration data from the YAML file.

**Behavior:**
- Removes all configuration keys
- File remains but becomes empty (contains only empty dictionary)

**Example:**
```python
config.clear()
```

## Examples

### Example 1: Application Configuration

```python
from themis.themis import Themis

# Initialize configuration
config = Themis('app_config.yaml')

# Set up application settings
config.write('app_name', 'My Awesome App')
config.write('version', '2.1.0')
config.write('debug_mode', 'False')
config.write('log_level', 'INFO')

# Read settings
app_name = config.read('app_name')
debug = config.read('debug_mode')
print(f"Running {app_name} (Debug: {debug})")
```

**Resulting YAML file (`app_config.yaml`):**
```yaml
app_name: My Awesome App
version: 2.1.0
debug_mode: 'False'
log_level: INFO
```

### Example 2: Database Configuration

```python
from themis.themis import Themis

# Initialize database config
db_config = Themis('database.yaml')

# Write database settings
db_config.write_dict({
    'host': 'localhost',
    'port': '5432',
    'database': 'myapp_db',
    'username': 'admin',
    'password': 'secret123',
    'pool_size': '10'
})

# Read connection settings
host = db_config.read('host')
port = db_config.read('port')
database = db_config.read('database')

print(f"Connecting to {host}:{port}/{database}")
```

### Example 3: Dynamic Configuration Management

```python
from themis.themis import Themis

config = Themis('settings.yaml')

# Check and set default values
if not config.exists('theme'):
    config.write('theme', 'dark')

if not config.exists('language'):
    config.write('language', 'en')

# Update user preferences
config.write('theme', 'light')
config.write('font_size', '14')

# Read current settings
current_theme = config.read('theme')
print(f"Current theme: {current_theme}")
```

### Example 4: Configuration with Nested Paths

```python
from themis.themis import Themis

# Themis will create the directory structure automatically
config = Themis('/path/to/my/project/config/settings.yaml')

config.write('project_name', 'My Project')
config.write('author', 'John Doe')

# File and directories are created automatically
```

### Example 5: Configuration Cleanup

```python
from themis.themis import Themis

config = Themis('temp_config.yaml')

# Add some settings
config.write('temp_setting_1', 'value1')
config.write('temp_setting_2', 'value2')
config.write('temp_setting_3', 'value3')

# Remove specific setting
config.delete('temp_setting_2')

# Check what remains
all_config = config.read()
print(all_config)  # {'temp_setting_1': 'value1', 'temp_setting_3': 'value3'}

# Clear everything
config.clear()
print(config.read())  # {}
```

### Example 6: Integration with Hermes Logger

```python
from themis.themis import Themis
from hermes import Hermes

# Initialize logger and config
log = Hermes('my_app')
config = Themis('app_config.yaml')

# Load configuration
app_name = config.read('app_name') or 'Unknown App'
debug_mode = config.read('debug_mode') == 'True'

log.post('INFO', f'Starting {app_name}')
log.post('INFO', f'Debug mode: {debug_mode}')

# Update configuration
config.write('last_run', '2025-01-25 14:30:00')
```

## YAML File Format

Themis stores all values as strings in YAML format. The resulting YAML files are human-readable and can be edited manually if needed.

**Example YAML file:**
```yaml
database_host: localhost
database_port: '5432'
api_key: your-secret-key
debug_mode: 'True'
max_connections: '100'
```

**Note:** All values are stored as strings. If you need to work with other data types, you'll need to convert them when reading:

```python
# Write as string
config.write('port', '5432')

# Read and convert to integer
port = int(config.read('port'))
```

## Error Handling

Themis handles common scenarios gracefully:

- **File doesn't exist**: Automatically creates the file
- **Directory doesn't exist**: Automatically creates parent directories
- **Empty file**: Returns empty dictionary `{}`
- **Key doesn't exist**: Returns `None` when reading a non-existent key

## Best Practices

1. **Use descriptive file names**: Choose clear names like `app_config.yaml` or `database.yaml`
2. **Organize by purpose**: Create separate config files for different concerns (database, API, app settings)
3. **Check before reading**: Use `exists()` to check if a key exists before reading critical values
4. **Set defaults**: Always provide default values for optional configuration
5. **Type conversion**: Remember to convert string values to appropriate types when needed
6. **Version control**: Add `.yaml` config files to `.gitignore` if they contain sensitive data

## Tips

- **Path handling**: Use absolute or relative paths. Themis will create directories as needed
- **String conversion**: All values are stored as strings. Convert to appropriate types when reading
- **File location**: Keep config files in a dedicated `config/` directory for better organization
- **Sensitive data**: Never commit sensitive configuration (API keys, passwords) to version control
- **Backup**: Consider backing up important configuration files

## Requirements

- Python 3.6+
- PyYAML (`pip install pyyaml`)

## License

This is a simple utility library. Use it as you see fit!

