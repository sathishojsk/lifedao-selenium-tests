from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Enter your email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Enter your password']")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    Error_msg = (By.XPATH, "//div[@id='root']/div[2]/div[@class='go4109123758']/div[@class='animate-enter font-roboto font-semibold text-sm p-4 rounded-xl transition-all pointer-events-auto flex justify-between shadow-toast bg-white border border-[#D0D5DD] max-w-xs items-center']/div[@class='flex items-center gap-2']/div[2]/div[@class='font-semibold text-[#101828] break-all']")
    Logout_menu = (By.XPATH, "//button[@class='flex items-center gap-2 cursor-pointer font-roboto border border-grey-300 px-3 py-3.5 rounded-2xl bg-white max-md:hidden']")
    Logout_button = (By.XPATH, "//button[@role='menuitem']")

    def open_login(self, url):
        self.open(url)

    def clear(self, by, locator):
        element = self.find(by, locator)
        element.clear()

    def login(self, email, password):
        self.send_keys(*self.EMAIL_INPUT, text=email)
        self.send_keys(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BTN)

    def open_user_menu(self):
        self.click(*self.Logout_menu)

    def logout(self):
        self.open_user_menu()
        self.click(*self.Logout_button)

