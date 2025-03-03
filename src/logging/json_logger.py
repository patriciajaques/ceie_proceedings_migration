# src/logging/json_logger.py
import json
import os
import datetime
from src.config.config_loader import ConfigLoader


class JsonLogger:
    """
    Utility class for logging in JSON format.

    Facilitates registering data structures in JSON files
    with timestamp and directory support.
    """

    # Class-level configuration
    _config_loader = None
    _base_dir = None

    @classmethod
    def initialize(cls, config_loader: ConfigLoader):
        """
        Initializes the logger with configuration.

        Args:
            config_loader (ConfigLoader): Configuration loader instance.
        """
        cls._config_loader = config_loader
        output_dir = config_loader.get_config_value("output_dir")
        year = config_loader.get_config_value("year")
        cls._base_dir = os.path.join(output_dir, f"{year}", "logs")

    @classmethod
    def get_base_dir(cls):
        """
        Gets the base directory for logs.

        Returns:
            str: Base directory path.
        """
        if cls._base_dir is None:
            # Default directory if not initialized
            return "outputs/logs"
        return cls._base_dir

    @classmethod
    def _prepare_path(cls, file_name, directory=None):
        """
        Prepares a file path by ensuring directory exists and formatting the file name.

        Args:
            file_name (str): File name (without extension).
            directory (str, optional): Directory to save the file. If None, uses the default directory.

        Returns:
            str: Complete file path ready for use.
        """
        # Determine target directory
        target_dir = directory or cls.get_base_dir()

        # Ensure directory exists
        if not os.path.exists(target_dir):
            os.makedirs(target_dir, exist_ok=True)

        # Add .json extension if not present
        if not file_name.lower().endswith(".json"):
            file_name = f"{file_name}.json"

        # Return complete path
        return os.path.join(target_dir, file_name)

    @classmethod
    def print_json(cls, file_name, data, directory=None):
        """
        Saves data in JSON format to a file.

        Args:
            file_name (str): File name (without extension).
            data (dict/list): Data to be saved as JSON.
            directory (str, optional): Directory to save the file. If None, uses the default directory.

        Returns:
            str: Complete path of the saved file.
        """
        # Prepare file path
        file_path = cls._prepare_path(file_name, directory)

        # Add timestamp if not an existing file update
        data_to_save = data
        if isinstance(data, dict) and not os.path.exists(file_path):
            now = datetime.datetime.now()
            data_to_save = {
                "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
                "data": data,
            }

        # Save data in JSON format
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=2)

        return file_path

    @classmethod
    def read_json_file(cls, file_name, directory=None):
        """
        Reads data from a JSON file.

        Args:
            file_name (str): File name (without extension).
            directory (str, optional): File directory. If None, uses the default directory.

        Returns:
            dict/list: Data read from the JSON file.
        """
        # Prepare file path
        file_path = cls._prepare_path(file_name, directory)

        # Read data from JSON file
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data
