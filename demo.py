import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys

url = "https://trytestingthis.netlify.app/"


class Login:
    def __init__(self):
        self.driver = None

    def set_up(self):
        # Use ChromeDriverManager to get the path to the ChromeDriver executable
        chrome_driver_path = ChromeDriverManager().install()

        # Initialize the Chrome WebDriver using the path obtained
        service = ChromeService(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)

    def launch(self):
        self.driver.get(url)
        time.sleep(5)


    def validate_login(self):
        user_name =self.driver.find_element(By.XPATH, "//input[@type='text']")
        user_name.send_keys("Test")
        time.sleep(3)
        passowrd = self.driver.find_element(By.ID, "pwd")
        passowrd.send_keys()






# Create an instance of the Login class
login = Login()

# Set up the WebDriver
login.set_up()

# Launch the browser and open the specified URL
login.launch()

login.enter_username()
