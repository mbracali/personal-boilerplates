# First party imports
import os, sys
from datetime import datetime

class Hermes:
    """
    Class to handle logging events. If you are confortable withe the
    default logging library use it, this project was made to be a
    alternative, with less code inside it.
    """
    
    # Emoji mapping for log types
    EMOJI_MAP = {
        "INFO": "💬", "SUCCESS": "✅", "DONE": "✅", "OK": "🆗",
        "COOL": "🆒", "WARN": "⚠️", "WARNING": "⚠️", "ERROR": "⛔",
        "ERRO": "⛔", "FAIL": "⛔", "START": "🏁", "STARTING": "🏁",
        "END": "🏁", "ENDING": "🏁", "IDEA": "💡", "FIXING": "🛠️",
        "FIX": "🛠️", "DESC": "🤖", "TRAINING": "🦾", "HEAR": "🎧",
        "GAME": "🕹️", "STAR": "⭐", "SET": "⚙️", "SETTINGS": "⚙️",
        "DETAIL": "🔍", "GRAPH": "📊", "LOCK": "🔓", "ATTACH": "📎",
        "ATENTION": "👀", "LOOK": "👀", "LOOKING": "👀", "MONEY": "💰",
        "RED": "🔴", "GREEN": "🟢", "ORANGE": "🟠", "YELLOW": "🟡",
        "SAVE": "💾", "SAVING": "💾", "DATE": "📅", "CALENDAR": "📅",
        "LOVE": "❤️", "HEARTH": "❤️", "FORBIDDEN": "🚫", "PARTY": "🎉",
        "BALLON": "🎈", "WRITE": "📝", "PENNYWISE": "🎈", "LIE": "🎂",
        "EASTER": "🥚"
    }

    def __init__(self, 
            log_app_name: str,
            log_file_name: str = "log.txt",
            log_file_path: str = "./"):
        """
        Class constructor, define logic and parameters.
        """
        # Get the day and year the object is created for naming the file
        file_date = datetime.now().strftime("%d_%m_%Y")

        # Set class attributes
        self.log_app_name = log_app_name.upper()
        self.log_file_name = f"{file_date}_{log_file_name}"
        self.log_file_path = log_file_path
        self.message_date = datetime.now().strftime("%d/%m/%Y %H:%M")

        # Set the first line of the log file
        self._write_message(f"LOG {self.log_app_name} START BY {os.getlogin().upper()}@{file_date}@{sys.platform.upper()} ", True)

    
    def _console_message(self, message):
        """ Print the message on the console """
        # Format the message with the date and print it
        print(f"{self.message_date } | {message}")


    def _write_message(self, message, blank_line = False):
        """ Write the message in the log file """

        # Format the message
        message = f"{self.message_date } | {message} \n"

        # Format the full file path
        full_file_path = (f"{self.log_file_path}{self.log_file_name}")

        # Write the string to the file
        with open(full_file_path, 'a') as f:

            # If blank line is true, write a blank line
            if blank_line: f.write("\n")

            # Write the message
            f.write(message)


    def post(self,
            log_type: str,
            log_message: str,
            log_action: str = "LOG",
            log_write: bool = True,
            log_print: bool = True):
        """
        Post an info message to the log.
        """
        # Set emoji based on the log_type using dictionary lookup
        log_emoji = self.EMOJI_MAP.get(log_type.upper(), "📝")

        # Define messages for log file and console output
        file_message = f"{os.getlogin().upper()}@{self.log_app_name} | {log_action} | {log_message}"
        console_message = f"{os.getlogin().upper()}@{self.log_app_name} {log_emoji} | {log_action} | {log_message}"

        # Get the current date and time with hour and minutes
        self.message_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Based on the parameters, print and log messages
        if log_print: self._console_message(console_message)
        if log_write: self._write_message(file_message)
