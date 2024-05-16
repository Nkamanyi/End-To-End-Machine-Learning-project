import logging
import os
from datetime import datetime

# Directory for logs
log_dir_name = "logs"
log_dir_path = os.path.join(os.getcwd(), log_dir_name)
# Ensure the directory exists
os.makedirs(log_dir_path, exist_ok=True)

# Log file with a timestamp
log_file_name = 'app.log'
log_file_path = os.path.join(log_dir_path, log_file_name)

# Basic configuration for logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")
