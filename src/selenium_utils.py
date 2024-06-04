from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from general_utils import init_log, path_util
import time, datetime, requests

class SeleniumUtils():
    
    def __init__(self):
        """
        Initializing Log
        """
        self.logger = init_log()
        self.get_driver()
    
    def get_driver(self):
        """
        Return Chroming Driver with settings and metadata
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--window-size=1920x1080")
        driver_path = path_util('./chromedriver')
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service = service, options=chrome_options)

    def capture_screenshot(self, url: str):
        """
        Function to capture screenshot using selenium and save it locally"
        """
        try:
            self.driver.get(url = url)
            time.sleep(2)
            self.driver.save_screenshot('./screenshot.png')
        except Exception as e:
            self.logger.error("Application failed during the execution of capture_screenshot")
            raise e
        finally: 
            self.driver.quit()

    def send_image(self, webhook: str):
        """
        Function to open a file stream and send data to gmail chat with
        a custom message
        """
        try:
            self.logger.info(f"Attempting to send image to chat {datetime.datetime.now}")
            with open("screenshot.png", "rb") as file_stream:
                screenshot_data = file_stream.read()
            files = { 
                "file": ("screenshot.png", screenshot_data)
            }
            payload = {
                "text": f"Screenshot of _ tkane at time {datetime.datetime.now()}",
                "channel": "your_gmail_channel_id"
            }
            requests.post(webhook, data=payload, files=files)
            self.logger.info("Sent image")
        except Exception as e:
            self.logger.error("Application failed during execution of send_image")
            raise e