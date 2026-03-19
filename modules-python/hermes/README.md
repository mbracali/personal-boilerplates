# Hermes - Simple Logging Library

Hermes is a lightweight alternative to Python's standard logging library, designed with simplicity and visual feedback in mind. It provides emoji-enhanced console output and automatic file logging.

## Features

- 🎯 **Simple API** - Easy to use with minimal code
- 📝 **Automatic File Logging** - Logs are automatically saved to files with date-stamped names
- 🎨 **Emoji Support** - Visual indicators for different log types
- 📅 **Date/Time Stamping** - All messages include timestamps
- 💻 **Console & File Output** - Control whether messages appear in console, file, or both

## Installation

Simply place the `hermes.py` file in your project directory or add it to your Python path.

## Basic Usage

### Import Hermes

```python
from hermes import Hermes
```

### Initialize a Logger

```python
# Basic initialization
log = Hermes('my_app')

# With custom file name
log = Hermes('my_app', log_file_name='custom_log.txt')

# With custom file path
log = Hermes('my_app', log_file_path='/path/to/logs/')
```

### Post Log Messages

```python
# Simple log message
log.post('INFO', 'Application started')

# With custom action
log.post('SUCCESS', 'Data saved successfully', log_action='SAVE')

# Console only (no file write)
log.post('WARN', 'This is a warning', log_write=False)

# File only (no console print)
log.post('ERROR', 'An error occurred', log_print=False)
```

## Parameters

### `__init__` Parameters

- **`log_app_name`** (required): Name of your application (will be converted to uppercase)
- **`log_file_name`** (optional, default: `"log.txt"`): Name of the log file
- **`log_file_path`** (optional, default: `"./"`): Directory path where log files will be saved

**Note:** Log files are automatically named with the date prefix: `DD_MM_YYYY_log_file_name.txt`

### `post()` Parameters

- **`log_type`** (required): Type of log message (see available types below)
- **`log_message`** (required): The message to log
- **`log_action`** (optional, default: `"LOG"`): Action identifier for the log entry
- **`log_write`** (optional, default: `True`): Whether to write to file
- **`log_print`** (optional, default: `True`): Whether to print to console

## Available Log Types

Hermes supports the following log types with their corresponding emojis:

| Log Type | Emoji | Description |
|----------|-------|-------------|
| `INFO` | 💬 | Informational messages |
| `SUCCESS` | ✅ | Success operations |
| `DONE` | ✅ | Completed tasks |
| `OK` | 🆗 | OK status |
| `COOL` | 🆒 | Cool/Great status |
| `WARN` / `WARNING` | ⚠️ | Warning messages |
| `ERROR` / `ERRO` / `FAIL` | ⛔ | Error messages |
| `START` / `STARTING` | 🏁 | Start operations |
| `END` / `ENDING` | 🏁 | End operations |
| `IDEA` | 💡 | Ideas or suggestions |
| `FIX` / `FIXING` | 🛠️ | Fixes or repairs |
| `DESC` | 🤖 | Descriptions |
| `TRAINING` | 🦾 | Training related |
| `HEAR` | 🎧 | Audio/hearing related |
| `GAME` | 🕹️ | Game related |
| `STAR` | ⭐ | Star/important |
| `SET` / `SETTINGS` | ⚙️ | Settings |
| `DETAIL` | 🔍 | Detailed information |
| `GRAPH` | 📊 | Graph/chart related |
| `LOCK` | 🔓 | Lock/unlock operations |
| `ATTACH` | 📎 | Attachments |
| `ATENTION` / `LOOK` / `LOOKING` | 👀 | Attention/observation |
| `MONEY` | 💰 | Money/financial |
| `RED` | 🔴 | Red status indicator |
| `GREEN` | 🟢 | Green status indicator |
| `ORANGE` | 🟠 | Orange status indicator |
| `YELLOW` | 🟡 | Yellow status indicator |
| `SAVE` / `SAVING` | 💾 | Save operations |
| `DATE` / `CALENDAR` | 📅 | Date/calendar related |
| `LOVE` / `HEARTH` | ❤️ | Love/heart related |
| `FORBIDDEN` | 🚫 | Forbidden operations |
| `PARTY` | 🎉 | Celebration |
| `BALLON` / `PENNYWISE` | 🎈 | Balloon related |
| `WRITE` | 📝 | Write operations |
| `LIE` | 🎂 | Lie/cake (Easter egg?) |
| `EASTER` | 🥚 | Easter egg |
| *Any other type* | 📝 | Default emoji |

