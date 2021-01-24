import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.NOTSET
)

logger = logging.getLogger("cli_Request")
