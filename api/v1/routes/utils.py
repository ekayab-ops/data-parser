import json
import logging
from typing import Dict, List, Tuple

def load_json_file(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File {file_path} not found")
        raise
    except json.JSONDecodeError:
        logging.error(f"Failed to parse JSON from {file_path}")
        raise

def extract_data_from_doubles(doubles: List[str]) -> Tuple[List[str], List[str]]:
    date_list = []
    value_list = []
    for double in doubles:
        parts = double.split(',')
        if len(parts) != 2:
            logging.warning(f"Invalid date-value pair: {double}")
            continue
        date_str, value_str = parts
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            value = float(value_str)
        except ValueError:
            logging.warning(f"Invalid date or value: {double}")
            continue
        date_list.append(date)
        value_list.append(value)
    return date_list, value_list