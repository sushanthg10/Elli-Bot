from selenium_utils import SeleniumUtils
from general_utils import init_log, read_json

if __name__ == "__main__":
    """
    Entry Point of this application
    """
    logger = init_log()
    logger.info("Starting Application")
    logger.info("ITILITE CRON JOB VERSION 1.0")
    config = read_json('./credentials.json')
    try:
        seleniumUtils = SeleniumUtils()
        seleniumUtils.capture_screenshot(url = config['URL'])
        seleniumUtils.send_image(webhook=config['webhookURL'])
    except Exception as e:
        logger.error("Application failed during the process with the followin error")
        logger.error(e)