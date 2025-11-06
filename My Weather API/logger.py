import logging 

def setup_logger(log_File, log_type ):
    logging.basicConfig(
        level=log_type,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler(log_File)]
    )
    logger = logging.getLogger(__name__)
    return logger
