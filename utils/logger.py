import logging
import os

log_dir = "reports/logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "test.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger()
