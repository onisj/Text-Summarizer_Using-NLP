import os
import sys
import logging

# Define the format for logging messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory and file for storing log messages
log_dir = "logs"                                          # Directory where log files will be stored
log_filepath = os.path.join(log_dir, "running_logs.log")  # Path to the log file

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True) 

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,                                   # Set the logging level to INFO
    format=logging_str,                                   # Use the defined format for log messages

    handlers=[
        logging.FileHandler(log_filepath),                # Log messages will be saved to the file
        logging.StreamHandler(sys.stdout)                 # Output log messages to the console for real-time debugging
    ]
)

# Create a logger instance for the 'textSummarizerLogger' with the configuration above
logger = logging.getLogger("textSummarizerLogger")

# Example usage of the logger:
# logger.info("This is an info message")
# logger.error("This is an error message")
