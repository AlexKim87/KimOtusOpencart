from classes import LoginPage, MainPage, Catalogue, ProductDescription, RegisterPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_check_elements_loginpage(browser):
    browser.get(browser.url + "/index.php?route=account/login")
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(LoginPage.CONTINUE_BTN))
    wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_BTN))
    wait.until(EC.visibility_of_element_located(LoginPage.EMAIL_FIELD))
    wait.until(EC.visibility_of_element_located(LoginPage.NEWSLETTER_LINK))
    wait.until(EC.visibility_of_element_located(LoginPage.DOWNLOADS_LINK))


def test_check_elements_mainpage(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(MainPage.OPENCART_LOGO))
    wait.until(EC.visibility_of_element_located(MainPage.BIG_PICTURE))
    wait.until(EC.visibility_of_element_located(MainPage.SEARCH_FIELD))
    wait.until(EC.visibility_of_element_located(MainPage.SEARCH_BUTTON))
    wait.until(EC.visibility_of_element_located(MainPage.PHOTOCAMERA))


def test_check_elements_product_description(browser):
    browser.get(browser.url + "/macbook")
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(ProductDescription.DESCR_TAB))
    wait.until(EC.visibility_of_element_located(ProductDescription.TWEET_LINK))
    wait.until(EC.visibility_of_element_located(ProductDescription.QTY_FIELD))
    wait.until(EC.visibility_of_element_located(ProductDescription.PRICE))
    wait.until(EC.visibility_of_element_located(ProductDescription.PRODUCT_PICTURE))


def test_check_elements_product_catalogue(browser):
    browser.get(browser.url + "/desktops/mac")
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(Catalogue.DESKTOP_IMAC))
    browser.get(browser.url + "/desktops")
    wait.until(EC.visibility_of_element_located(Catalogue.DROPDOWN_LIST_VALUE))
    browser.get(browser.url + "/component/mouse")
    wait.until(EC.visibility_of_element_located(Catalogue.MICE_TRACKBALLS))
    browser.get(browser.url + "/tablet")
    wait.until(EC.visibility_of_element_located(Catalogue.TABLETS_LBTN))
    browser.get(browser.url + "/smartphone")
    wait.until(EC.visibility_of_element_located(Catalogue.PDA_HTC))


def test_check_elements_register_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(RegisterPage.PRIVACY_CHECKBOX))
    wait.until(EC.visibility_of_element_located(RegisterPage.SUBSCRIBE_RADIOBUTTON))
    wait.until(EC.visibility_of_element_located(RegisterPage.PD_HEADER))
    wait.until(EC.visibility_of_element_located(RegisterPage.LOGIN_LINK))
    wait.until(EC.visibility_of_element_located(RegisterPage.FIRSTNAME))
