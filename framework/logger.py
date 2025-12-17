import logging
import os

LOG_PATH = "logs/validation.log"
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(msg: str) -> None:
    logging.info(msg)

def log_error(msg: str) -> None:
    logging.error(msg)
