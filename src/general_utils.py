import logging, json
from pathlib import Path

def init_log():
    """Log initialisation"""
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M%S')
    logger = logging.getLogger()
    return logger

def path_util(relative_path: str) -> str:
    """
    Function to allow the use of relative paths anywhere in this script.
    This must must be used before passing rleative paths to other functions
    """

    try: 
        absolute_dir = Path(__file__).resolve().parent
        relative_path = Path(relative_path)
        absolute_resource_path = (absolute_dir/relative_path).resolve()
        return str(absolute_resource_path)
    except Exception as e:
        logging.error("Error using path utils")
        raise e 
    

def read_json(relative_path: str): 
    """
    Function to read json
    """
    try: 
        absolute_resource_path = path_util(relative_path=relative_path)
        with open(absolute_resource_path, 'r') as json_file:
            json_data = json.load(json_file)
    except Exception as e:
        logging.error("Error using read_json utility")
        raise e 
    
    return json_data