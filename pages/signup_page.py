from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignupPage(BasePage):
    SIGNUP_BUTTON = (By.XPATH, "//div[@id='root']/div[@class='max-md:py-0 bg-grey-50']/div[@class='w-full']/div[@class='my-11 max-w-[500px] mx-auto w-full flex flex-col max-md:px-4']/div[@class='mt-3 flex justify-center gap-1 font-roboto']/a[@class='text-primary font-semibold text-sm']")

    INVITE_INPUT = (By.XPATH, "//input[@placeholder='Invite code/link']")
    INVITE_SUBMIT = (By.XPATH, "//button[@class='bg-primary px-4 py-3 text-white font-semibold font-roboto text-sm rounded-r-lg']")

    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Enter your email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Enter your password']")
    REPEAT_PASSWORD_INPUT = (By.XPATH, "//input[contains(@placeholder,'Repeat')]")
    SIGNUP_BTN = (By.XPATH, "//button[@type='submit']")

    def click_signup_link_on_login(self):
        self.click(*self.SIGNUP_BUTTON)

    def submit_invite(self, invite):
        self.send_keys(*self.INVITE_INPUT, text=invite)

    def submit_click_invite(self):
        self.click(*self.INVITE_SUBMIT)

    def fill_signup(self, email, password, repeat=None):
        self.send_keys(*self.EMAIL_INPUT, text=email)
        self.send_keys(*self.PASSWORD_INPUT, text=password)
        self.send_keys(*self.REPEAT_PASSWORD_INPUT, text=(repeat or password))

    def click_signup(self):
        self.click(*self.SIGNUP_BTN)
