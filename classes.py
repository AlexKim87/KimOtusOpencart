from selenium.webdriver.common.by import By
import pytest


class MainPage:
    OPENCART_LOGO = (By.CSS_SELECTOR, "img[title='Your Store']")
    BIG_PICTURE = (By.CSS_SELECTOR, "#slideshow0")
    SEARCH_FIELD = (By.CSS_SELECTOR, ".swiper-wrapper")
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'div[id="search"] button')
    PHOTOCAMERA = (By.CSS_SELECTOR, "[alt='Canon EOS 5D']")


class Catalogue:
    DESKTOP_IMAC = (By.CSS_SELECTOR, "h4 a[href*='/imac']")
    DROPDOWN_LIST_VALUE = (By.CSS_SELECTOR, "select[id = 'input-sort'] option[value *= 'p.price&order=ASC']")
    MICE_TRACKBALLS = (By.CSS_SELECTOR, ".col-sm-9 h2")
    TABLETS_LBTN = (By.CSS_SELECTOR, "button[id='list-view']")
    PDA_HTC = (By.CSS_SELECTOR, "div.image>a:first-child")


class ProductDescription:
    DESCR_TAB = (By.CSS_SELECTOR, "a[href='#tab-description']")
    TWEET_LINK = (By.CSS_SELECTOR, ".twitter-share-button")
    QTY_FIELD = (By.CSS_SELECTOR, "input[ name='quantity']")
    PRICE = (By.CSS_SELECTOR, "ul.list-unstyled>li>h2")
    PRODUCT_PICTURE = (By.CSS_SELECTOR, "a.thumbnail img")


class LoginPage:
    CONTINUE_BTN = (By.CSS_SELECTOR, "a.btn")
    LOGIN_BTN = (By.CSS_SELECTOR, "input.btn")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    NEWSLETTER_LINK = (By.CSS_SELECTOR, "div.list-group a:nth-child(8)")
    DOWNLOADS_LINK = (By.CSS_SELECTOR, "div.list-group a:nth-child(13)")


class RegisterPage:
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    SUBSCRIBE_RADIOBUTTON = (By.CSS_SELECTOR, "input[type='radio'][name='newsletter'][value='1']")
    # SUBSCRIBE_RADIOBUTTON = (By.CSS_SELECTOR, "input[type='radio']")
    PD_HEADER = (By.CSS_SELECTOR, "fieldset>legend")
    LOGIN_LINK = (By.CSS_SELECTOR, "div.list-group a:nth-child(1)")
    FIRSTNAME = (By.CSS_SELECTOR, "input[type='text'][name='firstname']")