## Examples

### Example 1: Basic Application Logging

```python
from hermes.hermes import Hermes

# Initialize logger
log = Hermes('my_application')

# Log application start
log.post('START', 'Application initialization')

# Log some info
log.post('INFO', 'Loading configuration files')
log.post('SUCCESS', 'Configuration loaded successfully')

# Log a warning
log.post('WARN', 'Using default settings')

# Log completion
log.post('DONE', 'Application ready')
```

**Console Output:**
```
25/01/2025 14:30:15 | USER@MY_APPLICATION 🏁 | LOG | Application initialization
25/01/2025 14:30:15 | USER@MY_APPLICATION 💬 | LOG | Loading configuration files
25/01/2025 14:30:15 | USER@MY_APPLICATION ✅ | LOG | Configuration loaded successfully
25/01/2025 14:30:15 | USER@MY_APPLICATION ⚠️ | LOG | Using default settings
25/01/2025 14:30:15 | USER@MY_APPLICATION ✅ | LOG | Application ready
```

### Example 2: Error Handling

```python
from hermes.hermes import Hermes

log = Hermes('data_processor')

try:
    log.post('INFO', 'Processing data file')
    # ... processing code ...
    log.post('SUCCESS', 'Data processed successfully', log_action='PROCESS')
except Exception as e:
    log.post('ERROR', f'Failed to process data: {str(e)}', log_action='ERROR')
```

### Example 3: Console-Only Debug Messages

```python
log = Hermes('debug_app')

# Debug message (console only, not saved to file)
log.post('INFO', 'Debug information', log_write=False)
```

### Example 4: Silent File Logging

```python
log = Hermes('background_task')

# Log to file only (no console output)
log.post('INFO', 'Background task completed', log_print=False)
```

### Example 5: Custom Actions

```python
log = Hermes('api_server')

log.post('START', 'Server starting', log_action='SERVER')
log.post('INFO', 'Listening on port 8080', log_action='NETWORK')
log.post('SUCCESS', 'Database connected', log_action='DATABASE')
log.post('DONE', 'Server ready', log_action='SERVER')
```

## File Structure

When you initialize Hermes, it creates a log file with the following naming convention:

```
DD_MM_YYYY_log_file_name.txt
```

For example:
- `25_01_2025_log.txt` (default)
- `25_01_2025_custom_log.txt` (with custom name)

The log file includes:
- A header line when the logger is initialized
- All log messages with timestamps
- User and application information

## Log File Format

Each log entry in the file follows this format:
```
DD/MM/YYYY HH:MM:SS | USER@APP_NAME | ACTION | MESSAGE
```

Example:
```
25/01/2025 14:30:15 | USER@MY_APP | LOG | Application started
25/01/2025 14:30:16 | USER@MY_APP | SAVE | Data saved successfully
```

## Tips

1. **Use descriptive log types**: Choose log types that clearly indicate the message purpose
2. **Custom actions**: Use `log_action` to categorize different types of operations
3. **File management**: Log files are appended to, so they grow over time. Consider implementing log rotation if needed
4. **Error handling**: Wrap file operations in try/except if you need custom error handling
5. **Path handling**: Make sure the `log_file_path` directory exists before initializing Hermes

## License

This is a simple utility library. Use it as you see fit!

