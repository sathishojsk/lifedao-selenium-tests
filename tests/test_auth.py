import unittest, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.signup_page import SignupPage

BASE_URL = "https://uat.thelifedao.io/app/sign-in?lang=en"

class AuthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

        cls.login = LoginPage(cls.driver)
        cls.signup = SignupPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

    def test_a_invalid_login(self):
        self.login.open_login(BASE_URL + "/login")
        self.login.login(email="invalid_user@example.com",password="WrongPass123!")
        time.sleep(5)
        error_present = self.login.is_visible(*LoginPage.Error_msg)
        self.assertTrue(error_present, "Invalid login did NOT show error message!")
        self.assertTrue(self.login.is_visible(*LoginPage.LOGIN_BTN))
        time.sleep(5)

    def test_b_valid_login(self):
        self.login.clear(*LoginPage.EMAIL_INPUT)
        self.login.clear(*LoginPage.PASSWORD_INPUT)
        time.sleep(2)
        self.login.login(email="lifetest2@yopmail.com",password="pass@1233")
        time.sleep(5)
        expected_url = "https://uat.thelifedao.io/app/subscribe"
        current_url = self.driver.current_url
        print("Current URL:", current_url)
        self.assertTrue(expected_url in current_url,f"Login failed — expected URL: {expected_url}, but got: {current_url}")
        time.sleep(5)
        self.login.logout()
        current_url = BASE_URL
        print("URL after logout:", current_url)
        time.sleep(5)

    def test_c_signup_link(self):
        self.signup.click_signup_link_on_login()
        self.assertTrue(self.signup.is_visible(*SignupPage.INVITE_INPUT),"Invite code input not visible after clicking Sign Up")

    def test_d_invite_code_opens_signup_form(self):
        self.signup.submit_invite(invite="tpg3pe")
        self.signup.submit_click_invite()
        self.assertTrue(self.signup.is_visible(*SignupPage.EMAIL_INPUT),"Signup email field not visible after submitting invite code")
        time.sleep(5)
    
    def test_e_signup_form(self):
        self.signup.fill_signup(email="testersathish2@gmail.com", password="Pass@1233", repeat= "Pass@1233")
        time.sleep(2)
        self.signup.click_signup()
        time.sleep(4)   

if __name__ == '__main__':
    unittest.main()
